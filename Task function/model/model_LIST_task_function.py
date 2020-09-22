import sys
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect
from datetime import datetime

class DataList():
    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_function LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.task_function_category_name FROM task_function AS a LEFT JOIN task_function_category AS b ON b.task_function_category_id = a.task_function_category_id ORDER BY task_function_id DESC LIMIT %s,%s"
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result    
    def count_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_function"
        mc.execute(query)
        mc.fetchall()
        count = mc.rowcount
        return count	
    def search_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.task_function_category_name FROM task_function AS a LEFT JOIN task_function_category AS b ON b.task_function_category_id = a.task_function_category_id WHERE b.task_function_category_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def search_data1(data):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.task_function_category_name FROM task_function AS a LEFT JOIN task_function_category AS b ON b.task_function_category_id = a.task_function_category_id WHERE a.task_function_name = %s "
        mc.execute(query,(data) )
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