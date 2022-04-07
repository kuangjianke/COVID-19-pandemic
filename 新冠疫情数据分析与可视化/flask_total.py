import pandas as pd

class FLASK_DATA(object):
    def pandas_ht(self):
        data = pd.read_excel('附件1.xlsx', sheet_name='城市疫情')
        data1 = data
        data1['日期'] = data1['日期'].apply(lambda x: str(x)[:7])
        data1 = data1[['日期', '新增确诊', '新增治愈', '新增死亡']].groupby('日期').sum()
        date = data1.index.tolist()
        count = [data1['新增确诊'].to_list(), data1['新增治愈'].to_list(), data1['新增死亡'].to_list()]

        return date,count