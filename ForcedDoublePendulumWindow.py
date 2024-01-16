from DoublePendulumWindow import *

class ForcedDoublePendulumWindow(DoublePendulumWindow) :

    def __init__(self, parent, w, h, text) :
        super().__init__(parent, w, h, text)

        wEntry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        wLabel = Label(self.entriesFrame, text="Frequence", bg =CANVAS_COLOR, font="Helvetica")
        AEntry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        ALabel = Label(self.entriesFrame, text="Amplitude", bg =CANVAS_COLOR, font="Helvetica")
        wLabel.grid(row = 12, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        wEntry.grid(row = 13, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        ALabel.grid(row = 12, column = 1, sticky = 'nsew',padx = 3, pady = 3)
        AEntry.grid(row = 13, column = 1, sticky = 'nsew',padx = 3, pady = 3)
        self.entriesFrame.rowconfigure(index=12, pad=1, weight=1)
        self.entriesFrame.rowconfigure(index=13, pad=1, weight=1)