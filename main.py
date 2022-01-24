from fastapi import FastAPI
from route import route_product, route_auth


app = FastAPI()

app.include_router(router=route_product.router, prefix="/api/product", tags=["product"])
app.include_router(router=route_auth.router, prefix="/api/auth", tags=["auth"])
