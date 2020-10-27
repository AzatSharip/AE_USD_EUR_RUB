# Курсы с новой версии оф. сайта ЦБ РФ. Рабочяя версия!
import requests
from bs4 import BeautifulSoup
import datetime


url = 'https://www.cbr.ru/'
r = requests.get(url)
with open('cbrf.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

with open('cbrf.html', 'rb') as output_file:
    text = output_file.read()

    soup = BeautifulSoup(text, features="lxml")


    all_doll_euro = soup.find_all('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})[1].get_text().replace('₽', '').replace(',', '.')
    print(all_doll_euro)
    # pre_doll = float(soup.find_all('div', {'class': 'indicator_el_value mono-num'})[0].get_text().replace('₽', '').replace(',', '.'))
    # cur_doll = float(soup.find_all('div', {'class': 'indicator_el_value mono-num'})[1].get_text().replace('₽', '').replace(',', '.'))
    # pre_euro = float(soup.find_all('div', {'class': 'indicator_el_value mono-num'})[2].get_text().replace('₽', '').replace(',', '.'))
    # cur_euro = float(soup.find_all('div', {'class': 'indicator_el_value mono-num'})[3].get_text().replace('₽', '').replace(',', '.'))

