# 隨機模組
# import random
# 隨機選取
# data=random.sample([1,5,6,10,20], 3) # 一次選擇3個
# print(data)
# 隨機調換順序 (洗牌的概念)
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)
# 隨機取得亂數
# data=random.random() # 0 ~ 1 之間的隨機亂數
# data=random.uniform(60,100) # 60 ~ 100 之間的隨機亂數
# print(data)
# 取得常態分配亂數
# 平均數 100, 標準差 10 得到的資料多數在 90 ~ 110 之間
# data=random.normalvariate(100,10)

# 平均數 0, 標準差 5, 得到的資料多數在 -5 ~ 5 之間
# data=random.normalvariate(0,5)
# print(data)

# 統計模組
import statistics as stat
# data=stat.mean([1,4,5,8]) # mean 平均數
# print(data)
# data=stat.median([1,2,3,4,5,8,9,23,100]) # median 中位數
# print(data)
data=stat.stdev([1,2,3,4,5,6,7,8,9]) # stdev 標準差
print(data)