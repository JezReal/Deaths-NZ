import tkinter as tk
from tkinter import ttk
from data.data import get_total_deaths_yearly
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

spacing = 20
FrameHeight = 100
FrameWeight = 250
color1 = '#140b1e'
color2 = '#423458'
color3 = '#64d3b5'


def get_total_deaths():
    deaths = get_total_deaths_yearly()
    deaths_sum = 0

    for death in deaths:
        deaths_sum += int(death['Count'])

    return deaths_sum


def get_graph_data():
    deaths = get_total_deaths_yearly()
    deaths_sum = 0
    years = []
    deaths_count = []

    for data in deaths:
        current_year = data['Period']
        current_death_count = data['Count']

        try:
            if current_year != years[-1]:
                years.append(current_year)
                deaths_count.append(deaths_sum)
                deaths_sum = int(current_death_count)
            elif current_year == '2021':
                deaths_sum += int(current_death_count)
            else:
                deaths_sum += int(current_death_count)
        except IndexError:
            years.append(current_year)
            deaths_sum = int(current_death_count)

    deaths_count.append(deaths_sum)

    return {'years': years, 'deaths_count': deaths_count}


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
        frame1.grid(column=0, row=1, rowspan=4, padx=(0, spacing), sticky='nsew')

        frame2 = Frame2(self)
        frame2.grid(column=1, row=1, pady=(0, spacing), sticky='nsew')

        frame3 = Frame3(self)
        frame3.grid(column=1, row=2, pady=(0, spacing), sticky='nsew')

        frame4 = Frame4(self)
        frame4.grid(column=1, row=3, pady=(0, spacing), sticky='nsew')

        frame5 = Frame5(self)
        frame5.grid(column=1, row=4, sticky='nsew')

        self.columnconfigure(tuple(range(2)), weight=1)
        self.rowconfigure(tuple(range(5)), weight=1)


class Frame1(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=465,
            width=760,
            bg=color1,
        )
        self.data = get_graph_data()
        self.years = self.data['years']
        self.deaths_count = self.data['deaths_count']
        self.pack_propagate(0)
        # label1 = tk.Label(self, text='GRAPH', bg=color1, fg=color3, font='arial 50 bold')
        # label1.pack(expand=1, fill='both')

        figure = plot.Figure()
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=1, fill='both')

        sub_plot = figure.add_subplot()
        sub_plot.plot(self.years, self.deaths_count)
        sub_plot.set_xlabel('Year')
        sub_plot.set_ylabel('Deaths')


class Frame2(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWeight,
            bg=color1,
        )
        self.deaths_sum = get_total_deaths()
        self.pack_propagate(0)

        label1 = tk.Label(self, text=self.deaths_sum, bg=color1, fg=color3, font='arial 35 bold')
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
