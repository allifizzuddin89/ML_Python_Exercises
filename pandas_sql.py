#Written by Allif Izzuddin bin Abdullah
#github : allifizzuddin89

#setup mysql server local
#setup mysql workbench
#install pymysql
#install sqlalchemy
#create database in workbench

import pandas as pd 
import sqlalchemy

#create SQL alchemy engine
#refer pandas doc for other sql connection
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost:3306/new_schema1')

df = pd.read_sql_table("Customers", engine) #pass the engine
print('\n',df)

#select only print name and phone number
df = pd.read_sql_table("Customers", engine, columns=['name','phone_number'])
print('\n',df)

#Orders table
df = pd.read_sql_table("Orders", engine) #pass the engine
print('\n',df)

#If use query
#syntax:
# SELECT table1.column1,table1.column2,table2.column1,....
# FROM table1 
# INNER JOIN table2
# ON table1.matching_column = table2.matching_column;

# table1: First table.
# table2: Second table
# matching_column: Column common to both the tables.

query = '''
SELECT Customers.name, Customers.phone_number, Orders.name, Orders.amount
FROM Customers INNER JOIN Orders
ON Customers.id=Orders.customer_id
'''

df = pd.read_sql_query(query,engine)
print('\n',df)


#Upload CSV to SQL

df1 = pd.read_csv("Customers.csv")
print('\n',df1)

#rename/matching the column name with the sql table

df1.rename(columns={
    'Customers name':'name',
    'Phone number':'phone_number',
    }, inplace=True)
print('\n',df1)

df1.to_sql(
    name='Customers',
    con=engine,
    # schema='new_schema1',
    if_exists='append',
    index=False,
    )

#check...

print('\n',pd.read_sql("Customers",engine))

#also can use query
#shorter version of read_sql

print('\n',pd.read_sql(query,engine))