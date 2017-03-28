#-*- coding:utf-8 -*-
import tushare as ts

#返回值
#date : 交易日期 (index)
#open : 开盘价
#high : 最高价
#close : 收盘价
#low : 最低价
#volume : 成交量
#amount : 成交金额
ts.get_h_data('002337') #前复权
ts.get_h_data('002337', autype='hfq') #后复权
ts.get_h_data('002337', autype=None) #不复权
ts.get_h_data('002337', start='2015-01-01', end='2015-03-16') #两个日期之间的前复权数据

ts.get_h_data('399106', index=True) #深圳综合指数