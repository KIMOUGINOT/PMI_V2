from Windows import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
from matplotlib.figure import Figure

# nuuuuuuuuuuuuuuuuuuuul faut faire des methodes mon reuf #
def clearAll(subFrame) :
    """clear all the entries given in parameters"""
    for widget in (subFrame.winfo_children()):
        if type(widget) == type(Entry()):
            widget.delete(0,END)

def loadGraph(subFrame) :
    """ Retrieve the parameters given in entries and call solving functions to show the graph"""
    variable_list = []
    for widget in (subFrame.winfo_children()):
        if type(widget) == type(Entry()):
            variable_list.append(float(widget.get()))
            
    theta0 = variable_list[0]*3.141592/180
    L = variable_list[1]
    t0 = variable_list[2]
    theta_dot0 = variable_list[3]
    n = variable_list[4]
    ti = variable_list[5]
    T,Theta,Theta_dot = solve_pendulum(theta0, theta_dot0, t0, ti, L, int(n))

    width = subFrame.master.master.leftFrame.winfo_width() / 100  # Converti en pouces pour la taille de la figure
    height = subFrame.master.master.leftFrame.winfo_height() / 100  # Converti en pouces pour la taille de la figure


    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(width-1, height-1))

    ax1.plot(T, Theta)
    ax1.set_title('Évolution de l\'angle du pendule en fonction du temps')
    ax1.set_xlabel('Temps')
    ax1.set_ylabel('Angle')

    ax2.plot(T, Theta_dot)
    ax2.set_title('Évolution de la vitesse angulaire du pendule en fonction du temps')
    ax2.set_xlabel('Temps')
    ax2.set_ylabel('Vitesse angulaire')

    canvas = FigureCanvasTkAgg(fig, master=subFrame.master.master.leftFrame)
    canvas.draw()
    canvas.get_tk_widget().place(relx = 0.06, rely=0.05, anchor='nw')



def solve_pendulum(theta0, theta_dot0, t0, ti, L, n):
    dt = (ti - t0) / n

    # Initialisation des listes pour stocker les valeurs calculées
    T_values = [t0]
    theta_values = [theta0]
    theta_dot_values = [theta_dot0]

    for i in range(n):
        # Équations du pendule simple
        theta = theta_values[-1]
        theta_dot = theta_dot_values[-1]
        theta_dot_dot = -(9.81 / L) * np.sin(theta)  # Formule pour l'accélération angulaire

        # Mise à jour des valeurs
        theta += (theta_dot * dt) 
        theta_dot += theta_dot_dot * dt

        # Ajout des valeurs à nos listes
        T_values.append(t0 + (i + 1) * dt)
        theta_values.append(theta)
        theta_dot_values.append(theta_dot)

    return T_values, theta_values, theta_dot_values

def back(window):
    parent_widget = window.winfo_parent()  # Obtenez l'objet parent
    if isinstance(parent_widget, str):
        parent_widget = window.nametowidget(parent_widget)  # Convertissez le nom en widget

    # Cachez tous les widgets enfants du parent
    for widget in parent_widget.winfo_children():
        widget.grid_remove()

    # Affichez le menu
    if hasattr(parent_widget, 'menu'):
        parent_widget.menu.grid(sticky='nsew')