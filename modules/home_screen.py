import tkinter as tk
from tkinter import ttk
from modules.campaigns import Campaigns
from modules.players import Players
from modules.rulesets import Rulesets


class HomeScreen(ttk.Frame):
    def __init__(self, parent, dbo, data_directory):
        super().__init__()

        self.parent = parent
        self.dbo = dbo
        self.data_directory = data_directory

        self.callbacks = {'return_to_home_screen': self.show_home_screen}

        ttk.Button(self, text='Campaigns', command=self.campaigns).grid()
        ttk.Button(self, text='Players', command=self.players).grid()
        ttk.Button(self, text='Rulesets', command=self.rulesets).grid()
        ttk.Button(self, text='Quit', command=parent.quit).grid()

        self.show_home_screen()

    def campaigns(self):
        self.pack_forget()
        Campaigns(
            self.parent,
            self.dbo,
            self.data_directory,
            self.callbacks
        )

    def players(self):
        self.pack_forget()
        Players(
            self.parent,
            self.dbo,
            self.data_directory,
            self.callbacks
        )

    def rulesets(self):
        self.pack_forget()
        Rulesets(
            self.parent,
            self.dbo,
            self.data_directory,
            self.callbacks
        )

    def show_home_screen(self):
        self.pack(in_=self.parent, expand=True, fill='both')
