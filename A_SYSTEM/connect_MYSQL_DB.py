import mysql.connector
from mysql.connector import Error
import pymysql as MySQLdb

mysql_connect = MySQLdb.connect(host='localhost',
        user='root',
        passwd='',
        db='automation_2019',
		autocommit = 'true') #autocommit 
		
print(mysql_connect)