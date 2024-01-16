from ForcedDoublePendulumWindow import *

class Menu(Windows):

    def __init__(self,parent,w,h):
        super().__init__(parent,w,h)
            ### demi-page de couverture du PMI 

        titleLabel = Label(self.leftFrame, text = "PMI", bg =FRAME_COLOR, font=("Helvetica",80))
        titleLabel.place(relx=0.5, rely=0, y=100, anchor="n")       
        subtitleLabel = Label(self.leftFrame, text = "Pendulum simulation", bg =FRAME_COLOR, font=("Helvetica", 40))
        subtitleLabel.place(relx=0.5, rely=0, y=300, anchor="n") 
        nameLabel = Label(self.leftFrame, text = "Kilian MOUGINOT\nVincent LEROI\nNicolas OBRIER\nAntoine MICHEL", bg = FRAME_COLOR,justify='left', font="Helvetica")
        nameLabel.place(relx=0.5, rely=0, y=400, anchor="n") 

            ### demi-page explication et redirection vers le bon pendule
        textFrame = Frame(self.rightFrame, bg=FRAME_COLOR) 
        textFrame.place(relx=0.5, rely=0.2, anchor="center")

        explanationText="Bienvenue sur l'interface graphique dédiée au PMI Z6.\nCliquez sur l'une des quatres simulations pour découvrir\nle comportement du pendule"
        explanationLabel = Label(textFrame, text = explanationText, bg = FRAME_COLOR, font=("Helvetica",15))
        explanationLabel.grid(row=0, column=0, sticky='nsew')

        buttonFrame = Frame(self.rightFrame, bg=FRAME_COLOR)
        buttonFrame.place(relx=0.5, rely=0.5, anchor="center")

        button_texts = [
            "Simple pendulum",
            "Forced simple\npendulum",
            "Double pendulum",
            "Forced double\npendulum"
        ]

        self.button = []
        for i, text in enumerate(button_texts):
            row = i // 2
            col = i % 2

            button = Button(buttonFrame, text=text, bg=CANVAS_COLOR, font=('Helvetica', 15))
            button.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
            self.button.append(button)