import sys
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect

class DataNEW():
    def add_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task_group"
        mc.execute(query)
        result = mc.fetchall()
        return result