from flask import request
from flask import render_template
from main import getPath

import sys

sys.path.insert(1, getPath()+'/Bot task/model/')
from model_LIST_bot_task import DataList

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
        elif request.form.get('Btn_save'):
            name = request.form['name']
            sn = request.form['sn']
            category = request.form['category']
            save_data = DataList.save_data(category, name, sn)
            result = DataList.get_data(start,limit)   
        else:
            result = DataList.get_data(start,limit)
        
        count = DataList.count_data()

        count = DataList.count_data()
        return render_template('tmpl_LIST_bot_task.html', title='List Bot task',listdata=result, countdata=count)