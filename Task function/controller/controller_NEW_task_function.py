from flask import request
from flask import render_template
import sys
import json
from main import getPath

sys.path.insert(1, getPath()+'/Task function/model/')
from model_NEW_task_function import DataList

class NewController():
    def scene_controller():
        data= request.form['category']
        # request.form.get('category_id')
        # request.POST.get('var2')
        result = DataList.get_scene_json(data)
        # print(result)
        return json.dumps(result)

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

        if request.form.get('Btn_save'):
            task_function_id = request.form.get('task_function_id')
            task_function_name = request.form.get('task_function_name')

            scene_category_id = request.form.get('scene_category_id')
            scene_category = request.form['scene_category']

            scene_id = request.form.get('scene_id')
            scene = request.form['scene']

            task_value_type_id = request.form.get('task_value_type_id')
            task_value_type_name = request.form.get('task_value_type_name')

            task_value_group_id = request.form.get('task_value_group_id')
            task_value_group_name = request.form.get('task_value_group_name')

            task_value_count = request.form.get('task_value_count')
            unique_value = request.form['options']
            comment = request.form.get('comment')
            list_group     = DataList.get_group()

            DataList.save_data(task_function_id, task_function_name, scene_category_id, scene_category, scene_id, scene, task_value_type_id, task_value_type_name, task_value_group_id, task_value_group_name, task_value_count, unique_value, comment)
            result = DataList.get_task_function(start,limit)

            return render_template('tmpl_NEW_bot_task_template.html', title='NEW bot task template',listdata=result,count=count,list_group =list_group )
        else:
            return render_template('tmpl_NEW_task_function.html', title='NEW Task function',listdata=result, countdata=count, listdataS=list_scene, listdataSC=list_scene_cat)
    
    def select_controller():
        checkId = request.form.get('task_function_id')
        checkName = request.form.get('task_function_name')

        scene_category_id = request.form.get('scene_category_id')
        scene_id = request.form.get('scene_id')

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
            result = DataList.get_data(start,limit)
        
        if request.form.get('Btn_Save'):
            return render_template('tmpl_NEW_task_function.html', title='New Task function',listdata=result, countdata=count, listdataS=list_scene, listdataSC=list_scene_cat, task_function_id=checkId, task_function_name=checkName, scene_category_id=scene_category_id,scene_id=scene_id)  
        else:
            return render_template('tmpl_SELECT_task_function.html', title='List Task function',listdata=result, countdata=count,scene_category_id=scene_category_id,scene_id=scene_id)     
