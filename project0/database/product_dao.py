#import psycopg2
#from database.connection import get_connection
#from models.product_dto import Product
# DAO = Data Access Object
# def insert_product_info(productname,addproduct, price):
  #   connection = get_connection()
   #  cursor = connection.cursor()
# 
   #  qry = "INSERT INTO product VALUES (default, %s, %s, %d ) RETURNING id;"

   #  try:
        # cursor.execute(qry, (productname, addproduct, price))
        # #id = cursor.fetchone()[0]
        #connection.commit()
        #return id
    #except(psycopg2.DatabaseError) as error:
        #print(error)
        #connection.rollback()
    #finally:
        #if connection is not None:
            #connection.close()