#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function/controller/')

from controller_NEW_task_function import NewController 

NEW_task_function = Blueprint('NEW_task_function', __name__,
                        template_folder='template')

@NEW_task_function.route("/view_NEW_task_function", methods=['GET', 'POST'])
def view_NEW_task_function():
                return NewController.new_controller()
@NEW_task_function.route("/scene_NEW_task_function", methods=['GET', 'POST'])
def scene_NEW_task_function():
                return NewController.scene_controller()                


