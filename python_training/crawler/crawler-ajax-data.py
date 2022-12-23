#抓取 Medium.com 的文章資料 2021 版,加入 Request Data 的觀念
import urllib.request as req
# 建立連線網址
# 建立一個 Request 物件,附上 Request Headers 和 Request Data 的資訊
request=req.Request(url, headers={
    "Content-Type":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
})
# 解析 JSON 格式的資料,取得每篇文章的標題