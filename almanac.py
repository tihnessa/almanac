import tkinter as tk
from tkinter.messagebox import askyesno
import os
from modules.db_manager import DBManager
from modules.home_screen import HomeScreen


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        working_directory = os.getcwd()
        data_directory = os.path.join(working_directory, 'data')
        if not os.path.isdir(data_directory):
            os.makedirs(data_directory)
        dbo = DBManager(
            os.path.join(data_directory, 'campaigns_master.db')
        )
        if not os.path.isfile(os.path.join(data_directory, 'campaigns_master.db')):
            dbo.create_database(
                os.path.join(working_directory, 'sql', 'almanac.sql')
            )

        HomeScreen(self, dbo, data_directory)

    def quit(self):
        if askyesno('Quit?', 'Are you sure', icon='warning'):
            self.destroy()

if __name__ == '__main__':
    app = App()
    app.mainloop()
