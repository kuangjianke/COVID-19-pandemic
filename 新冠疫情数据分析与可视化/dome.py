# coding=utf-8
# !/usr/bin/python

import pandas as pd
from sklearn.cluster import KMeans#KMeans聚类算法
from sklearn.preprocessing import StandardScaler#数据标准化

data=pd.read_excel('附件1.xlsx', sheet_name = '国际疫情')
a=[]
data=data.loc[data.国家.isin(['印度','伊朗','意大利','加拿大','秘鲁','南非']),['日期','国家','累计确诊','累计治愈','累计死亡']]
print(data)
# data=data[['国家','累计确诊','累计治愈','累计死亡']].groupby('国家').sum()
#
# print(data)
# # datas=data.iloc[:,1:]
# # print(datas)
# datas1=StandardScaler().fit_transform(data)#后面填入pandas需要标准化数据的
# print(datas1)
# print(KMeans(n_clusters=5).fit(datas1))
