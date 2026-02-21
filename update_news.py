import requests
from bs4 import BeautifulSoup

def get_hot_topic():
# 예시로 디시인사이드 실베 제목 하나를 가져오는 구조입니다.
try:
header = {'User-Agent': 'Mozilla/5.0'}
res = requests.get("https://www.dcinside.com/", headers=header)
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.select_one('.box_best .txt_box').text.strip()
return title
except:
return "실시간 이슈를 불러오는 중입니다..."

def update_html(new_title):
with open("index.html", "r", encoding="utf-8") as f:
html = f.read()

# 임시로 제목 부분만 갈아끼우는 로직입니다.
updated_html = html.replace("자동화 엔진 가동 준비 중...", new_title)

with open("index.html", "w", encoding="utf-8") as f:
f.write(updated_html)

if __name__ == "__main__":
topic = get_hot_topic()
update_html(topic)
print(f"업데이트 성공: {topic}")
