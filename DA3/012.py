import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./Students3.xlsx', index_col='From')
print(students)

# counterclock=False为逆时针旋转，默认为True即顺时针；startangle调整旋转角度
students['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270)
plt.title('Source of International', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=12, fontweight='bold')
plt.show()