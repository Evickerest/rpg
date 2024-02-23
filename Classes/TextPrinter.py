class TextPrinter:
    def __init__(self, tkinter):
        self.tkinter = tkinter
        self.ready = True

    # Method of printing defines where text will be printed in regards to other text
    # In most cases, it will be tk.END.
    def animate_text(self, text, text_id, method_of_printing):
        if self.ready is False:
            return
        
        self.ready = False

        delta = 25
        delay = 0

        # Offset textbox as text height is constantly changing
        self.offsetTextBox(text_id,-80)

        for char in text:
            update_text = lambda s=char: self.tkinter.bg_canvas.insert(text_id, method_of_printing, s)
            self.tkinter.bg_canvas.after(delay, update_text)
            delay += delta
        else:
            delay += delta
            self.tkinter.bg_canvas.after(delay, self.toggleReady)

    def toggleReady(self):
        self.ready = not self.ready

    def isTextReady(self):
        return self.ready
    
    def offsetTextBox(self, id, amount):
        self.tkinter.bg_canvas.move(id, 0, amount)




