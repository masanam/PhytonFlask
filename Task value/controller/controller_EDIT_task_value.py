from flask import request
from flask import render_template

class NewController():

    def new_controller():
        return render_template('tmpl_NEW_task_value.html', title='New Task Value')

