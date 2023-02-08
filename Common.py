from selenium import webdriver
import requests
import shutil
import os

phantomjs_path = 'Phantomjs\\bin\\phantomjs'

def form_link_1(year, number):
    if int(number) < 10:
        n1 = '0' + number
    else:
        n1 = number
    n2 = year
    link = 'http://novtex.ru/prin/full/' + n1 + '_' + n2 + '.pdf'
    return link


def form_link_2(year, number):
    n1 = str(int(number))
    n2 = year[2] + year[3]
    if int(year) < 2010 or (
        year == '2010' and int(number) in [
            10, 11, 12]) or (
            year == '2013' and int(number) in [
                7, 11, 12]):
        link = 'http://novtex.ru/IT/it' + year + '/It' + n1 + n2 + '.pdf'
    elif int(year) < 2015:
        link = 'http://novtex.ru/IT/it' + year + '/It' + n1 + n2 + '_web.pdf'
    else:
        link = 'http://novtex.ru/IT/it' + year + '/it' + n1 + n2 + '_web.pdf'
    return link


def form_link_3(year, number):
    n1 = number
    n2 = year[2] + year[3]
    if int(year) == 2010 and int(number) in [6, 11, 12]:
        link = 'http://novtex.ru/mech/mech' + year + '/Mh' + n1 + n2 + '_web.pdf'
    elif int(year) == 2010 and int(number) == 7:
        link = 'http://novtex.ru/mech/mech2010/mh710.pdf'
    elif int(year) == 2010 and int(number) == 9:
        link = 'http://novtex.ru/mech/mech2010/mh910_web.pdf'
    elif int(year) == 2010 or (year == '2013' and number == '7'):
        link = 'http://novtex.ru/mech/mech' + year + '/Mh' + n1 + n2 + '.pdf'
    elif int(year) > 2010:
        link = 'http://novtex.ru/mech/mech' + year + '/Mh' + n1 + n2 + '_web.pdf'
    else:
        link = 'http://novtex.ru/mech/mech' + n2 + '/Mh' + n1 + n2 + '.pdf'
    return link


def form_link_4(year, number):
    n1 = year
    if int(number) < 10:
        n2 = '0' + number
    else:
        n2 = number
    link = 'http://novtex.ru/nmst/files/full/mc' + n1 + n2 + '.pdf'
    return link


def form_link_5(year, number):
    if int(number) < 10:
        nn = '0' + number
    else:
        nn = number
    driver = webdriver.PhantomJS(phantomjs_path)
    if int(year) < 2010:
        url0 = 'http://novtex.ru/bjd/archiv' + year + '.htm'
    else:
        url0 = 'http://novtex.ru/bjd/archiv' + year + '.html'
    driver.get(url0)
    raw = driver.find_elements_by_tag_name('a')
    strf = 'g' + number + year[2] + year[3]
    strm = 'number' + nn
    for i in raw:
        url2 = i.get_attribute('href')
        if url2.find(strm) != -1:
            urlm = url2
    driver.get(urlm)
    raw = driver.find_elements_by_tag_name('a')

    for i in raw:
        url2 = i.get_attribute('href')
        if url2.find(strf) != -1:
            urlf = url2
        if year == '2011' and number == '9':
            urlf = 'http://novtex.ru/bjd/bgd2011/Bg911.pdf'
    return urlf


def download(link):
    (dirname, filename) = os.path.split(link)
    r = requests.get(link, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
