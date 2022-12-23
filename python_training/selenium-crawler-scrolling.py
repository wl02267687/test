# 載入 selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
# 設定 Chrom Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="D:\other\python_training\chromedriver.exe"
#----------- 讓瀏覽器不會關閉
options.add_experimental_option("detach", True)
# 建立 Driver 物件實體,用相關操作瀏覽器運作
driver=webdriver.Chrome(options=options)
# 連線到 Linkedin 工作搜尋網頁
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
# 捲動視窗並等待瀏覽器載入更多內容
n=0
while 3<n:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 捲動視窗到底部
    time.sleep(3) # 等待三秒鐘
    n+=1
# 取得網頁中工作的標題
titleTags=driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for titleTag in titleTags:
    print(titleTag.text)
driver.close()