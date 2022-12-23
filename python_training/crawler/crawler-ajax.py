# 抓取 Medium.COM 的文章資料
import urllib.request as req
url="https://medium.com/_/api/home-feed"
# 建立一個 Request 物件, 附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 根據觀察, 取得的資料是 JSON 格式

# 解析JSON 格式的資料, 取得每篇文章的標題
import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data) # 把原始的 JSON 資料解析成字典/列表的表示形式
# 取得 JSON 資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])