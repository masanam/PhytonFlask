#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task function/controller/')

from controller_SELECT_task_value_group import NewController 

SELECT_task_value_group = Blueprint('SELECT_task_value_group', __name__,
                        template_folder='template')


@SELECT_task_value_group.route("/view_SELECT_task_value_group", methods=['GET', 'POST'])
def view_SELECT_task_value_group():
                return NewController.select_controller()


