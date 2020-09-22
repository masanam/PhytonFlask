import sys
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect
from datetime import datetime

class DataList():
    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.bot_task_template_name FROM bot_task AS a LEFT JOIN bot_task_template as b ON b.bot_task_template_id=a.bot_task_template_id ORDER BY bot_task_id DESC LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result    
    def count_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task"
        mc.execute(query)
        mc.fetchall()
        count = mc.rowcount
        return count	
    def search_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.bot_task_template_name FROM bot_task AS a LEFT JOIN bot_task_template as b ON b.bot_task_template_id=a.bot_task_template_id WHERE bot_task_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall() 
        return result
    def search_data1(sn1,sn2):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.bot_task_template_name FROM bot_task AS a LEFT JOIN bot_task_template as b ON b.bot_task_template_id=a.bot_task_template_id WHERE SN >= %s AND SN <= %s "
        mc.execute(query,(sn1,sn2) )
        result = mc.fetchall()
        return result        
    def search_data2(data2):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task WHERE bot_task_template_id = %s "
        mc.execute(query,(data2) )
        result = mc.fetchall()
        return result    
    def search_data3(data3):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task WHERE bot_task_name = %s "
        mc.execute(query,(data3) )
        result = mc.fetchall()
        return result       
    def get_category():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task_template"
        mc.execute(query)
        result = mc.fetchall()
        return result       
    def save_data(kategori,name,sn):
        mc = mysql_connect.cursor()
        now = datetime.now()
        query = "INSERT INTO bot_task (bot_task_template_id, bot_task_name, SN ,created_at ) VALUES (%s,%s,%s,%s)"
        data = (kategori,name,sn,now)
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
        
