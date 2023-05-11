import datetime
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
#
# data = []
# pd = pandas.read_excel(r'./test_file/yeas.xlsx')
# writer = pandas.ExcelWriter(r'./test_file/test.xlsx', engine='openpyxl', if_sheet_exists='replace', mode='a')
#
# data.append(pd)
#
# conn = pandas.concat(data, ignore_index=False)
# conn.to_excel(writer, index=False, sheet_name='test3')
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
# data = {}
# df = pandas.read_excel(r'D:\共享\Seafile\重庆呼入/会员表.xlsx',
#                        sheet_name='会员等级', usecols={"会员工号", "职位"})
# for row in df.itertuples():
#     data[row[1]] = row[2]
# # print(data)
#
# pd = pandas.read_excel(r'C:\Users\Administrator\Desktop\BI\效能场景每日数据\bak\效能20230509.xlsx')
# pd = pd.loc[pd['人员归属省份名称'] == '重庆']
# pd['人员类型'] = pd.apply(lambda x: data.get(x['员工编号']), axis=1)
# print(pd)

#
# data =[{
#         "file_name": "会员表",
#         "sheet_name": "会员等级",
#         "columns": ["会员工号", "职位"],
#         "mapping_columns": "员工编号",
#         "replace/append_columns": "人员类型"
#       }]
# print(len(data))
#
# for i in data:
#     print(i['file_name'])


# str = ['众信佳一班', 'ZXJ一班', '维语一班']
# data = []
#
# for i in str:
#     # print(i)
#     if i.find('众信佳') >= 0 or i.find('ZXJ') >= 0:
#         data.append(i)
#
# print(data)

# data = []
# pd_result = pandas.read_excel(r'C:\Users\Administrator\Desktop\Python\DataCleaning\test_file\新疆10月.xlsx')
# # data.append(pd_result)
# writer = pandas.ExcelWriter(r'C:\Users\Administrator\Desktop\Python\DataCleaning\prod_test\新疆项目\新疆原始报表.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace')
# pd = pandas.read_excel(r'C:\Users\Administrator\Desktop\Python\DataCleaning\prod_test\新疆项目\新疆原始报表.xlsx', sheet_name='日报')
# con = pandas.concat([pd_result, pd], ignore_index=False)
# con.to_excel(writer, index=False, sheet_name='日报')
# writer.close()

# writer = pandas.ExcelWriter(r'C:\Users\Administrator\Desktop\Python\DataCleaning\prod_test\陕西呼入\陕西原始数据表.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay')
# df = pandas.read_excel(r'C:\Users\Administrator\Desktop\Python\DataCleaning\prod_test\陕西呼入\陕西原始数据表.xlsx', sheet_name='场景')
# print(writer)


pd = pandas.read_excel(r'C:\Users\Administrator\Desktop\Python\DataCleaning\test_file\yeas_out.xlsx')
print(pd)
pd['日期'] = pd.apply(lambda x: datetime.datetime.strptime(str(x['日期']), '%Y%m%d'), axis=1)
print(pd)

# date = datetime.datetime.strptime('20230101', '%Y%m%d')
# print(date)