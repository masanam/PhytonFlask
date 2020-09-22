#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Log/controller/')

from controller_EDIT_log import EditController 


EDIT_log = Blueprint('EDIT_log', __name__,
                        template_folder='template')

@EDIT_log.route("/view_EDIT_log", methods=['GET', 'POST'])
def Edit_log():
                return EditController.edit_controller()
