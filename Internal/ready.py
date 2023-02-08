import tkinter as tk

class ready(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Загрузка')
        self.geometry('300x100+635+350')
        self.resizable(False, False)
        self.grab_set()
        self.focus_get()
        self['bg'] = '#FFFFFF'
        tk.Label(
            self,
            bg='#ffffff',
            text='Файл(ы) успешно загружен(ы).').place(
            x=0,
            y=0,
            width=300,
            height=50)
        btn_exitroot = tk.Button(
            self,
            text='Ок',
            fg='#FFFFFF',
            bg='#000080',
            width=8,
            activebackground='#ffffff',
            command=self.exitself)
        btn_exitroot.pack(side=tk.BOTTOM, pady=15)

    def exitself(self):
        self.destroy()