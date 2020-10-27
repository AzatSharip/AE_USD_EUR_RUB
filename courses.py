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


    all_doll_euro = soup.find_all('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})[0].get_text()

    pre_doll = float(soup.find_all('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})[0].get_text().replace('₽', '').replace(',', '.'))
    cur_doll = float(soup.find_all('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})[1].get_text().replace('₽', '').replace(',', '.'))
    pre_euro = float(soup.find_all('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})[2].get_text().replace('₽', '').replace(',', '.'))
    cur_euro = float(soup.find_all('div', {'class': 'col-md-2 col-xs-9 _right mono-num'})[3].get_text().replace('₽', '').replace(',', '.'))

    doll_dyn = round((cur_doll - pre_doll), 2)
    if doll_dyn < 0:
        doll_arrow = 100
        doll_dynamics = doll_dyn * -1
        doll_null = 100
    elif doll_dyn > 0:
        doll_arrow = 0
        doll_dynamics = doll_dyn
        doll_null = 100
    else:
        doll_dynamics = doll_dyn
        doll_arrow = 0
        doll_null = 0  # Opacity of layer with arrow on doll_plus composition, "0" means 0%
        print('No changes in doll dynamics!')



    euro_dyn = round((cur_euro - pre_euro), 2)
    if euro_dyn < 0:
        euro_arrow = 100
        euro_dynamics = euro_dyn * -1
        euro_null = 100
    elif euro_dyn > 0:
        euro_arrow = 0
        euro_dynamics = euro_dyn
        euro_null = 100
    else:
        euro_dynamics = euro_dyn
        euro_arrow = 0
        euro_null = 0 # Opacity of layer with arrow on euro_plus composition, "0" means 0%
        print('No changes in euro dynamics!')



    doll_val = round(cur_doll, 2)
    euro_val = round(cur_euro, 2)

    today = datetime.datetime.today()
    day = today.strftime("%d")
    month = today.strftime("%m")
    month_dict = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
                  '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
                  }
    for keys in month_dict:
        if month == keys:
            month = month_dict[keys]

    date = day + ' ' + month


    print(date)
    print(doll_dynamics)
    print(euro_dynamics)
    print(doll_val)
    print(euro_val)
    print(doll_arrow)
    print(euro_arrow)

    print('tech info:', pre_doll, pre_euro, cur_doll, cur_euro)

