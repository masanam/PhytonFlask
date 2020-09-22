#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user/controller/')

from controller_NEW_bot_user import NewController 

NEW_bot_user = Blueprint('NEW_bot_user', __name__,
                        template_folder='template')

@NEW_bot_user.route("/view_NEW_bot_user", methods=['GET', 'POST'])
def view_NEW_bot_user():
                return NewController.new_controller()
