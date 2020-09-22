#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Bot user/controller/')

from controller_LIST_bot_user import ListController 

LIST_bot_user = Blueprint('LIST_bot_user', __name__,
                        template_folder='template')

@LIST_bot_user.route("/view_LIST_bot_user", methods=['GET', 'POST'])
def view_LIST_bot_user():
                return ListController.list_controller()
