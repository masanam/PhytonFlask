#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user/controller/')

from controller_EDIT_bot_user import EditController 

EDIT_bot_user = Blueprint('EDIT_bot_user', __name__,
                        template_folder='template')

@EDIT_bot_user.route("/view_EDIT_bot_user", methods=['GET', 'POST'])
def Edit_bot_user():
                return EditController.edit_controller()
