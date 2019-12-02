import pandas as pd 
df = pd.read_csv("stock_data.csv", skiprows=1) #skip row 1 from top, also similar to header=1
print(df,'\n')

#stock_data1.csv has no header
df = pd.read_csv("stock_data1.csv", header=None, names=["TICKER", "EPS", "REVENUE", "PRICE", "PEOPLE"]) #if header is missing, we can put it manually
print(df,'\n')

df =pd.read_csv("stock_data.csv", nrows=3) #only read 3 rows
print(df,'\n') 

#cleanup messy data, n.a, not available to NaN
df = pd.read_csv("stock_data.csv", na_values=["not available","n.a."])
print(df,'\n')

#use dict to cleanup messy data (data munging/ data wrangling)
#revenue never -1, so convert it to NaN

df = pd.read_csv("stock_data.csv", na_values={'eps': ["not available", "n.a."],
'revenue': ["not available", "n.a.", -1],
'people': ["not available", "n.a."], 'price':["not available", "n.a."]
})
print(df,'\n')

#WRITING BACK TO CSV

df.to_csv("new.csv", index=False) #with remove index column

#only write few columns, let say 2

print(df.columns)

df.to_csv("new.csv", columns=["tickers", "eps"])

#remove header
df.to_csv("new.csv", header=False)


#EXCEL

df = pd.read_excel("stock_data.xlsx", "Sheet1")
print(df)

#make converter to convert messy data

def converter_eps(cell):
    if cell=="n.a":
        return None
    if cell=="not available":
        return None
    return cell

def converter_price(cell):
    if cell=="n.a.":
        return None
    if cell=="not available":
        return None
    return cell

def converter_people(cell):
    if cell=="n.a.":
        return "Allif"
    if cell=="not available":
        return "Allif"
    return cell

df = pd.read_excel("stock_data.xlsx", "Sheet1", converters = {
    'people' : converter_people,
    'eps' : converter_eps,
    'price' : converter_price
})
print(df)

#WRITE TO EXCEL

df.to_excel("new.xlsx", sheet_name="stock", startrow=6, startcol=2) #start writing
