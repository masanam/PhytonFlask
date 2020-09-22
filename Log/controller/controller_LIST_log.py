from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Log/model/')
from model_LIST_log import DataList

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        data= request.form.get('text')
        
        if request.form.get('text'):            
            result = DataList.search_data(data)
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_log.html', title='List Log',listdata=result, countdata=count)