import os
# from DataSplit import efficiency
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

# fil = {'20230101', '20230102', '20230103'}
# fil = [20230101, 20230102, 20230103]
# data = []
#
# pd = pandas.read_excel(r'./test_file/yeas.xlsx')
# data.append(pd)
# writer = pandas.ExcelWriter(r'./test_file/test.xlsx', engine='openpyxl')
#
# con = pandas.concat(data, ignore_index=True)
#
# con.to_excel(writer, sheet_name="test2", index=False)
# con.to_excel(writer, sheet_name="test1", index=False)
#
# writer.close()

# data = []
# df = pandas.read_excel(r'./test_file/test.xlsx', sheet_name='test2')
# writer = pandas.ExcelWriter(r'./test_file/test.xlsx', engine='openpyxl', if_sheet_exists='replace', mode='a')
# for sheet in writer.sheets:
#     print(sheet)
# df = df.loc[df['日期'] == int(12)]
# print(df)
# # data.append(df)
# #
# # conn = pandas.concat(data, ignore_index=False)
# # conn.to_excel(writer, index=False, sheet_name='test3')
# writer.close()

# data1 = [20230430, 20230429, 20230428, 20230427, 20230426, 20230425, 20230424, 20230423, 20230422, 20230421, 20230420, 20230419, 20230418, 20230417, 20230416, 20230415, 20230414, 20230413, 20230412, 20230411, 20230410, 20230409, 20230408, 20230407, 20230406, 20230405, 20230404, 20230403, 20230402, 20230401]
# data2 = [20230501, 20230430]
# if set(data2) < set(data1):
#     print(1)
# else:
#     print(2)

# if [v for v in data1 if v in data2]:
#     print(1)
# else:
#     print(2)



# pds = pd.apply(lambda x: x['日期'] in fil, axis=1)
# columns = pd.columns.tolist()
# print(columns)
# df = pandas.DataFrame(columns=columns)
# print(df)
# df.to_excel(r'./test_file/test.xlsx')
# print(pd[pds])


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


# don = efficiency.get_config()


# columns = ['ww', 'ee']
# df = pandas.DataFrame(columns=columns)
# for project in config:
#     for index, row in enumerate(config[project]['out_sheets']):
#         print(config[project]['out_sheets'][index]['file_name'])
#         out_full_path = '{}/{}/{}.xlsx'.format(cfg.OUT_PATH, config[project]['out_dir'],
#                                                config[project]['out_sheets'][index]['file_name'])
#         df.to_excel(out_full_path, index=False)

df = pandas.read_excel(r'C:\Users\Administrator\Desktop\Python\DataCleaning\prod_test/河北呼入/场景表.xlsx',
                       sheet_name='场景表')
print(df)

