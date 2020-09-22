#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task type/controller/')

from controller_CSV_bot_task_type import CSVController 

CSV_bot_task_type = Blueprint('CSV_bot_task_type', __name__,
                        template_folder='template')

@CSV_bot_task_type.route("/view_CSV_bot_task_type", methods=['GET', 'POST'])
def view_CSV_bot_task_type():
                return CSVController.CSV_controller()
