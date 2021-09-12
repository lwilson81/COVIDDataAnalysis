import csv
import pandas as pd
import numpy as np
with open('cleaned_CSV.csv') as infile:
	df = pd.read_csv(infile)
df.columns = ['date','state','death','hospitalized','negative','positive']
NE = ['PA','NY','VT','NH','MA','RI','CT','NJ','DE','MD','DC','ME']
MW = ['ND','SD','NE','KS','MN','IA','MO','WI','IL','IN','MI','OH']
S = ['TX','OK','AR','LA','KY','TN','MS','AL','GA','FL','SC','NC','VA','WV']
W = ['WA','OR','CA','ID','NV','AZ','MT','WY','CO','NM','UT','AK','HI']
df['Region'] = np.where(df['state'].isin(NE),'NE',np.where(df['state'].isin(MW),'MW',np.where(df['state'].isin(S),'S',np.where(df['state'].isin(W),'W','T'))))
df[df['positive'] == 'No Data'] = np.nan
df = df.dropna()
df['positive'] = pd.to_numeric(df['positive'])
totalCases = df.groupby(['state'])['positive'].max().sum()
regionMax = df.groupby(['Region','state'])['positive'].max()

