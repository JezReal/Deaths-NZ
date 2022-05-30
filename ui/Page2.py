import tkinter as tk
from tkinter import ttk
from data.data import get_total_deaths_by_year

spacing = 20
FrameHeight = 100
FrameWidth = 330
color1 = '#140b1e'
color2 = '#423458'
color3 = '#64d3b5'


class Page2(ttk.Frame):
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
            text='Total Deaths by Year',
            bg=color2,
            pady=10,
        )
        titleLabel.grid(row=0, column=0, columnspan=2, pady=(0, spacing), )

        frame2 = Frame2(self)
        frame2.grid(column=0, row=1, padx=(0, spacing), pady=(0, spacing), sticky='nsew')
        bind_event_data(frame2, '<<CustomEvent>>', self.frame2_callback)

        frame3 = Frame3(self)
        frame3.grid(column=1, row=1, pady=(0, spacing), sticky='nsew')

        self.frame1 = Frame1(self)
        self.frame1.grid(column=0, row=2, columnspan=2, sticky='nsew')
        # self.frame1.update_label(101)

        self.columnconfigure(tuple(range(3)), weight=1)
        self.rowconfigure(tuple(range(3)), weight=1)

    # data returned from callback should be accessed here
    def frame2_callback(self, event):
        print(event.data['year'])
        self.frame1.update_label(event.data['year'])


class Frame1(tk.Frame):
    # listen for the event and then change the label
    deaths_count = 28446

    def __init__(self, container):
        super().__init__(
            container,
            height=450,
            width=FrameWidth * 3 + (spacing * 2),
            bg=color1,
        )
        self.pack_propagate(0)

        self.label1 = tk.Label(self, text=Frame1.deaths_count, bg=color1, fg=color3, font='arial 100 bold')
        self.label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Total Deaths', bg=color1, fg='pink', font='arial 50 bold')
        label2.pack(expand=1, fill='both', )

    def update_label(self, year):
        deaths = Frame1.get_total_deaths(year)
        self.label1['text'] = deaths

    @staticmethod
    def get_total_deaths(year):
        deaths_sum = 0
        deaths = get_total_deaths_by_year(year)

        for death in deaths:
            deaths_sum += int(death['Count'])

        return deaths_sum


class Frame2(tk.Frame):
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
            '2010', '2011',
            '2012', '2013',
            '2014', '2015',
            '2016', '2017',
            '2018', '2019',
            '2020', '2021'
        )
        self.selected_year = '2010'
        self.option_var = tk.StringVar(self)
        self.create_wigets()
        # self.option_var.trace_add(('write', 'unset'), self.select_callback)

        # Generate a custom event that we can then listen to whenever a choice is selected
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
        # Listen for the event that we created which should return the choice that was selected
        self.option_menu.bind('<<OptionMenuChanged>>', self.select_callback)

        label = tk.Label(self, text='Year', bg=color1, font='arial 20 bold')
        label.pack()

    # Displays the selected choice
    def select_callback(self, event):
        self.selected_year = self.option_var.get()

    def create_virtual_event(self, varname, idx, mode):
        self.option_menu.event_generate('<<OptionMenuChanged>>')
        self.generate_custom_event()

    def generate_custom_event(self):
        self.event_generate('<<CustomEvent>>', data={'year': self.selected_year})


class Frame3(tk.Frame):
    def __init__(self, container):
        super().__init__(
            container,
            height=FrameHeight,
            width=FrameWidth,
            bg='#140b1e',
        )
        self.pack_propagate(0)

        label1 = tk.Label(self, text='Male and Female', bg=color1, fg=color3, font='arial 30 bold')
        label1.pack(expand=1, fill='both', pady=0)
        label2 = tk.Label(self, text='Gender', bg=color1, font='arial 20 bold')
        label2.pack(expand=1, fill='both', )


# function that lets you access the data passed when generating events because Tkinter does not handle it:
# https://stackoverflow.com/questions/16369947/python-tkinterhow-can-i-fetch-the-value-of-data-which-was-set-in-function-eve?answertab=modifieddesc#tab-top
def bind_event_data(widget, sequence, func, add=None):
    def _substitute(*args):
        e = lambda: None  # simplest object with __dict__
        e.data = eval(args[0])
        e.widget = widget
        return (e,)

    funcid = widget._register(func, _substitute, needcleanup=1)
    cmd = '{0}if {{"[{1} %d]" == "break"}} break\n'.format('+' if add else '', funcid)
    widget.tk.call('bind', widget._w, sequence, cmd)
