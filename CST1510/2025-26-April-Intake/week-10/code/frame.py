'''tutorial https://www.pythontutorial.net/tkinter/'''

from tkinter import *


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()




if __name__ == '__main__':
    root = Tk()
    root.title('Window')
    root.geometry("700x500+100+100")
    my_app = App(root)
    my_app.mainloop()