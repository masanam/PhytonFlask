from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value/model/')
from model_LIST_task_value import DataList

class ListController():
    def list_controller():
        start = request.form.get('start', default=0, type=int)
        limit= request.form.get('limit', default=20, type=int )
        text= request.form.get('text')
        text1= request.form.get('text1')
        text2= request.form.get('text2')
        text3= request.form.get('text3')

        
        if request.form.get('text'):            
            result = DataList.search_data(text)
        elif request.form.get('text1'):            
            result = DataList.search_data1(text1)  
        elif request.form.get('text2'):            
            result = DataList.search_data2(text2)  
        elif request.form.get('text3'):            
            result = DataList.search_data3(text3)     
        elif request.form.get('Btn_save'):
            name = request.form['name']
            content = request.form['content']
            category = request.form['category']
            category1 = request.form['category1']
            category2 = request.form['category2']
            category3 = request.form['category3']
            save_data = DataList.save_data(name, content, category, category1, category2, category3)
            result = DataList.get_data(start,limit)          
        else:
            result = DataList.get_data(start,limit)

        count = DataList.count_data()
        return render_template('tmpl_LIST_task_value.html', title='List Task value',listdata=result, countdata=count)