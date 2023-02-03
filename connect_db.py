import psycopg2
import numpy as np
import psycopg2.extras as extras
import pandas as pd
from config import config

tm_dict ={"Arizona Diamondbacks":"ari",
"Atlanta Braves":"atl",
"Baltimore Orioles":"bal",
"Boston Red Sox": "bos",
"Chicago Cubs": "chc",
"Chicago White Sox": "chw",
"Cinncinatti Reds": "cin",
"Cleveland Indians": "cle",
"Colorado Rockies": "col",
"Detroit Tigers":"det",
"Houston Astros": "hou",
"Kansas City Royals": "kcr",
"Los Angeles Angels": "laa",
"Los Angeles Dodgers": "lad",
"Miami Marlins": "mia",
"Milwaukee Brewers": 'mil',
"Minnesota Twins": 'min',
"New York Mets": 'nym',
"New York Yankees":'nym',
"Oakland Athletics":"oak",
"Philadelphia Phillies": "phi",
"Pittsburgh Pirates": 'pit',
"San Diego Padres" : 'sdp',
"Seattle Mariners": 'sea',
"San Francisco Giants": 'sfg',
"St. Louis Cardinals": "stl",
"Tampa Bay Rays" : "tbr",
"Texas Rangers" : "tex",
"Toronto Blue Jays": "tor",
"Washington Nationals": "wsh"
}

def fix_pct(df):
    for name in df.columns:
        try:
            df[f'{name}_n'] = df[f'{name}'].str.rstrip('%').astype('float') / 100.0
        except: print("nothing to change")
    return df


