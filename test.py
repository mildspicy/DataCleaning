import os

import pandas
# pd = pandas.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a','b','c'])
# print(pd)
# print('________________________________')
# pd = pd.loc[(pd['a'] == 1)]
# print(pd)


# str = '效能1月.xlsx'
# print(str[:2])


# if os.path.exists(r'C:\Users\Administrator\Desktop\Python\DataCleaning\file\场景1月.xlsx'):
#     print(1)
# else:
#     print(2)


# os.chdir(r'C:\Users\Administrator\Desktop\Python\DataCleaning\file\场景1月.xlsx')

fil = {'20230101', '20230102', '20230103'}
# fil = [20230101, 20230102, 20230103]
# data = []
pd = pandas.read_excel(r'./test_file/日期数据.xlsx', engine='openpyxl', dtype=str)
pds = pd.apply(lambda x: x['日期'] in fil, axis=1)
print(pd[pds])

# data.append(pd)

# con = pandas.concat(data, ignore_index=False)
# con.to_excel(r'./test_file/file/', index=False, )

# pd = pd[pd.groupby['日期']['日期'].transform(lambda x: set(x) == fil)]
# pd = pd[pd..isin(fil)]
# print(pd.columns)
# pd = pd.groupby('日期')
# print(pd)

# df = pd.DataFrame({'project_id': [36423, 28564, 96648, 96648, 10042, 68277, 68277, 68277], 'codename': ['banana', 'apple', 'peach', 'peach', 'melon', 'pear', 'pear', 'pear'], 'studio': ['paris', 'amsterdam', 'frankfurt', 'paris', 'london', 'brussel', 'amsterdam', 'sofia']})
# reqd_studios = {'frankfurt', 'paris'}
# # idx_reqd_studios = df.apply(lambda x:  reqd_studios.issubset(set(df[df.project_id == x.project_id].studio)), axis=1)
# idx_reqd_studios = df.apply(lambda x:   x.studio in reqd_studios, axis=1)
# print(df[idx_reqd_studios])

