from Windows import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
from matplotlib.figure import Figure

# nuuuuuuuuuuuuuuuuuuuul faut faire des methodes mon reuf #
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

