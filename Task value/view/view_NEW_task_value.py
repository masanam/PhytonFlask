#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import sys
from main import getPath

sys.path.insert(1, getPath()+'/Task value/controller/')

from controller_NEW_task_value import NewController 

NEW_task_value= Blueprint('NEW_task_value', __name__,
                        template_folder='template')

@NEW_task_value.route("/view_NEW_task_value", methods=['GET', 'POST'])
def view_NEW_task_value():
                return NewController.new_controller()                
