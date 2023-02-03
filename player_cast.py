import psycopg2
from config import config



import psycopg2

params = config()





try:
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from seasons_team "

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    team_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in team_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conn:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

