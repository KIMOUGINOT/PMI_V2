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
        
        wEntry.insert(0,"10")
        AEntry.insert(0,"5")

    def ODE(self, state, t, l1, l2, m1, m2, A, w):
        phi1, phi2, phi1_dot, phi2_dot = state

        phi1_dot_dot = (3*m2*l2*phi2_dot**2*np.sin(phi2-phi1) + phi1_dot*phi2_dot*2*m1*l2 - phi1_dot**2*np.sin(phi2-phi1)*(m2*l2 - 2*m2*l1*np.cos(phi2-phi1)) - m2*A*w*phi1_dot*np.cos(w*t)*np.cos(phi1) - (m1+m2)*G*np.sin(phi1) + m2*G*np.cos(phi2-phi1)*np.sin(phi2))/((m1+3*m2)*l1 + 3*m2*l2*np.cos(phi2-phi1) - 2*m2*l2*l1*(np.cos(phi2-phi1))**2)
        phi2_dot_dot = (-2*l1*phi1_dot**2*np.sin(phi2-phi1) - G*np.sin(phi2) - 2*l1*np.cos(phi2-phi1)*phi1_dot_dot)/l2

        return [phi1_dot, phi2_dot, phi1_dot_dot, phi2_dot_dot]