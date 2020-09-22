#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function/controller/')

from controller_LIST_task_function import ListController 

LIST_task_function = Blueprint('LIST_task_function', __name__,
                        template_folder='template')

@LIST_task_function.route("/view_LIST_task_function", methods=['GET', 'POST'])
def view_LIST_task_function():
                return ListController.list_controller()
