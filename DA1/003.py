import pandas as pd

# d = {'x':100, 'y':200, 'z':300}
# # print(d.keys())
# # print(d.values())
# # print(d.items())
# # print(d['x'])
# s1 = pd.Series(d)
# # print(s1)
# # print(s1.index)

# L1 = [100, 200, 300]
# L2 = ['x', 'y', 'z']
# s1 = pd.Series(L1, index = L2)
# print(s1)

# s1 = pd.Series([100, 200, 300], index = ['x', 'y', 'z'])
# print(s1)

s1 = pd.Series([1,2,3], index=[1,2,3], name='A')
s2 = pd.Series([10,20,30], index=[1,2,3], name='B')
# s3 = pd.Series([100,200,300], index=[1,2,3], name='C')
s3 = pd.Series([100,200,300], index=[2,3,4], name='C')

df = pd.DataFrame({s1.name:s1, s2.name:s2, s3.name:s3})
# df = pd.DataFrame([s1,s2,s3])
print(df)