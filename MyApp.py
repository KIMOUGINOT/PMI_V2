from Menu import *
from MyApp_utilities import *

class MyApp(Tk) :
    
    def __init__(self, title) :
        super().__init__()
        self.title(title)
        self.state("zoomed")
        self.minsize(1000,600)

        app_width = self.winfo_screenwidth()  # Largeur de l'écran
        app_height = self.winfo_screenheight()  # Hauteur de l'écran

        ### Configuration des fenêtres ###

        self.simplePendulum = PendulumWindow(self, app_width, app_height, presentationText1)
        self.forcedSimplePendulum = ForcedSimplePendulumWindow(self, app_width, app_height,presentationText1)
        self.doublePendulum = DoublePendulumWindow(self, app_width, app_height,presentationText1)
        self.forcedDoublePendulum = ForcedDoublePendulumWindow(self, app_width, app_height,presentationText1) 

        ### Configuration du menu ###

        self.menu = Menu(self, app_width, app_height)

        #A terme modifier de sorte à ne pas faire de répétition de code -> changer les fonctions

        def loadSimplePendulum() :
            self.menu.grid_remove()
            self.simplePendulum.grid(sticky = 'nsew')

        def loadForcedSimplePendulum() :
            self.menu.grid_remove()
            self.forcedSimplePendulum.grid(sticky = 'nsew')

        def loadDoublePendulum() :
            self.menu.grid_remove()
            self.doublePendulum.grid(sticky = 'nsew')

        def loadForcedDoublePendulum() :
            self.menu.grid_remove()
            self.forcedDoublePendulum.grid(sticky = 'nsew')

        self.menu.button[0].config(command=loadSimplePendulum)
        self.menu.button[1].config(command=loadForcedSimplePendulum)
        self.menu.button[2].config(command=loadDoublePendulum)
        self.menu.button[3].config(command=loadForcedDoublePendulum)

        self.menu.grid()


  