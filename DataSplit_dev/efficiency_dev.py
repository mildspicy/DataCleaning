import datetime
import json
import os
import shutil

from config_dev import config as cfg
import pandas


def get_config():
    with open('./DataSplit_dev/config_dev.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config


def execute():
    config = get_config()
    sp: SplitData = SplitData()
    sp.start_split(config)


def get_team_name(df, columns_name, filter_name):
    filter_team = []
    teams = df[columns_name].drop_duplicates().tolist()
    for team in teams:
        for name in filter_name:
            if team.find(name) >= 0:
                filter_team.append(team)
    df = df[df.apply(lambda x: x[columns_name] in filter_team, axis=1)]
    return df


class SplitData:
    def __init__(self):
        # 根路径
        self.out_path = cfg.OUT_PATH
        # 数据源路径
        self.source_files = cfg.SOURCE_PATH
        # 结果数据集
        self.result = []
        # 筛选条件
        self.config = None
        # 历史文件路径
        self.move_path = cfg.MOVE_PATH
        # 数据表信息
        self.table = None
        # 项目名称
        self.name = None

    def start_split(self, config):
        # 循环文件
        for file in os.listdir(self.source_files):
            if os.path.isdir(file):
                continue
            print(file)
            source_full_path = '{}/{}'.format(self.source_files, file)
            pd = pandas.read_excel(source_full_path)
            # 获取文件类型名
            file_category = file[:2]
            for project in config:
                self.config = config[project]
                self.name = project
                for table in self.config['tables']:
                    self.table = table
                    if file_category != table['table_name']:
                        continue
                    filter_pd = self.filter_data(pd)
                    if len(self.config['mapping_tables']) > 0:
                        filter_pd = self.columns_replace_append(filter_pd)
                    update_date = filter_pd['统计日期'].drop_duplicates().tolist()
                    self.result.append(filter_pd)
                    if self.config['type'] == 1:
                        self.special_save_data(update_date)
                    else:
                        self.save_data(update_date)
                    self.result = []
                print('{}__{}成功'.format(file, project))
            move_path = '{}/{}'.format(self.move_path, file)
            shutil.move(source_full_path, move_path)
            print('移动文件成功！！！！')

    def filter_data(self, pd):
        for row in self.table['filter_name']:
            if row == "人工接通量":
                pd = pd.loc[(pd[row] > self.table['filter_name'][row])]
            elif self.name == "新疆" and row == '班组名称':
                pd = get_team_name(pd, row, self.table['filter_name'][row])
            else:
                pd = pd[pd.apply(lambda x: x[row] in self.table['filter_name'][row], axis=1)]
        print("filter success!!!!!")
        if self.name == '山东':
            pd['统计日期'] = pd.apply(lambda x: datetime.datetime.strptime(str(x['统计日期']), '%Y%m%d'), axis=1)
        return pd

    def columns_replace_append(self, df):
        mapping_data = {}
        for table in self.config['mapping_tables']:
            read_full_path = '{}/{}/{}.xlsx'.format(self.out_path, self.config['out_dir'],
                                                    table['file_name'])
            mapping_df = pandas.read_excel(read_full_path, sheet_name=table['sheet_name'],
                                           usecols=table['columns'])
            for row in mapping_df.itertuples():
                mapping_data[row[1]] = row[2]
            df[table['replace/append_columns']] = df.apply(lambda x: mapping_data.get(x[table['mapping_columns']]),
                                                           axis=1)
        return df

    def save_data(self, update_date):
        out_full_path = '{}/{}{}/{}.xlsx'.format(self.out_path, self.config['out_dir'],
                                                 self.table['out_path'],
                                                 self.table['file_name'])
        print(out_full_path)
        if os.path.exists(out_full_path):
            pd = pandas.read_excel(out_full_path, sheet_name=self.table['out_sheet_name'])
            result_date = pd['统计日期'].drop_duplicates().tolist()
            if [v for v in update_date if v in result_date]:
                for row in update_date:
                    pd = pd.loc[(pd['统计日期'] != row)]
            pd_result = pandas.DataFrame(self.result[0])
            con = pandas.concat([pd, pd_result], ignore_index=False)
        else:
            con = pandas.concat(self.result, ignore_index=False)

        con.to_excel(out_full_path, index=False, sheet_name=self.table['out_sheet_name'])
        print("Export excel Success !!!!!!!!!")

    # 特殊陕西、山东效能和场景合一个文件
    def special_save_data(self, update_date):
        out_full_path = '{}/{}{}/{}.xlsx'.format(self.out_path, self.config['out_dir'],
                                                 self.table['out_path'],
                                                 self.table['file_name'])

        if os.path.exists(out_full_path):
            writer = pandas.ExcelWriter(out_full_path, engine='openpyxl', mode='a', if_sheet_exists='overlay')
            if self.table['out_sheet_name'] in writer.sheets:
                pd = pandas.read_excel(out_full_path, sheet_name=self.table['out_sheet_name'])
                result_date = pd['统计日期'].drop_duplicates().tolist()
                if [v for v in update_date if v in result_date]:
                    for row in update_date:
                        pd = pd.loc[(pd['统计日期'] != row)]
                pd_result = pandas.DataFrame(self.result[0])
                con = pandas.concat([pd, pd_result], ignore_index=False)
            else:
                con = pandas.concat(self.result, ignore_index=False)
            con.to_excel(writer, index=False, sheet_name=self.table['out_sheet_name'])
            writer.close()
        else:
            con = pandas.concat(self.result, ignore_index=False)
            con.to_excel(out_full_path, index=False, sheet_name=self.table['out_sheet_name'])
        print("Export excel Success !!!!!!!!!")


if __name__ == '__main__':
    execute()
