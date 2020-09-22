import sys
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect
from datetime import datetime

class DataList():
    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name, c.scene_name, d.task_value_group_name, e.task_value_type_name FROM task_value as a \
        LEFT JOIN scene_category as b ON b.scene_category_id = a.scene_category_id \
        LEFT JOIN scene as c ON c.scene_id = a.scene_id \
        LEFT JOIN task_value_group as d ON d.task_value_group_id = a.task_value_group_id \
        LEFT JOIN task_value_type as e ON e.task_value_type_id = a.task_value_type_id \
        ORDER BY task_value_id DESC LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result    
    def count_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value"
        mc.execute(query)
        mc.fetchall()
        count = mc.rowcount
        return count	
    def get_category():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene_category"
        mc.execute(query)
        result = mc.fetchall()
        return result    
    def get_category1():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene"
        mc.execute(query)
        result = mc.fetchall()
        return result       
    def get_category2():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_group"
        mc.execute(query)
        result = mc.fetchall()
        return result     
    def get_category3():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_type"
        mc.execute(query)
        result = mc.fetchall()
        return result          
    def search_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name, c.scene_name, d.task_value_group_name, e.task_value_type_name FROM task_value as a \
        LEFT JOIN scene_category as b ON b.scene_category_id = a.scene_category_id \
        LEFT JOIN scene as c ON c.scene_id = a.scene_id \
        LEFT JOIN task_value_group as d ON d.task_value_group_id = a.task_value_group_id \
        LEFT JOIN task_value_type as e ON e.task_value_type_id = a.task_value_type_id \
        WHERE task_value_content = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def search_data1(data1):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name, c.scene_name, d.task_value_group_name, e.task_value_type_name FROM task_value as a \
        LEFT JOIN scene_category as b ON b.scene_category_id = a.scene_category_id \
        LEFT JOIN scene as c ON c.scene_id = a.scene_id \
        LEFT JOIN task_value_group as d ON d.task_value_group_id = a.task_value_group_id \
        LEFT JOIN task_value_type as e ON e.task_value_type_id = a.task_value_type_id \
        WHERE task_value_group_name = %s "
        mc.execute(query,(data1) )
        result = mc.fetchall()
        return result    
    def search_data2(data2):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name, c.scene_name, d.task_value_group_name, e.task_value_type_name FROM task_value as a \
        LEFT JOIN scene_category as b ON b.scene_category_id = a.scene_category_id \
        LEFT JOIN scene as c ON c.scene_id = a.scene_id \
        LEFT JOIN task_value_group as d ON d.task_value_group_id = a.task_value_group_id \
        LEFT JOIN task_value_type as e ON e.task_value_type_id = a.task_value_type_id \
        WHERE task_value_type_name = %s "
        mc.execute(query,(data2) )
        result = mc.fetchall()
        return result    
    def search_data3(data3):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name, c.scene_name, d.task_value_group_name, e.task_value_type_name FROM task_value as a \
        LEFT JOIN scene_category as b ON b.scene_category_id = a.scene_category_id \
        LEFT JOIN scene as c ON c.scene_id = a.scene_id \
        LEFT JOIN task_value_group as d ON d.task_value_group_id = a.task_value_group_id \
        LEFT JOIN task_value_type as e ON e.task_value_type_id = a.task_value_type_id \
        WHERE task_value_name = %s "
        mc.execute(query,(data3) )
        result = mc.fetchall()
        return result         
    def save_data(name, content, category, category1, category2, category3):
        mc = mysql_connect.cursor()
        now = datetime.now()
        query = "INSERT INTO task_value (task_value_name, task_value_content, scene_category_id, scene_id , task_value_group_id, task_value_type_id, created_at ) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (name, content, category, category1, category2, category3, now)
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