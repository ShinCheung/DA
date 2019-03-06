import pandas as pd

students = pd.read_excel('./Students_Duplicates.xlsx')
# 去除重复数据，keep为first是保留重复的第一次的数据，last保留重复数据的最后面的数据
# students.drop_duplicates(subset='Name', inplace=True, keep='first')
# students.drop_duplicates(subset='Name', inplace=True, keep='last')
# print(students)

# 找出重复数据，dupe返回值为True为有重复数据，False为无重复数据，subset为指定列
dupe = students.duplicated(subset='Name')
# 有没有重复数据，True为有
# print(dupe)
# print(dupe.any())
# 有多少重复数据
# print(dupe.sum())
dupe = dupe[dupe == True]
print(students.iloc[dupe.index])
