from fastapi import FastAPI
from route import route_product


app = FastAPI()

app.include_router(router=route_product.router, prefix="/api/product", tags=["product"])
