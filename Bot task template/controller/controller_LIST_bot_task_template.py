from flask import request
from flask import render_template
from main import getPath

import sys

sys.path.insert(1, getPath()+'/Bot task template/model/')
from model_LIST_bot_task_template import DataList

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        data= request.form.get('search')
        data1= request.form.get('search1')
        
        if request.form.get('search'):            
            result = DataList.search_data(data)
        elif request.form.get('search1'):            
            result = DataList.search_data1(data1)
        elif request.form.get('Btn_save'):
            checkId = request.form.get('bot_task_template_id')
            name = request.form['name']
            last_sn = request.form['last_sn']
            
            for x in range(int(last_sn)):
                DataList.save_bot_task(name, checkId, x)

            result = DataList.get_bot_task(start,limit)   
            count = DataList.count_bot_task()   
        else:
            result = DataList.get_data(start,limit)
            count = DataList.count_data()

        if request.form.get('Btn_save'):
            return render_template('tmpl_LIST_bot_task.html', title='List Bot task',listdata=result, countdata=count)
        else:
            return render_template('tmpl_LIST_bot_task_template.html', title='List Bot task template',listdata=result, countdata=count)
