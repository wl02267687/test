# 儲存檔案
# file=open("data.txt", mode="w", encoding="utf-8") # 開啟
# file.write("測試中文\nSecond Line") # 操作
# file.close() # 關閉
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("5\n3\n9\n67")

# 讀取檔案
# 把檔案中的數字資料, 一行一行的讀取出來, 並計算總合
# sum=0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for line in file: # 一行一行的讀取
#         sum+=int(line)
# print(sum)

# 使用 JSON 格式讀取, 複寫檔案
# import json
# with open("config.json", mode="r") as file:
#     data=json.load(file)
# print(data) # data 是一個字典資料
# print("name: ", data["name"])
# print("version: ", data["version"])

import json
# 從檔案中讀取 JSON 資料, 放入變數 data 裡面
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) # data 是一個字典資料
data["name"]="New name" # 修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)