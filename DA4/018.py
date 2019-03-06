import pandas as pd

employees = pd.read_excel('./Employees.xlsx', index_col='ID')
# 参数expand，这个参数取True时，会把切割出来的内容当做一列。 如果不需要pandas为你分好列，expand=False就可以了
df = employees['Full Name'].str.split(expand=True)
employees['FirstName'] = df[0]
employees['LastName'] = df[1].str.upper()
# print(df)
employees.drop(columns='Full Name', inplace=True)
print(employees)
