from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene/model/')
from model_LIST_scene import DataList
from datetime import datetime

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('search')
        text1= request.form.get('search1')
        logstart = datetime.now()
        
        if request.form.get('search'):            
            result = DataList.search_data(text)
        elif request.form.get('search1'):            
            result = DataList.search_data1(text1)    
        elif request.form.get('Btn_save'):
            name = request.form['name']
            description = request.form['description']
            category = request.form['scene_category']
            save_data = DataList.save_data(category, name,description)
            x = request.form['name']
            DataList.update_log('Add New - '+x,1,logstart)
            result = DataList.get_data(start,limit)    
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_scene.html', title='List Scene',listdata=result, countdata=count)