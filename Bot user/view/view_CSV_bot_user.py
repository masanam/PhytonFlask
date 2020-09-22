#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user/controller/')

from controller_CSV_bot_user import CSVController 

CSV_bot_user = Blueprint('CSV_bot_user', __name__,
                        template_folder='template')

@CSV_bot_user.route("/view_CSV_bot_user", methods=['GET', 'POST'])
def view_CSV_bot_user():
                return CSVController.CSV_controller()
