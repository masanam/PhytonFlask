#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

EDIT_task_function = Blueprint('EDIT_task_function', __name__,
                        template_folder='template')

@EDIT_task_function.route("/view_EDIT_task_function", methods=['GET', 'POST'])
def Edit_task_function():
    try:
        return render_template('some_demo.html')
    except TemplateNotFound:
        abort(404)