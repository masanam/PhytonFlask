        #import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Run bot task/controller/')

from controller_LIST_run_bot_task import ListController 

LIST_run_bot_task = Blueprint('LIST_run_bot_task', __name__,
                        template_folder='template')

@LIST_run_bot_task.route("/view_LIST_run_bot_task", methods=['GET', 'POST'])
def view_LIST_run_bot_task():
                return ListController.list_controller()
@LIST_run_bot_task.route("/view_RUN_run_bot_task", methods=['GET', 'POST'])
def view_RUN_run_bot_task():
                return ListController.run_run_controller()
