import requests
from bs4 import BeautifulSoup
import datetime

def get_realtime_issue():
# 디시인사이드 실시간 베스트 혹은 주요 커뮤니티 타겟팅
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

try:
# 디시인사이드 실베 주소
url = "https://www.dcinside.com/"
res = requests.get(url, headers=header)
soup = BeautifulSoup(res.text, 'html.parser')

# 가장 상단에 있는 핫한 게시글 제목 추출
title_element = soup.select_one('.box_best .txt_box')
if title_element:
return title_element.text.strip()
return "현재 새로운 이슈를 분석 중입니다."
except Exception as e:
return "이슈 로딩 중 (잠시 후 업데이트)"

def update_site(new_title):
with open("index.html", "r", encoding="utf-8") as f:
content = f.read()

# 날짜 정보 추가
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# HTML 내용 중 '자동화 엔진 가동 준비 중...' 부분을 실제 제목으로 교체
# 한 번 교체된 후에도 계속 교체될 수 있도록 타겟팅을 잡습니다.
import re
# 제목 교체
content = re.sub(r'id="title".*?>.*?</h2', f'id="title" class="text-xl font-bold mb-4 leading-snug tracking-tight text-gray-800">{new_title}</h2', content, flags=re.DOTALL)
# 업데이트 시간 표시 (Live Update 옆)
content = content.replace("Live Update", f"Live Update ({now})")

with open("index.html", "w", encoding="utf-8") as f:
f.write(content)

if __name__ == "__main__":
issue = get_realtime_issue()
update_site(issue)
print(f"Update Success: {issue}")
