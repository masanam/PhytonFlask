#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function category/controller/')

from controller_EDIT_task_function_category import EditController 

EDIT_task_function_category = Blueprint('EDIT_task_function_category', __name__,
                        template_folder='template')

@EDIT_task_function_category.route("/view_EDIT_task_function_category", methods=['GET', 'POST'])
def Edit_task_function_category():
                return EditController.list_controller()
