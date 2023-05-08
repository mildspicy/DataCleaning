import json
import os
import shutil

from config import config as cfg
import pandas


def get_config():
    with open('./DataSplit/config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config


def execute():
    config = get_config()
    sp: SplitData = SplitData()
    sp.start_split(config)


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

    def start_split(self, config):
        # 循环文件
        for file in os.listdir(self.source_files):
            print(file)
            full_path = '{}/{}'.format(self.source_files, file)
            pd = pandas.read_excel(full_path, engine='openpyxl')
            update_date = pd['统计日期'].drop_duplicates().tolist()
            # 获取文件类型名
            file_category = file[:2]
            for project in config:
                self.config = config[project]
                if file_category in config[project]['split_files']:
                    filter_pd = self.filter_data(file_category, pd)
                    self.result.append(filter_pd)
                self.save_data(file_category, update_date)
                self.result = []
                print('{}__{}成功'.format(file, project))
            move_path = '{}/{}'.format(self.move_path, file)
            shutil.move(full_path, move_path)
            print('移动文件成功！！！！')

    def filter_data(self, file_category, pd):
        if file_category == "效能":
            filter_efficiency = self.config["filter_efficiency"]
            for row in filter_efficiency:
                if row == "人工接通量":
                    pd = pd.loc[(pd[row] > filter_efficiency[row])]
                else:
                    pd = pd[pd.apply(lambda x: x[row] in filter_efficiency[row], axis=1)]
        elif file_category == "场景":
            filter_efficiency = self.config["filter_scene"]
            for row in filter_efficiency:
                if row == "人工接通量":
                    pd = pd.loc[(pd[row] > filter_efficiency[row])]
                else:
                    pd = pd[pd.apply(lambda x: x[row] in filter_efficiency[row], axis=1)]
        print("filter success!!!!!")
        return pd

    def save_data(self, file_category, update_date):
        out_full_path = '{}/{}/{}.xlsx'.format(self.out_path, self.config['out_dir'],
                                               self.config[file_category]['file_name'])
        if os.path.exists(out_full_path):
            pd = pandas.read_excel(out_full_path, engine='openpyxl',
                                   sheet_name=self.config[file_category]['out_sheet_name'])
            result_date = pd['统计日期'].drop_duplicates().tolist()
            if update_date in result_date:
                for row in update_date:
                    pd = pd.loc[(pd['统计日期'] != row)]
            pd_result = pandas.DataFrame(self.result[0])
            con = pandas.concat([pd, pd_result], ignore_index=False)
        else:
            con = pandas.concat(self.result, ignore_index=False)
        con.to_excel(out_full_path, index=False, sheet_name=self.config[file_category]['out_sheet_name'],
                     engine='openpyxl')
        print("Export excel Success !!!!!!!!!")


if __name__ == '__main__':
    execute()
