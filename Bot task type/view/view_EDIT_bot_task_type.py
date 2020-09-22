#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task type/controller/')

from controller_EDIT_bot_task_type import EditController 

EDIT_bot_task_type = Blueprint('EDIT_bot_task_type', __name__,
                        template_folder='template')

@EDIT_bot_task_type.route("/view_EDIT_bot_task_type", methods=['GET', 'POST'])
def Edit_bot_task_type():
                return EditController.edit_controller()
