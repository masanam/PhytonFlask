#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value type/controller/')

from controller_CSV_task_value_type import CSVController 

CSV_task_value_type = Blueprint('CSV_task_value_type', __name__,
                        template_folder='template')

@CSV_task_value_type.route("/view_CSV_task_value_type", methods=['GET', 'POST'])
def view_CSV_task_value_type():
                return CSVController.CSV_controller()
