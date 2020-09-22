#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task template/controller/')

from controller_LIST_bot_task_template import ListController 

LIST_bot_task_template = Blueprint('LIST_bot_task_template', __name__,
                        template_folder='template')

@LIST_bot_task_template.route("/view_LIST_bot_task_template", methods=['GET', 'POST'])
def view_LIST_bot_task_template():
                return ListController.list_controller()
