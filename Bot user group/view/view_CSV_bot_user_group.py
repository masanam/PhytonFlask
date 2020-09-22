#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user group/controller/')

from controller_CSV_bot_user_group import CSVController 

CSV_bot_user_group = Blueprint('CSV_bot_user_group', __name__,
                        template_folder='template')

@CSV_bot_user_group.route("/view_CSV_bot_user_group", methods=['GET', 'POST'])
def view_CSV_bot_user_group():
                return CSVController.csv_controller()
