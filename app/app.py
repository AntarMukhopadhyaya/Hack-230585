from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, ttk, PhotoImage
import json
import pathlib
import subprocess
from PIL import Image
import pystray
import os


root = Tk()
root.geometry("300x150")
root.eval('tk::PlaceWindow . center')


max_temp = StringVar()
min_temp = StringVar()
location = StringVar()
frequency = StringVar()


def run_subprocess():
    # Replace with the command you want to run
    filename = r""+str(pathlib.Path.cwd())+"/agents/agent.py"
    subprocess.Popen("python "+filename, close_fds=True)


def on_exit(icon, item):
    icon.stop()
    exit()


def submit():
    max_temp_value = max_temp.get()
    min_temp_value = min_temp.get()
    location_value = location.get()
    frequency_value = frequency.get()
    data = {
        "max_temp": max_temp_value,
        "min_temp": min_temp_value,
        "location": location_value,
        "frequency": frequency_value
    }
    with open('user-data.json', "w") as user_data_file:
        json.dump(data, user_data_file)
        messagebox.showinfo("Success", "User data stored successfully")

        run_subprocess()
        root.destroy()


Label(root, text="Maximum Temperature °(C)").grid(row=0)
Label(root, text="Minimum Temperature °(C) ").grid(row=1)
Label(root, text="Location").grid(row=2)
Label(root, text="Frequency").grid(row=3)
E1 = Entry(root, textvariable=max_temp)
E2 = Entry(root, textvariable=min_temp)
E3 = Entry(root, textvariable=location)
C1 = ttk.Combobox(root, width=15, textvariable=frequency)
C1['values'] = (
    'fast',
    'intermediate',
    'slow'
)
E1.grid(row=0, column=1, pady=5)
E2.grid(row=1, column=1, pady=5)
E3.grid(row=2, column=1, pady=5)
C1.grid(row=3, column=1, pady=5)
C1.current(1)
SaveButton = Button(root, text="Save", command=submit)
SaveButton.grid(row=4, column=1)

root.mainloop()
