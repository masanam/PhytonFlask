from flask import request
from flask import render_template

class EditController():

    def edit_controller():
        return render_template('tmpl_EDIT_scene.html', title='Edit Scene')