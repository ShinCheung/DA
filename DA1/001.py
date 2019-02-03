import pandas as pd

df = pd.DataFrame({'ID':[1,2,3], 'Name':['Tim', 'Victor', 'Nick']})
df.to_excel('./output.xlsx')
df = df.set_index('ID')
print(df)