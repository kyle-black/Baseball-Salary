import psycopg2
from config import config



def drop_tables(table_name):
    commands = (
        f"""
        DROP TABLE IF EXISTS {table_name} CASCADE 

        """

    )
    return commands


def execute_conn(table_name):
    commands = drop_tables(table_name)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
       
        cur.close()
        
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error code:",error)
    finally:
        if conn is not None:
            conn.close()


    
if __name__ == '__main__':
    execute_conn('seasons_team_off')
    
