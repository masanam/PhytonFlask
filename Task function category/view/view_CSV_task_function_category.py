#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function category/controller/')

from controller_CSV_task_function_category import CSVController 

CSV_task_function_category = Blueprint('CSV_task_function_category', __name__,
                        template_folder='template')

@CSV_task_function_category.route("/view_CSV_task_function_category", methods=['GET', 'POST'])
def view_CSV_task_function_category():
                return CSVController.CSV_controller()
