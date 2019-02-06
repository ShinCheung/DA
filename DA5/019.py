import pandas as pd

students = pd.read_excel('./Students.xlsx', index_col='ID')
tmp = students[['Test_1', 'Test_2', 'Test_3']]
# 按行求
row_sum = tmp.sum(axis=1)
row_mean = tmp.mean(axis=1)
students['Total'] = row_sum
students['Average'] = row_mean
# 按列求
col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
col_mean['Name'] = 'Summary'
students = students.append(col_mean, ignore_index=True)
print(students)