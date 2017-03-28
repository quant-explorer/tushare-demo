# -*- coding:utf-8 -*-
import pandas as pd
import tushare as ts
import sys

# 返回值
# 14个列：open,high,close,low,
# volume,
# price_change,
# p_change,
# ma5,ma10,ma20,
# v_ma5,v_ma10,v_ma20,
# turnover

# 参数
# code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
# start：开始日期，格式YYYY-MM-DD
# end：结束日期，格式YYYY-MM-DD
# ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
# retry_count：当网络异常后重试次数，默认为3
# pause:重试时停顿秒数，默认为0
df = ts.get_hist_data('002852')  # 获取单只股票历史数据，包括今天
df = ts.get_hist_data('600848', ktype='W')  # 获取周k线数据
df = ts.get_hist_data('600848', ktype='M')  # 获取月k线数据
df = ts.get_hist_data('600848', ktype='5')  # 获取5分钟k线数据
df = ts.get_hist_data('600848', ktype='15')  # 获取15分钟k线数据
df = ts.get_hist_data('600848', ktype='30')  # 获取30分钟k线数据
df = ts.get_hist_data('600848', ktype='60')  # 获取60分钟k线数据
df = ts.get_hist_data('sh')  # 获取上证指数k线数据，其它参数与个股一致，下同
df = ts.get_hist_data('sz')  # 获取深圳成指k线数据
df = ts.get_hist_data('hs300')  # 获取沪深300指数k线数据
df = ts.get_hist_data('sz50')  # 获取上证50指数k线数据
df = ts.get_hist_data('zxb')  # 获取中小板指数k线数据
df = ts.get_hist_data('cyb')  # 获取创业板指数k线数据
