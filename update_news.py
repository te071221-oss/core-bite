import requests
from bs4 import BeautifulSoup
import os
import re

def update():
try:
# 1. 뉴스 제목 가져오기
url = "https://pann.nate.com/talk/ranking"
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(res.text, 'html.parser')
new_title = soup.select_one('.tit').text.strip()

# 2. 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
content = f.read()

# 3. 글자 바꿔치기 (오타 수정 완료!)
# id="title" 태그의 내용을 실시간 제목으로 교체합니다.
content = re.sub(r'id="title".*?>.*?</h2>', f'id="title" class="text-xl font-bold mb-4 text-gray-800">{new_title}</h2>', content, flags=re.DOTALL)

# 4. 저장
with open("index.html", "w", encoding="utf-8") as f:
f.write(content)
print(f"업데이트 성공: {new_title}")

except Exception as e:
print(f"오류 발생: {e}")

if __name__ == "__main__":
update()
