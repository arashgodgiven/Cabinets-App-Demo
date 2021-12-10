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
        family="Helvetica",
        size=8,
        overstrike=0)
font2 = Font(
        family="Arial Rounded MT",
        size=13,
        overstrike=0)
font3 = Font(
        family="Arial Rounded MT Bold",
        size=14,
        overstrike=0)

def nextPage():

    for child in main_frame.winfo_children():
        child.destroy()

    # main_frame.pack_forget()

    p1Frame = Frame(main_frame)
    p1Frame.pack()

    statusFrame = Frame(p1Frame)
    statusFrame.pack()

    #Switch Button
    switchFrame = Frame(statusFrame, highlightbackground="Gray", highlightthickness=0.5)
    switchFrame.grid(row=0, rowspan=2, column=0, sticky=W+E, ipady=15)
    defaultLabel = Label(switchFrame, text="Standard", font = ('Helvetiva', 9, 'bold')).grid(row=0, rowspan=2, column=0, padx=10, sticky=E)
    customLabel = Label(switchFrame, text="Custom", font = ('Helvetiva', 9)).grid(row=0, rowspan=2, column=2, padx=10, sticky=W)
    def switchIt():
        if switch.get() == 0:
            switch.set(1)
            dLabel = Label(switchFrame, text="Standard", font = ('Helvetiva', 9, 'bold')).grid(row=0, rowspan=2, column=0, padx=10, sticky=E)
            cLabel = Label(switchFrame, text="Custom", font = ('Helvetiva', 9)).grid(row=0, rowspan=2, column=2, padx=10, sticky=W)
            switchButton = Button(switchFrame, text="⚫☷☷", command=switchIt).grid(row=0, rowspan=2, column=1, padx=5, sticky=W+E)
        elif switch.get() == 1:
            switch.set(0)
            cLabel = Label(switchFrame, text="Custom", font = ('Helvetiva', 9, 'bold')).grid(row=0, rowspan=2, column=2, padx=10, sticky=W)
            dLabel = Label(switchFrame, text="Standard", font = ('Helvetiva', 9)).grid(row=0, rowspan=2, column=0, padx=10, sticky=E)
            switchButton = Button(switchFrame, text="☷☷⚫", command=switchIt).grid(row=0, rowspan=2, column=1, padx=5, sticky=W+E)

    if switch.get() == 1:
        switchButton = Button(switchFrame, text="⚫☷☷", command=switchIt).grid(row=0, rowspan=2, column=1, padx=5, sticky=W+E)
    elif switch.get() == 0:
        switchButton = Button(switchFrame, text="☷☷⚫", command=switchIt).grid(row=0, rowspan=2, column=1, padx=5, sticky=W+E)

    #App Status
    status = Label(statusFrame, text="Cabinets App V1 - Rebuild", bd=1, relief=SUNKEN, pady=20)
    status.grid(row=0, rowspan=2, column=2, columnspan=6, ipadx=450, sticky=W+E)

    #Cabinets defined
    class CabinetFullDoor:
        def __init__(self, category, name, width, height, depth, shelfQty, toeKick, materialThickness):
            self.category = category
            self.name = name
            self.width = width
            self.height = height
            self.depth = depth
            self.shelfQty = shelfQty
            self.toeKick = toekick #4.5
            self.MT = materialThickness #0.625

            self.listParts = []

            if self.category == "Base":
                if self.name == "Full Door":
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                    self.listParts.append(self.gable)
                    self.bottom = Part(1, "Bottom", self.depth - self.MT, self.width - 2 * self.MT, "1S")
                    self.listParts.append(self.bottom)
<<<<<<< Updated upstream
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.MT, "-")
=======
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.MT, "-")  #TOEKICK -0.25
>>>>>>> Stashed changes
                    self.listParts.append(self.kick)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.MT - 0.125, self.width - 2 * self.MT - 0.0625, "1L")
                        self.listParts.append(self.shelf)
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-")
                    self.listParts.append(self.back)

            if self.category == "Wall":
                if self.name == "Full Door":
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L + 2S")
                    self.listParts.append(self.gable)
                    self.deck = Part(1, "Deck", self.depth - self.MT, self.width - 2 * self.MT, "1L")
                    self.listParts.append(self.deck)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.MT - 0.125, self.width - 2 * self.MT - 0.0625, "1L")
                        self.listParts.append(self.shelf)
                    self.back = Part(1, "Back", self.width, self.height, "2S")
                    self.listParts.append(self.back)

            if self.category == "Tall":
                if self.name == "Full Door":
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                    self.listParts.append(self.gable)
                    self.bottom = Part(1, "Bottom", self.depth - self.MT, self.width - 2 * self.MT, "1L")
                    self.listParts.append(self.bottom)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.MT, "1L")
                    self.listParts.append(self.kick)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.MT - 0.125, self.width - 2 * self.MT - 0.0625, "1L")
                        self.listParts.append(self.shelf)
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-")
                    self.listParts.append(self.back)

            if self.category == "Vanity":
                if self.name == "Full Door":
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                    self.listParts.append(self.gable)
                    self.bottom = Part(1, "Bottom", self.depth - self.MT, self.width - 2 * self.MT, "1L")
                    self.listParts.append(self.bottom)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.MT, "1L")
                    self.listParts.append(self.kick)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.MT - 0.125, self.width - 2 * self.MT - 0.0625, "1L")
                        self.listParts.append(self.shelf)
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-")
                    self.listParts.append(self.back)

    class CabinetDrawers:
        def __init__(self, category, name, width, height, depth, drawerQty, drawerHeights, drawerDepth, toekick, materialThickness):
            self.category = category
            self.name = name
            self.width = width
            self.height = height
            self.depth = depth
            self.drawerQty = drawerQty
            self.drawerHeights = []
            self.drawerHeights = drawerHeights
            self.drawerDepth = drawerDepth
            self.toeKick = toekick #4.5
            self.MT = materialThickness #0.625
            self.railType = railList[railNum.get()]
            self.railSpaceSides = railSpaceSidesList[railNum.get()]
            self.railSpaceUnder = railSpaceUnderList[railNum.get()]

            self.listParts = []

            if self.category == "Base":
                if name == "Drawers":
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                    self.listParts.append(self.gable)
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-")
                    self.listParts.append(self.back)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.MT, "-")
                    self.listParts.append(self.kick)
                    self.sides1 = Part(2, "Sides1", self.drawerHeights[0], self.drawerDepth, "1L")
                    self.listParts.append(self.sides1)
                    self.frontBack1 = Part(2, "Front & Back1", self.drawerHeights[0] - self.railSpaceUnder, self.width - 2 * self.MT - 2 * self.railSpaceSides, "1L")
                    self.listParts.append(self.frontBack1)
                    self.sides2 = Part(4, "Sides2", self.drawerHeights[1], self.drawerDepth, "1L")
                    self.listParts.append(self.sides2)
                    self.frontBack2 = Part(4, "Front & Back2", self.drawerHeights[1] - self.railSpaceUnder, self.width - 2 * self.MT - 2 * self.railSpaceSides, "1L")
                    self.listParts.append(self.frontBack2)
                    if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                        self.drawerBottom = Part(3, "Drawer Bottom", self.width - 2 * self.MT - 2 * self.railSpaceSides, self.drawerDepth, "-")
                        self.listParts.append(self.drawerBottom)
                    else:
                        self.drawerBottom = Part(3, "Drawer Bottom", self.width - 2 * self.railSpaceSides, self.drawerDepth, "-")
                        self.listParts.append(self.drawerBottom)
                    self.topStretcherFront = Part(1, "Top Stretcher", 4, self.width - 2 * self.MT, "1L")
                    self.listParts.append(self.topStretcherFront)
                    self.topStretcherBack = Part(1, "Top Stretcher", 4, self.width - 2 * self.MT, "-")
                    self.listParts.append(self.topStretcherBack)
                    self.bottom = Part(1, "Bottom", self.width - 2 * self.MT, self.depth - self.MT, "1S")
                    self.listParts.append(self.bottom)

            if self.category == "Vanity":
                if name == "Drawers":
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                    self.listParts.append(self.gable)
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-")
                    self.listParts.append(self.back)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.MT, "1L")
                    self.listParts.append(self.kick)

                    self.sides1 = Part(2, "Sides1", "--length by user--", "--width by user--", "1L")     #EDIT
                    self.listParts.append(self.sides1)
                    self.frontBack1 = Part(2, "Front & Back1", self.width - 2 * self.MT - 2 * self.railspace, "--width by user--", "1L")   #EDIT
                    self.listParts.append(self.frontBack1)
                    self.sides2 = Part(4, "Sides2", "--length by user--", "--width by user--", "1L")
                    self.listParts.append(self.sides2)
                    self.frontBack2 = Part(4, "Front & Back2", self.width - 2 * self.MT - 2 * self.railspace, "--width by user--", "1L")
                    self.listParts.append(self.frontBack2)
                    self.drawerBottom = Part(3, "Drawer Bottom", "--length by user--", self.width - 2 * self.MT - 2 * self.railspace, "-")
                    self.listParts.append(self.drawerBottom)
                    self.topStretcher = Part(2, "Top Stretcher", 4, self.width - 2 * self.MT, "-")
                    self.listParts.append(self.topStretcher)
                    self.bottom = Part(1, "Bottom", self.depth - self.MT, self.width - 2 * self.MT, "1L")
                    self.listParts.append(self.bottom)

