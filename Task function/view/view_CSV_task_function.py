#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

CSV_task_function = Blueprint('CSV_task_function', __name__,
                        template_folder='template')

@CSV_task_function.route("/view_CSV_task_function", methods=['GET', 'POST'])
def view_CSV_task_function():
            return render_template('tmpl_CSV_task_function.html')
