import pandas as pd

# # people = pd.read_excel('./People.xlsx', header = 1)
# people = pd.read_excel('./People.xlsx', header = None)
# people.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']
# # people = people.set_index('ID')
# people.set_index('ID', inplace = True)
# # print(people.shape)
# print(people.columns)
# # print(people.head())
# # print(people.head(3))
# # print('=====================================')
# # print(people.tail(3))
# people.to_excel('./output.xlsx')

df = pd.read_excel('./output.xlsx', index_col = 'ID')
df.to_excel('output2.xlsx')