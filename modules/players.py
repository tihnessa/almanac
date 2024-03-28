import tkinter as tk
from tkinter import ttk
from modules.utilities import Picker


class Players(ttk.Frame):
    def __init__(self, root, dbo, data_directory, callbacks):
        super().__init__()

        self.root = root
        self.dbo = dbo
        self.data_directory = data_directory
        self.callbacks = callbacks

        self.new_prompt = 'New Player'
        Picker(
            self,
            'players',
            columns=['name', 'contact_number', 'email', 'preferred_contact'],
            headings=['Name', 'Telephone', 'e-mail', 'Preferred contact']
        ).grid(row=0, column=0, columnspan=6)
        ttk.Button(
            self,
            text='Back',
            command=self.return_to_home_screen
        ).grid(row=1, column=5, sticky=tk.E)

        self.show_players()

    def return_to_home_screen(self):
        self.callbacks['return_to_home_screen']()
        self.destroy()

    def show_players(self):
        self.pack(in_=self.root, expand=True, fill='both')
