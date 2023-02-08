from tkinter.ttk import Combobox
from tkinter import scrolledtext
from Common import *
from Internal.ready import *
from Internal.mistake1 import *
from Internal.mistake2 import *
from Internal.mistake3 import *
from Internal.mistake4 import *

class parse_1(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Программная инженерия')
        self.geometry('650x600+435+100')
        self.resizable(False, False)
        self.grab_set()
        self.focus_get()
        self['bg'] = '#FFFFFF'
        tk.Label(self, bg='#aaaaff').place(x=20, y=20,
                                           width=610, height=560)
        tk.Label(
            self,
            bg='#aaaaff',
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

        lbl_4 = tk.Label(self, text='Номер:', bg='#aaaaff')
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
            bg='#aaaaff',
            text='Выберите выпуск:',
            font='Impact 20').place(
            x=20,
            y=250,
            width=610,
            height=30)
        tk.Label(self, text='Год:', bg='#aaaaff').place(x=70, y=295)
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
            activebackground='#aaaaff',
            command=self.parse)
        btn_parse.place(x=350, y=292)
        btn_download1 = tk.Button(
            self,
            text='Скачать выпуск',
            fg='#FFFFFF',
            bg='#000080',
            width=16,
            activebackground='#aaaaff',
            command=self.download1)
        btn_download1.place(x=70, y=326)
        btn_download2 = tk.Button(
            self,
            text='Скачать все выпуски одного года',
            fg='#FFFFFF',
            bg='#000080',
            width=30,
            activebackground='#aaaaff',
            command=self.download2)

        btn_download2.place(x=200, y=326)
        btn_download3 = tk.Button(
            self,
            text='Скачать все выпуски',
            fg='#FFFFFF',
            bg='#000080',
            width=20,
            activebackground='#aaaaff',
            command=self.download3)
        btn_download3.place(x=428, y=326)

        self.driver = webdriver.PhantomJS(
            executable_path=phantomjs_path)
        self.driver.get('http://novtex.ru/prin/rus/')
        maginfo = self.driver.find_element_by_xpath(
            '//*[@id="title_main"]/p').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('//*[@id="main_content"]/p[2]').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('//*[@id="main_content"]/p[3]').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('//*[@id="main_content"]/ul[1]').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('//*[@id="main_content"]/p[4]').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('//*[@id="main_content"]/ul[2]').text
        maginfo += '\n' + \
            self.driver.find_element_by_xpath('//*[@id="main_content"]/p[6]').text
        anno.insert(tk.INSERT, maginfo)
        anno.configure(state='disabled')

        btn_exitroot = tk.Button(
            self,
            text='Выход',
            fg='#FFFFFF',
            bg='#000080',
            width=8,
            activebackground='#aaaaff',
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
        elif int(self.combo2.get()) > 2017 or int(self.combo2.get()) < 2010 or (int(self.combo2.get()) == 2010 and int(self.combo1.get()) > 2) or (
                int(self.combo2.get()) == 2011 and int(self.combo1.get()) > 7) or (int(self.combo2.get()) == 2012 and int(self.combo1.get()) > 9):
            mistake2()
        else:
            driver = webdriver.PhantomJS(phantomjs_path)
            if int(year) > 2015:
                if year == '2016':
                    nt = '7'
                else:
                    nt = '8'
                url = 'http://novtex.ru/prin/rus/issues/' + \
                    nt + '_' + number + '_' + year + '.html'

                driver.get(url)
                annotations = driver.find_elements_by_class_name('issue_item')
                self.anno2.insert(
                    tk.INSERT, 'Содержание журнала "Программная инженерия"\n')
                self.anno2.insert(tk.INSERT, 'Номер ')
                self.anno2.insert(tk.INSERT, number)
                self.anno2.insert(tk.INSERT, ', ')
                self.anno2.insert(tk.INSERT, year)

                self.anno2.insert(tk.INSERT, ' год\n')
                for i in annotations:
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, i.text, '\n')
            else:
                if int(number) < 10:
                    nn = '0' + number
                else:
                    nn = number
                url = 'http://novtex.ru/prin/rus/issues/' + nn + '_' + year + '.html'
                driver.get(url)
                annotations = driver.find_elements_by_class_name('issue_item')
                self.anno2.insert(
                    tk.INSERT, 'Содержание журнала "Программная инженерия"\n')
                self.anno2.insert(tk.INSERT, 'Номер ')
                self.anno2.insert(tk.INSERT, number)
                self.anno2.insert(tk.INSERT, ', ')
                self.anno2.insert(tk.INSERT, year)
                self.anno2.insert(tk.INSERT, ' год\n')
                for i in annotations:
                    self.anno2.insert(tk.INSERT, '\n')
                    self.anno2.insert(tk.INSERT, i.text, '\n')
        self.anno2.configure(state='disabled')

    def download1(self):
        if self.combo1.get() == "" or self.combo2.get() == '':
            mistake1()
        elif int(self.combo2.get()) > 2017 or int(self.combo2.get()) < 2010 or (int(self.combo2.get()) == 2010 and int(self.combo1.get()) > 2) or (
                int(self.combo2.get()) == 2011 and int(self.combo1.get()) > 7) or (int(self.combo2.get()) == 2012 and int(self.combo1.get()) > 9):
            mistake2()
        else:
            download(form_link_1(self.combo2.get(), self.combo1.get()))
            ready()

    def download2(self):
        if self.combo2.get() == '':
            mistake3()
        elif int(self.combo2.get()) > 2017 or int(self.combo2.get()) < 2010:
            mistake4()
        else:
            if self.combo2.get() == '2010':
                for i in range(1, 3):
                    download(form_link_1(self.combo2.get(), str(i)))
            elif self.combo2.get() == '2011':
                for i in range(1, 8):
                    download(form_link_1(self.combo2.get(), str(i)))
            elif self.combo2.get() == '2012':
                for i in range(1, 10):
                    download(form_link_1(self.combo2.get(), str(i)))
            else:
                for i in range(1, 13):
                    download(form_link_1(self.combo2.get(), str(i)))
            ready()

    def download3(self):
        for i in range(1, 3):
            download(form_link_1('2010', str(i)))

        for i in range(1, 8):
            download(form_link_1('2011', str(i)))
        for i in range(1, 10):
            download(form_link_1('2012', str(i)))
        for j in range(2013, 2018):
            for i in range(1, 13):
                download(form_link_1(str(j), str(i)))
        ready()