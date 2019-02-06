import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./Student_Score.xlsx', sheet_name='Students', index_col='ID')
scores = pd.read_excel('./Student_Score.xlsx', sheet_name='Scores',index_col='ID')

# 默认相当于inner join取交集
# table = students.merge(scores, on='ID')
# 左连接，相当于left join
# table = students.merge(scores, how='left', on='ID').fillna(0)
# table = students.merge(scores, how='left', left_on=students.index, right_on=scores.index).fillna(0)
# 注意join方法没有left_on和right_on，只有how
table = students.join(scores, how='left', on='ID').fillna(0)
# 如果两表不叫ID不统一，用left_on和right_on
# table = students.merge(scores, how='left', left_on='ID1', right_on='ID2').fillna(0)
table.Score = table.Score.astype(int)
# table.drop(columns='ID2',inplace=True)
print(table)