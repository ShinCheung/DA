import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./Students.xlsx')
students.sort_values(by='Number', inplace=True, ascending=False)
print(students)
# students.plot.bar(x='Field', y='Number', color='orange', title='International Students by Field')
plt.bar(students.Field, students.Number, color='orange')
plt.xticks(students.Field, rotation='90')
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('International Students by Field', fontsize=16)
plt.tight_layout()  #  显示紧凑
plt.show()