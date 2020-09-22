from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value/model/')
from model_LIST_task_value import DataList

class NewController():
    def new_controller():
        list_data = DataList.get_category()
        list_data1 = DataList.get_category1()
        list_data2 = DataList.get_category2()
        list_data3 = DataList.get_category3()

        return render_template('tmpl_NEW_task_value.html', title='New Task Value', listdata=list_data, listdata1=list_data1, listdata2=list_data2, listdata3=list_data3)

