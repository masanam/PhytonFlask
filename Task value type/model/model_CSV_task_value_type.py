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
            mc.execute('INSERT INTO task_value_type(task_value_type_name, created_at) VALUES (%s,%s)' , (row,now)  )
        mysql_connect.commit()
        mc.close()

    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_type ORDER BY task_value_type_id DESC LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_type ORDER BY task_value_type_id DESC LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result    
    def count_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_type"
        mc.execute(query)
        mc.fetchall()
        count = mc.rowcount
        return count	
    def search_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_type WHERE task_value_type_name = %s ORDER BY task_value_type_id DESC"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def search_data1(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_type WHERE task_value_type_name = %s ORDER BY task_value_type_id DESC"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def delete_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_value_type WHERE task_value_type_name = %s ORDER BY task_value_type_id DESC"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result    
    def save_data(name,description,filename, filerow):
        mc = mysql_connect.cursor()
        query = "INSERT INTO task_value_type_file (name, description, file_name, file_row) VALUES (%s,%s,%s,%s)"
        data = (name,description,filename, filerow)
        mc.execute(query,(data) )
        mysql_connect.commit()
        result = mc.fetchall()
        return result        
