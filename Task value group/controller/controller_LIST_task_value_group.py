from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value group/model/')
from model_LIST_task_value_group import DataList

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
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_task_value_group.html', title='List Task value group',listdata=result, countdata=count)