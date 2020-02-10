# coding: Shift_JIS
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://p.eagate.573.jp/game/sdvx/v/p/playdata/rival/score.html?rival_id=SV-7841-1410&page=3"
LOGIN_URL = "https://p.eagate.573.jp/gate/p/common/login/api/login_auth.html"
MAIN_URL = "https://p.eagate.573.jp/gate/p/mypage/index.html"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)\
			AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
                        "Accept": "text/html,application/xhtml+xml,application/xml;\
			q=0.9,imgwebp,*/*;q=0.8", "Sec-Fetch-Site": "same-origin"}

user = 'realrlgus@naver.com'
password = 'wc960620'
otp = ''
resrv_url = 'http://p.eagate.573.jp/gate/p/login_complete.html'
captcha = 'k_79470362776506310632319309433945_399a73323dc939a31680e3495cb8cc3d__293c03a71c6ac5f7c4c33e86f6066aa6__'

session = requests.session()
session.headers.update(header)

params = dict()
params['login_id'] = user
params['pass_word'] = password
params['otp'] = otp
params['resrv_url'] = resrv_url
params['captcha'] = captcha

res = session.post(LOGIN_URL, data=params)

response = session.get(MAIN_URL, headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
pages = soup.find("a", {"id": "id_paseli_inquiry"})
print(pages)
# for page in pages:
#    print(page.text)
