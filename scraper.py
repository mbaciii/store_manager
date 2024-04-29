import requests
from bs4 import BeautifulSoup


def euToLeke(price, eu, us):
    lekep = float(price * eu)
    return lekep

def euToUSD(price, eu, us):
    price = euToLeke(price, eu, us)
    usdp = price * us / 10000
    return usdp


req = requests.get('https://www.bankofalbania.org/Tregjet/Kursi_zyrtar_i_kembimit/')

soup = BeautifulSoup(req.text, 'lxml')
eu = ''
us = ''

table = soup.find_all('table')[0]
trs = table.find_all('tr')
for tr in trs:
    try:
        if tr.find_all('td')[0].text == 'Dollar Amerikan':
            us = tr.find_all('td')[2].get_text()
        if tr.find_all('td')[0].text == 'Euro':
            eu = tr.find_all('td')[2].get_text()
    except:
        pass


print(us)
print(eu)
print(euToLeke(100, float(eu), us))
print(euToUSD(100, float(eu), float(us)))
input()