import tkinter as tk
from tkinter import ttk
from data.data import get_total_male_deaths, get_total_female_deaths
from ui.Page2 import bind_event_data

spacing = 20
FrameHeight = 100
FrameWidth = 330
color1 = '#140b1e'
color2 = '#423458'
color3 = '#64d3b5'


class Page3(ttk.Frame):
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
            text='Total Male Deaths from 2010-2021',
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
        bind_event_data(frame4, '<<CustomEvent>>', self.custom_event_callback)

        frame1 = Frame1(self)
        frame1.grid(column=0, row=2, columnspan=3, sticky='nsew')

        self.columnconfigure(tuple(range(3)), weight=1)
        self.rowconfigure(tuple(range(3)), weight=1)

    def custom_event_callback(self, event):
        self.frame2.update_death_count(event.data['gender'])


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

        self.deaths_sum = get_total_deaths('Male')
        self.pack_propagate(0)

        self.label1 = tk.Label(self, text=self.deaths_sum, bg=color1, fg=color3, font='arial 35 bold')
        self.label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Total Deaths', bg=color1, font='arial 20 bold')
        label2.pack(expand=1, fill='both', )

    def update_death_count(self, gender):
        self.label1['text'] = get_total_deaths(gender)


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
        self.language = ('Male', 'Female')
        self.selected_gender = 'Male'

        self.option_var = tk.StringVar(self)
        self.create_wigets()

        self.option_var.trace_add(('write', 'unset'), self.create_virtual_event)

    def create_wigets(self):
        paddings = {'padx': 90, 'pady': 7}

        self.option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.language[0],
            *self.language
        )

        self.option_menu.pack(fill='x', expand=1, )
        self.option_menu.bind('<<OptionMenuChanged>>', self.select_callback)

        label = tk.Label(self, text='Gender', bg=color1, font='arial 20 bold')
        label.pack()

    def option_changed(self, *args):
        pass

    def select_callback(self, event):
        self.selected_gender = self.option_var.get()

    def create_virtual_event(self, varname, idx, mode):
        self.option_menu.event_generate('<<OptionMenuChanged>>')
        self.generate_custom_event()

    def generate_custom_event(self):
        self.event_generate('<<CustomEvent>>', data={'gender': self.selected_gender})


def get_total_deaths(gender):
    deaths_sum = 0

    if gender == 'Male':
        deaths = get_total_male_deaths()
    else:
        deaths = get_total_female_deaths()

    for death in deaths:
        deaths_sum += int(death['Count'])

    return deaths_sum


def event_listen(widget, sequence, func, add=None):
    def _substitute(*args):
        e = lambda: None  # simplest object with __dict__
        e.data = eval(args[0])
        e.widget = widget
        return (e,)

    funcid = widget._register(func, _substitute, needcleanup=1)
    cmd = '{0}if {{"[{1} %d]" == "break"}} break\n'.format('+' if add else '', funcid)
    widget.tk.call('bind', widget._w, sequence, cmd)
