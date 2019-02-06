import pandas as pd
import matplotlib.pyplot as plt

# 设置最大columns
pd.options.display.max_columns=777

homes = pd.read_excel('./home_data.xlsx')
# print(homes.head())

# 散点图
# homes.plot.scatter(x='sqft_living', y='price')
# homes.plot.scatter(y='sqft_living', x='price')
# 面积、报价的直方图,并用bins分桶
# homes.sqft_living.plot.hist(bins=100)
# homes.price.plot.hist(bins=100)
# plt.xticks(range(0,max(homes.sqft_living),500), fontsize=8, rotation=90)
# plt.xticks(range(0,max(homes.price),100000), fontsize=8, rotation=90)
# 密度图
# homes.sqft_living.plot.kde()
# plt.xticks(range(0,max(homes.sqft_living),500), fontsize=8, rotation=90)
# plt.show()

# 范围[-1,1]，1为完全相关，0为不相关，-1为负相关
# 所有两列两列数据的相关性
# print(homes.corr())
# 指定两列数据的相关性
print(homes.sqft_living.corr(homes.price))
