import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import statistics
import math
#import stats
import scipy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn import metrics
import pickle
import joblib

plt.rcParams['figure.figsize'] = (12.0, 9.0)



seasons= [2011,2012,2013,2014,2015,2016,2017,2018,2019,2021,2022]

df = pd.DataFrame()


for season in seasons:
    
    new_df = pd.read_csv(f'./data/{season}_season.csv')
    new_df['Season'] = season
    new_df = new_df[new_df.Tm != "Average"]
    #new_df.drop('Luck▼', inplace=True)
    #new_df.drop('W-L%▼', inplace=True)
   # season_st = f"{new_df['Tm']}_{season}"
   # print(season_st)
    #new_df['Team_ID'] = f"{new_df.Tm}_{new_df.Season} " 
    
    
    df = pd.concat([df, new_df], ignore_index=True)



df.dropna(axis='columns', inplace=True)


df['Tm'] = df["Tm"].apply(lambda x: x.replace("Los Angeles Angels of Anaheim", "Los Angeles Angels"))
df['Tm']  = df["Tm"].apply(lambda x: x.replace("Florida Marlins", "Miami Marlins"))

df['Team_ID'] = df['Season'].astype(str) + df['Tm']

Y=df.iloc[:,2]
X= df['Rdiff'][:]


m = 0
c = 0

L = 0.01  # The learning Rate
epochs = 1000  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = m*X + c  # The current predicted value of Y
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c
    
print (m, c)

errors=Y-Y_pred

mean_squared_error(Y,Y_pred)

mean_absolute_error(Y,Y_pred)


std_dev =statistics.stdev(errors)


std_dev2 =std_dev*2


df['errors'] = errors

df['z-score'] = scipy.stats.zscore(df['errors'])

df[(df['z-score']>2) |(df['z-score']<-2) ]


df_off = pd.DataFrame()


for season in seasons:
    
    new_df = pd.read_csv(f'./data/off/{season}_season_off.csv')
    new_df['Season'] = season
    new_df = new_df[new_df.Tm != "Average"]
    new_df = new_df[new_df['Tm']!="League Average"]
    new_df = new_df[new_df['Tm'].notna()]
    #new_df.drop('Luck▼', inplace=True)
    #new_df.drop('W-L%▼', inplace=True)
    
    
    df_off = pd.concat([df_off, new_df], ignore_index=True)


df_off = df_off[:330]

df_off['Tm'] = df_off["Tm"].apply(lambda x: x.replace("Los Angeles Angels of Anaheim", "Los Angeles Angels"))
df_off['Tm']  = df_off["Tm"].apply(lambda x: x.replace("Florida Marlins", "Miami Marlins"))


df['Team_ID'] = df['Season'].astype(str) + df['Tm']


df_off.drop('EV',axis=1, inplace=True)
df_off.drop('HardH%',axis=1, inplace=True)


df_off['HR_'] = df_off['HR%'].str.rstrip('%').astype('float') / 100.0
df_off['SO_'] = df_off['SO%'].str.rstrip('%').astype('float') / 100.0
df_off['BB_'] = df_off['BB%'].str.rstrip('%').astype('float') / 100.0
#df_off['HardH_'] = df_off['HardH%'].str.rstrip('%').astype('float') / 100.0
df_off['LD_'] = df_off['LD%'].str.rstrip('%').astype('float') / 100.0
df_off['GB_'] = df_off['GB%'].str.rstrip('%').astype('float') / 100.0
df_off['FB_'] = df_off['FB%'].str.rstrip('%').astype('float') / 100.0
df_off['Pull_'] = df_off['Pull%'].str.rstrip('%').astype('float') / 100.0
df_off['Cent_'] = df_off['Cent%'].str.rstrip('%').astype('float') / 100.0
df_off['Oppo_'] = df_off['Oppo%'].str.rstrip('%').astype('float') / 100.0
df_off['RS_'] = df_off['RS%'].str.rstrip('%').astype('float') / 100.0
df_off['SB_'] = df_off['SB%'].str.rstrip('%').astype('float') / 100.0
df_off['XBT_'] = df_off['XBT%'].str.rstrip('%').astype('float') / 100.0
df_off['cWPA_'] = df_off['cWPA'].str.rstrip('%').astype('float') / 100.0


m_df= pd.merge(df,df_off, on =['Tm','Season'])

#m_df2 =m_df[['Team_ID','Tm','Season','R','rOBA','Rbat+', 'BAbip', 'ISO', 'HR_', 'SO_', 'BB_', 'LD_', 'GB_', 'FB_','GB/FB', 'Pull_', 'Cent_', 'Oppo_', 'WPA', 'cWPA_', 'RS_', 'SB_','XBT_']]










