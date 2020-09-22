from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene category/model/')
from model_LIST_scene_category import DataList
from datetime import datetime

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        data= request.form.get('search')
        logstart = datetime.now()

        if request.form.get('search'):            
            result = DataList.search_data(data)
        elif request.form.get('Btn_save'):
            name = request.form['name']
            description = request.form['description']
            DataList.save_data(name,description)
            result = DataList.get_data(start,limit)
            x = request.form['name']
            DataList.update_log('Add New - '+x,1,logstart)
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_scene_category.html', title='List Scene Category',listdata=result, countdata=count)