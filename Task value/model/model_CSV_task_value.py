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
            mc.execute('INSERT INTO task_value(task_value_name, task_value_category ,created_at) VALUES (%s, %s, %s)' , (row[0],row[1],now)  )
        mysql_connect.commit()
        mc.close()

    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value ORDER BY task_value_id DESC LIMIT 0,20 "
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
        LIMIT %s,%s "
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
        WHERE task_value_group = %s "
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
        WHERE task_value_type = %s "
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
    def save_data(name,description,filename, filerow):
        mc = mysql_connect.cursor()
        query = "INSERT INTO task_value_file (name, description, file_name, file_row) VALUES (%s,%s,%s,%s)"
        data = (name,description,filename, filerow)
        mc.execute(query,(data) )
        mysql_connect.commit()
        result = mc.fetchall()
        return result        
