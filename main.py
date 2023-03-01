import pandas as pd
import numpy as np

data = pd.read_csv(r'D:\Logesh\Coding\python\Udemy\Pandas\IPL_Sold_players_2013_23.csv')

print(round(data['Price'].mean(), 2))

print(data[data['Price']==data['Price'].max()])
print(data.loc[data['Price'].idxmax()])
print(data.loc[data['Price'].idxmin()])
print(data[data['Price']==data['Price'].min()])

#Access a column using GroupBy
print(data.groupby('Season').mean())

print('Top 5 Most appeared player: ')
print(data['Name'].value_counts().head(5))

print('Players with only one appearences : ')
print(data['Name'].unique())
print('Total : ',data['Name'].nunique())

print('Total No of players in 2023: ',sum(data[data['Season']==2023].value_counts()==1))

#Printing Chennai team players

n= input('Enter Team to search: ')
def search(n,s):
    if n.lower() in s.lower().split():
        return True
    else:
        return False

print(data[data['Team'].apply(lambda x: search(n,x))])
print('Total: ',sum(data['Team'].apply(lambda x: search(n,x))))
c=input('Enter category: ')
print(data[data['Type'].apply(lambda x: search(c,x))]['Name'])
