
from models.product_dto import Product
from models.login_dto import Login
from database.product_dao import insert_product_info
from database.login_dao import  select_user_by_id

def create_product_info(id, input):
    login_dto = select_user_by_id(id)
    product_id = insert_product_info(login_dto, input.get("productname"), input.get("addproduct"), input.get("price"))
    
    if product_id is not None:
        return product_id