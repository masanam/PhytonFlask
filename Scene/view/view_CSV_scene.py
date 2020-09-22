#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene/controller/')

from controller_CSV_scene import CSVController 

CSV_scene = Blueprint('CSV_scene', __name__,
                        template_folder='template')

@CSV_scene.route("/view_CSV_scene", methods=['GET', 'POST'])
def view_CSV_scene():
                return CSVController.CSV_controller()
