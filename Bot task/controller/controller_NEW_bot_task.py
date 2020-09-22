from flask import request
from flask import render_template
from main import getPath

import sys

sys.path.insert(1, getPath()+'/Bot task/model/')
from model_LIST_bot_task import DataList

class NewController():
    def new_controller():
        list_data = DataList.get_category()
        return render_template('tmpl_NEW_bot_task.html', title='Edit Bot Task', listdata=list_data)

