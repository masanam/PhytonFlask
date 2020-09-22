from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user/model/')
from model_LIST_bot_user import DataList

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        data = request.form.get('search')
        data1 = request.form.get('search1')
        data2 = request.form.get('search2')
        data3 = request.form.get('search3')

        
        if request.form.get('search'):            
            result = DataList.search_data(data)
        elif request.form.get('search1'): 
            result = DataList.search_data1(data1)
        elif request.form.get('search2'): 
            result = DataList.search_data2(data2)
        elif request.form.get('search3'): 
            result = DataList.search_data3(data3)
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_bot_user.html', title='List Bot user',listdata=result, countdata=count)