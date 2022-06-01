import psycopg2
from database.connection import get_connection
from models.user_dto import User
from models.login_dto import Login

def select_user_info_by_id(info_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM info_tablee WHERE info_id = {info_id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_info = User(record[0], record[1], record[2], record[3])
            return user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def select_by_user(login_dto: Login):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT * FROM info_tablee WHERE id = {login_dto.id};"

    try:
        cursor.execute(qry)
        while True:
            record = cursor.fetchone()
            if record is None:
                break
            user_info = User(record[0], record[1], record[2], record[3])
            return user_info
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def insert_user_info(login_dto: Login, firstname: str, lastname: str):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO info_tablee VALUES (default, %s, %s, %s) RETURNING info_id;"

    try:
        cursor.execute(qry, (login_dto.id, firstname, lastname))
        id = cursor.fetchone()[0]
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

