#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value group/controller/')

from controller_EDIT_task_value_group import EditController 

EDIT_task_value_group = Blueprint('EDIT_task_value_group', __name__,
                        template_folder='template')

@EDIT_task_value_group.route("/view_EDIT_task_value_group", methods=['GET', 'POST'])
def view_EDIT_task_value_group():
                return EditController.edit_controller()
