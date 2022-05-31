import tkinter as tk
from tkinter import ttk
from data.data import get_total_female_deaths

spacing = 20
FrameHeight = 100
FrameWidth = 330
color1 = '#140b1e'
color2 = '#423458'
color3 = '#64d3b5'


class Page4(ttk.Frame):
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
            font='arial 20 bold',
            text='Total Male and Female Deaths from 2010-2021 by Age',
            bg=color2,
            pady=10,
        )
        titleLabel.grid(row=0, column=0, columnspan=3, pady=(0, spacing), )

        frame2 = Frame2(self)
        frame2.grid(column=0, row=1, padx=(0, spacing), pady=(0, spacing), sticky='nsew')

        frame3 = Frame3(self)
        frame3.grid(column=1, row=1, padx=(0, spacing), pady=(0, spacing), sticky='nsew')

        frame4 = Frame4(self)
        frame4.grid(column=2, row=1, pady=(0, spacing), sticky='nsew')

        frame1 = Frame1(self)
        frame1.grid(column=0, row=2, columnspan=3, sticky='nsew')

        self.columnconfigure(tuple(range(3)), weight=1)
        self.rowconfigure(tuple(range(3)), weight=1)


class Frame1(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=450,
            width=FrameWidth * 3 + (spacing * 2),
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
            width=FrameWidth,
            bg=color1,
        )
        self.female_deaths_sum = get_total_deaths()
        self.pack_propagate(0)

        label1 = tk.Label(self, text=self.female_deaths_sum, bg=color1, fg=color3, font='arial 35 bold')
        label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Total Deaths', bg=color1, font='arial 20 bold')
        label2.pack(expand=1, fill='both', )


class Frame3(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWidth,
            bg='#140b1e',
        )
        self.pack_propagate(0)

        label1 = tk.Label(self, text='2010-2021', bg=color1, fg=color3, font='arial 35 bold')
        label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Year', bg=color1, font='arial 20 bold')
        label2.pack(expand=1, fill='both', )


class Frame4(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWidth,
            bg='#140b1e',
            padx=20,
            pady=10
        )
        self.pack_propagate(0)
        self.language = (
            'Infant', '1-4',
            '5-9', '10-14',
            '15-19', '20-24',
            '25-29', '30-34',
            '35-39', '40-44',
            '45-49', '50-54',
            '55-59', '60-64',
            '65-69', '70-74',
            '75-79', '80-84',
            '85-89', '90-94',
            '95-99', '100 and over'
        )
        self.option_var = tk.StringVar(self)
        self.create_wigets()

    def create_wigets(self):
        paddings = {'padx': 90, 'pady': 7}

        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.language[0],
            *self.language,
            command=self.option_changed)

        option_menu.pack(fill='x', expand=1, )

        label = tk.Label(self, text='Age', bg=color1, font='arial 20 bold')
        label.pack()

    def option_changed(self, *args):
        pass


def get_total_deaths():
    deaths = get_total_female_deaths()
    deaths_sum = 0

    for death in deaths:
        deaths_sum += int(death['Count'])

    return deaths_sum
