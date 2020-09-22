from flask import request
from flask import render_template

class CSVController():

    def csv_controller():
        return render_template('tmpl_CSV_log.html', title='Csv Log')

