import tkinter as tk
from tkinter import ttk
from data.data import get_total_deaths_by_age_group
from ui.Page2 import bind_event_data
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

        self.frame2 = Frame2(self)
        self.frame2.grid(column=0, row=1, padx=(0, spacing), pady=(0, spacing), sticky='nsew')

        frame3 = Frame3(self)
        frame3.grid(column=1, row=1, padx=(0, spacing), pady=(0, spacing), sticky='nsew')

        frame4 = Frame4(self)
        frame4.grid(column=2, row=1, pady=(0, spacing), sticky='nsew')
        bind_event_data(frame4, '<<AgeGroupSelectEvent>>', self.age_group_change_callback)

        self.frame1 = Frame1(self)
        self.frame1.grid(column=0, row=2, columnspan=3, sticky='nsew')
        bind_event_data(self.frame1, '<<RefreshEvent>>', self.resize_window)

        self.columnconfigure(tuple(range(3)), weight=1)
        self.rowconfigure(tuple(range(3)), weight=1)

    def age_group_change_callback(self, event):
        selected_age_group = event.data['age_group']
        self.frame2.update_death_count(selected_age_group)
        self.frame1.set_graph(selected_age_group)

    def resize_window(self, event):
        self.event_generate('<<RefreshEvent>>', data={'hello': 'world'})


class Frame1(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=450,
            width=FrameWidth * 3 + (spacing * 2),
            bg=color1,
        )
        self.pack_propagate(0)

        # label1 = tk.Label(self, text='GRAPH', bg=color1, fg=color3, font='arial 50 bold')
        # label1.pack(expand=1, fill='both')

        self.figure = plot.Figure()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.sub_plot = self.figure.add_subplot()

        self.set_graph('Infant')

    def set_graph(self, age_group):
        self.sub_plot.clear()

        data = get_graph_data(age_group)
        years = data['years']
        deaths = data['deaths_count']

        self.figure.set_canvas(self.canvas)
        self.canvas.draw()

        self.sub_plot.plot(years, deaths)
        self.sub_plot.set_xlabel('Year')
        self.sub_plot.set_ylabel('Deaths')

        self.refresh_frame()
        self.canvas.get_tk_widget().pack(expand=1, fill='both')

    def refresh_frame(self):
        # emit an event
        self.event_generate('<<RefreshEvent>>', data={})


class Frame2(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWidth,
            bg=color1,
        )
        self.deaths_sum = get_total_deaths('Infant')
        self.pack_propagate(0)

        self.label1 = tk.Label(self, text=self.deaths_sum, bg=color1, fg=color3, font='arial 35 bold')
        self.label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Total Deaths', bg=color1, font='arial 20 bold')
        label2.pack(expand=1, fill='both', )

    def update_death_count(self, age_group):
        print('Callback hit')
        self.label1['text'] = get_total_deaths(age_group)


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
        self.option_menu = None
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
        self.selected_age_group = 'Infant'

        self.option_var.trace_add(('write', 'unset'), self.create_virtual_event)

    def create_wigets(self):
        paddings = {'padx': 90, 'pady': 7}

        self.option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.language[0],
            *self.language)

        self.option_menu.pack(fill='x', expand=1)
        self.option_menu.bind('<<OptionMenuChanged>>', self.select_callback)

        label = tk.Label(self, text='Age', bg=color1, font='arial 20 bold')
        label.pack()

    def create_virtual_event(self, varname, idx, mode):
        self.option_menu.event_generate('<<OptionMenuChanged>>')
        self.generate_age_group_change_event()

    def select_callback(self, event):
        self.selected_age_group = self.option_var.get()
        self.generate_age_group_change_event()

    def generate_age_group_change_event(self):
        self.event_generate('<<AgeGroupSelectEvent>>', data={'age_group': self.selected_age_group})


def get_total_deaths(age_group):
    deaths_sum = 0

    deaths = get_total_deaths_by_age_group(age_group)

    for death in deaths:
        deaths_sum += int(death['Count'])

    return deaths_sum


def get_graph_data(age_group):
    deaths_sum = 0
    years = []
    deaths_count = []

    deaths = get_total_deaths_by_age_group(age_group)

    for death in deaths:
        current_year = death['Period']
        current_death_count = death['Count']

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
