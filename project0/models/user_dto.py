class User:
    def __init__(self, info_id: int, id: int, firstname: str, lastname: str):
        self.info_id = info_id
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
    
    def __repr__(self) -> str:
        return f"User Info: {self.info_id} + {self.id} + {self.firstname} + {self.lastname}"

    def validate_user_info(self) -> bool:
        if len(self.firstname) < 5 or len(self.lastname) < 5:
            return False
        elif len(self.firstname) > 20 or len(self.lastname) > 20:
            return False
        else:
            return True