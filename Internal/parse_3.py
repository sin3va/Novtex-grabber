from tkinter.ttk import Combobox
from tkinter import scrolledtext
from Common import *
from Internal.ready import *
from Internal.mistake1 import *
from Internal.mistake2 import *
from Internal.mistake3 import *
from Internal.mistake4 import *

class parse_3(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Мехатроника, автоматизация, управление')
        self.geometry('650x600+435+100')
        self.resizable(False, False)
        self.grab_set()
        self.focus_get()
        self['bg'] = '#FFFFFF'
        tk.Label(self, bg='#ffaaaa').place(x=20, y=20, width=610, height=560)
        tk.Label(
            self,
            bg='#ffaaaa',
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
        lbl_4 = tk.Label(self, text='Номер:', bg='#ffaaaa')
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
            bg='#ffaaaa',
            text='Выберите выпуск:',
            font='Impact 20').place(
            x=20,
            y=250,
            width=610,
            height=30)
        tk.Label(self, text='Год:', bg='#ffaaaa').place(x=70, y=295)
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
            activebackground='#ffaaaa',
            command=self.parse)
        btn_parse.place(x=350, y=292)
        btn_download1 = tk.Button(
            self,
            text='Скачать выпуск',
            fg='#FFFFFF',
            bg='#000080',
            width=16,
            activebackground='#ffaaaa',
            command=self.download1)
        btn_download1.place(x=70, y=326)
        btn_download2 = tk.Button(
            self,
            text='Скачать все выпуски одного года',
            fg='#FFFFFF',
            bg='#000080',
            width=30,
            activebackground='#ffaaaa',
            command=self.download2)
        btn_download2.place(x=200, y=326)
        btn_download3 = tk.Button(
            self,
            text='Скачать все выпуски',
            fg='#FFFFFF',
            bg='#000080',
            width=20,
            activebackground='#ffaaaa',
            command=self.download3)

        btn_download3.place(x=428, y=326)

        self.driver = webdriver.PhantomJS(
            executable_path=phantomjs_path)
        self.driver.get('http://novtex.ru/mech/index1.htm')
        maginfo = ''
        maginfo += self.driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td[2]/blockquote/p[ 5]/span').text
        maginfo += '\n' + self.driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td[2]/blockquot e/p[6]').text

        maginfo += '\n' + \
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td').text
        maginfo += '\n' + self.driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[4]/td/blockquote/block quote').text
        maginfo += '\n' + self.driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[4]/td/blockquote/p[1]').text
        anno.insert(tk.INSERT, maginfo)
        anno.configure(state='disabled')

        btn_exitroot = tk.Button(
            self,
            text='Выход',
            fg='#FFFFFF',
            bg='#000080',
            width=8,
            activebackground='#ffaaaa',
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
        elif int(self.combo2.get()) > 2016 or int(self.combo2.get()) < 2008 or (year == '2009' and int(self.combo1.get()) in [1, 3]):
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
            if year == '2009' and number == '6':
                url = 'http://novtex.ru/mech/mech09/archiv06.htm'
                driver.get(url)
                self.anno2.insert(tk.INSERT, '\n')

                self.anno2.insert(tk.INSERT, driver.find_element_by_xpath(
                    "/html/body/table/tbody/tr/td[2]/div/p[5]/em").text)
                self.anno2.insert(tk.INSERT, '\n')
                self.anno2.insert(tk.INSERT, driver.find_element_by_xpath(
                    "/html/body/table/tbody/tr/td[2]/div/p[6]").text)
            elif int(year) < 2010:
                try:
                    url = 'http://novtex.ru/mech/mech' + \
                        year[2] + year[3] + '/archiv' + nn + '.html'
                    driver.get(url)
                    annotation = driver.find_element_by_xpath(
                        "/html/body/table/tbody/tr/td[2]/div/table/tbody")
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, annotation.text)
                except Exception:
                    url = 'http://novtex.ru/mech/mech' + \
                        year[2] + year[3] + '/archiv' + nn + '.htm'
                    driver.get(url)
                    annotation = driver.find_element_by_xpath(
                        "/html/body/table/tbody/tr/td[2]/div/table/tbody")
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, annotation.text)
            elif int(year) == 2010:
                url = 'http://novtex.ru/mech/mech' + year + '/archiv' + nn + '.html'
                driver.get(url)
                if int(number) > 3:
                    annotation = driver.find_element_by_xpath(
                        "/html/body/table/tbody/tr/td[2]/div/div/table/tbody")
                else:

                    annotation = driver.find_element_by_xpath(
                        "/html/body/table/tbody/tr/td[2]/div/table/tbody")
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, annotation.text)
            elif int(year) == 2011:
                url = 'http://novtex.ru/mech/mech' + year + '/archiv' + nn + '.html'
                driver.get(url)
                if number == '5':
                    annotation = driver.find_element_by_xpath(
                        "/html/body/table/tbody/tr/td[2]/div/div/table/tbody")
                elif 8 > int(number) > 5 or int(number) > 8:
                    annotation = driver.find_element_by_xpath(
                        '/html/body/table/tbody/tr/td[2]/div/div/div/table/tbod y')

                elif int(number) == 8:
                    annotation = driver.find_element_by_xpath(
                        '/ html / body / table / tbody / tr / td[2] / div / div / div / div / table / tbody')

                else:
                    annotation = driver.find_element_by_xpath(
                        "/html/body/table/tbody/tr/td[2]/div/table/tbody")
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, annotation.text)
            elif (year == '2012' and int(number) in [7, 8]) or (year == '2013' and int(number) == 12):
                url = 'http://novtex.ru/mech/mech' + year + '/archiv' + nn + '.html'
                driver.get(url)
                annotation = driver.find_element_by_xpath(
                    "/html/body/table/tbody/tr/td[2]/div/table/tbody")
                self.anno2.insert(tk.INSERT, '\n')

                self.anno2.insert(tk.INSERT, annotation.text)
            else:
                url = 'http://novtex.ru/mech/mech' + year + '/archiv' + nn + '.html'
                driver.get(url)
                annotation = driver.find_element_by_xpath(
                    "/html/body/table/tbody/tr/td[2]/table/tbody")
                self.anno2.insert(tk.INSERT, '\n')
                self.anno2.insert(tk.INSERT, annotation.text)
                self.anno2.configure(state='disabled')

    def download1(self):
        if self.combo1.get() == "" or self.combo2.get() == '':
            mistake1()
        elif int(self.combo2.get()) > 2016 or int(self.combo2.get()) < 2008 or (self.combo2.get() == '2009' and int(self.combo1.get()) in [1, 3]):
            mistake2()
        else:
            download(form_link_3(self.combo2.get(), self.combo1.get()))
            ready()

    def download2(self):
        if self.combo2.get() == '':
            mistake3()
        elif int(self.combo2.get()) > 2016 or int(self.combo2.get()) < 2008:
            mistake4()
        elif self.combo2.get() == '2009':
            download(form_link_3(self.combo2.get(), '2'))
            for i in range(4, 13):
                download(form_link_3(self.combo2.get(), str(i)))
            ready()
        else:
            for i in range(1, 13):
                download(form_link_3(self.combo2.get(), str(i)))
            ready()

    def download3(self):
        for i in range(1, 13):
            download(form_link_3('2008', str(i)))
        download(form_link_3('2009', '2'))
        for i in range(4, 13):
            download(form_link_3('2009', str(i)))
        for j in range(2010, 2017):
            for i in range(1, 13):
                download(form_link_3(str(j), str(i)))
        ready()