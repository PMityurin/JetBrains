import datetime
import requests
from bs4 import BeautifulSoup
import time


def get_price():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=USDTTRY")
    data = response.json()
    return float(data['price'])

def get_price2():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=USDTRUB")
    data = response.json()
    return float(data['price'])

def read_my(money, n):
    with open('info.txt', 'r', encoding='utf-8') as f:
        with open('tratForDay.txt', 'w', encoding='utf-8') as tr:
            itog = {}
            itog2 = {}
            monthPrint = 0
            sumForMonth = 0
            lastMonth = {}
            for i in range(n):
                data = f.readline()
                dataM = data.split()[0]
                month = [int(temp) for temp in dataM.split('.')]
                if month[1] != monthPrint:
                    tr.write(f'За месяц {monthPrint:5} --> {sumForMonth:10.2f}\n')
                    tr.write('----------------------------------' * 2 + '\n')
                    monthPrint = month[1]
                    sumForMonth = 0
                    lastMonth = {key:itog[key] - itog2.get(key, 0) for key in itog.keys()}
                    copyitog = lastMonth.copy()
                    itog2 = itog.copy()
                    for i in range(len(copyitog)):
                        key = max(copyitog, key=copyitog.get)
                        if copyitog[key] > 0:
                            tr.write(f'{key:14} --> {copyitog[key]:10.2f} \n')
                        del copyitog[key]
                    tr.write('----------------------------------' * 2 + '\n')
                tr.write(f'{dataM:15}' + '-->')
                x = []
                sumForDay = 0
                strochka = f.readline()
                while strochka != '\n':
                    x.append(str(strochka).lower())
                    strochka = f.readline()
                for i in x:
                    how_much = [temp.strip() for temp in i.split(money)]
                    how_much[1] = how_much[1].split()
                    sumForDay += float(how_much[0])
                    itog[how_much[1][0]] = itog.get(how_much[1][0], 0) + float(how_much[0])
                # keys = [temp.strip() for temp in f.readline().split(',')]
                # cont1 = [temp.strip().split(',') for temp in f.readlines()]
                # cont = [dict(zip(keys, temp)) for temp in cont1]
                tr.write(f"{sumForDay:11.2f}")
                tr.write('\n')
                sumForMonth += sumForDay
            return itog

d1, m1 ,y1 = 26, 10, 2022  # Дата первой даты
d2, m2, y2 = 1, 3, 2023# Дата последней даты
t1 = datetime.datetime(y1, m1, d1)
t2 = datetime.datetime(y2, m2, d2)
delta = t2 - t1
n = delta.days + 1
m = "£" # обозначение денег
global_money = 0 # всего денег
global_slovar = {} # итоговый словарь

slovar = read_my("£", n)
global_money = sum(slovar.values())
#print(global_money)
#print(len(slovar))
global_slovar = slovar.copy()
curs_USDT_lir = get_price()
curs_USDT_rub = get_price2()
curs_lir_rub = 1 / curs_USDT_lir * curs_USDT_rub


with open('trat.txt', 'w', encoding='utf-8') as tr:
    tr.write(f'Всего потрачено --> {global_money:10.2f} лир за {n} дней. \nВ рублях        --> '
             f'{curs_lir_rub * global_money:10.2f} рублей\n')
    tr.write('***********' * 3 + '\n')
    for i in range(len(slovar)):
        key = max(slovar, key=slovar.get)
        tr.write(f'{key:15} --> {slovar[key]:10.2f} лир  --> {curs_lir_rub * slovar[key]:10.2f} '
                 f'рублей \n')
        #print(key, slovar[key])
        del slovar[key]
print('************************')
# print('Траты в день на необходимое:')
# slovar = global_slovar.copy()
# for i in range(len(slovar)):
#     key = max(slovar, key=slovar.get)
#     print(key, slovar[key]/n)
#     del slovar[key]
#     print('************************')
