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
        m1Entry.insert(0,"9")
        
        
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
        print(variable_list)
        initial_state = [variable_list[0]*np.pi/180, variable_list[6]*np.pi/180, variable_list[3], variable_list[8]]
        l_value = variable_list[1]
        t0 = int(variable_list[2])
        l2 = int(variable_list[7])
        m1 = int(variable_list[10])
        n = int(variable_list[4])
        ti = int(variable_list[5])
        m2 = int(variable_list[9])
        t_span = np.linspace(t0,ti,n)

        solution = odeint(self.ODE, initial_state, t_span, args=(l_value, l2, m1, m2 ))

        return [solution[:, 0], solution[:,1], solution[:,2], solution[:,3], t_span]
    
    def showGraph(self) :
        theta_values, phi_values, theta_dot_values, phi_dot_values, t_span = self.solveODE()
        width = self.leftFrame.winfo_width() / 100  # Converti en pouces pour la taille de la figure
        height = self.leftFrame.winfo_height() / 100  # Converti en pouces pour la taille de la figure
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(width-1, height-1))

        ax1.plot(t_span, theta_values)
        ax1.set_title('Évolution de l\'angle du pendule en fonction du temps')
        ax1.set_xlabel('Temps')
        ax1.set_ylabel('Angle')

        ax2.plot(theta_values, theta_dot_values)
        ax2.set_title('Portrait de phase')
        ax2.set_xlabel('Temps')
        ax2.set_ylabel('Vitesse angulaire')

        ax3.plot(t_span, phi_values)
        ax3.set_title('Évolution de l\'angle du pendule en fonction du temps')
        ax3.set_xlabel('Temps')
        ax3.set_ylabel('Angle')

        ax4.plot(phi_values, phi_dot_values)
        ax4.set_title('Portrait de phase')
        ax4.set_xlabel('Temps')
        ax4.set_ylabel('Vitesse angulaire')

        plt.tight_layout()

        self.canvas = FigureCanvasTkAgg(fig, master=self.leftFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx = 0.06, rely=0.05, anchor='nw')
