#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from main import getPath

import sys

sys.path.insert(1, getPath()+'/Bot task/controller/')

from controller_CSV_bot_task import CSVController 

CSV_bot_task = Blueprint('CSV_bot_task', __name__,
                        template_folder='template')

@CSV_bot_task.route("/view_CSV_bot_task", methods=['GET', 'POST'])
def view_CSV_bot_task():
                return CSVController.csv_controller()

        