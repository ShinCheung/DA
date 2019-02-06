import pandas as pd

def score_validation(row):
    # # 法1
    # try:
    #     assert 0<=row<=100
    # except:
    #     # 注意python的print字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式
    #     # 如果字符串里面没有表达式，那么前面加不加f输出应该都一样
    #     print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')
    # 法2
    if not 0<=row.Score<=100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')

# 注意：做数据校验的时候不要加index_col，这样逐行校验的时候所有的数据都能校验到
students = pd.read_excel('./Students.xlsx')
# print(students)
# 一行一行校验所以axis=1
students.apply(score_validation, axis=1)
