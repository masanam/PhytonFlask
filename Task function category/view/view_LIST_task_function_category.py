#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function category/controller/')

from controller_LIST_task_function_category import ListController 

LIST_task_function_category = Blueprint('LIST_task_function_category', __name__,
                        template_folder='template')

@LIST_task_function_category.route("/view_LIST_task_function_category", methods=['GET', 'POST'])
def view_LIST_task_function_category():
                return ListController.list_controller()
