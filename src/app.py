
import os
from dotenv import load_dotenv
load_dotenv()
import pymysql
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

# 1) Connect to the database here using the SQLAlchemy's create_engine function
""" import psycopg2 

conn = psycopg2.connect(database=os.getenv('DB_NAME'), 
                        user=os.getenv('DB_USER'), 
                        password=os.getenv('DB_PASSWORD'),
                        host=os.getenv('DB_HOST'),
                        port=5432)

cursor = conn.cursor()
cursor.execute("CREATE TABLE Movies(id VARCHAR (2) PRIMARY KEY, title VARCHAR(30), rating INT);")
conn.commit()

conn.close() """
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function


# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
""" import psycopg2 
conn = psycopg2.connect(database=os.getenv('DB_NAME'), 
                        user=os.getenv('DB_USER'), 
                        password=os.getenv('DB_PASSWORD'),
                        host=os.getenv('DB_HOST'),
                        port=5432)

cursor = conn.cursor()
#cursor.execute("INSERT INTO Movies(id, title, rating) VALUES('1','Toy Story',5);")
#cursor.execute("INSERT INTO Movies(id, title, rating) VALUES('2','Toy Story 2',5);")
cursor.execute("INSERT INTO Movies(id, title, rating) VALUES('3','Toy Story 3',3),('4','Harry Potter 1',4);")
conn.commit()
conn.close() """

# 4) Use pandas to print one of the tables as dataframes using read_sql function

#print('getenv',os.getenv('DB_NAME'))


conn = psycopg2.connect(database=os.getenv('DB_NAME'), 
                        user=os.getenv('DB_USER'), 
                        password=os.getenv('DB_PASSWORD'),
                        host=os.getenv('DB_HOST'),
                        port=5432)
                    
cursor = conn.cursor()
pd.read_sql("SELECT * FROM Movies",conn)
conn.close()
