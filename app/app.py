
# Importing the neccessary modules
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, ttk, PhotoImage
import json
import pathlib
import subprocess

# Intializing the root
root = Tk()
root.geometry("300x250")  # Setting window dimension
root.eval('tk::PlaceWindow . center')  # center the window to the screen
root.title("Temperature Alert Agent")  # window title
img = PhotoImage(file=r""+str(pathlib.Path.cwd())+"/app/logo.png")  # App logo
root.iconphoto(False, img)
# Initializing Text Variables
max_temp = StringVar()
min_temp = StringVar()
location = StringVar()
frequency = StringVar()


def run_subprocess():
    # getting the file path for agents.py
    filename = r""+str(pathlib.Path.cwd())+"/agents/agent.py"
    # running agents.py as a subprocess
    subprocess.Popen("python "+filename, close_fds=True)



# On submiting the save button
def submit():

    # Obtain the values from the entry
    max_temp_value = max_temp.get()
    min_temp_value = min_temp.get()
    location_value = location.get()
    frequency_value = frequency.get()
    # Initializing the data that will be stored in json file
    data = {
        "max_temp": max_temp_value,
        "min_temp": min_temp_value,
        "location": location_value,
        "frequency": frequency_value
    }
    # opening the user data file to store the contents of data variable
    with open('user-data.json', "w") as user_data_file:
        json.dump(data, user_data_file)
        # Showing success message to the user as data has been stored
        messagebox.showinfo("Success", "User data stored successfully")
        #
    # Running agents.py as a subprocess
    run_subprocess()
    # Exiting the current tkinter window
    root.destroy()


# Labels initializations
Label(root, text="Maximum Temperature °(C)").grid(row=0)
Label(root, text="Minimum Temperature °(C) ").grid(row=1)
Label(root, text="Location").grid(row=2)
Label(root, text="Frequency").grid(row=3)

# Entry Initilializations
E1 = Entry(root, textvariable=max_temp)
E2 = Entry(root, textvariable=min_temp)
E3 = Entry(root, textvariable=location)
# Combobox initiliaztion for Text choice
C1 = ttk.Combobox(root, width=15, textvariable=frequency)
C1['values'] = (
    'fast',
    'intermediate',
    'slow'
)
# Positioning the Entry and Combobox
E1.grid(row=0, column=1, pady=5)
E2.grid(row=1, column=1, pady=5)
E3.grid(row=2, column=1, pady=5)
C1.grid(row=3, column=1, pady=5)
C1.current(1)
# Save button Initialization and Positioning
SaveButton = Button(root, text="Save", command=submit)
SaveButton.grid(row=4, column=1)
# Setting window resize to false
root.resizable(False, False)
# Intializing the tkinter app
root.mainloop()
