import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk, Image



class Gui(tk.Tk):
    #Default size of the window.
    def __init__(self,title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size [1]}')  #Window size is provided by user.
        self.minsize (800, 500) #Minimum size of the window, can be maximized.
        self.iconbitmap('SpaceShip.ico')
        

        # #Widgets
        # self.menu = Menu(self)


        #Customize screen
        original_image = Image.open('bg2.jpeg').resize((900,700))
        bg = ImageTk.PhotoImage(original_image)


        background_canvas = tk.Canvas(self, width = 900, height = 700)
        background_canvas.pack(fill = 'both', expand = True) 
        background_canvas.create_image(0, 0, image = bg, anchor = 'nw')

        background_canvas.create_text(400,250, text = "Are You Ready for a New Adventure?", font = "Time_New_Roman 30", fill = 'white')


        user_name = tk.Label(self, text = 'User Name:', font = 'Time_New_Roman 15')
        user_name_window = background_canvas.create_window(30,100, anchor = 'sw', window = user_name)

        user_name_entry = tk.Entry(self, font = 'Time_New_Roman 20')
        user_name_entry_window = background_canvas.create_window(150,100, anchor = 'sw', window = user_name_entry) 

        start_button = tk.Button(self, text = "Start", font = "Time_New_Roman 20")
        start_button_window = background_canvas.create_window(30, 200, anchor = 'sw', window =  start_button)














        
#..

        self.mainloop()
    
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        pass




Gui("SpaceShip Game", (900, 700))

