import psycopg2
#this file used to define a function to get the database connection
def get_connection():
    connection = psycopg2.connect(
        database="project",
        user="postgres",
        password="computer",
        host="mydatabase.cxl26wnypzlr.us-east-2.rds.amazonaws.com",
        port=5432
    )
    return connection