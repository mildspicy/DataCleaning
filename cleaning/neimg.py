import pandas
from sqlalchemy import create_engine


class datacleaning:
    def __init__(self):
        self.rootpath = r'C:\Users\Administrator\Desktop\Python\DataCleaning\file'
        self.filename = '众包呼出每日生产数据.xlsx'
        self.dim_filename = '内蒙系数表.xlsx'
        self.server = 'localhost'
        self.databases = 'testbi'
        self.name = 'sa'
        self.password = '123456'
        self.filedata = []
        self.columns = {'手机号', '统计日期', '项目名称',  '营销成功量', '坐席通话总时长',
                        '结算通话时长', '省份', '内外网任务'}
        self.dim_filedata = []
        self.price = 65*0.92*0.8

    def get_server(self):
        # 'mssql+pymssql://sa:123456@localhost/testbi'
        engine = create_engine('mssql+pymssql://{}:{}@{}/{}'.format(self.name, self.password, self.server, self.databases))
        return engine

    def get_dim_file(self):
        dim_filepath = '{}/{}'.format(self.rootpath, self.dim_filename)
        dim_pd = pandas.read_excel(dim_filepath, sheet_name='内蒙古本地系数表', dtype=str,
                                   usecols={'项目', '响应系数', '小时目标', '秒数'})
        return dim_pd

    def merge_filedata(self):
        dim_pd = self.get_dim_file()
        filepath = '{}/{}'.format(self.rootpath, self.filename)
        engine = self.get_server()
        pd = pandas.ExcelFile(filepath)
        for sheet in pd.sheet_names:
            print(sheet)
            if sheet.endswith('xlsx'):
                continue
            # pds = pd.parse(sheet_name=sheet)
            fact_pd = pandas.read_excel(filepath, sheet_name=sheet, usecols=self.columns)
            merge_data = fact_pd.merge(dim_pd, left_on='项目名称', right_on='项目', how="left")
            merge_data['单价'] = self.price
            merge_filter = merge_data.loc[(merge_data['省份'] == "内蒙古") & (merge_data['内外网任务'] == "内网")]
            merge_filter.to_sql('Neimg', con=engine, index=False, if_exists='append')
            print("_______*100")
        print("数据成功")


if __name__ == '__main__':
    data = datacleaning()
    data.merge_filedata()
