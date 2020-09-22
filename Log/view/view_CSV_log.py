#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Log/controller/')

from controller_CSV_log import CSVController 


CSV_log = Blueprint('CSV_log', __name__,
                        template_folder='template')

@CSV_log.route("/view_CSV_log", methods=['GET', 'POST'])
def Csv_log():
                return CSVController.csv_controller()