def fix_tables(df, type_):

    if type_ =="season":
       
        df['Team_ID'] = df['Season'].astype(str) + df['Tm']
        team = df['Tm']
        df['Team'] = team
        df['Team_abr'] = tm_dict[f'{team}']
        wins = df['W']
        df['Wins'] = wins
        loses = df['L']
        df['Losses'] =loses
        win_pct = df["W-L%"]
        df['win_PCT'] = win_pct
        runs = df['R']
        df['Runs'] = runs
        runs_allow = df['RA']
        df['Runs_Allowed'] = runs_allow
        
        run_diff = df['Rdiff']
        df['Runs_Diff'] = run_diff
        one_run = df['1Run']
        df['One_Run'] =one_run
        gr_500 = df['≥.500']
        df['Greater_500'] = gr_500
        less_500 = df['<.500']
        df['Less_500'] =less_500

        df = df[['Team_ID', 'Team','Team_abr', 'Wins', 'Losses','win_PCT', 'Runs', 'Runs_Allowed', 'Runs_Diff', 'SOS', 'SRS','pythWL', 'vEast', 'vCent', 'vWest','Inter','Home', 'Road', 'ExInn', 'One_Run', 'vRHP', 'vLHP', 'Greater_500', 'Less_500', 'Season']]

       # df = df[df.isnull().any(axis=1)]
    elif type_ == "offense":
        df = fix_pct(df)
        df['Team_ID'] = df['Season'].astype(str) + df['Tm']
        team = df['Tm']
        df['Team'] = team
        df['Team_abr'] = tm_dict[f'{team}']
        Rbat_ = df['Rbat+']
        df['Rbat_plus'] = Rbat_
        BAbip = df['BAbip']
        df['BAbip'] = BAbip
        HR_ = df['HR%_n']
        df['HR_pct'] = HR_
        SO_pct = df['SO%_n']
        df['SO_pct'] = SO_pct
        BB_pct = df['BB%_n']
        df['BB_pct'] = BB_pct
        LD_pct = df['LD%_n']
        df['LD_pct'] = LD_pct
        GB_pct= df['GB%_n']
        FB_pct = df['FB%_n']
        df['FB_pct'] = FB_pct
        GB_FB = df['GB_FB']
        df['GB_FB'] = GB_FB
        GB_pct = df['GB%_n']
        df['GB_pct'] = GB_pct
        Pull_pct = df['Pull%_n']
        df['Pull'] = Pull_pct
        Cent_pct = df['Cent%_n']
        df['Cent'] = Cent_pct
        Oppo_pct = df['Oppo%_n']
        df['Oppo'] = Oppo_pct
        RS_pct = df['RS%_n']
        df['RS'] = RS_pct
        SB_pct = df['SB%_n']
        df['SB'] = SB_pct
        XBT_pct = df['XBT%_n']
        df['XBT'] = XBT_pct
        cWPA_pct = df['cWPA_n']
        df['cWPA'] = cWPA_pct

        df = df[['Team_ID', 'Team','Team_abr', 'Season', 'rOBA', 'Rbat_plus', 'BAbip', 'ISO', 'HR_pct', 'SO_pct', 'BB_pct', 'LD_pct', 'GB_pct', 'FB_pct', 'GB_FB', 'Pull', 'Cent', 'Oppo', 'RS', 'SB', 'XBT', 'cWPA', 'WPA']]
        print(type(df['cWPA'][0]))
     elif type_ == "p_offense":
        df = fix_pct(df)
        df['Team_ID'] = df['Season'].astype(str) + df['Tm']
        team = df['Tm']
        df['Team'] = team
        df['Team_abr'] = tm_dict[f'{team}']
        Rbat_ = df['Rbat+']
        df['Rbat_plus'] = Rbat_
        BAbip = df['BAbip']
        df['BAbip'] = BAbip
        HR_ = df['HR%_n']
        df['HR_pct'] = HR_
        SO_pct = df['SO%_n']
        df['SO_pct'] = SO_pct
        BB_pct = df['BB%_n']
        df['BB_pct'] = BB_pct
        LD_pct = df['LD%_n']
        df['LD_pct'] = LD_pct
        GB_pct= df['GB%_n']
        FB_pct = df['FB%_n']
        df['FB_pct'] = FB_pct
        GB_FB = df['GB_FB']
        df['GB_FB'] = GB_FB
        GB_pct = df['GB%_n']
        df['GB_pct'] = GB_pct
        Pull_pct = df['Pull%_n']
        df['Pull'] = Pull_pct
        Cent_pct = df['Cent%_n']
        df['Cent'] = Cent_pct
        Oppo_pct = df['Oppo%_n']
        df['Oppo'] = Oppo_pct
        RS_pct = df['RS%_n']
        df['RS'] = RS_pct
        SB_pct = df['SB%_n']
        df['SB'] = SB_pct
        XBT_pct = df['XBT%_n']
        df['XBT'] = XBT_pct
        cWPA_pct = df['cWPA_n']
        df['cWPA'] = cWPA_pct

        df = df[['Team_ID', 'Team','Team_abr', 'Season', 'rOBA', 'Rbat_plus', 'BAbip', 'ISO', 'HR_pct', 'SO_pct', 'BB_pct', 'LD_pct', 'GB_pct', 'FB_pct', 'GB_FB', 'Pull', 'Cent', 'Oppo', 'RS', 'SB', 'XBT', 'cWPA', 'WPA']]
    
    
    
    return df





    
    
def new_seasons():
        seasons= [2015,2016,2017,2018,2019,2021,2022]
        df = pd.DataFrame()
        for season in seasons:

        
    
            new_df = pd.read_csv(f'./data/{season}_season.csv')
            new_df['Season'] = season
            new_df = new_df[new_df.Tm != "Average"]
        
            new_df['Tm'] = new_df["Tm"].apply(lambda x: x.replace("Los Angeles Angels of Anaheim", "Los Angeles Angels"))
            new_df['Tm']  = new_df["Tm"].apply(lambda x: x.replace("Florida Marlins", "Miami Marlins"))
            new_df = new_df.reset_index(drop=True)

            df = pd.concat([df, new_df], ignore_index=True)
            df = df.reset_index(drop=True)

        df= fix_tables(df, 'seasons')


        
        return df

