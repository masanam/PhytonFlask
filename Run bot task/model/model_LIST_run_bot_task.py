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
        query = "SELECT a.*, b.bot_task_template_name FROM bot_task AS a LEFT JOIN bot_task_template as b ON b.bot_task_template_id=a.bot_task_template_id WHERE a.bot_task_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall() 
        return result
    def search_data1(sn1,sn2):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.bot_task_template_name FROM bot_task AS a LEFT JOIN bot_task_template as b ON b.bot_task_template_id=a.bot_task_template_id WHERE a.SN >= %s AND a.SN <= %s "
        mc.execute(query,(sn1,sn2) )
        result = mc.fetchall()
        return result    
    def update_data(c1, c2):
        mc = mysql_connect.cursor()
        query = "UPDATE bot_task SET run_count = %s WHERE bot_task_id = %s"
        data = (c1,c2)
        mc.execute(query,(data))
        mysql_connect.commit()
        result = mc.fetchall()
        print("Record Updated successfully ")
        return result        
    def get_run_count(checkbox_id):
        mc = mysql_connect.cursor()
        query = "SELECT run_count FROM bot_task WHERE bot_task_id = %s "
        mc.execute(query,(checkbox_id) )
        result = mc.fetchall() 
        return result    
    def update_log(log,task,logstart):
        mc = mysql_connect.cursor()
        now = datetime.now()
        query = "INSERT INTO log (log_description, bot_task_group_id, log_start_date_time, log_end_date_time, created_at ) VALUES (%s,%s,%s,%s,%s)"
        data = (log,task,logstart,now,now)
        mc.execute(query,(data) )
        mysql_connect.commit()
        result = mc.fetchall()
        return result
    def get_bottask(checkbox_id):
        mc = mysql_connect.cursor()
        query = "SELECT bot_task_name FROM bot_task WHERE bot_task_id = %s "
        mc.execute(query,(checkbox_id) )
        result = mc.fetchone() 
        return result    
    def get_bottasktemplate(checkbox_id):
        mc = mysql_connect.cursor()
        query = "SELECT b.bot_task_template_name FROM bot_task AS a LEFT JOIN bot_task_template as b ON b.bot_task_template_id=a.bot_task_template_id WHERE a.bot_task_id = %s "
        # query = "SELECT bot_task_template_name FROM bot_task WHERE bot_task_id = %s "
        mc.execute(query,(checkbox_id) )
        result = mc.fetchone() 
        return result  
        
