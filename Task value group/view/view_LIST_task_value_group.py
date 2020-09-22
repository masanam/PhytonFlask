#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value group/controller/')

from controller_LIST_task_value_group import ListController 

LIST_task_value_group = Blueprint('LIST_task_value_group', __name__,
                        template_folder='template')

@LIST_task_value_group.route("/view_LIST_task_value_group", methods=['GET', 'POST'])
def view_LIST_task_value_group():
                return ListController.list_controller()
