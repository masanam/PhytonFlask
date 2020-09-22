#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user group/controller/')

from controller_LIST_bot_user_group import ListController 

LIST_bot_user_group = Blueprint('LIST_bot_user_group', __name__,
                        template_folder='template')

@LIST_bot_user_group.route("/view_LIST_bot_user_group", methods=['GET', 'POST'])
def view_LIST_bot_user_group():
                return ListController.list_controller()
