import sqlite3


class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    # def create_table_users(self):
    #     sql = """
    #     CREATE TABLE IF NOT EXISTS Channel (
    #         channel_id int NOT NULL,
    #         channel_name varchar(255) NOT NULL
    #         );
    #     """
    #     # sql = """
    #     # CREATE TABLE Xabar (
    #     #     activ int NOT NULL
    #     #     );
    #     # """
        
    #     self.execute(sql, commit=True)
        

    def add_user(self, channel_id: int, channel_name: str):
        sql = """
        INSERT INTO Channel(channel_id, channel_name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(channel_id, channel_name), commit=True)
    
    def add_activ(self, activ: int):
        sql = """
        INSERT INTO Xabar(activ) VALUES(?)
        """
        self.execute(sql, parameters=(activ), commit=True)    
    
    
    def update_activ(self, activ: int):
        sql = f"""
        UPDATE Xabar SET activ=?
        """
        return self.execute(sql, parameters=(activ), commit=True)
    

    def select_all_users(self):
        sql = """
        SELECT * FROM Channel
        """
        return self.execute(sql, fetchall=True)

    def select_all_activ(self):
        sql = """
        SELECT * FROM Xabar
        """
        return self.execute(sql, fetchall=True)


def logger(statement):
    pass


dats = Database()
