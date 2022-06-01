import tkinter as tk
from tkinter import ttk
from ui.Page2 import Page2
from ui.Page3 import Page3
from ui.Page4 import Page4
from ui.Dashboard import Dashboard
from ui.Page2 import bind_event_data


def run():
    global root

    root = tk.Tk()

    root.tk.call('source', 'theme/forest-dark.tcl')
    ttk.Style().theme_use('forest-dark')
    root.geometry('1080x720')
    root.title('Deaths-NZ')
    style = ttk.Style(root)
    style.configure('New.TFrame', background="#423458")

    tabs = ttk.Notebook(root)

    dashboard = Dashboard(tabs)
    page2 = Page2(tabs)
    page3 = Page3(tabs)
    bind_event_data(page3, '<<RefreshEvent>>', resize_window)
    page4 = Page4(tabs)
    bind_event_data(page4, '<<RefreshEvent>>', resize_window)
    tabs.add(dashboard, text='Dashboard')
    tabs.add(page2, text='page2')
    tabs.add(page3, text='page3')
    tabs.add(page4, text='page4')

    tabs.pack(expand=1, fill="both")

    root.mainloop()


# hacky way to force refresh a window to reload the graphs
def resize_window(event):
    if root.winfo_height() == 720:
        root.geometry('1080x721')
    else:
        root.geometry('1080x720')
