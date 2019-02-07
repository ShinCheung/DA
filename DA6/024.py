import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 原始数据Month是像2017.01这样的会识别为float，所以转为str
sales = pd.read_excel('./Sales.xlsx', dtype={'Month':str})
print(sales)

slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)
exp = sales.index * slope + intercept
# 预测第35的值
print(slope*35 + intercept)

# plt.bar(sales.index, sales.Revenue)
plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='orange')
plt.title(f'y={slope}*x + {intercept}')
plt.xticks(sales.index, sales.Month, rotation=90)
plt.tight_layout()
plt.show()