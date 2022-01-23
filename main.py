from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
from test import calculator

class windowLogic:

    def __init__(self):
        self.title = "ADSDB PROJECT GUI"
        self.maxWidth = 1100
        self.maxHeight = 800
        self.resizable = False

        self.LabelSettings = {
            'bg':"lightgray",
            'padx':15,
            'pady':15
        }

        self.FooterSettings = {
            'padx':15, 
            'pady':15, 
            'bg':"lightblue", 
            'fg':"black",
            'font':("Arial", 12)
        }

        self.font = 'Arial 11'
        self.fontBold = 'Arial 11 bold'

        self.buttons = []

    #### FUNCTIONS ####
    def function(self, functionId, text):
        MessageBox.showinfo("Info", f"Running {text} script")

        if functionId == 0:
            calc = calculator().doCalc()

            self.results.set(calc[0] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1] + "\n" + calc[1])

            for i in range(0,5):
                self.buttons[i].config(state="disabled", bg='lightgreen')
                

        if functionId == 1:
            calc = calculator().doCalc()

            self.results.set(self.results.get() + "\n" + calc[0] + "\n" + calc[1] + "\n -------------------------")
            self.buttons[0].config(state="disabled", bg='lightcoral')
            self.buttons[1].config(state="disabled", bg='lightgreen')
            self.buttons[2].config(state="normal", bg='lightblue')

        if functionId == 2:
            calc = calculator().doCalc()

            self.results.set(self.results.get() + "\n" + calc[0] + "\n" + calc[1] + "\n -------------------------")
            self.buttons[2].config(state="disabled", bg='lightgreen')
            self.buttons[3].config(state="normal", bg='lightblue')

        if functionId == 3:
            calc = calculator().doCalc()

            self.results.set(self.results.get() + "\n" + calc[0] + "\n" + calc[1] + "\n -------------------------")
            self.buttons[3].config(state="disabled", bg='lightgreen')
            self.buttons[4].config(state="normal", bg='lightblue')

        if functionId == 4:
            calc = calculator().doCalc()

            self.results.set(self.results.get() + "\n" + calc[0] + "\n" + calc[1] + "\n -------------------------")
            self.buttons[4].config(state="disabled", bg='lightgreen')

        MessageBox.showinfo("Info", "Script has finished successfully")

    def reset(self):

        self.results.set("")

        for i in range(0,5):
            if i == 0 or i == 1:
                self.buttons[i].config(state="normal", bg='lightblue')
            elif i > 1:
                self.buttons[i].config(state="disabled", bg='lightcoral')


    def exitWindowsAlert(self):
        exitValue = MessageBox.askquestion("Exit", "Do you want to quit the application?")

        if exitValue == "yes":
            self.window.destroy()

    def teamWindow(self):

        window = Tk()

        window.title("Team members")
        window.geometry("400x250")
        window.configure(bg="lightgray")
        window.resizable(0, 0)

        text0 = Label(window, text="We are the team formed by the following members: ", font=self.font)
        text0.config(self.LabelSettings)
        text0.grid(row=0, column=0, padx=10, columnspan= 3)

        text1 = Label(window, text="-Marc Maynou", font= self.fontBold)
        text1.config(self.LabelSettings)
        text1.grid(row=1, column=0, padx=10, sticky=W, columnspan= 3)

        text2 = Label(window, text="-Carlos Moyano", font= self.fontBold)
        text2.config(self.LabelSettings)
        text2.grid(row=2, column=0, padx=10, sticky=W, columnspan= 3)

        text3 = Label(window, text="-Enrique Reyes", font= self.fontBold)
        text3.config(self.LabelSettings)
        text3.grid(row=3, column=0, padx=10, sticky=W, columnspan= 3)

        window.mainloop()

        #MessageBox.showinfo("Info", "We are the team formed by the following members: Marc Maynou, Carlos Moyano, Enrique Reyes")

    ### WINDOWS ####
    def load(self):
        # Create a new window
        self.window = Tk()

        main_menu = self.createMenu()
        # Window properties
        self.window.title(self.title)
        self.window.geometry(str(self.maxWidth) + "x" + str(self.maxHeight))  # "1100x800"
        self.window.configure(bg="lightgray", menu= main_menu)
        
        if self.resizable:
            self.window.resizable(1, 1)
        else:
            self.window.resizable(0, 0)

        self.results = StringVar()

        

    def createMenu(self):
        menu = Menu(self.window)

        menu.add_command(label="About us", command=self.teamWindow)
        menu.add_command(label="Exit", command=self.window.quit)

        return menu

        

    def addFrame(self, w, h, bg_color = 'lightgray', side_value = '', anchor_value = 'center'):
        frame = Frame(self.window, width=w, height= h)
        frame.config(
            padx= 5,
            pady=5,
            bg= bg_color
        )

        if side_value == '':
            frame.pack(anchor=anchor_value)
            
        else:
            frame.pack(side=side_value, anchor=anchor_value)

        return frame

    def addLabel(self, frame, labelText, nrow, ncol, sticky_value=W):
        text = Label(frame, text=labelText, font=self.font)
        text.config(self.LabelSettings)
        text.grid(row=nrow, column=ncol, padx=10, sticky=sticky_value)

    def addButton(self, frame, labelText, nrow, ncol):

        button = Button(self.bodyFrame, text=labelText, command=lambda: self.function(nrow, labelText))
        
        button.config(
                padx=5, 
                pady=5, 
                bg="lightblue", 
                fg="black")
        button.grid(row=nrow, column=1, padx=10, sticky=W)  

        self.buttons.append(button)

    # Header + Body + Footer
    def addHeader(self, headerText):

        frame = self.addFrame(self.maxWidth, 75, "black", TOP, N)
        text = Label(frame, text=headerText)
        text.config(
                fg="white",
                bg="black",
                padx=20,
                pady=20,
                font=("Arial", 20)
        )
        text.pack(anchor=N, fill=X)
        frame.pack_propagate(FALSE)

    def addBody(self):
        self.bodyFrame = self.addFrame(950, 700, anchor_value=W)

    def addFooter(self):

        frame = self.addFrame(950, 100, "lightgrey", BOTTOM, S)

        buttonReset = Button(frame, text="Reset", command=self.reset)
        buttonReset.config(self.FooterSettings)
        buttonReset.grid(row=0, column=1, padx=10, sticky=W) 

        buttonExit = Button(frame, text="Exit", command=self.exitWindowsAlert)
        buttonExit.config(self.FooterSettings)
        buttonExit.grid(row=0, column=2, padx=10, sticky=W) 

    # Auxiliar body functions
    def addObject(self, labelText, nrow):
        
        self.addLabel(self.bodyFrame, labelText, nrow, 0)
        self.addButton(self.bodyFrame, labelText, nrow, 1)


    def addText(self, labelText, nrow):
        self.addLabel(self.bodyFrame, labelText, nrow, 0, NW)
        text = Label(self.bodyFrame, textvariable=self.results, relief="solid", bd=1, justify=LEFT, anchor=NW, font=self.font)
        text.config(
                bg="white",
                padx=10,
                pady=10,
                width=80,
                height=15
        )
        text.grid(row=nrow, column=1, padx=10, sticky=W)


    def show(self):
        # Show the new window
        self.window.mainloop()

    
    


