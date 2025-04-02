import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import pytz

# 日本時間で現在時刻取得
jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst)
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# YahooニュースRSS
url = "https://news.yahoo.co.jp/rss/topics/top-picks.xml"
response = requests.get(url)
soup = BeautifulSoup(response.content, "xml")
items = soup.find_all("item")

# ファイル名
filename = f"news_{timestamp}.csv"

# CSV保存
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["日付", "タイトル", "URL"])
    for item in items:
        title = item.title.text
        link = item.link.text
        writer.writerow([now.strftime("%Y-%m-%d"), title, link])

print(f"✅ {filename} に保存しました！（{now.strftime('%H:%M:%S')} に実行）")
