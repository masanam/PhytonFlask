from flask import request
from flask import render_template
import sys
import os
import csv
from main import getPath

sys.path.insert(1, getPath()+'/Bot task type/model/')
from model_CSV_bot_task_type import DataCSV

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
        else:
            result = DataCSV.get_data(start,limit)
            file_path = ''
            row_count = 0

        path, filename = os.path.split(file_path)
        count = DataCSV.count_data()

        if request.form.get('Btn_save'):
            return render_template('tmpl_LIST_bot_task_type.html', title='List Bot task type',listdata=result, countdata=count)   
        else:
            return render_template('tmpl_CSV_bot_task_type.html', title='CSV Bot task type',csvdata=result,countdata=count,filepath=filename,csvrow=row_count)       