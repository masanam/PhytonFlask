from flask import request
from flask import render_template
import sys
from datetime import datetime
from main import getPath


sys.path.insert(1, getPath()+'/Bot task template/model/')
from model_NEW_bot_task_template import DataList

class NewController():
    def edit_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        data= request.form.get('search')
        
        if request.form.get('search'):            
            result = DataList.search_data(data)
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_NEW_bot_task_template.html', title='NEW bot task template',listdata=result,count=count)
    def from_new_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int)
        data= request.form.get('search')
        
        if request.form.get('search'):            
            result = DataList.search_data(data)
        else:
            result = DataList.get_template(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_NEW_bot_task_from_template.html', title='NEW bot task from template',listdata=result,count=count)    
    def new_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )

        if request.form.get('Btn_save'):            
            filename    = request.form.get('name')
            description = request.form.get('description')
            group_id = request.form.get('group_id')

            now = datetime.now()
            count = DataList.count_data()
            sn = '1-'+str(count)
            DataList.insert_data(filename,now,group_id,sn,count)
            
            result = DataList.get_data_2(start,limit)
            return render_template('tmpl_LIST_bot_task_template.html', title='List Bot task template',listdata=result, countdata=count)
        elif request.form.get('Btn_delete'):   
            checkId = request.form.getlist('checkbox')
            start = request.form.get('start', default=0, type=int)
            limit= request.form.get('limit', default=20, type=int )

            for x in checkId:
                DataList.delete_data(x)

            result = DataList.get_data(start,limit)
            count = DataList.count_data()
            return render_template('tmpl_NEW_bot_task_template.html', title='NEW bot task template',listdata=result,count=count)
        elif request.form.get('Btn_new1'):            
            filename    = '1'
            
            now = datetime.now()
            DataList.insert_space(filename,now)
            
            result = DataList.get_data(start,limit)
            count = DataList.count_data()
            return render_template('tmpl_NEW_bot_task_template.html', title='NEW bot task template',listdata=result,count=count)
        elif request.form.get('Btn_delete1'):   
            checkId = request.form.getlist('checkbox')
            start = request.form.get('start', default=0, type=int)
            limit= request.form.get('limit', default=20, type=int )

            for x in checkId:
                DataList.delete_space(x)

            result = DataList.get_data(start,limit)
            count = DataList.count_data()
            return render_template('tmpl_NEW_bot_task_template.html', title='NEW bot task template',listdata=result,count=count)
        else :
            start = request.form.get('start', default=0, type=int)
            limit= request.form.get('limit', default=20, type=int )
            data= request.form.get('search')
        
            result = DataList.get_data(start,limit)
            list_group     = DataList.get_group()

            count = DataList.count_data()
            return render_template('tmpl_NEW_bot_task_template.html', title='NEW bot task template',listdata=result,count=count,list_group=list_group)
    


