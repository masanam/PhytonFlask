import sys
from datetime import datetime
from main import getPath

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, getPath()+'/A_SYSTEM/')
from connect_MYSQL_DB import mysql_connect

class DataList():
    def retrieve_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group LIMIT 0,20 "
        mc.execute(query )
        result = mc.fetchall()
        return result
    def get_data(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result    
    def count_data():
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group"
        mc.execute(query)
        mc.fetchall()
        count = mc.rowcount
        return count	
    def search_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group WHERE bot_user_group_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def search_data1(data1):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user_group WHERE bot_user_count = %s "
        mc.execute(query,(data1) )
        result = mc.fetchall()
        return result
    def get_data_tv(start,limit):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user LIMIT %s,%s "
        mc.execute(query,(start,limit) )
        result = mc.fetchall()
        return result      
    def search_data_tv(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user WHERE bot_user_name = %s "
        mc.execute(query,(data) )
        result = mc.fetchall()
        return result
    def search_data1_tv(data1):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user WHERE bot_user_content = %s "
        mc.execute(query,(data1) )
        result = mc.fetchall()
        return result    
    def insert_data(filename,qty,now):
        mc = mysql_connect.cursor()
        query = "INSERT INTO bot_user_group (bot_user_group_name,bot_user_count,created_at)  VALUES (%s,%s,%s) "
        mc.execute(query,(filename,qty,now) )
        result = mc.fetchall()
        return result  
    def clone_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user WHERE bot_user_id IN (%s) "
        ids = ", ".join(data)
        mc.execute(query % ids )
        result = mc.fetchall()
        return result   
    def count_clone_data(data):
        mc = mysql_connect.cursor()
        query = "SELECT * FROM bot_user WHERE bot_user_id IN (%s) "
        ids = ", ".join(data)
        mc.execute(query % ids )
        mc.fetchall()
        count = mc.rowcount
        return count	
