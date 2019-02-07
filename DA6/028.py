import pandas as pd
import numpy as np

page_001 = pd.read_excel('./Students2.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('./Students2.xlsx', sheet_name='Page_002')

# 两张表并在一起
# students = pd.concat([page_001, page_002], axis=1)

# 追加列
students = pd.concat([page_001, page_002]).reset_index(drop=True)
# students['Age'] = np.repeat(26, len(students))
# students['Age'] = 26
students['Age'] = np.arange(0, len(students))
# students['Age'] = range(0, len(students))
# 删除列
# students.drop(columns=['Age', 'Score'], inplace=True)
# 在第二列插一列
students.insert(1, column='Foo', value=np.repeat('foo', len(students)))
# 改列名
students.rename(columns={'Foo':'FOO', 'Name':'NAME'}, inplace=True)

# float浮点数才能设置为NaN,转ID类型为float
students['ID'] = students['ID'].astype(float)
for i in range(5,15):
    students['ID'].at[i] = np.nan
# 每行只要含NaN就删掉这一行
students.dropna(inplace=True)
print(students)