from flask import request
from flask import render_template
import sys
from main import getPath

# sys.path.insert(1, 'C:/python/Automation/Run bot task/model/')
sys.path.insert(1, getPath()+'/Run bot task/model/')
from model_LIST_run_bot_task import DataList

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('search')
        from_sn= request.form.get('from_sn')
        to_sn= request.form.get('to_sn')


        if request.form.get('search'):            
            result = DataList.search_data(text)
        elif request.form.get('from_sn'):            
            result = DataList.search_data1(from_sn,to_sn)    
        else:
            result = DataList.get_data(start,limit)
        
        count = DataList.count_data()
        return render_template('tmpl_LIST_run_bot_task.html', title='List Run bot task',listdata=result, countdata=count)