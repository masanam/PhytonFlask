from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function/model/')
from model_NEW_task_function import DataList

class NewController():
    def new_controller():
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

        list_scene_cat = DataList.get_scene_cat()
        list_scene     = DataList.get_scene()

        count = DataList.count_data()
        return render_template('tmpl_NEW_task_function.html', title='List Task function',listdata=result, countdata=count, listdataS=list_scene, listdataSC=list_scene_cat)
    def select_controller():
        checkId = request.form.get('task_value_group_id')
        checkName = request.form.get('task_value_group_name')
        checkCount = request.form.get('task_value_group_count')

        task_function_id = request.args.get('task_function_id')
        task_function_name = request.args.get('task_function_name')

        task_value_type_id = request.args.get('task_value_type_id')
        task_value_type_name = request.args.get('task_value_type_name')

        scene_category_id = request.args.get('scene_category_id')
        scene_id = request.args.get('scene_id')

        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('search')
        text1= request.form.get('search1')
        count = DataList.count_data()
        list_scene_cat = DataList.get_scene_cat()
        list_scene     = DataList.get_scene()
        
        if request.form.get('search'):            
            result = DataList.search_data(text)
        elif request.form.get('search1'):            
            result = DataList.search_data1(text1)    
        else:
            result = DataList.get_task_value_group(start,limit)

        if request.form.get('Btn_save'):
            task_function_id = request.form.get('task_function_id')
            task_function_name = request.form.get('task_function_name')
            task_value_type_id = request.form.get('task_value_type_id')
            task_value_type_name = request.form.get('task_value_type_name')
            scene_category_id = request.form.get('scene_category_id')
            scene_id = request.form.get('scene_id')

            return render_template('tmpl_NEW_task_function.html', title='New Task function',listdata=result, countdata=count, listdataS=list_scene, listdataSC=list_scene_cat, task_value_group_id=checkId, task_value_group_name=checkName, task_value_group_count=checkCount, task_value_type_id=task_value_type_id, task_value_type_name=task_value_type_name, task_function_id=task_function_id, task_function_name=task_function_name,scene_category_id=scene_category_id,scene_id=scene_id)  
        else:
            return render_template('tmpl_SELECT_task_value_group.html', title='List _task_value_group',listdata=result, countdata=count,  task_value_type_id=task_value_type_id, task_value_type_name=task_value_type_name, task_function_id=task_function_id, task_function_name=task_function_name,scene_category_id=scene_category_id,scene_id=scene_id)     
