import json
import os

import pandas


class Efficiency:
    def __init__(self):
        self.name = None

    def get_config(self):
        with open('./DataSplit/config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config[self.name]

    def execute(self, name):
        self.name = name
        config = self.get_config()
        print(config)
        sp: SplitData = SplitData(config)
        sp.start_split()


class SplitData:
    def __init__(self, config):
        # 根路径
        self.rootpath = config['rootpath']
        # 项目文件夹名
        self.name = config['out_dir']
        # 数据源路径
        self.source_files = config['source_files']
        # 需要处理的数据表
        self.split_files = config['split_files']
        # 数据范围
        self.start_date = config['start_date']
        self.end_date = config['end_date']
        # 结果数据集
        self.result = []
        # 筛选条件
        self.config = config

    def start_split(self):
        for target_file in self.split_files:
            print(target_file)
            for file in os.listdir(self.source_files):
                print(file)
                if file.startswith(target_file):
                    full_path = '{}/{}'.format(self.source_files, file)
                    pd = pandas.read_excel(full_path, engine='openpyxl')
                    filter_pd = self.filter_data(target_file, pd)
                    self.result.append(filter_pd)
            self.save_data(target_file)
            self.result = []

    def filter_data(self, target_file, pd):
        if target_file == "效能":
            filter_efficiency = self.config["filter_efficiency"]
            for row in filter_efficiency:
                if row == "人工接通量":
                    pd = pd.loc[(pd[row] > filter_efficiency[row])]
                else:
                    pd = pd.loc[(pd[row] == filter_efficiency[row])]
        elif target_file == "场景":
            filter_efficiency = self.config["filter_scene"]
            for row in filter_efficiency:
                if row == "人工接通量":
                    pd = pd.loc[(pd[row] > filter_efficiency[row])]
                else:
                    pd = pd.loc[(pd[row] == filter_efficiency[row])]
        return pd

    def save_data(self, target_file):
        out_full_path = '{}/{}/{}.xlsx'.format(self.rootpath, self.name, target_file)
        con = pandas.concat(self.result, ignore_index=False)
        con.to_excel(out_full_path, index=False)


if __name__ == '__main__':
    Efficiency = Efficiency()
    tables = [
        "北京",
        # "广西"
    ]
    for name in tables:
        Efficiency.execute(name)

