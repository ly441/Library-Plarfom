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
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM categories
            """)

            rows = cur.fetcall()
            print("CATEGORIES FETCHED", rows)
            return rows

    @staticmethod
    def update(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                UPDATE categories SET title = %s, description = %s WHERE id = %s
            """, (self.title, self.description, self.id))
            print("CATEGORY UPDATED SUCCESSFULLY")
            return True

    @staticmethod
    def delete(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                DELETE FROM categories WHERE id = %s 
            """, (self.id))
            print(f"CATEGORY WTH ID {self.id} HAS BEEN DELETED SUCCESSFULLY")
            return True

    @staticmethod
    def listonecategory(self: Category):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM categories WHERE id = %s
            """, (self.id))

            row = cur.fetchone()
            print("CATEGORY RECORD HAS BEEN FETCHED")
            return row
