import tkinter as tk
from tkinter import ttk

spacing = 20
FrameHeight = 100
FrameWeight = 250
color1 = '#140b1e'
color2 = '#423458'
color3 = '#64d3b5'


class Dashboard(ttk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=400,
            width=500,
            padding=20,
            style='New.TFrame'
        )
        self.pack_propagate(0)

        titleLabel = tk.Label(
            self,
            font='arial 35 bold',
            text='Total Deaths From New Zealand by 2010-2021',
            bg=color2,
            pady=10,
        )
        titleLabel.grid(row=0, column=0, columnspan=2, pady=20)

        frame1 = Frame1(self)
        frame1.grid(column=0, row=1, rowspan=4, padx=(0, spacing))

        frame2 = Frame2(self)
        frame2.grid(column=1, row=1, pady=(0, spacing))

        frame3 = Frame3(self)
        frame3.grid(column=1, row=2, pady=(0, spacing))

        frame4 = Frame4(self)
        frame4.grid(column=1, row=3, pady=(0, spacing))

        frame5 = Frame5(self)
        frame5.grid(column=1, row=4, )


class Frame1(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=465,
            width=760,
            bg=color1,
        )
        self.pack_propagate(0)

        label1 = tk.Label(self, text='GRAPH', bg=color1, fg=color3, font='arial 50 bold')
        label1.pack(expand=1, fill='both')


class Frame2(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWeight,
            bg=color1,
        )
        self.pack_propagate(0)

        label1 = tk.Label(self, text='100,000', bg=color1, fg=color3, font='arial 35 bold')
        label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Total Deaths', bg=color1, font='arial 15 bold')
        label2.pack(expand=1, fill='both', )


class Frame3(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWeight,
            bg='#140b1e',
        )
        self.pack_propagate(0)

        label1 = tk.Label(self, text='2010-2021', bg=color1, fg=color3, font='arial 35 bold')
        label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Year', bg=color1, font='arial 15 bold')
        label2.pack(expand=1, fill='both', )


class Frame4(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWeight,
            bg='#140b1e',
        )
        self.pack_propagate(0)

        label1 = tk.Label(self, text='All', bg=color1, fg=color3, font='arial 30 bold')
        label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Gender', bg=color1, font='arial 15 bold')
        label2.pack(expand=1, fill='both', )


class Frame5(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWeight,
            bg='#140b1e',
        )
        self.pack_propagate(0)

        label1 = tk.Label(self, text='infant-100', bg=color1, fg=color3, font='arial 35 bold')
        label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Age', bg=color1, font='arial 15 bold')
        label2.pack(expand=1, fill='both', )
