#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene category/controller/')
from controller_EDIT_scene_category import EditController 

EDIT_scene_category = Blueprint('EDIT_scene_category', __name__,
                        template_folder='template')

@EDIT_scene_category.route("/view_EDIT_scene_category", methods=['GET', 'POST'])
def view_EDIT_scene_category():
                return EditController.edit_controller()