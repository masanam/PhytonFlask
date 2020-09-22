#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from main import getPath

import sys

sys.path.insert(1, getPath()+'/Bot task/controller/')

from controller_LIST_bot_task import ListController 

LIST_bot_task = Blueprint('LIST_bot_task', __name__,
                        template_folder='template')

@LIST_bot_task.route("/view_LIST_bot_task", methods=['GET', 'POST'])
def view_LIST_bot_task():
                return ListController.list_controller()

        