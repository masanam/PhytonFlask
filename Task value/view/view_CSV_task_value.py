#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value/controller/')

from controller_CSV_task_value import CSVController 

CSV_task_value = Blueprint('CSV_task_value', __name__,
                        template_folder='template')

@CSV_task_value.route("/view_CSV_task_value", methods=['GET', 'POST'])
def view_CSV_task_value():
                return CSVController.CSV_controller()
