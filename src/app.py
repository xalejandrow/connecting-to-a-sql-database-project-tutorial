

# 1) Connect to the database here using the SQLAlchemy's create_engine function
""" import psycopg2 

conn = psycopg2.connect(database='d9v1k7oo2sg6ov', 
                        user='oxkaeubmnqxvxi', 
                        password='26f907c61376056246af18a2d44bb8f5b861892ec63969926945ecae8e68deb4',
                        host='ec2-18-214-134-226.compute-1.amazonaws.com',
                        port=5432)

cursor = conn.cursor()
cursor.execute("CREATE TABLE Movies(id VARCHAR (2) PRIMARY KEY, title VARCHAR(30), rating INT);")
conn.commit()

conn.close() """
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function


# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
""" import psycopg2 
conn = psycopg2.connect(database='d9v1k7oo2sg6ov', 
                        user='oxkaeubmnqxvxi', 
                        password='26f907c61376056246af18a2d44bb8f5b861892ec63969926945ecae8e68deb4',
                        host='ec2-18-214-134-226.compute-1.amazonaws.com',
                        port=5432)

cursor = conn.cursor()
#cursor.execute("INSERT INTO Movies(id, title, rating) VALUES('1','Toy Story',5);")
#cursor.execute("INSERT INTO Movies(id, title, rating) VALUES('2','Toy Story 2',5);")
cursor.execute("INSERT INTO Movies(id, title, rating) VALUES('3','Toy Story 3',3),('4','Harry Potter 1',4);")
conn.commit()
conn.close() """

# 4) Use pandas to print one of the tables as dataframes using read_sql function
import psycopg2
import pandas as pd

conn = psycopg2.connect(database='d9v1k7oo2sg6ov', 
                        user='oxkaeubmnqxvxi', 
                        password='26f907c61376056246af18a2d44bb8f5b861892ec63969926945ecae8e68deb4',
                        host='ec2-18-214-134-226.compute-1.amazonaws.com',
                        port=5432)

cursor = conn.cursor()
pd.read_sql("SELECT * FROM Movies",conn)
conn.close()
