#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene/controller/')

from controller_LIST_scene import ListController 

LIST_scene = Blueprint('LIST_scene', __name__,
                        template_folder='template')

@LIST_scene.route("/view_LIST_scene", methods=['GET', 'POST'])
def view_LIST_scene():
                return ListController.list_controller()
