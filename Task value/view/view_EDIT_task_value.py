#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

EDIT_task_value = Blueprint('EDIT_task_value', __name__,
                        template_folder='template')

@EDIT_task_value.route("/view_EDIT_task_value", methods=['GET', 'POST'])
def Edit_task_value():
    try:
        return render_template('some_demo.html')
    except TemplateNotFound:
        abort(404)