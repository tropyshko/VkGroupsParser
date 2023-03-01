import sqlite3
from datetime import datetime

class GroupsDB():
    def __init__(self) -> None:
        self.con = sqlite3.connect("db.db")
        self.cur = self.con.cursor()

    def get_groups(self):
        res = self.cur.execute("SELECT * FROM groups ORDER BY subscribers DESC")
        groups = res.fetchall()
        return groups

    def change_group(self,url):
        now = datetime.now()
        sql = f''' UPDATE groups
            SET last_post = '{now}'
            WHERE url = '{url}'
            '''
        self.cur.execute(sql)
        self.con.commit()

    def add_group(self,url,title,subs):
        try:
            sql = f""" INSERT INTO groups(url,title,subscribers)
                    VALUES('{url}','{title}','{subs}') """
            self.cur.execute(sql)
            self.con.commit()
        except:
            pass

class AccountsDB():
    def __init__(self) -> None:
        self.con = sqlite3.connect("db.db")
        self.cur = self.con.cursor()

    def create(self):
        self.cur.execute("""
        CREATE TABLE "tasks" (
            "id"	INTEGER UNIQUE,
            "name"	TEXT,
            "datetime"	TEXT,
            "repeat"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
        )
        """)
        self.con.commit()

    def remove_account(self,tid):
        pass

    def add_account(self,name,date,repeat=False):
        sql = f""" INSERT INTO tasks(name,datetime,repeat)
                VALUES('{name}','{date}','{repeat}') """
        self.cur.execute(sql)
        self.con.commit()

    def get_accounts(self):
        res = self.cur.execute("SELECT * FROM accounts")
        accounts = res.fetchall()
        return accounts


    def add_useragent(self,number,user_agent):
        sql = f''' UPDATE accounts
            SET useragent = '{user_agent}'
            WHERE number = '{number}'
            '''
            
        self.cur.execute(sql)
        self.con.commit()

    def update_account(self,tid):
        pass
