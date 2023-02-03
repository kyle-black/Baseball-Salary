import streamlit as st
import pandas as pd 
import numpy as np

import mysql.connector
import connection

my_db = mysql.connector.connect(host= connection.host, user=connection.user, password=connection.user, database= connection.database)

mycursor = my_db.cursor()

mycursor.close()
#mycursor.execute("SHOW DATABASES")


#for x in mycursor:
#    print(x)
