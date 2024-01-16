from Windows import *
from PendulumWindow_utilities import *

class PendulumWindow(Windows) :

    def __init__(self, parent, w, h, text):
        super().__init__(parent, w, h)
        self.grid_columnconfigure(0, weight=7)
        self.grid_columnconfigure(1, weight=3)

        ###############################
        ### Back to the menu button ###

        backButton = Button(self.leftFrame, text='back',command=lambda: back(self),bg =CANVAS_COLOR, font="Helvetica")
        backButton.place(relx = 0.005, rely=0.005, anchor='nw')

        #########################
        ### Presentation text ###

        self.presentationLabel = Label(self.rightFrame,text=text, bg=FRAME_COLOR, font="Helvetica")
        self.presentationLabel.place(relx = 0.5, rely=0.1, anchor='c')

        ####################################
        ### Frame of parameters to enter ###

        self.entriesFrame = Frame(self.rightFrame, bg=CANVAS_COLOR)
        self.entriesFrame.place(relx = 0.5, rely=0.45, anchor='center')

        theta0Entry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        theta0Label = Label(self.entriesFrame, text=chr(952)+"(t0)  (deg)", bg =CANVAS_COLOR, font="Helvetica")
        lEntry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        lLabel = Label(self.entriesFrame, text="L", bg =CANVAS_COLOR, font="Helvetica")
        aEntry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        aLabel = Label(self.entriesFrame, text="t0", bg =CANVAS_COLOR, font="Helvetica")

        thetaPoint0Entry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        thetaPoint0Label = Label(self.entriesFrame, text="d" + chr(952) +"/dt" +"(t0)  (rad/s)", bg =CANVAS_COLOR, font="Helvetica")
        nEntry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        nLabel = Label(self.entriesFrame, text="n", bg =CANVAS_COLOR, font="Helvetica")
        bEntry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        bLabel = Label(self.entriesFrame, text="ti", bg =CANVAS_COLOR, font="Helvetica")

        theta0Label.grid(row = 0, column = 0, sticky = 'nsew',padx = 3, pady = 3) 
        theta0Entry.grid(row = 1, column = 0 , sticky = 'nsew',padx = 3, pady = 3)
        lLabel.grid(row = 2, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        lEntry.grid(row = 3, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        aLabel.grid(row = 4, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        aEntry.grid(row = 5, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        thetaPoint0Label.grid(row = 0, column = 1, sticky = 'nsew',padx = 3, pady = 3) 
        thetaPoint0Entry.grid(row = 1, column = 1, sticky = 'nsew',padx =3, pady = 3) 
        nLabel.grid(row = 2, column = 1, sticky = 'nsew',padx = 3, pady = 3)
        nEntry.grid(row = 3, column = 1, sticky = 'nsew',padx = 3, pady = 3)
        bLabel.grid(row = 4, column = 1, sticky = 'nsew',padx = 3, pady = 3)
        bEntry.grid(row = 5, column = 1, sticky = 'nsew',padx = 3, pady = 3)

        #Pre-remplissage des entries
        theta0Entry.insert(0,"30")
        thetaPoint0Entry.insert(0,"0")
        lEntry.insert(0,"2")
        nEntry.insert(0,"100")
        aEntry.insert(0,"0")
        bEntry.insert(0,"5")

        for i in range(4):
            self.entriesFrame.rowconfigure(index = i, pad = 1, weight=1)
        self.entriesFrame.columnconfigure(index=0, pad=1, weight=1)
        self.entriesFrame.columnconfigure(index=1, pad=1, weight=1)

        ########################
        ### Frame of buttons ###
        self.buttonFrame = Frame(self.rightFrame, bg=FRAME_COLOR)
        self.buttonFrame.place(relx = 0.5, rely=0.8, anchor='center')
        clearButton = Button(self.buttonFrame, text = "clear", command =lambda: clearAll(self.entriesFrame), bg =CANVAS_COLOR, font="Helvetica")
        self.loadButton = Button(self.buttonFrame, text = "load", command =lambda: loadGraph(self.entriesFrame) , bg =CANVAS_COLOR, font="Helvetica")
        clearButton.grid(row=0, column=0, sticky = 'nsew',padx = 3, pady = 3)
        self.loadButton.grid(row=0, column=1, sticky = 'nsew',padx = 3, pady = 3)
        self.buttonFrame.rowconfigure(index = 0, pad = 1, weight=1)
        self.buttonFrame.columnconfigure(index = 0, pad = 1, weight=1)
        self.buttonFrame.columnconfigure(index = 1, pad = 1, weight=1)

        #########################################################################


