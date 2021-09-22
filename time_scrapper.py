import requests
from bs4 import BeautifulSoup

url = 'https://www.bing.com/search?q=horas&cvid=7a16026623034fa2b9e2aa7816615a57&aqs=edge.0.0l7.4487j0j4&FORM=ANAB01&PC=U531'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52"}


page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

time = soup.find(id="digit_time").get_text()

print(time)
