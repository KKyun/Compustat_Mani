import pandas as pd
import numpy as np

result = []

Filename = r".xlsx"

df = pd.read_excel(Filename)

MinYear = df['Year'].min()
MaxYear = df['Year'].max()
for k in range(MinYear, MaxYear+1):
  dfTemp = df[df['Year'] == k]
  TotalPat = xlTemp['FILED'].count()
  SemiPat = xlTemp['SemiPat'].sum()
  EquiPat = xlTemp['EquiPat'].sum()
