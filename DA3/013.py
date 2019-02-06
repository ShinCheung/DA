import pandas as pd
import matplotlib.pyplot as plt

weeks = pd.read_excel('./Orders.xlsx', index_col='Week')
print(weeks)
print(weeks.columns)
# 普通趋势图
# weeks.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])
# 画叠加曲线图只需要在plot后加area
# weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])
# 叠加柱状图,stacked=True
weeks.plot.bar(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'], stacked=True)
plt.title('Sales Weekly Trend', fontsize=16, fontweight='bold')
plt.ylabel('Total', fontsize=12, fontweight='bold')
plt.xticks(weeks.index, fontsize=8)
plt.show()