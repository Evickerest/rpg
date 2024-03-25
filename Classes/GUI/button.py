import customtkinter

class Button:
   def __init__(self, container, msg: str, command: callable, x: int, y: int, anchor: str = "sw", font: tuple[str, int] = ("Time New Romans", 20), width=140, height=28, padding=10,color="white",hcolor="#CCCCCC",tags=""):
        button = customtkinter.CTkButton(
            container, font=font, text=msg, command=command, corner_radius=0, text_color="black", hover_color=hcolor,
            border_spacing=padding, fg_color=color, width=width, height=height,bg_color=color)
        container.bg_canvas.create_window(x, y, anchor=anchor, window=button,tags=tags)