#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function/controller/')

from controller_NEW_task_function import NewController 

SELECT_task_function = Blueprint('SELECT_task_function', __name__,
                        template_folder='template')


@SELECT_task_function.route("/view_SELECT_task_function", methods=['GET', 'POST'])
def view_SELECT_task_function():
                return NewController.select_controller()


