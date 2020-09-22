#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from main import getPath

import sys

sys.path.insert(1, getPath()+'/Bot task/controller/')

from controller_EDIT_bot_task import EditController 

EDIT_bot_task = Blueprint('EDIT_bot_task', __name__,
                        template_folder='template')

@EDIT_bot_task.route("/view_EDIT_bot_task", methods=['GET', 'POST'])
def view_EDIT_bot_task():
                return EditController.edit_controller()

        