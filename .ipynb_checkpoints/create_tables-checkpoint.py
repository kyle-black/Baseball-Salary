#!/usr/bin/python

import psycopg2
from config import config


def drop_tables(table_name):
    commands = (
        f"""
        DROP TABLE IF EXISTS {table_name} CASCADE 

        """

    )

def create_tables():
    """ create tables in the PostgreSQL database"""
    
    commands = (
         """
        CREATE TABLE IF NOT EXISTS seasons_team (
            Team_ID VARCHAR(255) PRIMARY KEY,
            Team VARCHAR(255) NOT NULL,
            Wins  INTEGER NOT NULL,
            Losses INTEGER NOT NULL,
            win_PCT NUMERIC(5,3) NOT NULL,
            Runs INTEGER NOT NULL,
            Runs_Allowed INTEGER NOT NULL,
            Runs_Diff NUMERIC(5,3) NOT NULL,
            SOS NUMERIC(5,3) NOT NULL,
            SRS NUMERIC(5,3) NOT NULL,
            pythWL VARCHAR(255) NOT NULL,
            vEast VARCHAR(255) NOT NULL,
            vCent VARCHAR(255)  NOT NULL,
            vWest VARCHAR(255)  NOT NULL,
            Inter VARCHAR(255) NOT NULL,
            Home VARCHAR(255) NOT NULL,
            Road VARCHAR(255) NOT NULL,
            ExInn VARCHAR(255) NOT NULL,
            One_Run VARCHAR(255) NOT NULL,
            vRHP VARCHAR(255) NOT NULL,
            vLHP VARCHAR(255) NOT NULL,
            Greater_500 VARCHAR(255) NOT NULL,
            Less_500 VARCHAR(255) NOT NULL,
            Season VARCHAR(255) NOT NULL
        )
        """,
        
        """
        CREATE TABLE IF NOT EXISTS seasons_team_off (
            Team_ID VARCHAR(255) NOT NULL,
            Team VARCHAR(255) NOT NULL,
            Season VARCHAR(255) NOT NULL,
            rOBA NUMERIC(5,3) NOT NULL,
            Rbat_plus INTEGER NOT NULL,
            BAbip NUMERIC(5,3) NOT NULL,
            ISO NUMERIC(5,3) NOT NULL,
            HR_pct NUMERIC(5,3) NOT NULL,
            SO_pct NUMERIC (5,3) NOT NULL,
            BB_pct NUMERIC(5,3) NOT NULL,
            EV NUMERIC(5,3) NOT NULL,
            HardH_pct NEMERIC(5,3) NOT NULL,
            LD_pct NUMERIC(5,3) NOT NULL,
            GB_pct NUMERIC(5,3) NOT NULL,
            FB_pct NUMERIC(5,3) NOT NULL,
            GB_FB NUMERIC(5,3) NOT NULL,
            Pull NUMERIC(5,3) NOT NULL,
            Cent NUMERIC(5,3) NOT NULL,
            Oppo NUMERIC(5,3) NOT NULL,
            RS NUMERIC(5,3) NOT NULL,
            SB NUMERIC(5,3) NOT NULL,
            XBT NUMERIC(5,3) NOT NULL,
            cWPA NUMERIC(5,3) NOT NULL,
            WPA NUMERIC(5,3) NOT NULL
        )
        """

      
      
      
      )



    conn = None
    
    
    
   

    
if __name__ == '__main__':
    create_tables()
