import sys
from datetime import datetime
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect

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
        query = "SELECT * FROM task_function WHERE task_function_category = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def search_data1(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_function WHERE task_function_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result 
    def get_scene():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene"
        mc.execute(query)
        result = mc.fetchall()
        return result     
    def get_scene_cat():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene_category"
        mc.execute(query)
        result = mc.fetchall()
        return result    
    def get_task_value_type(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_type LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result     
    def get_task_value_group(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_group LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result  
    def save_data(task_function_id, task_function_name, scene_category_id, scene_category, scene_id, scene, task_value_type_id, task_value_type_name, task_value_group_id, task_value_group_name, task_value_count, unique_value, comment):
        mc = mysql_connect.cursor()
        now = datetime.now()
        query = "INSERT INTO bot_task_template_tf (task_function_id, task_function, scene_category_id, scene_category, scene_id, scene, task_value_type_id, task_value_type, task_value_group_id, task_value_group, task_value_count, unique_task_value, comment, created_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (task_function_id, task_function_name, scene_category_id, scene_category, scene_id, scene, task_value_type_id, task_value_type_name, task_value_group_id, task_value_group_name, task_value_count, unique_value, comment, now)
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result    
    def get_task_function(start,limit):
        mc = mysql_connect.cursor()
        # query = "SELECT * FROM bot_task_template_tf LIMIT %s,%s "
        query = "SELECT a.*, b.scene_name, c.scene_category_name, d.task_value_type_name FROM bot_task_template_tf as a LEFT JOIN scene as b ON b.scene_id = a.scene_id LEFT JOIN scene_category as c ON c.scene_category_id=a.scene_category_id LEFT JOIN task_value_type as d ON d.task_value_type_id=a.task_value_type_id ORDER BY a.bot_task_template_tf_id ASC LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result      
    def get_scene_json(data):
        mc = mysql_connect.cursor()
        query = "SELECT scene_id,scene_name FROM scene WHERE scene_category_id = %s"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result        
    def get_group():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group"
        mc.execute(query)
        result = mc.fetchall()
        return result 
