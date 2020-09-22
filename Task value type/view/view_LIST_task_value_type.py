#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value type/controller/')

from controller_LIST_task_value_type import ListController 

LIST_task_value_type = Blueprint('LIST_task_value_type', __name__,
                        template_folder='template')

@LIST_task_value_type.route("/view_LIST_task_value_type", methods=['GET', 'POST'])
def view_LIST_task_value_type():
                return ListController.list_controller()
