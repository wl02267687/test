# 抓取 PTT 八卦版的網頁原始碼 (HTML)
import urllib.request as req
def getDate(url):
    # 建立一個 Request 物件, 附加 Request Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    # 解析原始碼, 取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
    titles=root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除). 印出來
            print(title.a.string)
    # 抓取上一頁的連結
    nextLink=root.find("a", string="‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
    return nextLink["href"]

# 主程序: 抓取一個頁面的標籤
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getDate(pageURL)
    count+=1