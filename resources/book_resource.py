from db import get_connection
from models.book import Book

class BookResource:

    @staticmethod
    def create(self: Book):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                INSERT INTO books (id, title, isbn, published_date, total_copies, available_copies ,category_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (self.id, self.title, self.isbn, self.published_date, self.total_copies, self.available_copies, self.category_id)
            )
            print(f"{self.title} book has been added successfully!!")
        return True

    @staticmethod
    def listall():
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM books")
            rows = cur.fetchall()
            books = []
            for row in rows:
                book = Book(
                    id=row[0],
                    title=row[1],
                    isbn=row[2],
                    published_date=row[3],
                    total_copies=row[4],
                    available_copies=row[5],
                    category_id=row[6]
                )
                books.append(book)
        return books

    @staticmethod
    def update(self: Book):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                UPDATE books
                SET title = %s, isbn = %s, published_date = %s, total_copies = %s, available_copies = %s, category_id = %s
                WHERE id = %s
            """,
            (self.title, self.isbn, self.published_date, self.total_copies, self.available_copies, self.category_id, self.id)
            )
            print(f"{self.title} book has been updated successfully!!")
        return True

    @staticmethod
    def delete(self: Book):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM books WHERE id = %s", (self.id,))
            print(f"{self.title} book has been deleted successfully!!")
        return True

    @staticmethod
    def listone(self: Book):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM books WHERE id = %s", (self.id,))
            row = cur.fetchone()
            if row:
                book = Book(
                    id=row[0],
                    title=row[1],
                    isbn=row[2],
                    published_date=row[3],
                    total_copies=row[4],
                    available_copies=row[5],
                    category_id=row[6]
                )
                return book
            else:
                print(f"Book with ID {self.id} not found.")
        return None