<<<<<<< Updated upstream
=======
                    # cabinetCorner = CabinetCorner(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)

>>>>>>> Stashed changes
    class CabinetCorner:
        def __init__(self, category, name, width, height, depth, shelfQty, secSide, toekick, materialThickness):
            self.category = category
            self.name = name
            self.width = width
            self.height = height
            self.depth = depth
            self.shelfQty = shelfQty
            self.secSide = secSide
            self.toeKick = toekick #4.5
            self.MT = materialThickness #0.625

            self.listParts = []

            if self.category == "Base":
                if name == "Corner 90":
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                    self.listParts.append(self.gable)
                    self.side1 = Part(1, "Side#1", self.secSide - 12, self.height - self.toeKick, "-")
                    self.listParts.append(self.side1)
                    self.side2 = Part(1, "Side#2", self.width - 12, self.height - self.toeKick, "-")
                    self.listParts.append(self.side2)
<<<<<<< Updated upstream
                    self.deck = Part(2, "Deck", self.secSide - 2 * self.MT, self.width - 2 * self.MT, "1S") # "1S 90°"
=======
                    self.deck = Part(2, "Deck", self.secSide - 2 * self.MT, self.depth - 2 * self.MT, "1S") #1S 90°
>>>>>>> Stashed changes
                    self.listParts.append(self.deck)
                    self.kick1 = Part(1, "Kick#1", self.toeKick - 0.25, self.secSide - self.depth + 2.5, "-")
                    self.listParts.append(self.kick1)
                    self.kick2 = Part(1, "Kick#2", self.toeKick - 0.25, self.width - self.depth + 2.5 + self.MT, "-")
                    self.listParts.append(self.kick2)
<<<<<<< Updated upstream
                    self.shelf = Part(1, "Shelf", self.secSide - 2 * self.MT - 0.0625, self.width - 2 * self.MT - 0.0625, "1S") # "1S 90°"
                    self.listParts.append(self.shelf)
                    self.back = Part(1, "Back", "18", self.height, "-") #Back width is 18 in standard
=======
                    self.shelf = Part(1, "Shelf", self.secSide - 2 * self.MT - 0.0625, self.width - 2 * self.MT - 0.0625, "1S") #1S 90°
                    self.listParts.append(self.shelf)
                    self.back = Part(1, "Back", "Unsure 18", self.height, "-")
