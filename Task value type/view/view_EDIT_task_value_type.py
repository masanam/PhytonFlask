#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value type/controller/')

from controller_EDIT_task_value_type import EditController 

EDIT_task_value_type = Blueprint('EDIT_task_value_type', __name__,
                        template_folder='template')

@EDIT_task_value_type.route("/view_EDIT_task_value_type", methods=['GET', 'POST'])
def Edit_task_value_type():
                return EditController.edit_controller()
