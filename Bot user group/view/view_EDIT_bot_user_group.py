#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user group/controller/')

from controller_EDIT_bot_user_group import EditController 

EDIT_bot_user_group = Blueprint('EDIT_bot_user_group', __name__,
                        template_folder='template')

@EDIT_bot_user_group.route("/view_EDIT_bot_user_group", methods=['GET', 'POST'])
def view_EDIT_bot_user_group():
                return EditController.edit_controller()