>>>>>>> Stashed changes
                    self.listParts.append(self.back)


                if name == "Corner Diagonal":
                    # --UNSURE-- Everything is same as Corner 90.
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                    self.listParts.append(self.gable)
                    self.deck = Part(2, "Deck", self.secSide - 2 * self.MT, self.depth - 2 * self.MT, "1S 90°")
                    self.listParts.append(self.deck)
                    self.kick1 = Part(1, "Kick#1", self.toeKick - 0.25, self.secSide - self.depth + 2.5, "-")
                    self.listParts.append(self.kick1)
                    self.kick2 = Part(1, "Kick#2", self.toeKick - 0.25, self.width - self.depth + 2.5 + self.MT, "-")
                    self.listParts.append(self.kick2)
                    self.shelf = Part(1, "Shelf", self.secSide - 2 * self.MT - 0.0625, self.width - 2 * self.MT - 0.0625, "1S 90°")
                    self.listParts.append(self.shelf)
                    self.back = Part(1, "Back", "Unsure 18", self.height, "-")
                    self.listParts.append(self.back)
                    self.side1 = Part(1, "Side#1", self.secSide - 12, self.height - self.toeKick, "-")
                    self.listParts.append(self.side1)
                    self.side2 = Part(1, "Side#2", self.width - 12, self.height - self.toeKick, "-")
                    self.listParts.append(self.side2)

            if self.category == "Wall":
                if self.name == "Corner 90": #No kick for Corner 90?
                    self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L + 2S")
                    self.listParts.append(self.gable)
                    self.deck = Part(3, "Deck", self.width - 2 * self.MT, self.width - 2 * self.MT, "1A")
                    self.listParts.append(self.deck)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.width - 2 * self.MT - 0.0625, self.width - 2 * self.MT - 0.0625, "1A")
                        self.listParts.append(self.shelf)
                    self.back1 = Part(1, "Back#1", self.width, self.height, "2S")
                    self.listParts.append(self.back1)
                    self.back2 = Part(1, "Back#2", self.width - self.MT, self.height, "2S")
                    self.listParts.append(self.back2)

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    class Cabinet:
        def __init__(self, category, name, width, height, depth, shelfQty, secSide, toekick, materialThickness):
            self.category = category
            self.name = name
            self.width = width
            self.height = height
            self.depth = depth
            self.shelfQty = shelfQty
            self.secSide = secSide
            self.toeKick = toekick #4.5
            self.MT = materialThickness #0.625
            self.railspace = railSpaceSidesList[railNum.get()]

            self.listParts = []

            #FORMULAS:
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
                # if self.name == "Microwave Slot":
                #     # --UNSURE-- Will implement later.
                #     self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L + 2S")
                #     self.listParts.append(self.gable)

            # if self.category == "Tall":

            # if self.category == "Vanity":

            # if self.category == "Custom":
                # --UNSURE-- Implement Custom Formulas here.

    class Part:
        def __init__(self, qty, name, width, height, tape):
            self.qty = qty
            self.name = name
            self.width = width
            self.height = height
            self.tape = tape

    #FOR INCREASING B
    def checkedB(givenNumber):
        if itemsB[givenNumber].get() == 1:
            tempNum = amountB[givenNumber].get()
            tempNum = tempNum + 1
            amountB[givenNumber].set(tempNum)
        else:
            tempNum = 0
            amountB[givenNumber].set(0)
        newLabel = Label(frameBase,text=f'{tempNum}').grid(row=givenNumber, column=2, padx=5, sticky=E)

    def decB(givenNumber, givenRow):
        if itemsB[givenRow].get() == 1:
            if givenNumber <= 1:
                print("count will be negative")
            else:
                givenNumber = givenNumber - 1
                newLabel = Label(frameBase, text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
                amountB[givenRow].set(givenNumber)

    def incB(givenNumber, givenRow):
        if itemsB[givenRow].get() == 1:
            givenNumber = givenNumber + 1
            newLabel = Label(frameBase,text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
            amountB[givenRow].set(givenNumber)

    #FOR INCREASING W
    def checkedW(givenNumber):
        if itemsW[givenNumber].get() == 1:
            tempNum = amountW[givenNumber].get()
            tempNum = tempNum + 1
            amountW[givenNumber].set(tempNum)
        else:
            tempNum = 0
            amountW[givenNumber].set(0)
        newLabel = Label(frameWall,text=f'{tempNum}').grid(row=givenNumber, column=2, padx=5, sticky=E)

    def decW(givenNumber, givenRow):
        if itemsW[givenRow].get() == 1:
            if givenNumber <= 1:
                print("count will be negative")
            else:
                givenNumber = givenNumber - 1
                newLabel = Label(frameWall, text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
                amountW[givenRow].set(givenNumber)

    def incW(givenNumber, givenRow):
        if itemsW[givenRow].get() == 1:
            givenNumber = givenNumber + 1
            newLabel = Label(frameWall,text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
            amountW[givenRow].set(givenNumber)

    #FOR INCREASING T
    def checkedT(givenNumber):
        if itemsT[givenNumber].get() == 1:
            tempNum = amountT[givenNumber].get()
            tempNum = tempNum + 1
            amountT[givenNumber].set(tempNum)
        else:
            tempNum = 0
            amountT[givenNumber].set(0)
        newLabel = Label(frameTall,text=f'{tempNum}').grid(row=givenNumber, column=2, padx=5, sticky=E)

    def decT(givenNumber, givenRow):
        if itemsT[givenRow].get() == 1:
            if givenNumber <= 1:
                print("count will be negative")
            else:
                givenNumber = givenNumber - 1
                newLabel = Label(frameTall, text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
                amountT[givenRow].set(givenNumber)

    def incT(givenNumber, givenRow):
        if itemsT[givenRow].get() == 1:
            givenNumber = givenNumber + 1
            newLabel = Label(frameTall,text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
            amountT[givenRow].set(givenNumber)

    #FOR INCREASING V
    def checkedV(givenNumber):
        if itemsV[givenNumber].get() == 1:
            tempNum = amountV[givenNumber].get()
            tempNum = tempNum + 1
            amountV[givenNumber].set(tempNum)
        else:
            tempNum = 0
            amountV[givenNumber].set(0)
        newLabel = Label(frameVanity,text=f'{tempNum}').grid(row=givenNumber, column=2, padx=5, sticky=E)

    def decV(givenNumber, givenRow):
        if itemsV[givenRow].get() == 1:
            if givenNumber <= 1:
                print("count will be negative")
            else:
                givenNumber = givenNumber - 1
                newLabel = Label(frameVanity, text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
                amountV[givenRow].set(givenNumber)

    def incV(givenNumber, givenRow):
        if itemsV[givenRow].get() == 1:
            givenNumber = givenNumber + 1
            newLabel = Label(frameVanity,text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
            amountV[givenRow].set(givenNumber)

    #CUSTOM
    def checkedC():
        if custom.get() == 1:
            tempNum = 1
            numCustom.set(1)
        else:
            tempNum = 0
            numCustom.set(0)
        newLabel = Label(frameCustom, text=f'{tempNum}').grid(row=0, column=2, padx=5, sticky=E)

    def decC(givenNumber):
        if custom.get() == 1:
            if givenNumber <= 1:
                print("count will be negative")
            else:
                givenNumber = givenNumber - 1
                newLabel = Label(frameCustom, text=f'{givenNumber}').grid(row=0, column=2, padx=5, sticky=E)
                numCustom.set(givenNumber)

    def incC(givenNumber):
        if custom.get() == 1:
            givenNumber = givenNumber + 1
            newLabel = Label(frameCustom,text=f'{givenNumber}').grid(row=0, column=2, padx=5, sticky=E)
            numCustom.set(givenNumber)

    #App Scrollbar
    back_frame = Frame(root)
    back_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(back_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(back_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    app_frame = Frame(my_canvas)
    my_canvas.create_window((0,0), window=app_frame, anchor="nw")

    #Workspace Scrollbar
    workspace_backFrame = LabelFrame(app_frame, text="Workspace", padx=0, pady=5)
    workspace_backFrame.grid(row=1, rowspan = 5, column=1, columnspan=18, padx=0, pady=5, sticky=W+E+N+S)
    workspace_canvas = Canvas(workspace_backFrame)
    workspace_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    workspace_scrollbar = ttk.Scrollbar(workspace_backFrame, orient=VERTICAL, command=workspace_canvas.yview)
    workspace_scrollbar.pack(side=RIGHT, fill=Y)
    workspace_canvas.configure(yscrollcommand=workspace_scrollbar.set)
    workspace_canvas.bind('<Configure>', lambda e: workspace_canvas.configure(scrollregion = workspace_canvas.bbox("all")))
    workspace_frame = Frame(workspace_canvas)
    workspace_canvas.create_window((0,0), window=workspace_frame, anchor="nw")

<<<<<<< Updated upstream
    for newthing in range(40):
        Label(workspace_frame, text=".").grid(row = newthing+30, column = 0, pady=10, padx=10)
=======
    for newthing in range(80):
        Label(workspace_frame, text=".", fg='#fff').grid(row = newthing+30, column = 0, pady=10, padx=10)
>>>>>>> Stashed changes

    #Cutlist Scrollbar
    cutlist_backFrame = LabelFrame(app_frame, text="Cutlist", padx=5, pady=5)
    cutlist_backFrame.grid(row=1, rowspan = 5, column=19, columnspan=6, padx=5, pady=5, sticky=W+E+N+S)
    cutlist_canvas = Canvas(cutlist_backFrame)
    cutlist_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    cutlist_scrollbar = ttk.Scrollbar(cutlist_backFrame, orient=VERTICAL, command=cutlist_canvas.yview)
    cutlist_scrollbar.pack(side=RIGHT, fill=Y)
    cutlist_canvas.configure(yscrollcommand=cutlist_scrollbar.set)
    cutlist_canvas.bind('<Configure>', lambda e: cutlist_canvas.configure(scrollregion = cutlist_canvas.bbox("all")))
    cutlist_frame = Frame(cutlist_canvas)
    cutlist_canvas.create_window((0,0), window=cutlist_frame, anchor="nw")

<<<<<<< Updated upstream
    for newthing in range(40):
        Label(cutlist_frame, text=".").grid(row = newthing+30, column = 0, pady=10, padx=10)
=======
    for newthing in range(80):
        Label(cutlist_frame, text=".", fg='#fff').grid(row = newthing+30, column = 0, pady=10, padx=10)
>>>>>>> Stashed changes

    baseBinary = LabelFrame(workspace_frame, text="Base", padx=5, pady=5)
    baseBinary.grid(row=0, column=0, padx=5, pady=5, sticky=W+E)

    wallBinary = LabelFrame(workspace_frame, text="Wall", padx=5, pady=5)
    wallBinary.grid(row=1, column=0, padx=5, pady=5, sticky=W+E)

    tallBinary = LabelFrame(workspace_frame, text="Tall", padx=5, pady=5)
    tallBinary.grid(row=2, column=0, padx=5, pady=5, sticky=W+E)

    vanityBinary = LabelFrame(workspace_frame, text="Vanity", padx=5, pady=5)
    vanityBinary.grid(row=3, column=0, padx=5, pady=5, sticky=W+E)

    class Send:
        def __init__(self, parent, givenList):
            self.spec = ["Quantity", "Name", "Width", "Length", "Tape"]
            self.i = 0
            for self.obj in givenList:
                self.j = 1
                self.newFrame = LabelFrame(parent, text = self.obj.name, padx = 5, pady = 5)
                self.newFrame.grid(row=self.i, column=0, columnspan=5, padx=10, pady=5, sticky=N+W+E)
                for self.s in range(5):
                    self.typelabel = Label(self.newFrame, text=self.spec[self.s], padx=10, pady=5).grid(row=0, column=self.s, sticky=W+E)
                for self.part in self.obj.listParts:
                    self.qtyLabel = Label(self.newFrame, text=self.part.qty, padx=10, pady=5).grid(row=self.j, column=0, sticky=W+E)
                    self.nameLabel = Label(self.newFrame, text=self.part.name, padx=10, pady=5).grid(row=self.j, column=1, sticky=W+E)
                    self.widthLabel = Label(self.newFrame, text=self.part.width, padx=10, pady=5).grid(row=self.j, column=2, sticky=W+E)
                    self.heightLabel = Label(self.newFrame, text=self.part.height, padx=10, pady=5).grid(row=self.j, column=3, sticky=W+E)
                    self.tapeLabel = Label(self.newFrame, text=self.part.tape, padx=10, pady=5).grid(row=self.j, column=4, sticky=W+E)
                    self.j = self.j + 1
                self.i = self.i + 1

    class Show:
        def __init__(self, parent, givenIndex, givenString):
            self.index = givenIndex
            self.category = givenString
            self.columnIndex = 0
            self.rowIndex = 0
            self.drawerQty = 0
            self.drawerHeights = []

            def placement():
                self.columnIndex += 1
                if self.columnIndex > 6:
                    self.columnIndex = 0
                    self.rowIndex += 1
                    rowNumInShow.set(self.rowIndex + 1)

            self.MTLabel1 = Label(parent, text = "M.T. : " + str(materialThickness), padx = 10, pady = 5, anchor = E)
            self.MTLabel1.grid(row=self.rowIndex, column=self.columnIndex)
            placement()

            def width_height_depth(givenHeight, givenDepth):
                self.widthLabel = Label(parent, text="Width: ", padx=10, pady=5)
                self.widthLabel.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
                self.widthEntry = Entry(parent, width = 10)
                self.widthEntry.grid(row=self.rowIndex, column=self.columnIndex)
                placement()

                self.heightLabel = Label(parent, text="height: ", padx=10, pady=5, anchor=E)
                self.heightLabel.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
                self.heightEntry = Entry(parent, width = 10)
                self.heightEntry.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
                self.heightEntry.insert(0, givenHeight)

                self.depthLabel = Label(parent, text="Depth: ", padx=10, pady=5, anchor=E)
                self.depthLabel.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
                self.depthEntry = Entry(parent, width = 10)
                self.depthEntry.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
                self.depthEntry.insert(0, givenDepth)

                self.sendButton = Button(parent, text=">", command=self.send)
                self.sendButton.grid(row=self.rowIndex-1, column=7, padx=10, pady=5)

            def shelf():
                self.shelfLabel = Label(parent, text = "Shelves #: ", padx=10, pady=5, anchor=E)
                self.shelfLabel.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
                self.shelfEntry = Entry(parent, width = 10)
                self.shelfEntry.grid(row=self.rowIndex, column=self.columnIndex)
                if switch.get() == 1:
                    self.shelfEntry.insert(0, 1)
                placement()

            def toeKick():
                self.kickLabel = Label(parent, text = "Toe Kick: ", padx=10, pady=5, anchor=E)
                self.kickLabel.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
                self.kickEntry = Entry(parent, width = 10)
                self.kickEntry.grid(row=self.rowIndex, column=self.columnIndex)
                if switch.get() == 1:
                    self.kickEntry.insert(0, 4.5)
                placement()

            def secondSide():
                self.secSideLabel = Label(parent, text = "Sec Side: ", padx=10, pady=5, anchor=E)
<<<<<<< Updated upstream
                self.secSideEntry = Entry(parent, width = 10)
                if switch.get() == 0:
                    self.secSideLabel.grid(row=self.rowIndex, column=self.columnIndex)
                    placement()
                    self.secSideEntry.grid(row=self.rowIndex, column=self.columnIndex)
                    placement()
=======
                self.secSideLabel.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
                self.secSideEntry = Entry(parent, width = 10)
                self.secSideEntry.grid(row=self.rowIndex, column=self.columnIndex)
                placement()
>>>>>>> Stashed changes

            if self.category == "Base":
                if switch.get() == 1:
                    width_height_depth(34.75, 23.75)
                elif switch.get() == 0:
                    width_height_depth(0, 0)

                self.text = textB[self.index]
                if self.text == textB[1]:
                    self.railSpaceLabel = Label(parent, text = "Railing:\n" + railList[railNum.get()] + " , " + str(railSpaceSidesList[railNum.get()]), padx = 10, pady = 5, anchor = E)
                    self.railSpaceLabel.grid(row=self.rowIndex, column=self.columnIndex)
                    placement()
                    toeKick()
                    self.drawerNumLabel = Label(parent, text = "Drawer #: ", padx=10, pady=5, anchor=E)
                    self.drawerNumLabel.grid(row=self.rowIndex, column=self.columnIndex)
                    placement()
                    self.drawerNumEntry = Entry(parent, width = 10)
                    self.drawerNumEntry.grid(row=self.rowIndex, column=self.columnIndex)
                    placement()

                    def generateDrawerEntries():
                        placement()
                        self.drawerHeightLabel = Label(parent, text = "Drawer\nheight:", padx=10, pady=5, anchor=E)
                        self.drawerHeightLabel.grid(row=self.rowIndex, column=self.columnIndex)
                        self.drawerQty = int(self.drawerNumEntry.get())
                        placement()

                        # Correct Method:
                        for i in range(self.drawerQty):
                            self.drawerHeightEntry = Entry(parent, width = 10)
                            self.drawerHeightEntry.grid(row=self.rowIndex, column=self.columnIndex, padx=3, pady=5)
                            if i == 0:
                                self.drawerHeightEntry.insert(0, 3.375)
                                self.drawerHeights.append(3.375)
                            else:
                                self.drawerHeightEntry.insert(0, 7.375)
                                self.drawerHeights.append(7.375)
                            placement()

                        self.drawerDepthLabel = Label(parent, text = "Drawer\nDepth:", padx=10, pady=5, anchor=E)
                        self.drawerDepthLabel.grid(row=self.rowIndex, column=self.columnIndex, padx=3, pady=5)
                        placement()

                        self.drawerDepthEntry = Entry(parent, width = 10)
                        self.drawerDepthEntry.grid(row=self.rowIndex, column=self.columnIndex, padx=3, pady=5)
                        self.drawerDepthEntry.insert(0, 22)
                        placement()

                    if switch.get() == 1:
                        self.drawerNumEntry.insert(0, 3)
                        placement()
                        generateDrawerEntries()

                    elif switch.get() == 0:
                        self.generateDrawerButton = Button(parent, text="˅", command=generateDrawerEntries)
                        self.generateDrawerButton.grid(row=self.rowIndex, column=self.columnIndex, padx=3, pady=3)
                        placement()
                else:
                    shelf()
<<<<<<< Updated upstream
                    if self.text == textB[2] or self.text == textB[3]:
                        secondSide()
                    toeKick()

                    # if switch.get() == 1:
                    #     shelf()
                    #     toeKick()
                    # elif switch.get() == 0:
                    #     if self.text == textB[0]:
                    #         shelf()
                    #         toeKick()
                    #     elif self.text == textB[2] or self.text == textB[3]:
                    #         shelf()
                    #         secondSide()
                    #         toeKick()

                        #Temporary Method:
                        # self.drawerHeightEntry1 = Entry(parent, width = 10)
                        # self.drawerHeightEntry1.grid(row=self.rowIndex, column=self.columnIndex, padx=3, pady=5)
                        # self.drawerHeightEntry1.insert(0, "1.")
                        # placement()
                        # self.drawerHeightEntry2 = Entry(parent, width = 10)
                        # self.drawerHeightEntry2.grid(row=self.rowIndex, column=self.columnIndex, padx=3, pady=5)
                        # self.drawerHeightEntry2.insert(0, "2.")
                        # placement()
                        # self.drawerHeightEntry3 = Entry(parent, width = 10)
                        # self.drawerHeightEntry3.grid(row=self.rowIndex, column=self.columnIndex, padx=3, pady=5)
                        # self.drawerHeightEntry3.insert(0, "3.")
                        # placement()

=======
                    if switch.get() == 0 and self.text == textB[3] or switch.get() == 0 and self.text == textB[2]:
                        secondSide()
                    toeKick()
>>>>>>> Stashed changes
                    # refreshPage()

            elif self.category == "Wall":
                if switch.get() == 1:
                    width_height_depth(0, 11.75)
                elif switch.get() == 0:
                    width_height_depth(0, 0)
                shelf()
                self.text = textW[self.index]
                print(self.text)
                if self.text == textW[1]:
                    secondSide()

            elif self.category == "Tall":
                if switch.get() == 1:
                    width_height_depth(0, 23.75)
                elif switch.get() == 0:
                    width_height_depth(0, 0)
                shelf()
                toeKick()

            elif self.category == "Vanity":
                if switch.get() == 1:
                    width_height_depth(30.25, 20.75)
                elif switch.get() == 0:
                    width_height_depth(0, 0)
                shelf()
                toeKick()

        def send(self):
            if self.category == "Base":
                self.text = textB[self.index]
<<<<<<< Updated upstream
                if self.text == textB[0]:
                    self.width = float(self.widthEntry.get())
                    self.height = float(self.heightEntry.get())
                    self.depth = float(self.depthEntry.get())
                    self.shelfQty = int(self.shelfEntry.get())
                    self.kick = float(self.kickEntry.get())
                elif self.text == textB[1]:
                    self.width = float(self.widthEntry.get())
                    self.height = float(self.heightEntry.get())
                    self.depth = float(self.depthEntry.get())
=======
                def width_height_depth_get():
                    self.width = float(self.widthEntry.get())
                    self.height = float(self.heightEntry.get())
                    self.depth = float(self.depthEntry.get())
                if self.text == textB[0]:
                    width_height_depth_get()
                    self.shelfQty = int(self.shelfEntry.get())
                    self.kick = float(self.kickEntry.get())
                elif self.text == textB[1]:
                    width_height_depth_get()
>>>>>>> Stashed changes
                    self.drawerQty = int(self.drawerNumEntry.get())
                    self.kick = float(self.kickEntry.get())
                    self.drawerDepth = float(self.drawerDepthEntry.get())
                elif self.text == textB[2] or self.text == text[3]:
<<<<<<< Updated upstream
                    self.width = float(self.widthEntry.get())
                    self.height = float(self.heightEntry.get())
                    self.depth = float(self.depthEntry.get())
                    self.shelfQty = int(self.shelfEntry.get())
                    if switch.get() == 1:
                        self.secSide = float(self.depthEntry.get())
                    else:
=======
                    width_height_depth_get()
                    self.shelfQty = int(self.shelfEntry.get())
                    if switch.get() == 1:
                        self.secSide = float(self.widthEntry.get())
                    elif switch.get() == 0:
>>>>>>> Stashed changes
                        self.secSide = float(self.secSideEntry.get())
                    self.kick = float(self.kickEntry.get())
            elif self.category == "Wall":
                self.text = textW[self.index]
<<<<<<< Updated upstream
                self.width = float(self.widthEntry.get())
                self.height = float(self.heightEntry.get())
                self.depth = float(self.depthEntry.get())
=======
                width_height_depth_get()
>>>>>>> Stashed changes
                self.shelfQty = int(self.shelfEntry.get())
                self.kick = float(self.kickEntry.get())
                if self.text == textW[1]:
                    self.secSide = int(self.secSideEntry.get())
            elif self.category == "Tall":
<<<<<<< Updated upstream
                self.width = float(self.widthEntry.get())
                self.height = float(self.heightEntry.get())
                self.depth = float(self.depthEntry.get())
                self.shelfQty = int(self.shelfEntry.get())
                self.kick = float(self.kickEntry.get())
            elif self.category == "Vanity":
                self.width = float(self.widthEntry.get())
                self.height = float(self.heightEntry.get())
                self.depth = float(self.depthEntry.get())
=======
                width_height_depth_get()
                self.shelfQty = int(self.shelfEntry.get())
                self.kick = float(self.kickEntry.get())
            elif self.category == "Vanity":
                width_height_depth_get()
>>>>>>> Stashed changes
                self.shelfQty = int(self.shelfEntry.get())
                self.kick = float(self.kickEntry.get())

            baseCutlist = LabelFrame(cutlist_frame, text="Base", padx=5, pady=5)
            baseCutlist.grid(row=0, column=0, padx=5, pady=5, sticky=W+E)
            wallCutlist = LabelFrame(cutlist_frame, text="Wall", padx=5, pady=5)
            wallCutlist.grid(row=1, column=0, padx=5, pady=5, sticky=W+E)
            tallCutlist = LabelFrame(cutlist_frame, text="Tall", padx=5, pady=5)
            tallCutlist.grid(row=2, column=0, padx=5, pady=5, sticky=W+E)
            vanityCutlist = LabelFrame(cutlist_frame, text="Vanity", padx=5, pady=5)
            vanityCutlist.grid(row=3, column=0, padx=5, pady=5, sticky=W+E)
            customCutlist = LabelFrame(cutlist_frame, text="Custom", padx=5, pady=5)
            customCutlist.grid(row=4, column=0, padx=5, pady=5, sticky=W+E)

            if self.category == "Base":
                self.text = textB[self.index]
                if self.text == textB[0]:
                    cabinetFullDoor = CabinetFullDoor(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.kick, materialThickness)
                    listB.append(cabinetFullDoor)
                elif self.text == textB[1]:
                    cabinetDrawers = CabinetDrawers(self.category, self.text, self.width, self.height, self.depth, self.drawerQty, self.drawerHeights, self.drawerDepth, self.kick, materialThickness)
                    listB.append(cabinetDrawers)
                elif self.text == textB[2] or self.text == textB[3]:
                    cabinetCorner = CabinetCorner(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
                    listB.append(cabinetCorner)
                showOutputs = Send(baseCutlist, listB)
            if self.category == "Wall":
                self.text = textW[self.index]
                cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
                listW.append(cabinet)
                showOutputs = Send(wallCutlist, listW)
            if self.category == "Tall":
                self.text = textT[self.index]
                cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
                listT.append(cabinet)
                showOutputs = Send(tallCutlist, listT)
            if self.category == "Vanity":
                self.text = textV[self.index]
                cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
                listV.append(cabinet)
                showOutputs = Send(vanityCutlist, listV)
            if self.category == "Custom":
                self.text = "Custom Cabinet"
                cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
                listC.append(cabinet)
                showOutputs = Send(customCutlist, listC)

    def show():
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        i = 0
        for item in itemsB:
            if item.get() == 1:
                numB = amountB[i].get()
                for count in range(numB):
                    r = rowNumInShow.get()
<<<<<<< Updated upstream
                    if switch.get() == 1:
                        frameLabelB = textB[i] + "(Standard)"
                    elif switch.get() == 0:
                        frameLabelB = textB[i] + "(Custom)"
                    itemFrameB = LabelFrame(baseBinary, text=frameLabelB, padx=5, pady=5)
=======
                    itemFrameB = LabelFrame(baseBinary, text=textB[i], padx=5, pady=5)
>>>>>>> Stashed changes
                    itemFrameB.pack(anchor=W)
                    receiveInputsB = Show(itemFrameB, i, "Base")
                amountB[i].set(0)
            i = i + 1
        #update frame base for correct quantity(0)

        i = 0
        for item in itemsW:
            if item.get() == 1:
                numW = amountW[i].get()
                for count in range(numW):
                    r = rowNumInShow.get()
<<<<<<< Updated upstream
                    if switch.get() == 1:
                        frameLabelW = textW[i] + "(Standard)"
                    elif switch.get() == 0:
                        frameLabelW = textW[i] + "(Custom)"
                    itemFrameW = LabelFrame(wallBinary, text=frameLabelW, padx=5, pady=5)
=======
                    itemFrameW = LabelFrame(wallBinary, text=textW[i], padx=5, pady=5)
>>>>>>> Stashed changes
                    itemFrameW.pack(anchor=W)
                    receiveInputsW = Show(itemFrameW, i, "Wall")
                amountW[i].set(0)
            i = i + 1
        #update frame base for correct quantity(0)

        i = 0
        for item in itemsT:
            if item.get() == 1:
                numT = amountT[i].get()
                for count in range(numT):
                    r = rowNumInShow.get()
<<<<<<< Updated upstream
                    if switch.get() == 1:
                        frameLabelT = textT[i] + "(Standard)"
                    elif switch.get() == 0:
                        frameLabelT = textT[i] + "(Custom)"
                    itemFrameT = LabelFrame(tallBinary, text=frameLabelT, padx=5, pady=5)
=======
                    itemFrameT = LabelFrame(tallBinary, text=textT[i], padx=5, pady=5)
>>>>>>> Stashed changes
                    itemFrameT.pack(anchor=W)
                    receiveInputsT = Show(itemFrameT, i, "Tall")
                amountT[i].set(0)
            i = i + 1
        #update frame base for correct quantity(0)

        i = 0
<<<<<<< Updated upstream
        r = rowNumInShow.get()
=======
>>>>>>> Stashed changes
        for item in itemsV:
            if item.get() == 1:
                numV = amountV[i].get()
                for count in range(numV):
                    r = rowNumInShow.get()
<<<<<<< Updated upstream
                    if switch.get() == 1:
                        frameLabelV = textV[i] + "(Standard)"
                    elif switch.get() == 0:
                        frameLabelV = textV[i] + "(Custom)"
                    itemFrameV = LabelFrame(vanityBinary, text=frameLabelV, padx=5, pady=5)
=======
                    itemFrameV = LabelFrame(vanityBinary, text=textV[i], padx=5, pady=5)
>>>>>>> Stashed changes
                    itemFrameV.pack(anchor=W)
                    receiveInputsV = Show(itemFrameV, i, "Vanity")
                amountV[i].set(0)
            i = i + 1
        #update frame base for correct quantity(0)

        customBinary = LabelFrame(workspace_frame, text="Custom", padx=5, pady=5)
        customBinary.grid(row=3, column=0, padx=5, pady=5, sticky=W+E)

        i = 0
        j = 0
        amountC = numCustom.get()
        for count in range(amountC):
            itemLabelC = Label(customBinary, text = "Custom" + str(i + 1), font = ('Helvetica', 10, 'bold'), padx=7, pady=5).grid(row=j, column=0, sticky=W+E)
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
            receiveInputsC = Show(customBinary, i, "Custom")

            j += 2
            i += 1

    listB = []
    listW = []
    listT = []
    listV = []
    listC = []

    fulldoorB = IntVar()
    drawersB = IntVar()
    corner90B = IntVar()
    cornerdiagonalB = IntVar()

    fulldoorW = IntVar()
    drawersW = IntVar()
    microwaveW = IntVar()

    fulldoorT = IntVar()
    ovenT = IntVar()

    fulldoorV = IntVar()
    drawersV = IntVar()
    linentowerV = IntVar()

    custom = IntVar()
    numCustom = IntVar()
    numCustom.set(0)

    amountFullB = IntVar()
    amountFullB.set(0)
    amountDraB = IntVar()
    amountDraB.set(0)
    amount90B = IntVar()
    amount90B.set(0)
    amountDiaB = IntVar()
    amountDiaB.set(0)

    amountFullW = IntVar()
    amountFullW.set(0)
    amountDraW = IntVar()
    amountDraW.set(0)
    amountMicW = IntVar()
    amountMicW.set(0)

    amountFullT = IntVar()
    amountFullT.set(0)
    amountOvenT = IntVar()
    amountOvenT.set(0)

    amountFullV = IntVar()
    amountFullV.set(0)
    amountDraV = IntVar()
    amountDraV.set(0)
    amountLinV = IntVar()
    amountLinV.set(0)

    rowNumInShow = IntVar()
    rowNumInShow.set(0)

    materialThickness = 0.625
    toekick = 4.5

    newBase = Cabinet("null", "null", 0, 0, 0, 0, 0, 0, 0)

    itemsB = [fulldoorB, drawersB, corner90B, cornerdiagonalB]
    textB = ["Full Door", "Drawers", "Corner 90", "Corner Diagonal"]
    amountB = [amountFullB, amountDraB, amount90B, amountDiaB]
    itemsW = [fulldoorW, drawersW, microwaveW]
    textW = ["Full Door", "Corner 90", "Microwave Slot"]
    amountW = [amountFullW, amountDraW, amountMicW]
    itemsT = [fulldoorT, ovenT]
    textT = ["Full Door", "Oven Slot"]
    amountT = [amountFullT, amountOvenT]
    itemsV = [fulldoorV, drawersV, linentowerV]
    textV = ["Full Door", "Drawers", "Linen Tower"]
    amountV = [amountFullV, amountDraV, amountLinV]

    #Base Frame
    frameBase = LabelFrame(app_frame, text="Base", padx=5, pady=5)
    frameBase.grid(row=1, column=0, padx=5, pady=5, sticky=W+E)
    i = 0
    for item in textB:
        newBL = Label(frameBase, text="0").grid(row=i, column=2, padx=5, sticky=E)
        i = i + 1

    checkFullB = Checkbutton(frameBase, text=textB[0], variable = itemsB[0], onvalue=1, offvalue=0, command = lambda: checkedB(0)).grid(row=0, column=0, sticky=W)
    check3DB = Checkbutton(frameBase, text=textB[1], variable = itemsB[1], onvalue=1, offvalue=0, command = lambda: checkedB(1)).grid(row=1, column=0, sticky=W)
    check90B = Checkbutton(frameBase, text=textB[2], variable = itemsB[2], onvalue=1, offvalue=0, command = lambda: checkedB(2)).grid(row=2, column=0, sticky=W)
    checkDiaB = Checkbutton(frameBase, text=textB[3], variable = itemsB[3], onvalue=1, offvalue=0, command = lambda: checkedB(3)).grid(row=3, column=0, sticky=W)

    decFullB = Button(frameBase, text="-", command = lambda: decB(amountB[0].get(), 0)).grid(row=0, column=1, sticky=E)
    dec3DB = Button(frameBase, text="-", command = lambda: decB(amountB[1].get(), 1)).grid(row=1, column=1, sticky=E)
    dec90B = Button(frameBase, text="-", command = lambda: decB(amountB[2].get(), 2)).grid(row=2, column=1, sticky=E)
    decDiaB = Button(frameBase, text="-", command = lambda: decB(amountB[3].get(), 3)).grid(row=3, column=1, sticky=E)

    incFullB = Button(frameBase, text="+", command = lambda: incB(amountB[0].get(), 0)).grid(row=0, column=3, sticky=E)
    inc3DB = Button(frameBase, text="+", command = lambda: incB(amountB[1].get(), 1)).grid(row=1, column=3, sticky=E)
    inc90B = Button(frameBase, text="+", command = lambda: incB(amountB[2].get(), 2)).grid(row=2, column=3, sticky=E)
    incDiaB = Button(frameBase, text="+", command = lambda: incB(amountB[3].get(), 3)).grid(row=3, column=3, sticky=E)

    #Wall Frame
    frameWall = LabelFrame(app_frame, text="Wall", padx=5, pady=5)
    frameWall.grid(row=2, column=0, padx=5, pady=5, sticky=W+E)
    i = 0
    for item in textW:
        newWL = Label(frameWall, text="0").grid(row=i, column=2, padx=5, sticky=E)
        i = i + 1

    checkFullW = Checkbutton(frameWall, text=textW[0], variable = itemsW[0], onvalue=1, offvalue=0, command = lambda: checkedW(0)).grid(row=0, column=0, sticky=W)
    checkDraW = Checkbutton(frameWall, text=textW[1], variable = itemsW[1], onvalue=1, offvalue=0, command = lambda: checkedW(1)).grid(row=1, column=0, sticky=W)
    checkMicW = Checkbutton(frameWall, text=textW[2], variable = itemsW[2], onvalue=1, offvalue=0, command = lambda: checkedW(2)).grid(row=2, column=0, sticky=W)

    decFullW = Button(frameWall, text="-", command = lambda: decW(amountW[0].get(), 0)).grid(row=0, column=1, sticky=W+E)
    decDraW = Button(frameWall, text="-", command = lambda: decW(amountW[1].get(), 1)).grid(row=1, column=1, sticky=W+E)
    decMicW = Button(frameWall, text="-", command = lambda: decW(amountW[2].get(), 2)).grid(row=2, column=1, sticky=W+E)

    incFullW = Button(frameWall, text="+", command = lambda: incW(amountW[0].get(), 0)).grid(row=0, column=3, sticky=W+E)
    incDraW = Button(frameWall, text="+", command = lambda: incW(amountW[1].get(), 1)).grid(row=1, column=3, sticky=W+E)
    incMicW = Button(frameWall, text="+", command = lambda: incW(amountW[2].get(), 2)).grid(row=2, column=3, sticky=W+E)

    #Tall Frame
    frameTall = LabelFrame(app_frame, text="Tall", padx=5, pady=5)
    frameTall.grid(row=3, column=0, padx=5, pady=5, sticky=W+E)
    i = 0
    for item in textT:
        newTL = Label(frameTall, text="0").grid(row=i, column=2, padx=5, sticky=E)
        i = i + 1

    checkFullT = Checkbutton(frameTall, text=textT[0], variable = itemsT[0], onvalue=1, offvalue=0, command = lambda: checkedT(0)).grid(row=0, column=0, sticky=W)
    checkOvenT = Checkbutton(frameTall, text=textT[1], variable = itemsT[1], onvalue=1, offvalue=0, command = lambda: checkedT(1)).grid(row=1, column=0, sticky=W)

    decFullT = Button(frameTall, text="-", command = lambda: decT(amountT[0].get(), 0)).grid(row=0, column=1, sticky=E)
    decOvenT = Button(frameTall, text="-", command = lambda: decT(amountT[1].get(), 1)).grid(row=1, column=1, sticky=E)

    incFullT = Button(frameTall, text="+", command = lambda: incT(amountT[0].get(), 0)).grid(row=0, column=3, sticky=E)
    incOvenT = Button(frameTall, text="+", command = lambda: incT(amountT[1].get(), 1)).grid(row=1, column=3, sticky=E)

    #Vanity Frame
    frameVanity = LabelFrame(app_frame, text="Vanity", padx=5, pady=5)
    frameVanity.grid(row=4, column=0, padx=5, pady=5, sticky=W+E)
    i = 0
    for item in textV:
        newVL = Label(frameVanity, text="0").grid(row=i, column=2, padx=5, sticky=E)
        i = i + 1

    checkFullV = Checkbutton(frameVanity, text=textV[0], variable = itemsV[0], onvalue=1, offvalue=0, command = lambda: checkedV(0)).grid(row=0, column=0, sticky=W)
    checkDraV = Checkbutton(frameVanity, text=textV[1], variable = itemsV[1], onvalue=1, offvalue=0, command = lambda: checkedV(1)).grid(row=1, column=0, sticky=W)
    checkLinV = Checkbutton(frameVanity, text=textV[2], variable = itemsV[2], onvalue=1, offvalue=0, command = lambda: checkedV(2)).grid(row=2, column=0, sticky=W)

    decFullV = Button(frameVanity, text="-", command = lambda: decV(amountV[0].get(), 0)).grid(row=0, column=1, sticky=E)
    decDraV = Button(frameVanity, text="-", command = lambda: decV(amountV[1].get(), 1)).grid(row=1, column=1, sticky=E)
    decLinV = Button(frameVanity, text="-", command = lambda: decV(amountV[2].get(), 2)).grid(row=2, column=1, sticky=E)

    incFullV = Button(frameVanity, text="+", command = lambda: incV(amountV[0].get(), 0)).grid(row=0, column=3, sticky=E)
    incDraV = Button(frameVanity, text="+", command = lambda: incV(amountV[1].get(), 1)).grid(row=1, column=3, sticky=E)
    incLinV = Button(frameVanity, text="+", command = lambda: incV(amountV[2].get(), 2)).grid(row=2, column=3, sticky=E)

    #Custom Frame
    frameCustom = LabelFrame(app_frame, text = "Custom", padx = 5, pady = 5)
    frameCustom.grid(row=5, column=0, padx=5, pady=5, sticky=W+E)
    checkCustom = Checkbutton(frameCustom, text="Custom Cabinet", variable = custom, onvalue=1, offvalue=0, command = lambda: checkedC()).grid(row=0, column=0, sticky=W)
    numCustomLabel = Label(frameCustom, text="0").grid(row=0, column=2, padx=5, sticky=E)
    decCustom = Button(frameCustom, text="-", command = lambda: decC(numCustom.get())).grid(row=0, column=1, sticky=E)
    incCustom = Button(frameCustom, text="+", command = lambda: incC(numCustom.get())).grid(row=0, column=3, sticky=E)

    submit_base_button = Button(app_frame, text="Submit", command=show).grid(row=6, column=0, sticky=W+E, pady=30)
    submit_workspace_button = Button(app_frame, text="Generate Cutlist").grid(row=6, column=18, sticky=W+E, pady=30)

    for dotthing in range(30):
        Label(app_frame, text="........ ").grid(row=7, column=dotthing)

#-------------------------------------------------------------------------------

main_frame = Frame(root)
main_frame.pack(fill=BOTH)

status = Label(main_frame, text="Cabinets App V1 - Rebuild", bd=2, relief=SUNKEN, pady=20)
status.pack(fill=BOTH)

#For Rails
railList = ["Regular", "Side Mount", "P-2-O SM", "P-2-O UM", "Under Mount"]
railSpaceSidesList = [2.25, 2.25, 2.25, 1.75, 1.5625]
railSpaceUnderList = [0, 0, 0, 1.125, 1.125]
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
    railSpaceLabel = Label(railFrame, text="Rail Space : " + str(railSpaceSidesList[railNum.get()])).grid(row=3, column=1, padx=10, sticky=W)
def railChangeDown():
    railNum.set(railNum.get() - 1)
    if railNum.get() < 0:
        railNum.set(4)
    railType = Label(railFrame, text = "---------------------", fg='#fff', font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
    railType = Label(railFrame, text = railList[railNum.get()], font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
    railSpaceLabel = Label(railFrame, text="---------------------", fg='#fff').grid(row=3, column=1, padx=10, sticky=W)
    railSpaceLabel = Label(railFrame, text="Rail Space : " + str(railSpaceSidesList[railNum.get()])).grid(row=3, column=1, padx=10, sticky=W)

railQLabel = Label(railFrame, text="What kind of railing for drawers?", font=font3)
railQLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=W+E)
railLabel = Label(railFrame, text = "Rail Type :", font=font3).grid(row=1, rowspan=2, column=0, padx=10, sticky=W)
railType = Label(railFrame, text = "---------------------", fg='#fff', font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
railType = Label(railFrame, text = railList[railNum.get()], font=font3).grid(row=1, rowspan=2, column=1, padx = 10, sticky=W)
railUpButton = Button(railFrame, text="˄", command=railChangeUp).grid(row=1, rowspan=1, column=2, padx=10, sticky=W)
railDownButton = Button(railFrame, text="˅", command=railChangeDown).grid(row=2, rowspan=1, column=2, padx=10, sticky=W)
railSpaceLabel = Label(railFrame, text="Rail Space : " + str(railSpaceSidesList[railNum.get()])).grid(row=3, column=1, padx=10, sticky=W)

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
switchFrame = Frame(main_frame, pady=40)
switchFrame.pack()

switchQLabel = Label(switchFrame, text = "Standard or Custom measurements?", font=font3)
switchQLabel.grid(row=0, column=0, columnspan=3, pady=10, sticky=E)
defaultLabel = Label(switchFrame, text = "---------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
defaultLabel = Label(switchFrame, text="Standard", font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
customLabel = Label(switchFrame, text = "---------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
customLabel = Label(switchFrame, text="Custom", font=font2).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
def switchIt():
    if switch.get() == 0:
        switch.set(1)
        dLabel = Label(switchFrame, text = "--------------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
        dLabel = Label(switchFrame, text="Standard", font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
        cLabel = Label(switchFrame, text = "-----------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
        cLabel = Label(switchFrame, text="Custom", font=font2).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
        switchButton = Button(switchFrame, text="⚫☷☷", command=switchIt).grid(row=2, rowspan=2, column=1, padx=5, sticky=W+E)
    elif switch.get() == 1:
        switch.set(0)
        cLabel = Label(switchFrame, text = "-----------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
        cLabel = Label(switchFrame, text="Custom", font=font3).grid(row=2, rowspan=2, column=2, padx=10, sticky=W)
        dLabel = Label(switchFrame, text = "--------------", fg='#fff', font=font3).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
        dLabel = Label(switchFrame, text="Standard", font=font2).grid(row=2, rowspan=2, column=0, padx=10, sticky=E)
        switchButton = Button(switchFrame, text="☷☷⚫", command=switchIt).grid(row=2, rowspan=2, column=1, padx=5, sticky=W+E)

if switch.get() == 1:
    switchButton = Button(switchFrame, text="⚫☷☷", command=switchIt).grid(row=2, rowspan=2, column=1, padx=5, sticky=W+E)
elif switch.get() == 0:
    switchButton = Button(switchFrame, text="☷☷⚫", command=switchIt).grid(row=2, rowspan=2, column=1, padx=5, sticky=W+E)

#Next Page Button
submitButtonP1 = Button(main_frame, text="Start", font=font3, command=nextPage)
submitButtonP1.pack(pady=20)

root.mainloop()
