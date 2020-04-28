import requests
from bs4 import BeautifulSoup
import re

url = 'https://kovalut.ru/kurs/ufa/'
r = requests.get(url)
with open('best.html', 'wb') as output_file:
    output_file.write(r.text.encode('utf8'))

with open('best.html', 'rb') as output_file:
    text = output_file.read()
    soup = BeautifulSoup(text, features="lxml")


    exception_list = list()
    ex = soup.find_all('tr', {'class': ['wi', 'wigr1']})

    # Лист исключения. Эти банки не берем, потому что у них есть условия и комиссии
    for e in ex:
        if 'комиссия' in e.text:
            exc_bank = e.find_previous_sibling("tr")
            exc_bank = exc_bank.find('a', {'class': ['t-b']})
            exc_bank = str(exc_bank)
            exc_bank = re.sub(r'<a.*?>', '', exc_bank).replace('</a>', '')
            exception_list.append(exc_bank)
        elif 'обмен только' in e.text:
            ex_bank = e.find_previous_sibling("tr")
            ex_bank = ex_bank.find('a', {'class': ['t-b']})
            ex_bank = str(ex_bank)
            ex_bank = re.sub(r'<a.*?>', '', ex_bank).replace('</a>', '')
            exception_list.append(ex_bank)
    # print('Exception banks list:', exception_list)


    banks = soup.find_all('a', {'class': ['t-b']})
    print('Banks: ', len(banks))

    banks = soup.find_all('tr', {'class': ['wi', 'wigr1']})
    dec = soup.find(class_ = 'wigr1 bot')

    elem = list()
    for b in banks:
        content = b.get_text()
        content = content.strip(' ')
        content = content.strip('\xa0')
        content = content.split('\n')
        elem.append(content)

    [e.remove('') for e in elem]
    elements = list()
    for e in elem:
        elements.append(e[0:5])

    # Очищаем список от шлака, оставляем только банки и цены покупки/продажи
    for e in elements:
        if len(e) < 5:
            i = elements.index(e)
            elements.pop(i)
    elements.pop(0)

    # Удаляем из списка все банки - исключения
    for ex in exception_list:
        for e in elements:
            if ex in e:
                i = elements.index(e)
                elements.pop(i)

    # Создаем словари, где ключи - название банка, а значения - стоимость продажи или покупки
    elements2 = list()
    db = dict()
    ds = dict()
    eb = dict()
    es = dict()
    for e in elements:
        e = [e.replace(',', '.') for e in e]
        db[float(e[1])] = e[0]
        ds[float(e[2])] = e[0]
        eb[float(e[3])] = e[0]
        es[float(e[4])] = e[0]

    # Находим минимальные и максимальные значения ключей в словарях. А потом вытаскиваем по ключу название банка
    doll_buy = max(db)
    doll_buy_b = db[doll_buy]

    doll_sale = min(ds)
    doll_sale_b = ds[doll_sale]

    euro_buy = max(eb)
    euro_buy_b = eb[euro_buy]

    euro_sale = min(es)
    euro_sale_b = es[euro_sale]
    print(doll_buy, doll_buy_b, doll_sale, doll_sale_b, euro_buy, euro_buy_b, euro_sale, euro_sale_b)