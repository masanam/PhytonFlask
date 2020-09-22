#Must register blueprints with the flask program to run the flask application

from flask import Flask, render_template, request
import sys
import os
from main import getPath

def getPath():
 return str(os.getcwd())
#application.config

# import bot_task_group then register 
sys.path.insert(1, getPath()+'/main/view/')
from main_view import index_blueprint

application = Flask(__name__)
application.register_blueprint(index_blueprint)

sys.path.insert(1, getPath()+'/Run bot task/view/')
from view_CSV_run_bot_task import CSV_run_bot_task
from view_LIST_run_bot_task import LIST_run_bot_task 
from view_EDIT_run_bot_task import EDIT_run_bot_task 

application.register_blueprint(CSV_run_bot_task)
application.register_blueprint(LIST_run_bot_task)
application.register_blueprint(EDIT_run_bot_task)

# import Bot task type then register with blueprint
sys.path.insert(1, getPath()+'/Bot task/view/')
from view_CSV_bot_task import CSV_bot_task
from view_LIST_bot_task import LIST_bot_task 
from view_EDIT_bot_task import EDIT_bot_task
from view_NEW_bot_task import NEW_bot_task

application.register_blueprint(CSV_bot_task)
application.register_blueprint(LIST_bot_task)
application.register_blueprint(EDIT_bot_task)
application.register_blueprint(NEW_bot_task)

# import Bot task type then register with blueprint
sys.path.insert(1, getPath()+'/Bot task template/view/')
from view_CSV_bot_task_template import CSV_bot_task_template
from view_LIST_bot_task_template import LIST_bot_task_template 
from view_EDIT_bot_task_template import EDIT_bot_task_template
from view_NEW_bot_task_template import NEW_bot_task_template


application.register_blueprint(CSV_bot_task_template)
application.register_blueprint(LIST_bot_task_template)
application.register_blueprint(EDIT_bot_task_template)
application.register_blueprint(NEW_bot_task_template)

# import Bot task type then register with blueprint
sys.path.insert(1, getPath()+'/Bot task type/view/')
 
from view_NEW_bot_task_type import NEW_bot_task_type
from view_LIST_bot_task_type import LIST_bot_task_type
from view_CSV_bot_task_type import CSV_bot_task_type
from view_EDIT_bot_task_type import EDIT_bot_task_type

application.register_blueprint(NEW_bot_task_type)
application.register_blueprint(LIST_bot_task_type)
application.register_blueprint(CSV_bot_task_type)
application.register_blueprint(EDIT_bot_task_type)


# # import bot user then register with blueprint
sys.path.insert(1, getPath()+'/Bot user/view/')
 
from view_NEW_bot_user import NEW_bot_user
from view_LIST_bot_user import LIST_bot_user
from view_CSV_bot_user import CSV_bot_user
from view_EDIT_bot_user import EDIT_bot_user
 
application.register_blueprint(NEW_bot_user)
application.register_blueprint(LIST_bot_user)
application.register_blueprint(CSV_bot_user)
application.register_blueprint(EDIT_bot_user)

# # import bot user then register with blueprint
sys.path.insert(1, getPath()+'/Bot user group/view/')
 
from view_NEW_bot_user_group import NEW_bot_user_group
from view_LIST_bot_user_group import LIST_bot_user_group
from view_CSV_bot_user_group import CSV_bot_user_group
from view_EDIT_bot_user_group import EDIT_bot_user_group
 
application.register_blueprint(NEW_bot_user_group)
application.register_blueprint(LIST_bot_user_group)
application.register_blueprint(CSV_bot_user_group)
application.register_blueprint(EDIT_bot_user_group)

# import Scene then register with blueprint 
sys.path.insert(1, getPath()+'/Scene/view/')
 
from view_NEW_scene import NEW_scene 
from view_LIST_scene import LIST_scene 
from view_CSV_scene import CSV_scene
from view_EDIT_scene import EDIT_scene 
 
application.register_blueprint(NEW_scene)
application.register_blueprint(LIST_scene)
application.register_blueprint(CSV_scene)
application.register_blueprint(EDIT_scene)


