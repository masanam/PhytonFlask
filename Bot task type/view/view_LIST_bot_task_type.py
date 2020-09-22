#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task type/controller/')

from controller_LIST_bot_task_type import ListController 

LIST_bot_task_type = Blueprint('LIST_bot_task_type', __name__,
                        template_folder='template')

@LIST_bot_task_type.route("/view_LIST_bot_task_type", methods=['GET', 'POST'])
def view_LIST_bot_task_type():
                return ListController.list_controller()
