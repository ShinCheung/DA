import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./Students2.xlsx')
students.sort_values(by='2017',ascending=False, inplace=True)
print(students)
students.plot.bar(x='Field', y=['2016', '2017'], color=['orange', 'red'])
plt.title('International Students by Field', fontsize=16, fontweight='bold')
plt.xlabel('Field', fontweight='bold')
plt.ylabel('Number', fontweight='bold')
ax = plt.gca()  # 拿到当前轴axis
ax.set_xticklabels(students['Field'], rotation='45', ha='right')
f = plt.gcf()   # 拿到当前figure，即当前图
f.subplots_adjust(left=0.2, bottom=0.42)
# plt.tight_layout()
plt.show()