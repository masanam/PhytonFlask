#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot task template/controller/')

from controller_CSV_bot_task_template import CSVController 

CSV_bot_task_template = Blueprint('CSV_bot_task_template', __name__,
                        template_folder='template')

@CSV_bot_task_template.route("/view_CSV_bot_task_template", methods=['GET', 'POST'])
def Csv_bot_task_template():
                return CSVController.csv_controller()
