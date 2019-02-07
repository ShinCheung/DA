import pandas as pd

page_001 = pd.read_excel('./Students2.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('./Students2.xlsx', sheet_name='Page_002')

# 表2追加到表1结尾
students = page_001.append(page_002).reset_index(drop=True)

# 结尾追加一行
stu = pd.Series({'ID':41, 'Name':'Abel', 'Score':99})
students = students.append(stu, ignore_index=True)

# 改变一行
# 法一
# students.at[39, 'Name'] = 'Bailey'
# students.at[39, 'Score'] = '120'
# 法二
stu = pd.Series({'ID':40, 'Name':'Bailey', 'Score':120})
students.iloc[39] = stu

# 插入一行
stu = pd.Series({'ID':101, 'Name':'Danni', 'Score':101})
part1 = students[:20]
part2 = students[20:]
students = part1.append(stu, ignore_index=True).append(part2).reset_index(drop=True)

# 删除指定行
# students.drop(index=[0,1,2],inplace=True)
# students.drop(index=range(0,10),inplace=True)
# students.drop(index=students[0:10].index,inplace=True)

for i in range(5,15):
    students['Name'].at[i] = ''
# 删除Name为空的行
missing = students.loc[students['Name'] == '']
students.drop(index=missing.index, inplace=True)
# students.reset_index(drop=True, inplace=True)
students = students.reset_index(drop=True)
print(students)