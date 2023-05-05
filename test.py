import pandas

rootpath = r'C:\Users\Administrator\Desktop\Python\DataCleaning\file'
filename = '众包呼出每日生产数据.xlsx'
dim_filename = '内蒙系数表.xlsx'
filedata = []
columns = {'手机号', '统计日期', '项目名称'}
dim_filedata = []

dim_filepath = '{}/{}'.format(rootpath, dim_filename)
dim_pd = pandas.read_excel(dim_filepath, sheet_name='内蒙古本地系数表', dtype=str,
                           usecols={'项目', '响应系数', '小时目标', '秒数'})


filepath = '{}/{}'.format(rootpath, filename)
fact_filedata = pandas.read_excel(filepath, sheet_name='202304')
merge_data = fact_filedata.merge(dim_pd,left_on='项目名称',right_on='项目', how="left")
data = merge_data.loc[(fact_filedata['省份'] == "内蒙古") & (fact_filedata['内外网任务'] == "内网")]
print(data)
