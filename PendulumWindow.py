from Windows import *
from PendulumWindow_utilities import *

class PendulumWindow(Windows) :

    def __init__(self, parent, w, h, text):
        super().__init__(parent, w, h)
        self.grid_columnconfigure(0, weight=7)
        self.grid_columnconfigure(1, weight=3)

        ###############################
        ### Back to the menu button ###

        backButton = Button(self.leftFrame, text='back',command=lambda: self.back(),bg =CANVAS_COLOR, font="Helvetica")
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
        clearButton = Button(self.buttonFrame, text = "clear", command =lambda: self.clearAll(), bg =CANVAS_COLOR, font="Helvetica")
        self.loadButton = Button(self.buttonFrame, text = "load", command =lambda: self.loadGraph() , bg =CANVAS_COLOR, font="Helvetica")
        clearButton.grid(row=0, column=0, sticky = 'nsew',padx = 3, pady = 3)
        self.loadButton.grid(row=0, column=1, sticky = 'nsew',padx = 3, pady = 3)
        self.buttonFrame.rowconfigure(index = 0, pad = 1, weight=1)
        self.buttonFrame.columnconfigure(index = 0, pad = 1, weight=1)
        self.buttonFrame.columnconfigure(index = 1, pad = 1, weight=1)

        #########################################################################

    def clearAll(self) :
        """clear all the entries given in parameters"""
        for widget in (self.entriesFrame.winfo_children()):
            if type(widget) == type(Entry()):
                widget.delete(0,END)

    def loadGraph(self) :
        """ Retrieve the parameters given in entries and call solving functions to show the graph"""
        variable_list = []
        for widget in (self.entriesFrame.winfo_children()):
            if type(widget) == type(Entry()):
                variable_list.append(float(widget.get()))
                
        theta0 = variable_list[0]*3.141592/180
        L = variable_list[1]
        t0 = variable_list[2]
        theta_dot0 = variable_list[3]
        n = variable_list[4]
        ti = variable_list[5]
        T,Theta,Theta_dot = solve_pendulum(theta0, theta_dot0, t0, ti, L, int(n))

        width = self.leftFrame.winfo_width() / 100  # Converti en pouces pour la taille de la figure
        height = self.leftFrame.winfo_height() / 100  # Converti en pouces pour la taille de la figure


        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(width-1, height-1))

        ax1.plot(T, Theta)
        ax1.set_title('Évolution de l\'angle du pendule en fonction du temps')
        ax1.set_xlabel('Temps')
        ax1.set_ylabel('Angle')

        ax2.plot(T, Theta_dot)
        ax2.set_title('Évolution de la vitesse angulaire du pendule en fonction du temps')
        ax2.set_xlabel('Temps')
        ax2.set_ylabel('Vitesse angulaire')

        self.canvas = FigureCanvasTkAgg(fig, master=self.leftFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx = 0.06, rely=0.05, anchor='nw')
    
    def back(self):
        self.canvas.get_tk_widget().place_forget()
        parent_widget = self.winfo_parent()  # Obtenez l'objet parent
        if isinstance(parent_widget, str):
            parent_widget = self.nametowidget(parent_widget)  # Convertissez le nom en widget

        # Cachez tous les widgets enfants du parent
        for widget in parent_widget.winfo_children():
            widget.grid_remove()

        # Affichez le menu
        if hasattr(parent_widget, 'menu'):
            parent_widget.menu.grid(sticky='nsew')