#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value/controller/')

from controller_LIST_task_value import ListController 

LIST_task_value = Blueprint('LIST_task_value', __name__,
                        template_folder='template')

@LIST_task_value.route("/view_LIST_task_value", methods=['GET', 'POST'])
def view_LIST_task_value():
                return ListController.list_controller()
