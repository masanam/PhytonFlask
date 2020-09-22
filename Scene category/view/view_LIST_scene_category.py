#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Scene category/controller/')

from controller_LIST_scene_category import ListController 

LIST_scene_category = Blueprint('LIST_scene_category', __name__,
                        template_folder='template')

@LIST_scene_category.route("/view_LIST_scene_category", methods=['GET', 'POST'])
def view_LIST_scene_category():
                return ListController.list_controller()

   