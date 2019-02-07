import pandas as pd
import numpy as np

pd.options.display.max_columns=999
orders = pd.read_excel('./Orders.xlsx', sheet_name='Orders')
orders['Year'] = pd.DatetimeIndex(orders['Date']).year

# pt1 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)
# print(pt1)

groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pt2 = pd.DataFrame({'Sum':s, 'Count':c})
print(pt2)