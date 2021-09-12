import csv
import pandas as pd
import numpy as np
with open('cleaned_JSON.csv') as infile:
	df = pd.read_csv(infile)
states = df['state'].drop_duplicates()
allStates = states.to_list()
wantedStates = ['CA','TX','FL','NY','PA','IL','OH','GA','NC','MI']
unwantedStates = [i for i in allStates if i not in wantedStates]
for state in unwantedStates:
	df[df['state'] == state] = np.nan
df = df.dropna()
df.index = range(len(df))
redStates = ['FL','NC','OH','TX']
df['Party'] = np.where((df['state'] == 'FL')|(df['state'] == 'NC')|(df['state'] == 'OH')|(df['state'] == 'TX'), 'R','D')
df = df.groupby(['Party'])['positive'].mean()
print(df)