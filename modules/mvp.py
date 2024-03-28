import tkinter as tk
import tkinter.ttk as ttk


class Main(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        items = {}
        callback = {'open': self.open}

        f = tk.Frame(self)

        for i in range(5):
            items[i] = PickerObject(i, callback)
            items[i].pack(in_=f)

        f.pack()

    def open(self, id):
        print(f'ID = {id}')


class PickerObject(tk.Frame):
    def __init__(self, i, callback):
        super().__init__()

        self.id = i
        self.callbacks = callback

        self.widget = ttk.Label(self, text = f'Label: {i}')
        self.widget.pack()
        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)
        self.bind('<Double-Button-1>', self.on_double_click)

    def enter(self, event=None):
        self.config(background='light blue')
        self.widget.config(background='light blue')

    def leave(self, event=None):
        self.config(background='light grey')
        self.widget.config(background='light grey')

    def on_double_click(self, event=None):
        self.callbacks['open'](self.id)


if __name__ == '__main__':
    mw = tk.Tk()
    list_frame = Main(mw)
    list_frame.pack()
    mw.mainloop()
