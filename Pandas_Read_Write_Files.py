import pandas as pd 
df = pd.read_csv("stock_data.csv", skiprows=1) #skip row 1 from top, also similar to header=1
print(df,'\n')

#stock_data1.csv has no header
df = pd.read_csv("stock_data1.csv", header=None, names=["TICKER", "EPS", "REVENUE", "PRICE", "PEOPLE"]) #if header is missing, we can put it manually
print(df,'\n')

df =pd.read_csv("stock_data.csv", nrows=3) #only read 3 rows
print(df,'\n') 