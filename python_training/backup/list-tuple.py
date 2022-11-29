#有序可變動列表List
#grades=[12,43,24,78,54]
#grades[1:4]=[] #連續刪除列表中從編號1到編號4(不包刮)的資料
#grades=grades+[12,33]
#length=len(grades) # 取得列表的長度len(列表資料)
#print(length)
#grades[0]=55 #把55放到列表中第一個位置
#print(grades)

data=[[3,4,5],[6,7,8]]
print(data)
data[0][0:2]=[5,5,5]
print(data)

#有序不可變動列表Tuple
# data=(3,4,5)
# data[0]=5 #錯誤:Tuple的資料不可以變動
# print(data)