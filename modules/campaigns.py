# IMPORTS {{{
import tkinter as tk
from tkinter import ttk
from modules.utilities import Picker
# }}}


class Campaigns(ttk.Frame):  # {{{
    def __init__(self, root, dbo, data_directory, callbacks):  # {{{
        super().__init__()

        self.root = root
        self.dbo = dbo
        self.data_directory = data_directory
        self.callbacks = callbacks
        self.campaign_callbacks = {'open': self.open_campaign}

        details = {}
        list_of_campaigns = {'new_prompt': 'New campaign'}
        rows = self.dbo.select_data(
            'campaigns',
            ['title', 'ruleset', 'started', 'last_update', 'status', 'id']
        )
        for row in rows:
            title = {
                'text': {'text': row[0],},
                'grid': {
                    'row': 0,
                    'column': 0,
                    'columnspan': 2,
                    'sticky': tk.W,
                }
            }
            ruleset = {
                'text': {'text': row[1],},
                'grid': {
                    'row': 0,
                    'column': 2,
                    'sticky': tk.W,
                }
            }
            started = {
                'text': {'text': f'Start date: {row[2]}',},
                'grid': {
                    'row': 1,
                    'column': 0,
                    'sticky': tk.W,
                }
            }
            last_update = {
                'text': {'text': f'Last update: {row[3]}',},
                'grid': {
                    'row': 1,
                    'column': 1,
                    'sticky': tk.W,
                }
            }
            status = {
                'text': {'text': f'Status: {row[4]}',},
                'grid': {
                    'row': 1,
                    'column': 2,
                    'sticky': tk.W,
                }
            }

            list_of_campaigns.update(
                {
                    row[5]:{
                        'title': title,
                        'ruleset': ruleset,
                        'started': started,
                        'last_update': last_update,
                        'status': status,
                    }
                }
            )

        self.picker = Picker(self, list_of_campaigns, self.campaign_callbacks)

        self.picker.pack(side=tk.TOP, expand=True, fill='both')
        self.button = ttk.Button(
            self,
            text='Back',
            command=self.return_to_home_screen
        )
        self.button.pack(side=tk.RIGHT)

        self.show_campaigns()
    # }}}

    def return_to_home_screen(self):  #{{{
        self.callbacks['return_to_home_screen']()
        self.destroy()
    #}}}

    def show_campaigns(self):  #{{{
        self.pack(in_=self.root, expand=True, fill='both')
    # }}}

    def open_campaign(self, id):  # {{{
        self.picker.pack_forget()
        self.button.pack_forget()
    # }}}
# }}}

