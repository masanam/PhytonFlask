import sys
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect
from datetime import datetime

class DataList():
    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group ORDER BY bot_user_group_id DESC LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result    
    def count_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group"
        mc.execute(query)
        mc.fetchall()
        count = mc.rowcount
        return count	
    def search_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group WHERE bot_user_group_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def save_data(name,description):
        mc = mysql_connect.cursor()
        now = datetime.now()
        query = "INSERT INTO bot_user_group (bot_user_group_name, created_at ) VALUES (%s,%s)"
        data = (name,now)
        mc.execute(query,(data) )
        mysql_connect.commit()
        result = mc.fetchall()
        return result        
    def update_log(log,task):
        mc = mysql_connect.cursor()
        now = datetime.now()
        query = "INSERT INTO log (log_description, bot_task_group_id, log_start_date_time, log_end_date_time, created_at ) VALUES (%s,%s,%s,%s,%s)"
        data = (log,task,now,now,now)
        mc.execute(query,(data) )
        mysql_connect.commit()
        result = mc.fetchall()
        return result
