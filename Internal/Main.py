from Internal.parse_1 import *
from Internal.parse_2 import *
from Internal.parse_3 import *
from Internal.parse_4 import *
from Internal.parse_5 import *


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.img1 = tk.PhotoImage(file='prin.gif')
        self.img2 = tk.PhotoImage(file='it.gif')
        self.img3 = tk.PhotoImage(file='mech.gif')
        self.img4 = tk.PhotoImage(file='mst.gif')
        self.img5 = tk.PhotoImage(file='bjd.gif')
        tk.Label(
            root,
            bg='#bfdfff',
            text='Выберите журнал:',
            font='Impact 20').place(
            x=20,
            y=33,
            width=610,
            height=30)
        btn_open_parse_1 = tk.Button(
            root,
            text='ПРОГРАММНАЯ\nИНЖЕНЕРИЯ',
            font='Arial 8',
            command=self.open_parse_1,
            activebackground='#bfdfff',
            compound=tk.TOP,
            image=self.img1,
            fg='#FFFFFF',
            bg='#000080')
        btn_open_parse_1.place(x=80, y=80)
        btn_open_parse_2 = tk.Button(
            root,
            text='ИНФОРМАЦИОННЫЕ\nТЕХНОЛОГИИ',
            font='Arial 8',
            command=self.open_parse_2,
            compound=tk.TOP,
            fg='#FFFFFF',
            activebackground='#bfdfff',
            bg='#000080',
            image=self.img2)
        btn_open_parse_2.place(x=260, y=80)
        btn_open_parse_3 = tk.Button(
            root,
            text='МЕХАТРОНИКА,\nАВТОМАТИЗАЦИЯ,\nУПРАВЛЕНИЕ',
            font='Arial 8',
            command=self.open_parse_3,
            compound=tk.TOP,
            fg='#FFFFFF',
            activebackground='#bfdfff',
            bg='#000080',
            image=self.img3)
        btn_open_parse_3.place(x=350, y=320)
        btn_open_parse_4 = tk.Button(
            root,
            text='НАНО- И\nМИКРОСИСТЕМНАЯ\nТЕХНИКА',
            command=self.open_parse_4,
            font='Arial 8',
            compound=tk.TOP,
            fg='#FFFFFF',
            activebackground='#bfdfff',
            bg='#000080',
            image=self.img4)
        btn_open_parse_4.place(x=170, y=320)
        btn_open_parse_5 = tk.Button(
            root,
            text='БЕЗОПАСНОСТЬ\nЖИЗНЕДЕЯТЕЛЬНОСТИ',
            font='Arial 8',
            command=self.open_parse_5,
            compound=tk.TOP,
            fg='#FFFFFF',
            activebackground='#bfdfff',
            bg='#000080',
            image=self.img5)
        btn_open_parse_5.place(x=441, y=80)

        

    def open_parse_1(self): 
        parse_1()
    def open_parse_2(self): 
        parse_2()
    def open_parse_3(self): 
        parse_3()
    def open_parse_4(self): 
        parse_4()
    def open_parse_5(self): 
        parse_5()