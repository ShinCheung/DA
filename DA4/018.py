import pandas as pd

employees = pd.read_excel('./Employees.xlsx', index_col='ID')
df = employees['Full Name'].str.split(expand=True)
employees['FirstName'] = df[0]
employees['LastName'] = df[1].str.upper()
# print(df)
employees.drop(columns='Full Name', inplace=True)
print(employees)
