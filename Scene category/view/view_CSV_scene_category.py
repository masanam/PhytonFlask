#import blueprint

from flask import Blueprint, render_template, abort,request
from jinja2 import TemplateNotFound
import sys
from flask import Flask
import csv
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect

sys.path.insert(1, getPath()+'/Scene category/controller/')
from controller_CSV_scene_category import CSVController 

CSV_scene_category = Blueprint('CSV_scene_category', __name__,
                        template_folder='template')

@CSV_scene_category.route("/view_CSV_scene_category", methods=['GET', 'POST'])
def view_CSV_scene_category():
    # param = request.args.get('param')
    # print(request.args.get('param'))
    # if param == '1' :
    #     return CSVController.import_CSV_controller()
    # else:
        return CSVController.CSV_controller()    


		
		
		
		
   