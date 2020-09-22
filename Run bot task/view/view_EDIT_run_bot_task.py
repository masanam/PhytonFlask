#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

EDIT_run_bot_task = Blueprint('EDIT_run_bot_task', __name__,
                        template_folder='template')

@EDIT_run_bot_task.route("/view_EDIT_run_bot_task", methods=['GET', 'POST'])
def view_EDIT_run_bot_task():
    try:
        return render_template('some_demo.html')
    except TemplateNotFound:
        abort(404)