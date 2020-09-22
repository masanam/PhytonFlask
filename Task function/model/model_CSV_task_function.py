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
            id2 = int(row[2])
            id4 = int(row[4])
            id6 = int(row[6])

            mc.execute('INSERT INTO task_function(task_function_name, task_function_content , task_function_category_id , task_function_category, task_value_group_id ,task_value_group, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)' , (row[0],row[1],id2,row[3],id4,row[5],id6,now)  )
        mysql_connect.commit()
        mc.close()

    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_function ORDER BY task_function_id DESC LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_function ORDER BY task_function_id DESC LIMIT %s,%s "
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
        query = "SELECT * FROM task_function WHERE task_function_category = %s ORDER BY task_function_id DESC"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def search_data1(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_function WHERE task_function_name = %s ORDER BY task_function_id DESC"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def delete_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM task_function WHERE task_function_name = %s ORDER BY task_function_id DESC"
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result    
    def save_data(name,description,filename, filerow):
        mc = mysql_connect.cursor()
        query = "INSERT INTO task_function_file (name, description, file_name, file_row) VALUES (%s,%s,%s,%s)"
        data = (name,description,filename, filerow)
        mc.execute(query,(data) )
        mysql_connect.commit()
        result = mc.fetchall()
        return result        
