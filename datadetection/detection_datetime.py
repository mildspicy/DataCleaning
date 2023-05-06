import datetime
import time
import os

import pandas

path = r'D:\共享\Seafile'
dirs_file = {'UA人员表', 'Seafile', '安徽呼入', '权限表', '全网排名', '新模型', '运营日报上传数据', '整合数据', '众包外呼整合数据', '众信佳',
            'Desktop.ini' , 'seafile-data', 'Seafile项目文件.rar', '日期表.xlsx'}
active_dir = r'C:\Users\Administrator\Desktop'
active_file = 'Update_Active_Time.xlsx'

active_excel = '{}/{}'.format(active_dir, active_file)
result = []


if __name__ == '__main__':
    for dir in os.listdir(path):
        if os.path.isfile(dir):
            continue
        if dir not in dirs_file:
            print(dir)
            dir_path = '{}/{}'.format(path, dir)
            for file in os.listdir(dir_path):
                if file.endswith('xlsx'):
                    full_path = '{}/{}/{}'.format(path, dir, file)
                    print(full_path)
                    # pd = open(full_path, 'r')
                    start_date = os.path.getmtime(full_path)
                    start_date_up = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_date))
                    active_des = {
                        '运行时间': [datetime.datetime.now()],
                        '项目': [dir],
                        '文件': [file],
                        '更新时间': [start_date_up]
                    }
                    des = pandas.DataFrame(active_des)
                    result.append(des)

    con = pandas.concat(result, ignore_index=False, axis=0)
    con.to_excel(active_excel, index=False)






