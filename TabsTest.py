from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
# from tkinter.font import alienleagueiileft

root = Tk()
root.title("Cabinets")
root.configure(background='black')
root.geometry("700x500")

font1 = Font(
        family="Arial Rounded MT",
        size=13,
        overstrike=0)
font2 = Font(
        family="Alien League",
        size=12,
        overstrike=0)
font3 = Font(
        family="Arial Rounded MT Bold",
        size=14,
        overstrike=0)

status = Label(root, text="Cabinets App V1 - Rebuild", bd=2, relief=SUNKEN, pady=20)
status.pack(fill=BOTH)

main_frame = Frame(root)
main_frame.pack(fill=BOTH)

#For Rails
railList = ["Regular", "Side Mount", "P-2-O SM", "P-2-O UM", "Under Mount"]
railSpaceList = [2.25, 2.25, 2.25, 1.75, 1.5625]
railNum = IntVar()
railNum.set(0)
railFrame = Frame(main_frame, pady=40)
railFrame.pack()

def railChangeUp():
    railNum.set(railNum.get() + 1)
    if railNum.get() > 4:
        railNum.set(0)
    railType = Label(railFrame, text = "---------------------", fg='#fff', font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
    railType = Label(railFrame, text = railList[railNum.get()], font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
    railSpaceLabel = Label(railFrame, text="---------------------", fg='#fff').grid(row=3, column=1, padx=10, sticky=W)
    railSpaceLabel = Label(railFrame, text="Rail Space : " + str(railSpaceList[railNum.get()])).grid(row=3, column=1, padx=10, sticky=W)
def railChangeDown():
    railNum.set(railNum.get() - 1)
    if railNum.get() < 0:
        railNum.set(4)
    railType = Label(railFrame, text = "---------------------", fg='#fff', font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
    railType = Label(railFrame, text = railList[railNum.get()], font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
    railSpaceLabel = Label(railFrame, text="---------------------", fg='#fff').grid(row=3, column=1, padx=10, sticky=W)
    railSpaceLabel = Label(railFrame, text="Rail Space : " + str(railSpaceList[railNum.get()])).grid(row=3, column=1, padx=10, sticky=W)

railQLabel = Label(railFrame, text="What kind of railing for drawers?", font=font3)
railQLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=W+E)
railLabel = Label(railFrame, text = "Rail Type :", font=font3).grid(row=1, rowspan=2, column=0, padx=10, sticky=W)
railType = Label(railFrame, text = "---------------------", fg='#fff', font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
railType = Label(railFrame, text = railList[railNum.get()], font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
railUpButton = Button(railFrame, text="˄", command=railChangeUp).grid(row=1, rowspan=1, column=2, padx=10, sticky=W)
railDownButton = Button(railFrame, text="˅", command=railChangeDown).grid(row=2, rowspan=1, column=2, padx=10, sticky=W)
railSpaceLabel = Label(railFrame, text="Rail Space : " + str(railSpaceList[railNum.get()])).grid(row=3, column=1, padx=10, sticky=W)

#For Material

materialList = ["Ply Wood", "White Melamin", "Custom"]
materialThicknessList = [0.625, 0.625, 0.625]
materialNum = IntVar()
materialNum.set(0)
materialFrame = Frame(main_frame, pady=40)
materialFrame.pack()

def materialChangeUp():
    materialNum.set(materialNum.get() + 1)
    if materialNum.get() > 2:
        materialNum.set(0)
    materialType = Label(materialFrame, text = "-----------------------", fg='#fff', font=font3).grid(row=1, rowspan=2, column=1, padx=10, sticky=W)
    materialType = Label(materialFrame, text = materialList[materialNum.get()], font=font3).grid(row=1, rowspan=2, column=1, padx=10, sticky=W)
    materialThicknessLabel = Label(materialFrame, text="---------------------", fg='#fff').grid(row=3, column=1, padx=10, sticky=W)
    materialThicknessLabel = Label(materialFrame, text="Thickness : " + str(materialThicknessList[materialNum.get()])).grid(row=3, column=1, padx=10, sticky=W)
def materialChangeDown():
    materialNum.set(materialNum.get() - 1)
    if materialNum.get() < 0:
        materialNum.set(2)
    materialType = Label(materialFrame, text = "-----------------------", fg='#fff', font=font3).grid(row=1, rowspan=2, column=1, padx=10, sticky=W)
    materialType = Label(materialFrame, text = materialList[materialNum.get()], font=font3).grid(row=1, rowspan=2, column=1, padx=10, sticky=W)
    materialThicknessLabel = Label(materialFrame, text="---------------------", fg='#fff').grid(row=3, column=1, padx=10, sticky=W)
    materialThicknessLabel = Label(materialFrame, text="Thickness : " + str(materialThicknessList[materialNum.get()])).grid(row=3, column=1, padx=10, sticky=W)

materialQLabel = Label(materialFrame, text="What type of material?", font=font3)
materialQLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=W+E)
materialLabel = Label(materialFrame, text = "Material Type :", font=font3).grid(row=1, rowspan=2, column=0, padx=10, sticky=W)
materialType = Label(materialFrame, text = "-----------------------", fg='#fff', font=font3).grid(row=1, rowspan=2, column=1, padx=10, sticky=W)
materialType = Label(materialFrame, text = materialList[materialNum.get()], font=font3).grid(row=1, rowspan=2, column=1, padx=10, sticky=W)
materialUpButton = Button(materialFrame, text="˄", command=materialChangeUp).grid(row=1, rowspan=1, column=2, padx=10, sticky=W)
materialDownButton = Button(materialFrame, text="˅", command=materialChangeDown).grid(row=2, rowspan=1, column=2, padx=10, sticky=W)
materialThicknessLabel = Label(materialFrame, text="Thickness : " + str(materialThicknessList[materialNum.get()])).grid(row=3, column=1, padx=10, sticky=W)

#Switch Button
switch = IntVar()
switch.set(1)
statusFrame = Frame(main_frame, pady=30)
statusFrame.pack()

switchFrame = Frame(statusFrame)
switchFrame.grid(row=0, rowspan=2, column=0, padx=10, sticky=E, ipadx = 15, ipady=15)
switchQLabel = Label(switchFrame, text = "Standard or Custom measurements?", font=font3)
switchQLabel.grid(row=0, column=0, columnspan=3, pady=10, sticky=E)
defaultLabel = Label(switchFrame, text = "---------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
defaultLabel = Label(switchFrame, text="Standard", font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
customLabel = Label(switchFrame, text = "---------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
customLabel = Label(switchFrame, text="Custom", font=font1).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
def switchIt():
    if switch.get() == 0:
        switch.set(1)
        dLabel = Label(switchFrame, text = "--------------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
        dLabel = Label(switchFrame, text="Standard", font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
        cLabel = Label(switchFrame, text = "-----------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
        cLabel = Label(switchFrame, text="Custom", font=font1).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
        switchButton = Button(switchFrame, text="⚫☷☷", command=switchIt).grid(row=2, rowspan=2, column=1, padx=5, sticky=W+E)
    elif switch.get() == 1:
        switch.set(0)
        cLabel = Label(switchFrame, text = "-----------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
        cLabel = Label(switchFrame, text="Custom", font=font3).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
        dLabel = Label(switchFrame, text = "--------------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
        dLabel = Label(switchFrame, text="Standard", font=font1).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
        switchButton = Button(switchFrame, text="☷☷⚫", command=switchIt).grid(row=2, rowspan=2, column=1, padx=5, sticky=W+E)

if switch.get() == 1:
    switchButton = Button(switchFrame, text="⚫☷☷", command=switchIt).grid(row=2, rowspan=2, column=1, padx=5, sticky=W+E)
elif switch.get() == 0:
    switchButton = Button(switchFrame, text="☷☷⚫", command=switchIt).grid(row=2, rowspan=2, column=1, padx=5, sticky=W+E)

#Next Page Button
submitButtonP1 = Button(main_frame, text="Start", font=font3)
submitButtonP1.pack(pady=20)


# railQLabel = Label(main_frame, text="What kind of railing for drawers?", font = font1)
# railQLabel.pack()
# railQLabel = Label(main_frame, text="What kind of railing for drawers?", font = font2)
# railQLabel.pack()
# railQLabel = Label(main_frame, text="What kind of railing for drawers?", font = font3)
# railQLabel.pack()

root.mainloop()
