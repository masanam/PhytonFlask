#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function category/controller/')

from controller_NEW_task_function_category import NewController 

NEW_task_function_category = Blueprint('NEW_task_function_category', __name__,
                        template_folder='template')

@NEW_task_function_category.route("/view_NEW_task_function_category", methods=['GET', 'POST'])
def view_NEW_task_function_category():
                return NewController.new_controller()
