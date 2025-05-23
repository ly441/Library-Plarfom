from db import get_connection
from models.member import Member

class MemberResource:
    
    @staticmethod
    def create(self: Member):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                INSERT INTO members (id, first_name, last_name, surname, email, joined_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (self.id, self.first_name, self.last_name, self.surname, self.email, self.joined_date)
            )
            print(f"{self.first_name} {self.last_name} has been added successfully!!")
        return True
    
    @staticmethod
    def listall():
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM members")
            rows = cur.fetchall()
            members = []
            for row in rows:
                member = Member(
                    id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    surname=row[3],
                    email=row[4],
                    joined_date=row[5]
                )
                members.append(member)
        return members
    
    @staticmethod
    def update(self: Member):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""
                UPDATE members
                SET first_name = %s, last_name = %s, surname = %s, email = %s, joined_date = %s
                WHERE id = %s
            """,
            (self.first_name, self.last_name, self.surname, self.email, self.joined_date, self.id)
            )
            print(f"{self.first_name} {self.last_name} has been updated successfully!!")
        return True
    
    @staticmethod
    def delete(self: Member):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("DELETE FROM members WHERE id = %s", (self.id,))
            print(f"{self.first_name} {self.last_name} has been deleted successfully!!")
        return True
    
    @staticmethod
    def listone(self: Member):
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM members WHERE id = %s", (self.id,))
            row = cur.fetchone()
            if row:
                member = Member(
                    id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    surname=row[3],
                    email=row[4],
                    joined_date=row[5]
                )
                return member
            else:
                print("Member not found")
                return None