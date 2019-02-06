import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('./Users.xlsx')
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True, ascending=True)
print(users)

# users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
# 转90度用barh
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
plt.tight_layout()
plt.show()