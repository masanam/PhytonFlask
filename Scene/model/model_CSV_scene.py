from flask import Flask
import sys
import csv
import os.path
from main import getPath

sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect
from datetime import datetime

class DataCSV():
    def import_data(file_path):
        mc = mysql_connect.cursor()
        csv_data = csv.reader(open(file_path))
        next(csv_data)
        now = datetime.now()
        for row in csv_data:
            mc.execute('INSERT INTO scene(scene_name, scene_category, scene_category_id, created_at) VALUES (%s, %s, %s, %s)' , (row[0],row[1],row[2],now)  )
        mysql_connect.commit()
        mc.close()

    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene ORDER BY scene_id DESC LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT a.*, b.scene_category_name FROM scene AS a LEFT JOIN scene_category AS b ON b.scene_category_id = a.scene_category_id LIMIT %s,%s"
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
    def delete_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM scene WHERE scene_name = %s ORDER BY scene_id DESC"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result    
    def save_data(name,description,filename, filerow):
        mc = mysql_connect.cursor()
        query = "INSERT INTO scene_file (name, description, file_name, file_row) VALUES (%s,%s,%s,%s)"
        data = (name,description,filename, filerow)
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
