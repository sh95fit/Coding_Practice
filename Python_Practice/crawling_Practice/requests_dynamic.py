# requests 이용 - 동적페이지 크롤링 테스트
import login_info
from bs4 import BeautifulSoup
import requests

# django-pydenticon 내에서 사용되는 collections.Callable 참조가 collections.abc.Callable로 이동해 제거된 Attribute라 발생하는 에러
import collections
if not hasattr(collections, 'Callable') :
    collections.Callable = collections.abc.Callable

#rems 로그인 세션 구현

hdr = {'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

session = requests.session()

url_login = 'https://rems.energy.or.kr/pub/view/login'
res = session.get(url_login, data = login_info.login_info, headers=hdr)
res.raise_for_status()

print(res)

# 동적 페이지를 request를 이용해 크롤링을 해야할 경우 Fetch/XHR을 확인하여 데이터를 업로드하는 실제 주소를 가져와야 함


# 해당 발전소 이동 세션
webpage = "https://rems.energy.or.kr/admin/stats/operHist?ensoType=15001&end=20221202&start=20221202&rtuEnteCode=10&meainTypeSeriNo=10&makrSeriNo=10&take=100&skip=0&page=1&pageSize=100&field=gathDtm&dir=desc&consmId=ugs-9&cid=&cityProvCode=&rgnCode=&fixbylawBundCode=&bsmanId=ugs"
res = session.get(webpage)
res.raise_for_status()
print(res)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

data = soup.find("results")

print(data)



# HTML 스크랩 시 데이터 크롤링 불가!