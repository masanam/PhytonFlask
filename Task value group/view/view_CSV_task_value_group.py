#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value group/controller/')

from controller_CSV_task_value_group import CSVController 

CSV_task_value_group = Blueprint('CSV_task_value_group', __name__,
                        template_folder='template')

@CSV_task_value_group.route("/view_CSV_task_value_group", methods=['GET', 'POST'])
def Csv_task_value_group():
                return CSVController.csv_controller()
