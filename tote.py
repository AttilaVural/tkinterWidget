# Status: works fine. Now find out how to pass either -1 or 1 into the function from the button call, so you 
#         dont have to make two functions (one or increment verse/ayah and one for decrement).
#         Next make a button to do the same thing with the verse number.



import requests
#import pandas as pd
from pprint import pprint
import tkinter as tk

class ayah():
    def write_slogan(self,direction):
        if not hasattr(write_slogan, "counter"):
            write_slogan.counter = 0  # it doesn't exist yet, so initialize it
            print("initalized")
        write_slogan.counter += 1
        print(write_slogan.counter)
        url = "http://api.alquran.cloud/v1/ayah/0"+str(write_slogan.verse)+str(write_slogan.counter)
        
        response = requests.request("GET", url).json()
        info_message = response["data"]["text"]
        # Insert the text into the window
        tk.Label(master, text=info_message).grid(row=2, column=1)

# Instantiate the tinker object
master = tk.Tk()


write_slogan.verse = 2
btn = tk.Button(master, text='next', command=write_slogan)
btn.grid(row=3, column=1, sticky=tk.W, pady=4)

# Show the window
master.mainloop()