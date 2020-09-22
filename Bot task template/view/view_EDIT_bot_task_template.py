#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task template/controller/')

from controller_EDIT_bot_task_template import EditController 

EDIT_bot_task_template = Blueprint('EDIT_bot_task_template', __name__,
                        template_folder='template')

@EDIT_bot_task_template.route("/view_EDIT_bot_task_template", methods=['GET', 'POST'])
def Edit_bot_task_template():
                return EditController.edit_controller()
