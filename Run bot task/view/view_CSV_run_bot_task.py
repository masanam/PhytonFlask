#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

CSV_run_bot_task = Blueprint('CSV_run_bot_task', __name__,
                        template_folder='template')

@CSV_run_bot_task.route("/view_CSV_run_bot_task", methods=['GET', 'POST'])
def Csv_run_bot_task():
    try:
        return render_template('some_demo.html')
    except TemplateNotFound:
        abort(404)