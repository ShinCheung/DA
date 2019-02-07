# import pyodbc
# import sqlalchemy
# import pandas as pd

# connection = pyodbc.connect('DRIVER={SQL Server}; SERVER=(local); DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')
# engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventureWorks?driver=SQL+Server')

# query = 'SELECT FirstName, LastName FROM Person.Person'
# df1 = pd.read_sql_query(query, connection)
# df2 = pd.read_sql_query(query, engine)

# pd.options.display.max_columns = 999
# print(df1.head())
# print(df2.head())

import sys
import MySQLdb
# 注意：MySQLdb只适用于python2
test=MySQLdb.connect(db='mysql',host='localhost',user='root',passwd='123456')
cursor = test.cursor()
cursor.execute('show databases;')
for data in cursor.fetchall():
    print(data)