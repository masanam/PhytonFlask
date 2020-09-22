#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task type/controller/')

from controller_NEW_bot_task_type import NewController 

NEW_bot_task_type = Blueprint('NEW_bot_task_type', __name__,
                        template_folder='template')

@NEW_bot_task_type.route("/view_NEW_bot_task_type", methods=['GET', 'POST'])
def view_NEW_bot_task_type():
                return NewController.new_controller()
