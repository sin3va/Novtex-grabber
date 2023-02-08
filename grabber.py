from Internal.Main import Main
import tkinter as tk


def main():
    root = tk.Tk()
    tk.Label(root, bg='#bfdfff').place(x=20, y=20,
                                       width=610, height=560)
    app = Main(root)
    app.pack()
    root.title('Novtex.ru Ultimate Parser 3000')
    root.geometry('650x600+435+100')
    root['bg'] = '#FFFFFF'
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()
