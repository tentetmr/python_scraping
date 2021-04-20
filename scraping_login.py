
import requests
import re
from bs4 import BeautifulSoup

URL = "https://pdt.r-agent.com/"
LOGIN = "pdt/app/pdt_login_view"
LOGIN_ROUTE = "pdt/app/pdt_login?PDT31A"

s = requests.session()
response = s.get(URL + LOGIN)
bs = BeautifulSoup(response.content, "html.parser")
authenticity = bs.find(attrs={'name': 'sn'}).get('value')
cookie = response.cookies

info = {
    "sn": authenticity,
    "updateCheckFlag": "false",
    "accountId": "",
    "password": "",
    "autoLoginFlag": "true",
    "complete": "true"
}

res = s.post(URL + LOGIN_ROUTE, data=info, cookies=cookie)

soup = BeautifulSoup(res.content, "html.parser")


# title_tag = soup.h3
# title = title_tag.string
#
# companyNames = soup.select(".jobOfferPost-jobSubTitle")
# for companyName in companyNames:
#     print(companyName)

# companyName = soup.find_all(class_='jobOfferPost-jobSubTitle')
# print(companyName)

# print(soup)

p_list = soup.find_all(class_='jobOfferPost-jobSubTitle')
for p in p_list:
    print(p)
