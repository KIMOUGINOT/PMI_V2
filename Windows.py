from tkinter import * 

CANVAS_COLOR = '#cbb9aa'
RED = "red"
FRAME_COLOR = '#d3d3d3'
BLUE = "blue"

class Windows(Canvas) :

    def __init__(self, parent, w, h) :
        super().__init__(parent, width=w, height=h)
        self.parent = parent
        self.configure(bg = CANVAS_COLOR)  

        ### Frames droite et gauche ###
        self.leftFrame = Frame(self, bg=FRAME_COLOR)
        self.rightFrame = Frame(self, bg=FRAME_COLOR)

        self.leftFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.rightFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.leftFrame.grid_propagate(False)
        self.rightFrame.grid_propagate(False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_propagate(False)