def new_offense():
        seasons= [2015,2016,2017,2018,2019,2021,2022]
        df = pd.DataFrame()
        for season in seasons:

        
    
            new_df = pd.read_csv(f'./data/off/{season}_season_off.csv')
            new_df['Season'] = season
            new_df = new_df[new_df.Tm != "Average"]
        
            new_df['Tm'] = new_df["Tm"].apply(lambda x: x.replace("Los Angeles Angels of Anaheim", "Los Angeles Angels"))
            new_df['Tm']  = new_df["Tm"].apply(lambda x: x.replace("Florida Marlins", "Miami Marlins"))
            new_df = new_df.reset_index(drop=True)

            df = pd.concat([df, new_df], ignore_index=True)
            df = df.reset_index(drop=True)

        df= fix_tables(df, 'offense')


        
        return df

def new_offense_player():
        teams = ['ari','atl','bal','bos','chc','chw','cin', 'cin', 'cle', 'col', 'det','hou','kcr','laa','lad','mia', 'mil','min','nym','nyy','oak','phi', 'pit','sdp', 'sea', 'sfg', 'stl','tbr', 'tex', 'tor', 'wsh' ]
        seasons= [2015,2016,2017,2018,2019,2021,2022]
        df = pd.DataFrame()
        for team, season in zip(teams,seasons):

        
            new_df = pd.read_csv(f'./data/player_data/{team}/{season}.csv')
            #new_df = pd.read_csv(f'./data/off/{season}_season_off.csv')
            new_df['Season'] = season
            new_df = new_df[new_df.Tm != "Average"]
            new_df['Tm_abr'] = team 
            #new_df['Tm'] = new_df["Tm"].apply(lambda x: x.replace("Los Angeles Angels of Anaheim", "Los Angeles Angels"))
            #new_df['Tm']  = new_df["Tm"].apply(lambda x: x.replace("Florida Marlins", "Miami Marlins"))
            new_df = new_df.reset_index(drop=True)

            df = pd.concat([df, new_df], ignore_index=True)
            df = df.reset_index(drop=True)

        df= fix_tables(df, 'p_offense')


        
        return df




params = config()

conn = psycopg2.connect(
	**params
)


def execute_values(conn, df, table):

	tuples = [tuple(x) for x in df.to_numpy()]

	cols = ','.join(list(df.columns))
	# SQL query to execute
	query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
	cursor = conn.cursor()
	try:
		extras.execute_values(cursor, query, tuples)
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print("Error: %s" % error)
		conn.rollback()
		cursor.close()
		return 1
	print("the dataframe is inserted")
	cursor.close()

if __name__ == '__main__':
    df = new_offense()
    
    execute_values(conn, df, 'seasons_team_off')


tm_dict ={"Arizona Diamondbacks":"ari",
"Atlanta Braves":"atl",
"Baltimore Orioles":"bal",
"Boston Red Sox": "bos",
"Chicago Cubs": "chc",
"Chicago White Sox": "chw",
"Cinncinatti Reds": "cin",
"Cleveland Indians": "cle",
"Colorado Rockies": "col",
"Detroit Tigers":"det",
"Houston Astros": "hou",
"Kansas City Royals": "kcr",
"Los Angeles Angels": "laa",
"Los Angeles Dodgers": "lad",
"Miami Marlins": "mia",
"Milwaukee Brewers": 'mil',
"Minnesota Twins": 'min',
"New York Mets": 'nym',
"New York Yankees":'nym',
"Oakland Athletics":"oak",
"Philadelphia Phillies": "phi",
"Pittsburgh Pirates": 'pit',
"San Diego Padres" : 'sdp',
"Seattle Mariners": 'sea',
"San Francisco Giants": 'sfg',
"St. Louis Cardinals": "stl",
"Tampa Bay Rays" : "tbr",
"Texas Rangers" : "tex",
"Toronto Blue Jays": "tor",
"Washington Nationals": "wsh"
}