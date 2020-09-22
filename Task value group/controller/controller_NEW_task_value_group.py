from flask import request
from flask import render_template
import sys
from datetime import datetime
from main import getPath

sys.path.insert(1, getPath()+'/Task value group/model/')
from model_NEW_task_value_group import DataList

class NewController():
    def new_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('search')
        text1= request.form.get('search1')

        
        if request.form.get('search'):            
            result_tv = DataList.search_data_tv(text)
            result = DataList.get_data(start,limit)
        elif request.form.get('search1'):            
            result_tv = DataList.search_data1_tv(text1)    
            result = DataList.get_data(start,limit)
        else:
            result = DataList.get_data(start,limit)
            result_tv = DataList.get_data_tv(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_NEW_task_value_group.html', title='New Task value group',listdata_tv=result_tv, listdata=result, countdata=count)    
    
    def save_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        filename    = request.form.get('name')
        description = request.form.get('description')
        
        qty = request.form.get('countL')
        now = datetime.now()

        DataList.insert_data(filename,qty,now)
        
        result = DataList.get_data(start,limit)
        count = DataList.count_data()
        return render_template('tmpl_LIST_task_value_group.html', title='List Task value group',listdata=result, countdata=count)

    def insert_controller():
        checkId = request.form.getlist('checkbox')
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        result = DataList.get_data(start,limit)
        count = DataList.count_data()

        for x in checkId:
            DataList.insert_data(x)
        count = DataList.count_data()
        return render_template('tmpl_NEW_task_value_group.html', title='New Task value group', listdata=result, countdata=count)      

    def clone_controller():
        checkId = request.form.getlist('checkbox')
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('search')
        text1= request.form.get('search1')

        if request.form.get('search'):            
            result_tv = DataList.search_data_tv(text)
        elif request.form.get('search1'):            
            result_tv = DataList.search_data1_tv(text1)    
        else:
            result_tv = DataList.get_data_tv(start,limit)

        if checkId:
            resultL = DataList.clone_data(checkId)
            countL = DataList.count_clone_data(checkId)
        else:
            resultL = ''
            countL = 1

        count = DataList.count_data()
        return render_template('tmpl_NEW_task_value_group.html', title='New Task value group', listdata_tv=result_tv, listdataL=resultL, countdata=count, countL=countL)              