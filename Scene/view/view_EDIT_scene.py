#import blueprint

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

EDIT_scene = Blueprint('EDIT_scene', __name__,
                        template_folder='template')

@EDIT_scene.route("/view_EDIT_scene", methods=['GET', 'POST'])
def view_EDIT_scene():
    try:
        return render_template('some_demo.html')
    except TemplateNotFound:
        abort(404)