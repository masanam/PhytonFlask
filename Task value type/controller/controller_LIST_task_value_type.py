from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value type/model/')
from model_LIST_task_value_type import DataList

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('search')
        text1= request.form.get('search1')

        
        if request.form.get('search'):            
            result = DataList.search_data(text)
        elif request.form.get('search1'):            
            result = DataList.search_data1(text1)  
        elif request.form.get('Btn_save'):
            name = request.form['name']
            description = request.form['description']
            save_data = DataList.save_data(name,description)
            result = DataList.get_data(start,limit)    
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_task_value_type.html', title='List Task value type',listdata=result, countdata=count)