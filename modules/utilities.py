# IMPORTS {{{
import platform
import tkinter as tk
import tkinter.ttk as ttk
from functools import partial
from copy import copy
# }}}


class Picker(ttk.Frame):  # {{{
    def __init__(self, parent, rows, callbacks):
        super().__init__(parent)

        self.picker_objects = {}
        self.callbacks = copy(callbacks)

        self.picker_frame = ScrollFrame(self)
        self.picker_frame.pack(expand=True, fill='both')

        for k, v in rows.items():
            entry = PickerObject(self.picker_frame.viewPort, k, v, self.callbacks)
            self.picker_objects.update({k: entry})
# }}}


class PickerObject(tk.Frame):  #  {{{
    def __init__(self, parent, row_id, row_items, callbacks):  # {{{
        super().__init__(parent)

        self.callbacks = callbacks

        self.configure(highlightbackground='black')
        self.configure(highlightthickness=1)
        self.rowconfigure(20, weight=1)
        self.columnconfigure(3, weight=1)

        self.row_id=row_id
        self.widgets = {}
        if self.row_id == 'new_prompt':
            self.widgets['prompt'] = ttk.Label(self, text=row_items)
            self.widgets['prompt'].grid(row=0, column=0, rowspan=2, sticky=tk.W, pady=10)
        else:
            for k, v in row_items.items():
                self.widgets[k] = ttk.Label(self, **v['text'])
                self.widgets[k].grid(padx=(0,25), **v['grid'])

        self.grid(in_=parent, padx=5, pady=(5, 0), sticky=tk.W + tk.E)
        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)
        self.bind('<Double-Button-1>', self.on_double_click)
    # }}}

    def enter(self, event=None):  # {{{
        self.config(background='light blue')
        for widget in self.widgets:
            self.widgets[widget].config(background='light blue')
    # }}}

    def leave(self, event=None):  # {{{
        self.config(background='light grey')
        for widget in self.widgets:
            self.widgets[widget].config(background='light grey')
    #}}}

    def on_double_click(self, event=None):  # {{{
        self.callbacks['open'](self.row_id)
    # }}}
# }}}


class ScrollFrame(ttk.Frame):  # {{{
    """
    Scrollable Frame Class
    ======================
    The following code is from
        https://gist.github.com/mp035/9f2027c3ef9172264532fcd6262f3b01

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at https://mozilla.org/MPL/2.0/.
    """
    def __init__(self, parent, width=500):  # {{{
        super().__init__(parent)  # create a frame (self)

        self.canvas = tk.Canvas(self, borderwidth=0, width=width)  # place canvas on self
        self.viewPort = tk.Frame(
            self.canvas
        )  # place a frame on the canvas, this frame will hold the child widgets
        self.vsb = tk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview
        )  # place a scrollbar on self
        self.canvas.configure(
            yscrollcommand=self.vsb.set
        )  # attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")  # pack scrollbar to right of self
        self.canvas.pack(
            side="left", fill="both", expand=True
        )  # pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window(
            (4, 4),
            window=self.viewPort,
            anchor="nw",  # add view port frame to canvas
            tags="self.viewPort",
        )

        self.viewPort.bind(
            "<Configure>", self.onFrameConfigure
        )  # bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind(
            "<Configure>", self.onCanvasConfigure
        )  # bind an event whenever the size of the canvas frame changes.

        self.viewPort.bind(
            "<Enter>", self.onEnter
        )  # bind wheel events when the cursor enters the control
        self.viewPort.bind(
            "<Leave>", self.onLeave
        )  # unbind wheel events when the cursorl leaves the control

        self.onFrameConfigure(
            None
        )  # perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize
    # }}}

    def onFrameConfigure(self, event):  # {{{
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )  # whenever the size of the frame changes, alter the scroll region respectively.
    # }}}

    def onCanvasConfigure(self, event):  # {{{
        """Reset the canvas window to encompass inner frame when required"""
        canvas_width = event.width
        self.canvas.itemconfig(
            self.canvas_window, width=canvas_width
        )  # whenever the size of the canvas changes alter the window region respectively.
    # }}}

    def onMouseWheel(self, event):  # {{{
        """ Cross platform scroll wheel event """
        if platform.system() == "Windows":
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif platform.system() == "Darwin":
            self.canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")
    # }}}

    def onEnter(self, event):  # {{{
        """ Bind wheel events when the cursor enters the control """
        if platform.system() == "Linux":
            self.canvas.bind_all("<Button-4>", self.onMouseWheel)
            self.canvas.bind_all("<Button-5>", self.onMouseWheel)
        else:
            self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)
    # }}}

    def onLeave(self, event):  # {{{
        """ Unbind wheel events when the cursorl leaves the control """
        if platform.system() == "Linux":
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")
        else:
            self.canvas.unbind_all("<MouseWheel>")
    # }}}
# }}}

