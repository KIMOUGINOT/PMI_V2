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
        l2 = variable_list[7]
        m1 = variable_list[10]
        n = int(variable_list[4])
        ti = int(variable_list[5])
        m2 = variable_list[9]
        A = variable_list[11]
        w = variable_list[12]
        t_span = np.linspace(t0,ti,n)

        solution = odeint(self.ODE, initial_state, t_span, args=(l_value, l2, m1, m2,A ,w ))

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