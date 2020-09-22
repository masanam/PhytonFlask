#import blueprint

from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/main/controller/')

from main_controller import ListController 

index_blueprint = Blueprint('index', __name__,template_folder='template', static_folder='static')

@index_blueprint.route("/", methods=['GET', 'POST'])
def index():
        return ListController.list_controller()
