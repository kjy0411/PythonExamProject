#_*_ coding:utf-8 _*_
import urllib.request as req
from bs4 import BeautifulSoup
from urllib import parse
import json

selnum=int(input("1.박스오피스\n2.실시간 예매율\n3.좌석 점유율\n선택:"))
url='https://www.kobis.or.kr/kobis/business/main/'
if selnum==1:
    print("박스 오피스")
    url+='searchMainDailyBoxOffice.do'
elif selnum==2:
    print("실시간 예매율")
    url+='searchMainRealTicket.do'
elif selnum==3:
    print("좌석 점유율")
    url+='searchMainDailySeatTicket.do'
web_data=req.urlopen(url).read().decode("utf-8")
#print(web_data)
#print(type(web_data))
json_data=json.loads(web_data)
print(json_data)
print(type(json_data))
i=1
for movie in json_data:
    print(str(i)+"."+movie['movieNm']+" - "+movie['movieNmEn'])
    i+=1
print()
mno=int(input("상세볼 영화 번호 입력:"))
for movie in json_data:
    if movie['rank']==mno:
        print(movie['movieNm'])
        print(movie['genre'])
        print(movie['director'])
        print(movie['synop'])