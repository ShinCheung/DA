import pandas as pd
import numpy as np

# 外接圆面积
def get_circumcircle_area(l, h):
    r = np.sqrt(l ** 2 + h ** 2) / 2
    return r ** 2 * np.pi

# def wrapper(row):
#     return get_circumcircle_area(row['Length'], row['Height'])

rects = pd.read_excel('./Rectangles.xlsx', index_col='ID')
# axis=1为一行一行扫描
# rects['Circumcircle Area'] = rects.apply(wrapper, axis=1)
rects['Circumcircle Area'] = rects.apply(lambda row : get_circumcircle_area(row['Length'], row['Height']), axis=1)
print(rects)