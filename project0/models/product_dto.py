class Product:
    def __init__(self, product_id, productname, addproduct,price):
        self.product_id = product_id
        self.productname = productname
        self.addproduct = addproduct
        self.price = price
    def __repr__(self) -> str:
        return f"Product : Product_id - {self.product_id} productname - {self.productname} addproduct - {self.addproduct} price - {self.price}"