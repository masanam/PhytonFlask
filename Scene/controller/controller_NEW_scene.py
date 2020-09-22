from flask import request
from flask import render_template
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene/model/')
from model_LIST_scene import DataList

class NewController():

    def new_controller():
        list_data = DataList.get_scene_cat()
        return render_template('tmpl_NEW_scene.html', title='NEW scene',listdataSC=list_data)