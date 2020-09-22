from flask import request
from flask import render_template
import sys
import os
import csv
from main import getPath

sys.path.insert(1, getPath()+'/Task function category/model/')
from model_CSV_task_function_category import DataCSV

class CSVController():
    def CSV_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )

        if request.form.get('import_CSV'): 
            file_path = request.form.get('CSV_file_name')
            DataCSV.import_data(file_path)
            csv_data = csv.reader(open(file_path))
            row_count = (sum(1 for row in csv_data)) - 1 
            result = DataCSV.get_data(start,limit)
        elif request.form.get('Btn_delete'):
            data = request.form['name']
            DataCSV.delete_data(data)  
        elif request.form.get('Btn_save'):
            name = request.form['name']
            description = request.form['description']
            filename = request.form['filename']
            filerow = request.form['filerow']
            file_path = ''
            row_count = 0
            result = DataCSV.get_data(start,limit)
            DataCSV.save_data(name,description,filename,filerow)      
        elif request.form.get('Btn_search'):       
            text =  request.form.get('search')
            result = DataCSV.search_data(text)    
            file_path = ''
            row_count = 0
        elif request.form.get('Btn_search1'):       
            text1 =  request.form.get('search1')
            result = DataCSV.search_data1(text1)    
            file_path = ''
            row_count = 0    
        else:
            result = DataCSV.get_data(start,limit)
            file_path = ''
            row_count = 0

        path, filename = os.path.split(file_path)
        count = DataCSV.count_data()

        if request.form.get('Btn_save'):
            return render_template('tmpl_LIST_task_function_category.html', title='List Task function category',listdata=result, countdata=count)   
        else:
            return render_template('tmpl_CSV_task_function_category.html', title='CSV Task function category',csvdata=result,countdata=count,filepath=filename,csvrow=row_count)       