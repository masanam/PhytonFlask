#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from main import getPath

import sys

sys.path.insert(1, getPath()+'/Bot task/controller/')

from controller_NEW_bot_task import NewController 
NEW_bot_task = Blueprint('NEW_bot_task', __name__,
                        template_folder='template')

@NEW_bot_task.route("/view_NEW_bot_task", methods=['GET', 'POST'])
def view_NEW_bot_task():
                return NewController.new_controller()

        