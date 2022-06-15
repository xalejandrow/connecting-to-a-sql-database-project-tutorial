
# 1) Connect to the database here using the SQLAlchemy's create_engine function
import os
from dotenv import load_dotenv
load_dotenv()
import pymysql
from sqlalchemy import create_engine
import pandas as pd



connection_string = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
engine = create_engine(connection_string)
engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
#engine.execute("CREATE TABLE publishers(publisher_id INT NOT NULL,name VARCHAR(255) NOT NULL,PRIMARY KEY(publisher_id));")
engine.execute("SHOW DATABASES")
engine.execute("SHOW TABLES")

def insertData(data):
    file1 = open(data, 'r')
    Lines = file1.readlines()
  
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        engine.execute(line)


# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
#engine.execute("INSERT INTO publishers(publisher_id,name) values (1,'O Reilly Media');")
#engine.execute("SELECT * FROM publishers;")
data = 'src/sql/publishers.sql'
insertData(data)

#4) Use pandas to print one of the tables as dataframes using read_sql function
df = pd.read_sql("SELECT * FROM publishers;", engine)
print(df)