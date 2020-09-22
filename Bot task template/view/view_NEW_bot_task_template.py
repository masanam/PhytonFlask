#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task template/controller/')

from controller_NEW_bot_task_template import NewController 

NEW_bot_task_template = Blueprint('NEW_bot_task_template', __name__,
                        template_folder='template')

@NEW_bot_task_template.route("/view_NEW_bot_task_template", methods=['GET', 'POST'])
def view_NEW_bot_task_template():
                return NewController.new_controller()   
@NEW_bot_task_template.route("/view_NEW_bot_task_from_template", methods=['GET', 'POST'])
def view_NEW_bot_task_from_template():
                return NewController.from_new_controller()                   

