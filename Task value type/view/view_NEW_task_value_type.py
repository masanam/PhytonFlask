#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value type/controller/')

from controller_NEW_task_value_type import NewController 

NEW_task_value_type = Blueprint('NEW_task_value_type', __name__,
                        template_folder='template')

@NEW_task_value_type.route("/view_NEW_task_value_type", methods=['GET', 'POST'])
def view_NEW_task_value_type():
                return NewController.new_controller()
