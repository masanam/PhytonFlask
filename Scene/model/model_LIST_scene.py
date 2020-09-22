import sys
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect
from datetime import datetime

class DataList():
    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name FROM scene AS a LEFT JOIN scene_category AS b ON b.scene_category_id = a.scene_category_id ORDER BY scene_id DESC LIMIT %s,%s"
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result    
    def count_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene"
        mc.execute(query)
        mc.fetchall()
        count = mc.rowcount
        return count	
    def search_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name FROM scene AS a LEFT JOIN scene_category AS b ON b.scene_category_id = a.scene_category_id WHERE b.scene_category_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def search_data1(data):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name FROM scene AS a LEFT JOIN scene_category AS b ON b.scene_category_id = a.scene_category_id WHERE a.scene_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def get_scene_cat():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene_category"
        mc.execute(query)
        result = mc.fetchall()
        return result    
    def save_data(kategori,name,description):
        mc = mysql_connect.cursor()
        now = datetime.now()
        query = "INSERT INTO scene (scene_category_id, scene_name, created_at ) VALUES (%s,%s,%s)"
        data = (kategori,name,now)
        mc.execute(query,(data) )
        mysql_connect.commit()
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
