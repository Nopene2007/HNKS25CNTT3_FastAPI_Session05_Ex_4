# phan tich
    # input: product_id:int , code:str, name:str, price:int, stock:int
    # output: 200 OK
    # 404 Not Found, "detail": "Nội dung lỗi chi tiết"
#code
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "stock": 10},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "stock": 5}
]
class ProductUpdate(BaseModel):
    code: str
    name: str
    price: int
    stock: int
@app.put("/products/{product_id}")
def update_product(product_id: int, payload: ProductUpdate):
    if not payload.name.strip():
        return {"detail": "Name cannot be empty"}
    if payload.price <= 0:
        return {"detail": "Price must be greater than 0"}
    if payload.stock < 0:
        return {"detail": "Stock must be greater than or equal to 0"}
    product_check = None
    for product in products:
        if product["id"] == product_id:
            product_check = product
            break
    if product_check is None:
        return {"detail": "Product not found"}
    for product in products:
        if product["code"] == payload.code and product["id"] != product_id:
            return {"detail": "Product code already exists"}
    product_check["code"] = payload.code
    product_check["name"] = payload.name
    product_check["price"] = payload.price
    product_check["stock"] = payload.stock
    return {
        "message": "Product updated successfully",
        "data": product_check
    }