from flask import request
from flask import render_template

class EditController():

    def edit_controller():
        return render_template('tmpl_EDIT_task_value_type.html', title='EDIT task value type')