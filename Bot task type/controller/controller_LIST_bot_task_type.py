from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task type/model/')
from model_LIST_bot_task_type import DataList

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        data= request.form.get('search')
        
        if request.form.get('search'):            
            result = DataList.search_data(data)
        elif request.form.get('Btn_save'):
            name = request.form['name']
            description = request.form['description']
            save_data = DataList.save_data(name,description)
            result = DataList.get_data(start,limit)    
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_bot_task_type.html', title='List Bot task type',listdata=result, countdata=count)