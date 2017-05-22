import pandas as pd
import numpy as np

Result = []

Filename = r".xlsx"

df = pd.read_excel(Filename)

MinYear = df['Year'].min()
MaxYear = df['Year'].max()
for year in range(MinYear, MaxYear+1):
    dfTemp = df[df['Year'] == year]
    dfTemp['Rank'] = s['Revenue'].rank(ascending=False)
    try:
        Result.append({'Year':year, '1st':dfTemp[dfTemp['Rank'] == 1]['Company_Name'][0],
                       '2nd':dfTemp[dfTemp['Rank'] == 2]['Company_Name'][0],
                       '3rd':dfTemp[dfTemp['Rank'] == 3]['Company_Name'][0],
                       '4th':dfTemp[dfTemp['Rank'] == 4]['Company_Name'][0],
                       '5th':dfTemp[dfTemp['Rank'] == 5]['Company_Name'][0]})
     
df = pd.DataFrame(Result, columns=['Year','1st','2nd','3rd', '4th', '5th'])
print(result)
