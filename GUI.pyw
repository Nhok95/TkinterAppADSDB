from tkinter import *
from main import windowLogic
from tkinter import ttk

CheckButtonSettings = {'bg':"lightgray", 'font':("Arial", 12)}

main = windowLogic()
main.load()

main.addHeader("ADSDB PROJECT GRAPHICAL USER INTERFACE")
main.addBody()

main.addObject("Complete Pipeline", 0)
main.addObject("Landing to Formated", 1)
main.addObject("Formatted to Trusted", 2)
main.addObject("Check Data Quality (Trusted)", 3)
main.addObject("Generate Model", 4)
main.addText("Results", 5)

main.addFooter()

main.reset()



main.show()