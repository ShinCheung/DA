import pandas as pd

def age_18_to_30(a):
    return a >= 18 and a < 30

def level_a(s):
    return 85 <= s <= 100

students = pd.read_excel('./Students.xlsx', index_col='ID')
# students = students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_a)]
# students = students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_a)]
# 可用lambda匿名函数代替def
students = students.loc[students.Age.apply(lambda a : a >= 18 and a < 30)] \
    .loc[students.Score.apply(lambda s : 85 <= s <= 100)]
print(students)