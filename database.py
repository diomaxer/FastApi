import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DatabaseConfig

engine = create_engine(DatabaseConfig.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class PgDriver:
    """
    Контекстный менеджер для работы с БД прямыми SQL запросами.
    Usage:
        from api.services.database import PgDriver
        with PgDriver() as curr:
            curr.execute("SELECT first_name, last_name FROM users")
            result = curr.fetchall()
            for row in result:
                print(row["first_name"], row["last_name"])
    Usage with SqlAlchemy models:
        from api.models.operator import Operator
        from api.services.database import PgDriver
        with PgDriver() as curr:
            curr.execute("SELECT * FROM operators")
            items = curr.fetchall()
        if not items:
            return None
        return [Operator(**item) for item in items]
    """
    def __init__(self, db_name: str = None, db_password: str = None, db_user: str = None, db_host: str = None, db_port: str = None, db_dsn: str = None):
        """
        Если хотя бы один из параметров для доступа к БД будет None, выкинет ошибку.
        Если все параметры для доступа к БД будут заполнены, то они будут использоваться для соединения с Базой.
        Если ни один из параметров не будет заполнен, будет использоваться дефолтное соединение, определенное в конфигах
        базы в settings.py файле.
        """
        self._db_name = db_name
        self._db_password = db_password
        self._db_user = db_user
        self._db_host = db_host
        self._db_port = db_port
        self._dsn = db_dsn

        if any([self._db_name, self._db_password, self._db_port, self._db_user, self._db_host]):
            if self._dsn is not None:
                raise ValueError("Если заполняется DSN, остальные поля должны быть пустыми")
            if not all([self._db_name, self._db_password, self._db_port, self._db_user, self._db_host]):
                raise ValueError("В драйвере заполнены не все поля для подключения к БД")
            self._dsn = f"postgresql://{self._db_user}:{self._db_password}@{self._db_host}:{self._db_port}/{self._db_name}"
        else:
            if not self._dsn:
                self._dsn = DatabaseConfig.DB_URL

    def __enter__(self):
        self.conn = psycopg2.connect(self._dsn, cursor_factory=RealDictCursor)
        self.curr = self.conn.cursor()

        return self.curr

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        self.curr.close()
