# CRUD OPERATIONS

from db import get_connection
from models.category import Category


class CategoryResource:

    @staticmethod
    def create(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                INSERT INTO categories (title, description)
                VALUES (%s, %s)
                RETURNING id 
            """,
            (self.title, self.description)
            )
            print(f"{self.title} has been added successfully!!")
        return True

    @staticmethod
    def list():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

    @staticmethod
    def listone():
        pass

