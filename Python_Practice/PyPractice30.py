# 정적 크롤링 - 주식 종가 가져오기
from bs4 import BeautifulSoup as BS
import requests as req

# module 'collections' has no attribute 'Callable' 에러 대응
# collections.Callable 참조가 파이썬 3.10부터 collections.abc.Callable로 이동하여, 제거된 Attribute라서 발생하는 오류
import collections     
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable
#------------------------------------------------------------------

url = "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

# 종목명 가져오기

# title_list = soup.select("a.tltle")
# # title_list = soup.select("div.box_type_l table.type_5 td > a")

# for title in title_list :
#     print(title.get_text(strip=True))


# 주식 리스트를 가져와 종목명, 현재가 출력
# stock_list = soup.select("table.type_5 tr td")
stock_list = soup.select("table.type_5 tr")
print("-------------------------------")
name = soup.select("tr.type1 th")[1].get_text(strip=True)
now = soup.select("tr.type1 th")[3].get_text(strip=True)
percent = soup.select("tr.type1 th")[5].get_text(strip=True)
print(f"{name}  {now}  {percent}")
print("-------------------------------")
for stock in stock_list :
    if len(stock.select("a.tltle")) == 0 :
        continue
    title = stock.select("a.tltle")[0].get_text(strip=True)
    price = stock.select("td:nth-of-type(4)")[0].get_text(strip=True)
    change = stock.select("td:nth-of-type(6)")[0].get_text(strip=True)
    print(title, price, change)