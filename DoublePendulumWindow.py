from ForcedPendulumWindow import *

class DoublePendulumWindow(PendulumWindow) :
    
    def __init__(self, parent, w, h, text) :
        super().__init__(parent, w, h, text)

        phi0Entry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        phi0Label = Label(self.entriesFrame, text=chr(966)+"(t0)  (deg)", bg =CANVAS_COLOR, font="Helvetica")
        l2Entry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        l2Label = Label(self.entriesFrame, text="L2", bg =CANVAS_COLOR, font="Helvetica")
       
        phiPoint0Entry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        phiPoint0Label = Label(self.entriesFrame, text="d" + chr(966) +"/dt" +"(t0)  (rad/s)", bg =CANVAS_COLOR, font="Helvetica")
        m2Entry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        m2Label = Label(self.entriesFrame, text="m2", bg =CANVAS_COLOR, font="Helvetica")
        m1Entry = Entry(self.entriesFrame, bg =FRAME_COLOR)
        m1Label = Label(self.entriesFrame, text="m1", bg =CANVAS_COLOR, font="Helvetica")

        phi0Entry.insert(0,"30")
        phiPoint0Entry.insert(0,"0")
        l2Entry.insert(0,"1")
        m2Entry.insert(0,"10")
        m1Entry.insert(0,"10")
        
        
        phi0Label.grid(row = 6, column = 0, sticky = 'nsew',padx = 3, pady = 3) 
        phi0Entry.grid(row = 7, column = 0 , sticky = 'nsew',padx = 3, pady = 3)
        l2Label.grid(row = 8, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        l2Entry.grid(row = 9, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        m1Label.grid(row = 10, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        m1Entry.grid(row = 11, column = 0, sticky = 'nsew',padx = 3, pady = 3)
        phiPoint0Label.grid(row = 6, column = 1, sticky = 'nsew',padx = 3, pady = 3) 
        phiPoint0Entry.grid(row = 7, column = 1, sticky = 'nsew',padx =3, pady = 3) 
        m2Label.grid(row = 8, column = 1, sticky = 'nsew',padx = 3, pady = 3)
        m2Entry.grid(row = 9, column = 1, sticky = 'nsew',padx = 3, pady = 3)

        for i in range(6,12):
            self.entriesFrame.rowconfigure(index = i, pad = 1, weight=1)

    def ODE(self, state, t, l1, l2, m1, m2):
        phi1, phi2, phi1_dot, phi2_dot = state

        phi1_dot_dot = (m2*G*np.sin(phi2)*np.cos(phi2-phi1) - m2*np.sin(phi2-phi1)*(l1*phi1_dot**2*np.cos(phi2-phi1) + l2*phi2_dot**2) - (m1+m2)*G*np.sin(phi1))/(l1*(m1 + m2*(np.sin(phi2-phi1))**2))
        phi2_dot_dot = ((m1+m2)*(l1*phi1_dot**2*np.sin(phi2-phi1) - G*np.sin(phi2) + G*np.sin(phi1)*np.cos(phi2-phi1)) + m2*l2*phi2_dot**2*np.sin(phi2-phi1)*np.cos(phi2-phi1))/(l2*(m1 + m2*(np.sin(phi2-phi1)**2)))

        return [phi1_dot, phi2_dot, phi1_dot_dot, phi2_dot_dot]
    
    def solveODE(self) :
        """ Retrieve the parameters given in entries and solve the equations"""

        variable_list = []
        for widget in (self.entriesFrame.winfo_children()):
            if type(widget) == type(Entry()):
                variable_list.append(float(widget.get()))
                
        initial_state = [variable_list[0]*np.pi/180, variable_list[3]*np.pi/180, variable_list[6], variable_list[9]]
        l_value = variable_list[1]
        t0 = int(variable_list[2])
        l2 = int(variable_list[4])
        m1 = int(variable_list[5])
        n = int(variable_list[7])
        ti = int(variable_list[8])
        m2 = int(variable_list[10])
        t_span = np.linspace(t0,ti,n)

        solution = odeint(self.ODE, initial_state, t_span, args=(l_value, l2, m1, m2 ))

        return [solution[:, 0], solution[:,1], solution[:,2], solution[:,3], t_span]
