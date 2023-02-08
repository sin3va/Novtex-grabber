from tkinter.ttk import Combobox
from tkinter import scrolledtext
from Common import *
from Internal.ready import *
from Internal.mistake1 import *
from Internal.mistake2 import *
from Internal.mistake3 import *
from Internal.mistake4 import *

class parse_5(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title('Мехатроника, автоматизация, управление')
        self.geometry('650x600+435+100')
        self.resizable(False, False)
        self.grab_set()
        self.focus_get()
        self['bg'] = '#FFFFFF'
        tk.Label(self, bg='#bfffbf').place(x=20, y=20,
                                           width=610, height=560)
        tk.Label(
            self,
            bg='#bfffbf',
            text='Информация о журнале:',
            font='Impact 20').place(
            x=20,
            y=33,
            width=610,
            height=30)
        self.combo2 = Combobox(self, width=10, state='readonly')
        self.combo2.place(x=100, y=295)
        self.combo2['values'] = (
            '2020',
            '2019',
            '2018',
            '2017',
            '2016',
            '2015',
            '2014',
            '2013',
            '2012',
            '2011',
            '2010',
            '2009',
            '2008',
            '2007',
            '2006',
            '2005',
            '2004',
            '2003',
            '2002',
            '2001',
            '2000',
            '1999')

        lbl_4 = tk.Label(self, text='Номер:', bg='#bfffbf')
        lbl_4.place(x=200, y=295)
        self.combo1 = Combobox(self, width=10, state='readonly')
        self.combo1.place(x=250, y=295)
        self.combo1['values'] = (
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12')

        tk.Label(
            self,
            bg='#bfffbf',
            text='Выберите выпуск:',
            font='Impact 20').place(
            x=20,
            y=250,
            width=610,
            height=30)
        tk.Label(self, text='Год:', bg='#bfffbf').place(x=70, y=295)
        anno = scrolledtext.ScrolledText(self, width=69, height=10)
        anno.place(x=40, y=75)

        self.anno2 = scrolledtext.ScrolledText(self, width=69, height=10)
        self.anno2.place(x=40, y=360)
        self.anno2.configure(state='disabled')
        btn_parse = tk.Button(
            self,
            text='Показать содержание',
            fg='#FFFFFF',
            bg='#000080',
            width=31,
            activebackground='#bfffbf',
            command=self.parse)
        btn_parse.place(x=350, y=292)
        btn_download1 = tk.Button(
            self,
            text='Скачать выпуск',
            fg='#FFFFFF',
            bg='#000080',
            width=16,
            activebackground='#bfffbf',
            command=self.download1)
        btn_download1.place(x=70, y=326)
        btn_download2 = tk.Button(
            self,
            text='Скачать все выпуски одного года',
            fg='#FFFFFF',
            bg='#000080',
            width=30,
            activebackground='#bfffbf',
            command=self.download2)
        btn_download2.place(x=200, y=326)
        btn_download3 = tk.Button(
            self,
            text='Скачать все выпуски',
            fg='#FFFFFF',
            bg='#000080',
            width=20,
            activebackground='#bfffbf',
            command=self.download3)
        btn_download3.place(x=428, y=326)

        self.driver = webdriver.PhantomJS(
            executable_path=phantomjs_path)
        self.driver.get('http://novtex.ru/bjd/')
        maginfo = ''
        maginfo += self.driver.find_element_by_xpath(
            '/html/body/div/table/tbody/tr/td/div/p[2]').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/div/p[3]').text

        maginfo += '\n' + \
            self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/div/p[4]').text

        maginfo += '\n' + \
            self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/div/p[5]').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/div/p[6]').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td/div/p[7]').text
        anno.insert(tk.INSERT, maginfo)
        anno.configure(state='disabled')

        btn_exitroot = tk.Button(
            self,
            text='Выход',
            fg='#FFFFFF',
            bg='#000080',
            width=8,
            activebackground='#bfffbf',
            command=self.exitself)
        btn_exitroot.place(x=550, y=540)

    def exitself(self):
        self.destroy()


    def parse(self):
        year = self.combo2.get()
        number = self.combo1.get()

        self.anno2.configure(state='normal')
        self.anno2.delete(1.0, tk.END)
        if self.combo1.get() == "" or self.combo2.get() == '':
            mistake1()
        elif int(self.combo2.get()) > 2017 or int(self.combo2.get()) < 2008 or (year == '2017' and 6 < int(number) < 13) or (year == '2016' and number == '11'):
            mistake2()
        else:
            driver = webdriver.PhantomJS(phantomjs_path)

            if int(number) < 10:
                nn = '0' + number
            else:
                nn = number
            self.anno2.insert(
                tk.INSERT,
                'Содержание журнала "Мехатроника, Автоматизация, Управление"\n')
            self.anno2.insert(tk.INSERT, 'Номер ')
            self.anno2.insert(tk.INSERT, str(int(number)))
            self.anno2.insert(tk.INSERT, ', ')
            self.anno2.insert(tk.INSERT, year)
            self.anno2.insert(tk.INSERT, ' год\n')
            if int(year) < 2010:
                url0 = 'http://novtex.ru/bjd/archiv' + year + '.htm'
            else:
                url0 = 'http://novtex.ru/bjd/archiv' + year + '.html'
            driver.get(url0)
            raw = driver.find_elements_by_tag_name('a')
            strm = 'number' + nn
            for i in raw:
                url2 = i.get_attribute('href')
                if url2.find(strm) != -1:
                    url = url2
            driver.get(url)
            if (year == '2009' and int(number) in [8, 11, 12]) or (
                    year == '2010' and int(number) in [1, 2, 3, 5, 6, 7, 8, 9]):
                annotation = driver.find_elements_by_xpath(
                    "/html/body/table/tbody/tr/td/div")
                for i in annotation:
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, i.text)

            elif (year == '2009' and int(number) in [9, 10]):
                annotation = driver.find_element_by_xpath(
                    "/html/body/table/tbody/tr/td/table/tbody/tr/td/div[1]")
                self.anno2.insert(tk.INSERT, '\n')
                self.anno2.insert(tk.INSERT, annotation.text)
            elif (year == '2010' and int(number) in [11, 12]) or (year == '2011' and int(number) in [1]):
                if year == '2011' and int(number) == 1:
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, driver.find_element_by_xpath(
                        '/ html / body / table / tbody / tr[1] / td / p[5]').text)
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, driver.find_element_by_xpath(
                        '/html/body/table/tbody/tr[1]/td/div').text)
                    raw = driver.find_elements_by_tag_name('tr')
                    for i in raw[2:]:
                        self.anno2.insert(tk.INSERT, '\n')
                        self.anno2.insert(tk.INSERT, i.text)
                else:
                    raw = driver.find_elements_by_tag_name('tr')
                    if (year == '2010' and number == '10') or (
                            year == '2011' and int(number) in [2, 3, 4]):
                        raw1 = driver.find_elements_by_xpath(
                            '/html/body/table/tbody/tr[1]/td/p')
                        for i in raw1[4:]:
                            self.anno2.insert(tk.INSERT, '\n')
                            self.anno2.insert(tk.INSERT, i.text)
                    if year == '2010' and number == '10':
                        self.anno2.insert(tk.INSERT, '\n')

                        self.anno2.insert(tk.INSERT, driver.find_element_by_xpath(
                            '/html/body/table/tbody/tr[1]/td/div').text)
                    if year == '2011' and number == '5':
                        self.anno2.insert(tk.INSERT, '\n')
                        self.anno2.insert(tk.INSERT, driver.find_element_by_xpath(
                            '/ html / body / table / tbody / tr[1] / td / p[5]').text)
                        for i in raw[1:]:
                            self.anno2.insert(tk.INSERT, '\n')
                            self.anno2.insert(tk.INSERT, i.text)
                    if (year == '2010' and number == '4'):
                        self.anno2.insert(tk.INSERT, '\n')
                        self.anno2.insert(tk.INSERT, 'Приложение')
                        self.anno2.insert(tk.INSERT, '\n')

                        self.anno2.insert(tk.INSERT, driver.find_element_by_xpath(
                            '/html/body/table/tbody/ tr/td/div[1]/p[1]').text)
            self.anno2.configure(state='normal')

    def download1(self):
        if self.combo1.get() == "" or self.combo2.get() == '':
            mistake1()
        elif int(self.combo2.get()) > 2017 or int(self.combo2.get()) < 2008 or (self.combo2.get() == '2017' and
                                                                                6 < int(self.combo1.get()) < 13) or (self.combo2.get() == '2016' and self.combo1.get() == '11'):
            mistake2()
        else:
            download(form_link_5(self.combo2.get(), self.combo1.get()))

            ready()

    def download2(self):
        if self.combo2.get() == '':
            mistake3()
        elif int(self.combo2.get()) > 2017 or int(self.combo2.get()) < 2008:
            mistake4()
        elif self.combo2.get() == '2017':
            for i in range(1, 7):
                download(form_link_5(self.combo2.get(), str(i)))
            ready()
        elif self.combo2.get() == '2016':
            for i in range(1, 11):
                download(form_link_5(self.combo2.get(), str(i)))
            download(form_link_5(self.combo2.get(), '12'))
            ready()
        else:
            for i in range(1, 13):
                download(form_link_4(self.combo2.get(), str(i)))
            ready()

    def download3(self):
        for j in range(2008, 2016):
            for i in range(1, 13):
                download(form_link_3(str(j), str(i)))
        for i in range(1, 11):
            download(form_link_3('2016', str(i)))
        download(form_link_5('2016', '12'))
        for i in range(1, 7):
            download(form_link_3('2017', str(i)))

        ready()