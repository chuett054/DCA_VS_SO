import pandas as pd

#READ BTC CSV FILE 
df = pd.read_csv('BTC.csv')
print(df.Close[4]) 