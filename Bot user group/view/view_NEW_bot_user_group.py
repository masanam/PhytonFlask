#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user group/controller/')

from controller_NEW_bot_user_group import NewController 

NEW_bot_user_group = Blueprint('NEW_bot_user_group', __name__,
                        template_folder='template')

@NEW_bot_user_group.route("/view_NEW_bot_user_group", methods=['GET', 'POST'])
def view_NEW_bot_user_group():
                return NewController.new_controller()
@NEW_bot_user_group.route("/clone_NEW_bot_user_group", methods=['GET', 'POST'])
def clone_NEW_bot_user_group():
                return NewController.clone_controller()
@NEW_bot_user_group.route("/save_NEW_bot_user_group", methods=['GET', 'POST'])
def save_NEW_bot_user_group():
                return NewController.save_controller()                


