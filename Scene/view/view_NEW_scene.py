#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene/controller/')
from controller_NEW_scene import NewController 

NEW_scene = Blueprint('NEW_scene', __name__,
                        template_folder='template')

@NEW_scene.route("/view_NEW_scene", methods=['GET', 'POST'])
def view_NEW_scene():
                return NewController.new_controller()