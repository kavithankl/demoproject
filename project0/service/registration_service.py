
# In order to register to my service, they need:
# Valid Username and password
# Valid first_name and Last_name
# In this case, my only validation is checking the length of each input

from models.login_dto import Login
from models.user_dto import User
from database.login_dao import insert_user, select_user_by_id
from database.user_dao import insert_user_info

def validate_registration(input):
    login_dto = Login(0, input.get("username"), input.get("password"))
    info_dto = User(0, 0, input.get("firstname"), input.get("lastname"))

    return login_dto.validate_login() and info_dto.validate_user_info()

def create_login(input):
    id = insert_user(input.get("username"), input.get("password"))

    if id is not None:
        return id

def create_user_info(id, input):
    login_dto = select_user_by_id(id)
    info_id = insert_user_info(login_dto, input.get("firstname"), input.get("lastname"))
    
    if info_id is not None:
        return info_id