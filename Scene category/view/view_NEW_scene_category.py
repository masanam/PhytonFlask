#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene category/controller/')
from controller_NEW_scene_category import NewController 

NEW_scene_category = Blueprint('NEW_scene_category', __name__,
                        template_folder='template')

@NEW_scene_category.route("/view_NEW_scene_category", methods=['GET', 'POST'])
def view_NEW_scene_category():
                return NewController.new_controller()