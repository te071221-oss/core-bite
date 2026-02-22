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

# 2. index.html 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
content = f.read()

# 3. 글자 바꿔치기 (줄바꿈을 넣어 확실하게 만듦)
target_pattern = r'id="title".*?>.*?</h2>'
replacement_text = f'id="title" class="text-xl font-bold mb-4 text-gray-800">{new_title}</h2>'

content = re.sub(target_pattern, replacement_text, content, flags=re.DOTALL)

# 4. 저장
with open("index.html", "w", encoding="utf-8") as f:
f.write(content)
print(f"성공: {new_title}")

except Exception as e:
print(f"오류: {e}")

if __name__ == "__main__":
update()
