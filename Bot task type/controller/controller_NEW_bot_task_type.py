from flask import request
from flask import render_template

class NewController():

    def new_controller():
        return render_template('tmpl_NEW_bot_task_type.html', title='NEW bot task type')