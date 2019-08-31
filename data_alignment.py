# _*_ coding=utf-8 _*_

import pandas as pd

"""DataAlignment"""
# 两个对象的索引相同
data1 = pd.Series([12, 23, 10], index=['a', 'b', 'c'])
data2 = pd.Series([11, 22, 33], index=['b', 'c', 'a'])
# Series进行两个对象计算时，会按照索引进行对齐后计算
print(data1 + data2)

# 两个对象的索引不相同,如果只有一个对象在某个索引下有值，则结果中该索引的值为nan（缺失值）
data3 = pd.Series([23, 21, 24], index=['b', 'c', 'd'])
print(data1 + data3)

# 灵活运算,只存在一个对象中的索引下的值没有进行运算，直接合并了
data4 = data1.add(data3, fill_value=0)
print(data4)
