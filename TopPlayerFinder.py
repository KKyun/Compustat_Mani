import pandas as pd

Result = []
CustomRange = 5
StartingYear = 1970
EndYear = 2010

Filename = r".xlsx"

df = pd.read_excel(Filename)
df.dropna(inplace = True)

df["rank"] = df.groupby("Year")["Revenue"].rank(ascending=False)
df = df[df["rank"]<=CustomRange]
df = df[df["Year"]>=StartingYear]
df = df[df["Year"]<=EndYear]

dfList = df['Ticker_Symbol'].tolist()
dfList = list(set(dfList))

for tickers in range(0, len(dfList)):
    Result.append({'Ticker':dfList[tickers],'Count':df[df["Ticker_Symbol"]==dfList[tickers]]["Ticker_Symbol"].count()})
df2 = pd.DataFrame(Result, columns=['Ticker', 'Count'])
df2.sort_values(['Count'], ascending=[False], inplace=True)

print(df2)
print("The result is from Year "+str(StartingYear)+" to "+str(EndYear)+" which is "+str(EndYear-StartingYear+1)+" Years Long")
