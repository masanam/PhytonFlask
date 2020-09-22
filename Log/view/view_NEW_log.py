#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Log/controller/')

from controller_NEW_log import NewController 


NEW_log = Blueprint('NEW_log', __name__,
                        template_folder='template')

@NEW_log.route("/view_NEW_log", methods=['GET', 'POST'])
def New_log():
                return NewController.new_controller()
