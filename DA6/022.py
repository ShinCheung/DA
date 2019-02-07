import pandas as pd

# csv是指用逗号分割的
# tsv是指用\t分割的，即tab键
# 无论csv还是tsv都用pd.read_csv读取

# students1 = pd.read_csv('./Students.csv', sep=',', index_col='ID')
students1 = pd.read_csv('./Students.csv', index_col='ID')
print(students1)

# students2 = pd.read_csv('./Students.tsv', sep='\t', index_col='ID')
# print(students2)

# students3 = pd.read_csv('./Students.txt', sep='|', index_col='ID')
# print(students3)