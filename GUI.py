import tkinter as tk

class GUI:
    def __init__(self):
        window = tk.Tk()


        button = tk.Button(window, text="hello")
        button.pack();

        window.mainloop()