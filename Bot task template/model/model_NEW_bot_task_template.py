import sys
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect

class DataList():
    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task_template LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_name, c.scene_category_name, d.task_value_type_name FROM bot_task_template_tf as a LEFT JOIN scene as b ON b.scene_id = a.scene_id LEFT JOIN scene_category as c ON c.scene_category_id=a.scene_category_id LEFT JOIN task_value_type as d ON d.task_value_type_id=a.task_value_type_id ORDER BY a.bot_task_template_tf_id ASC LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result    
    def get_data_2(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.bot_user_group_name FROM bot_task_template as a LEFT JOIN bot_user_group as b ON b.bot_user_group_id = a.bot_user_group_name ORDER BY bot_task_template_id DESC LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result     
    def count_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task_template_tf where task_function != '' "
        mc.execute(query)
        mc.fetchall()
        count = mc.rowcount
        return count	
    def search_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_task_template_tf WHERE bot_task_template_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def insert_data(filename,now,group_id,sn,count):
        mc = mysql_connect.cursor()
        query = "INSERT INTO bot_task_template (bot_task_template_name,created_at,bot_user_group_name,sn_range,cloned_create_bot_task_groups)  VALUES (%s,%s,%s,%s,%s) "
        mc.execute(query,(filename,now,group_id,sn,count) )
        result = mc.fetchall()
        return result     
    def delete_data(data):
        mc = mysql_connect.cursor()
        query = "DELETE FROM bot_task_template_tf WHERE bot_task_template_tf_id = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result    
    def insert_space(filename,now):
        mc = mysql_connect.cursor()
        query = "INSERT INTO bot_task_template_tf (space,created_at)  VALUES (%s,%s) "
        mc.execute(query,(filename,now) )
        result = mc.fetchall()
        return result     
    def delete_space(data):
        mc = mysql_connect.cursor()
        query = "DELETE FROM bot_task_template_tf WHERE bot_task_template_tf_id = %s AND space = '1'"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result      
    def get_template(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.bot_user_group_name FROM bot_task_template as a LEFT JOIN bot_user_group as b ON b.bot_user_group_id = a.bot_user_group_name ORDER BY bot_task_template_id DESC LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result     
    def get_group():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group"
        mc.execute(query)
        result = mc.fetchall()
        return result   
