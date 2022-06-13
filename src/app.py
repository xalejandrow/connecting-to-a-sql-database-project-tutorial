# importing the reusable functions
# We created the "connect" function on the file reusable_functions.py
# and we are going to use it every time we want to connect to the database
from reusable_functions import connect, run_file, run_query
# importing pandas
import pandas as pd

# 1) Connect to the database here using the SQLAlchemy's create_engine function

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function
