# -*-coding:utf-8-*-
import tushare as ts
import pandas as pd

# 参数
# index 是否为指数
df = ts.get_k_data('000001')
print df.head(10)
df = ts.get_k_data('000001', index=True)
print df.head(10)
