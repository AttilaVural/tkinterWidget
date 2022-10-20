import requests
import tkinter as tk

class window():
    def __init__(self):
        self.root = tk.Tk()
        self.counter = 0
        
    def run(self):
        self.root.mainloop()
    
    def create_label(self):
        self.myLabel = tk.Label(self.root, text="")
        self.myLabel.grid(row=2, column=1)
    
    def create_button_next(self):
        btn_next = tk.Button(self.root, text='next', command = lambda : self.update_label_text(1))
        btn_next.grid(row=3, column=1, sticky=tk.W, pady=4)
        
    def create_button_prev(self):
        btn_prev = tk.Button(self.root, text='prev', command = lambda : self.update_label_text(-1))
        btn_prev.grid(row=3, column=6, sticky=tk.W, pady=4)
    
    def update_label_text(self,direction):
        self.counter += direction
        url = "http://api.alquran.cloud/v1/ayah/0"+str(2)+str(self.counter)
        # Retrieve text string
        response = requests.request("GET", url).json()
        info_message = response["data"]["text"]
        # Insert the text into the window
        self.myLabel.config(text=info_message)
        print(self.counter)
    
a = window()
a.create_label()
a.create_button_next()
a.create_button_prev()
a.run()


