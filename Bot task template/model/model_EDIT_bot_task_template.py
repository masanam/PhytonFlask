import sys
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect

class DataEdit():
    def edit_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task_template"
        mc.execute(query)
        result = mc.fetchall()
        return result