# import Scene category then register with blueprint
sys.path.insert(1, getPath()+'/Scene category/view/')
 
from view_NEW_scene_category import NEW_scene_category 
from view_LIST_scene_category import LIST_scene_category
from view_CSV_scene_category import CSV_scene_category
from view_EDIT_scene_category import EDIT_scene_category 
 
application.register_blueprint(NEW_scene_category)
application.register_blueprint(LIST_scene_category)
application.register_blueprint(CSV_scene_category)
application.register_blueprint(EDIT_scene_category)


# import Task function then register with blueprint
sys.path.insert(1, getPath()+'/Task function/view/')
 
from view_NEW_task_function import NEW_task_function 
from view_LIST_task_function import LIST_task_function
from view_CSV_task_function import CSV_task_function
from view_EDIT_task_function import EDIT_task_function 
from view_SELECT_task_function import SELECT_task_function 
from view_SELECT_task_value_group import SELECT_task_value_group
from view_SELECT_task_value_type import SELECT_task_value_type

application.register_blueprint(NEW_task_function)
application.register_blueprint(LIST_task_function)
application.register_blueprint(CSV_task_function)
application.register_blueprint(EDIT_task_function)
application.register_blueprint(SELECT_task_function)
application.register_blueprint(SELECT_task_value_group)
application.register_blueprint(SELECT_task_value_type)

# import Task function category then register with blueprint
sys.path.insert(1, getPath()+'/Task function category/view/')
 
from view_NEW_task_function_category import NEW_task_function_category
from view_LIST_task_function_category import LIST_task_function_category
from view_CSV_task_function_category import CSV_task_function_category
from view_EDIT_task_function_category import EDIT_task_function_category 
 
application.register_blueprint(NEW_task_function_category)
application.register_blueprint(LIST_task_function_category)
application.register_blueprint(CSV_task_function_category)
application.register_blueprint(EDIT_task_function_category)


# import Task value then register with blueprint
sys.path.insert(1, getPath()+'/Task value/view/')
 
from view_NEW_task_value import NEW_task_value
from view_LIST_task_value import LIST_task_value
from view_CSV_task_value import CSV_task_value
from view_EDIT_task_value import EDIT_task_value
 
application.register_blueprint(NEW_task_value)
application.register_blueprint(LIST_task_value)
application.register_blueprint(CSV_task_value)
application.register_blueprint(EDIT_task_value)


# import Task value group then register with blueprint
sys.path.insert(1, getPath()+'/Task value group/view/')
 
from view_NEW_task_value_group import NEW_task_value_group
from view_LIST_task_value_group import LIST_task_value_group
from view_CSV_task_value_group import CSV_task_value_group
from view_EDIT_task_value_group import EDIT_task_value_group
 
application.register_blueprint(NEW_task_value_group)
application.register_blueprint(LIST_task_value_group)
application.register_blueprint(CSV_task_value_group)
application.register_blueprint(EDIT_task_value_group)


# import Task value type then register with blueprint
sys.path.insert(1, getPath()+'/Task value type/view/')
 
from view_NEW_task_value_type import NEW_task_value_type
from view_LIST_task_value_type import LIST_task_value_type
from view_CSV_task_value_type import CSV_task_value_type
from view_EDIT_task_value_type import EDIT_task_value_type
 
application.register_blueprint(NEW_task_value_type)
application.register_blueprint(LIST_task_value_type)
application.register_blueprint(CSV_task_value_type)
application.register_blueprint(EDIT_task_value_type)

# import Task value type then register with blueprint
sys.path.insert(1, getPath()+'/Log/view/')
 
from view_NEW_log import NEW_log
from view_LIST_log import LIST_log
from view_CSV_log import CSV_log
from view_EDIT_log import EDIT_log
 
application.register_blueprint(NEW_log)
application.register_blueprint(LIST_log)
application.register_blueprint(CSV_log)
application.register_blueprint(EDIT_log)

if __name__ == '__main__':
    application.run(debug=False)
