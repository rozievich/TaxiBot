from .connect import conn, cur


class TaxiDB:
    def __init__(self) -> None:
        self.cur = cur
        self.con = conn
    
    def create_user(self, user_id: str):
        query = "INSERT INTO users(user_id) VALUES(%s)"
        self.cur.execute(query, (user_id, ))
        self.con.commit()

    def get_user(self, user_id: str):
        query = "SELECT * FROM users WHERE user_id = %s"
        self.cur.execute(query, (user_id, ))
        return self.cur.fetchone()

    def get_users(self):
        query = "SELECT * FROM users"
        self.cur.execute(query)
        return self.cur.fetchall()
    

    def create_taxi(self, fullname, phone, photo, description=None, username=None, top=False):
        query = "INSERT INTO taxis(fullname, phone, username, description, photo, top) VALUES(%s, %s, %s, %s, %s, %s)"
        self.cur.execute(query, (fullname, phone, username, description, photo, top))
        self.con.commit()
    
    def get_taxi(self, fullname: str):
        query = "SELECT * FROM taxis WHERE fullname = %s"
        self.cur.execute(query, (fullname, ))
        return self.cur.fetchone()

    def get_taxies(self):
        query = "SELECT * FROM taxis"
        self.cur.execute(query)
        return self.cur.fetchall()

    def delete_taxi(self, id: int):
        query = "DELETE FROM taxis WHERE id = %s"
        self.cur.execute(query, (id, ))
        self.con.commit()
    
    def get_top_taxi(self):
        query = "SELECT * FROM taxis WHERE top = true"
        self.cur.execute(query)
        self.cur.fetchall()
    
    def update_top_taxi(self, _id: int, top: bool):
        query = "UPDATE taxis SET top = %s WHERE id = %s"
        self.cur.execute(query, (top, _id))
        self.con.commit()
    