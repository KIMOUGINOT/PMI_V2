from PendulumWindow import *

class ForcedSimplePendulumWindow(PendulumWindow) :
    def __init__(self, parent, w, h, text) :
        super().__init__(parent, w, h, text)

        wEntry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        wLabel = Label(self.entriesFrame, text="Frequence", bg =CANVAS_COLOR, font="Helvetica")
        AEntry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        ALabel = Label(self.entriesFrame, text="Amplitude", bg =CANVAS_COLOR, font="Helvetica")
        wLabel.grid(row = 6, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        wEntry.grid(row = 7, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        ALabel.grid(row = 6, column = 1, sticky = 'nsew',padx = 3, pady = 3)
        AEntry.grid(row = 7, column = 1, sticky = 'nsew',padx = 3, pady = 3)
        self.entriesFrame.rowconfigure(index=6, pad=1, weight=1)
        self.entriesFrame.rowconfigure(index=7, pad=1, weight=1)

        wEntry.insert(0,"10")
        AEntry.insert(0,"5")

    def ODE(self, state, t, l, A, w):
        phi, phi_dot = state[0], state[1]
        phi_dot_dot = -(G / l) * np.sin(phi) + w**2/l*A*np.sin(w*t)*np.sin(phi)

        return [phi_dot, phi_dot_dot]
    
    def solveODE(self):
        """ Retrieve the parameters given in entries and solve the equations"""

        variable_list = []
        for widget in (self.entriesFrame.winfo_children()):
            if type(widget) == type(Entry()):
                variable_list.append(float(widget.get()))
                
        initial_state = [variable_list[0]*np.pi/180, variable_list[3]]
        l_value = variable_list[1]
        t0 = int(variable_list[2])
        n = int(variable_list[4])
        ti = int(variable_list[5])
        w = variable_list[6]
        A = variable_list[7]
        t_span = np.linspace(t0,ti,n)

        solution = odeint(self.ODE, initial_state, t_span, args=(l_value, A, w))

        
        return [solution[:, 0], solution[:,1], t_span]
