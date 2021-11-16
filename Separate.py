from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Hello

root = Tk()
root.title("Cabinets")
root.configure(background='black')
root.geometry("700x500")

status = Label(root, text="Cabinets App V1 - Rebuild", bd=1, relief=SUNKEN, pady=20)
status.pack(fill=BOTH)

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

        self.listParts = []

        #FORMULAS:
        if self.category == "Base":
            if self.name == "Full Door":
                self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                self.listParts.append(self.gable)
                self.bottom = Part(1, "Bottom", self.depth - self.MT, self.width - 2 * self.MT, "1L")
                self.listParts.append(self.bottom)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.MT, "1L")  #TOEKICK -0.25
                self.listParts.append(self.kick)
                if self.shelfQty > 0:
                    self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.MT - 0.125, self.width - 2 * self.MT - 0.0625, "1L")
                    self.listParts.append(self.shelf)
                self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-")
                self.listParts.append(self.back)

            if name == "Drawers":
                self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                self.listParts.append(self.gable)
                self.bottom = Part(1, "Bottom", self.depth - self.MT, self.width - 2 * self.MT, "1L")
                self.listParts.append(self.bottom)
                self.kick = Part(1, "Kick", self.toeKick - 0.5, self.width - 2 * self.MT, "1L")
                self.listParts.append(self.kick)
                self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-")
                self.listParts.append(self.back)
                self.sides1 = Part(2, "Sides", self.height - self.width - self.MT, self.height - self.toeKick, "1L")
                self.listParts.append(self.sides1)
                self.frontBack1 = Part(2, "Front & Back", (self.height - self.toeKick - 0.25) / 3, "Unsure 27 1/16", "1L")
                self.listParts.append(self.frontBack1)
                self.sides2 = Part(4, "Sides", 2 * (self.height - self.width - self.MT) - 0.125, self.height - self.toeKick, "1L")
                self.listParts.append(self.sides2)
                self.frontBack2 = Part(4, "Front & Back", 2 * (self.height - self.width - 2 * self.MT), "Unsure 27 1/16", "1L")
                self.listParts.append(self.frontBack2)
                self.drawerBottom = Part(3, "Drawer Bottom", "Unsure 27 1/16", "Unsure 21 3/8", "-")

            if name == "Corner 90":
                self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                self.listParts.append(self.gable)
                self.deck = Part(2, "Deck", self.secSide - 2 * self.MT, self.depth - 2 * self.MT, "1S 90°")
                self.listParts.append(self.deck)
                self.kick1 = Part(1, "Kick#1", self.toeKick - 0.5, self.secSide - self.depth + 2.5, "-")
                self.listParts.append(self.kick1)
                self.kick2 = Part(1, "Kick#2", self.toeKick - 0.5, self.width - self.depth + 2.5 + self.MT, "-")
                self.listParts.append(self.kick2)
                self.shelf = Part(1, "Shelf", self.secSide - 2 * self.MT - 0.0625, self.width - 2 * self.MT - 0.0625, "1S 90°")
                self.listParts.append(self.shelf)
                self.back = Part(1, "Back", "Unsure 18", self.height, "-")
                self.listParts.append(self.back)
                self.side1 = Part(1, "Side#1", self.secSide - 12, self.height - self.toeKick, "-")
                self.listParts.append(self.side1)
                self.side2 = Part(1, "Side#2", self.width - 12, self.height - self.toeKick, "-")
                self.listParts.append(self.side2)

            if name == "Corner Diagonal":
                # --UNSURE-- Everything is same as Corner 90.
                self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                self.listParts.append(self.gable)
                self.deck = Part(2, "Deck", self.secSide - 2 * self.MT, self.depth - 2 * self.MT, "1S 90°")
                self.listParts.append(self.deck)
                self.kick1 = Part(1, "Kick#1", self.toeKick - 0.5, self.secSide - self.depth + 2.5, "-")
                self.listParts.append(self.kick1)
                self.kick2 = Part(1, "Kick#2", self.toeKick - 0.5, self.width - self.depth + 2.5 + self.MT, "-")
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

            if self.name == "Corner 90":
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

            if self.name == "Microwave Slot":
                # --UNSURE-- Will implement later.
                self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L + 2S")
                self.listParts.append(self.gable)

        if self.category == "Tall":
            if self.name == "Full Door":
                self.gable = Part(2, "Gable", self.depth - self.MT, self.height, "1L")
                self.listParts.append(self.gable)
                self.bottom = Part(1, "Bottom", self.depth - self.MT, self.width - 2 * self.MT, "1L")
                self.listParts.append(self.bottom)
                self.kick = Part(1, "Kick", self.toeKick - 0.5, self.width - 2 * self.MT, "1L")
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
                self.kick = Part(1, "Kick", self.toeKick - 0.5, self.width - 2 * self.MT, "1L")
                self.listParts.append(self.kick)
                if self.shelfQty > 0:
                    self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.MT - 0.125, self.width - 2 * self.MT - 0.0625, "1L")
                    self.listParts.append(self.shelf)
                self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-")
                self.listParts.append(self.back)

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
        tempNum = numB[givenNumber].get()
        tempNum = tempNum + 1
        numB[givenNumber].set(tempNum)
    else:
        tempNum = 0
        numB[givenNumber].set(0)
    newLabel = Label(frameBase,text=f'{tempNum}').grid(row=givenNumber, column=2, padx=5, sticky=E)

def decB(givenNumber, givenRow):
    if itemsB[givenRow].get() == 1:
        if givenNumber <= 1:
            print("count will be negative")
        else:
            givenNumber = givenNumber - 1
            newLabel = Label(frameBase, text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
            numB[givenRow].set(givenNumber)

def incB(givenNumber, givenRow):
    if itemsB[givenRow].get() == 1:
        givenNumber = givenNumber + 1
        newLabel = Label(frameBase,text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
        numB[givenRow].set(givenNumber)

#FOR INCREASING W
def checkedW(givenNumber):
    if itemsW[givenNumber].get() == 1:
        tempNum = numW[givenNumber].get()
        tempNum = tempNum + 1
        numW[givenNumber].set(tempNum)
    else:
        tempNum = 0
        numW[givenNumber].set(0)
    newLabel = Label(frameWall,text=f'{tempNum}').grid(row=givenNumber, column=2, padx=5, sticky=E)

def decW(givenNumber, givenRow):
    if itemsW[givenRow].get() == 1:
        if givenNumber <= 1:
            print("count will be negative")
        else:
            givenNumber = givenNumber - 1
            newLabel = Label(frameWall, text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
            numW[givenRow].set(givenNumber)

def incW(givenNumber, givenRow):
    if itemsW[givenRow].get() == 1:
        givenNumber = givenNumber + 1
        newLabel = Label(frameWall,text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
        numW[givenRow].set(givenNumber)

#FOR INCREASING T
def checkedT(givenNumber):
    if itemsT[givenNumber].get() == 1:
        tempNum = numT[givenNumber].get()
        tempNum = tempNum + 1
        numT[givenNumber].set(tempNum)
    else:
        tempNum = 0
        numT[givenNumber].set(0)
    newLabel = Label(frameTall,text=f'{tempNum}').grid(row=givenNumber, column=2, padx=5, sticky=E)

def decT(givenNumber, givenRow):
    if itemsT[givenRow].get() == 1:
        if givenNumber <= 1:
            print("count will be negative")
        else:
            givenNumber = givenNumber - 1
            newLabel = Label(frameTall, text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
            numT[givenRow].set(givenNumber)

def incT(givenNumber, givenRow):
    if itemsT[givenRow].get() == 1:
        givenNumber = givenNumber + 1
        newLabel = Label(frameTall,text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
        numT[givenRow].set(givenNumber)

#FOR INCREASING V
def checkedV(givenNumber):
    if itemsV[givenNumber].get() == 1:
        tempNum = numV[givenNumber].get()
        tempNum = tempNum + 1
        numV[givenNumber].set(tempNum)
    else:
        tempNum = 0
        numV[givenNumber].set(0)
    newLabel = Label(frameVanity,text=f'{tempNum}').grid(row=givenNumber, column=2, padx=5, sticky=E)

def decV(givenNumber, givenRow):
    if itemsV[givenRow].get() == 1:
        if givenNumber <= 1:
            print("count will be negative")
        else:
            givenNumber = givenNumber - 1
            newLabel = Label(frameVanity, text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
            numV[givenRow].set(givenNumber)

def incV(givenNumber, givenRow):
    if itemsV[givenRow].get() == 1:
        givenNumber = givenNumber + 1
        newLabel = Label(frameVanity,text=f'{givenNumber}').grid(row=givenRow, column=2, padx=5, sticky=E)
        numV[givenRow].set(givenNumber)

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
main_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=main_frame, anchor="nw")

#Workspace Scrollbar
workspace_backFrame = LabelFrame(main_frame, text="Workspace", padx=0, pady=5)
workspace_backFrame.grid(row=1, rowspan = 5, column=1, columnspan=18, padx=0, pady=5, sticky=W+E+N+S)
workspace_canvas = Canvas(workspace_backFrame)
workspace_canvas.pack(side=LEFT, fill=BOTH, expand=1)
workspace_scrollbar = ttk.Scrollbar(workspace_backFrame, orient=VERTICAL, command=workspace_canvas.yview)
workspace_scrollbar.pack(side=RIGHT, fill=Y)
workspace_canvas.configure(yscrollcommand=workspace_scrollbar.set)
workspace_canvas.bind('<Configure>', lambda e: workspace_canvas.configure(scrollregion = workspace_canvas.bbox("all")))
workspace_frame = Frame(workspace_canvas)
workspace_canvas.create_window((0,0), window=workspace_frame, anchor="nw")

for newthing in range(40):
    Label(workspace_frame, text=".").grid(row = newthing+30, column = 0, pady=10, padx=10)

#Cutlist Scrollbar
cutlist_backFrame = LabelFrame(main_frame, text="Cutlist", padx=5, pady=5)
cutlist_backFrame.grid(row=1, rowspan = 5, column=21, columnspan=5, padx=5, pady=5, sticky=W+E+N+S)
cutlist_canvas = Canvas(cutlist_backFrame)
cutlist_canvas.pack(side=LEFT, fill=BOTH, expand=1)
cutlist_scrollbar = ttk.Scrollbar(cutlist_backFrame, orient=VERTICAL, command=cutlist_canvas.yview)
cutlist_scrollbar.pack(side=RIGHT, fill=Y)
cutlist_canvas.configure(yscrollcommand=cutlist_scrollbar.set)
cutlist_canvas.bind('<Configure>', lambda e: cutlist_canvas.configure(scrollregion = cutlist_canvas.bbox("all")))
cutlist_frame = Frame(cutlist_canvas)
cutlist_canvas.create_window((0,0), window=cutlist_frame, anchor="nw")

for newthing in range(40):
    Label(cutlist_frame, text=".").grid(row = newthing+30, column = 0, pady=10, padx=10)

class Send:
    def __init__(self, parent, givenList):
        self.spec = ["Quantity", "Name", "Length", "Width", "Tape"]
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
    def __init__(self, parent, givenRow, givenIndex, givenString):
        self.index = givenIndex
        self.category = givenString
        self.widthLabel = Label(parent, text="Width: ", padx=10, pady=5)
        self.widthLabel.grid(row = givenRow, column=1)
        self.widthEntry = Entry(parent, width = 10)
        self.widthEntry.grid(row = givenRow, column=2)
        self.heightLabel = Label(parent, text="height: ", padx=10, pady=5, anchor=E)
        self.heightLabel.grid(row = givenRow, column=3)
        self.heightEntry = Entry(parent, width = 10)
        self.heightEntry.grid(row = givenRow, column=4)
        self.heightEntry.insert(0, 34.75)
        self.depthLabel = Label(parent, text="Depth: ", padx=10, pady=5, anchor=E)
        self.depthLabel.grid(row = givenRow, column=5)
        self.depthEntry = Entry(parent, width = 10)
        self.depthEntry.grid(row = givenRow, column=6)
        self.depthEntry.insert(0, 23.75)
        self.MTLabel1 = Label(parent, text = "M.T. : " + str(materialThickness), padx = 10, pady = 5, anchor = E)
        self.MTLabel1.grid(row = givenRow + 1, column=0)
        self.shelfLabel = Label(parent, text = "Shelves #: ", padx=10, pady=5, anchor=E)
        self.shelfLabel.grid(row = givenRow + 1, column=1)
        self.shelfEntry = Entry(parent, width = 10)
        self.shelfEntry.grid(row = givenRow + 1, column=2)

        self.secSideLabel = Label(parent, text = "Sec Side: ", padx=10, pady=5, anchor=E)
        self.secSideLabel.grid(row = givenRow + 1, column=3)
        self.secSideEntry = Entry(parent, width = 10)
        self.secSideEntry.grid(row = givenRow + 1, column=4)

        self.kickLabel = Label(parent, text = "Toe Kick: ", padx=10, pady=5, anchor=E)
        self.kickLabel.grid(row = givenRow + 1, column=5)
        self.kickEntry = Entry(parent, width = 10)
        self.kickEntry.grid(row = givenRow + 1, column=6)

        self.sendButton = Button(parent, text=">", command=self.send)
        self.sendButton.grid(row = givenRow, column=7, padx=10, pady=5)

    def send(self):
        self.width = float(self.widthEntry.get())
        self.height = float(self.heightEntry.get())
        self.depth = float(self.depthEntry.get())
        self.shelfQty = int(self.shelfEntry.get())
        self.secSide = int(self.secSideEntry.get())
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
            cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
            listB.append(cabinet)
            for self.obj in listB:
                print(self.obj.name, self.obj.width, self.obj.height, self.obj.depth, sep=" ")
            showOutputs = Send(baseCutlist, listB)
        if self.category == "Wall":
            self.text = textW[self.index]
            cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
            listW.append(cabinet)
            for self.obj in listW:
                print(self.obj.name, self.obj.width, self.obj.height, self.obj.depth, sep=" ")
            showOutputs = Send(wallCutlist, listW)
        if self.category == "Tall":
            self.text = textT[self.index]
            cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
            listT.append(cabinet)
            for self.obj in listT:
                print(self.obj.name, self.obj.width, self.obj.height, self.obj.depth, sep=" ")
            showOutputs = Send(tallCutlist, listT)
        if self.category == "Vanity":
            self.text = textV[self.index]
            cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
            listV.append(cabinet)
            for self.obj in listV:
                print(self.obj.name, self.obj.width, self.obj.height, self.obj.depth, sep=" ")
            showOutputs = Send(vanityCutlist, listV)
        if self.category == "Custom":
            self.text = "Custom Cabinet"
            cabinet = Cabinet(self.category, self.text, self.width, self.height, self.depth, self.shelfQty, self.secSide, self.kick, materialThickness)
            listC.append(cabinet)
            for self.obj in listC:
                print(self.obj.name, self.obj.width, self.obj.height, self.obj.depth, sep=" ")
            showOutputs = Send(customCutlist, listC)

def show():
    baseBinary = LabelFrame(workspace_frame, text="Base", padx=5, pady=5)
    baseBinary.grid(row=0, column=0, padx=5, pady=5, sticky=W+E)

    i = 0
    j = 0

    for item in itemsB:
        if item.get() == 1:
            amountB = numB[i].get()
            for count in range(amountB):
                itemLabelB = Label(baseBinary, text=textB[i], font = ('Helvetiva', 10, 'bold'), padx=7, pady=5).grid(row=j, column=0, sticky=W+E)

                receiveInputsB = Show(baseBinary, j, i, "Base")

                j = j + 2
        i = i + 1

    wallBinary = LabelFrame(workspace_frame, text="Wall", padx=5, pady=5)
    wallBinary.grid(row=1, column=0, padx=5, pady=5, sticky=W+E)

    i = 0
    j = 0
    for item in itemsW:
        if item.get() == 1:
            amountW = numW[i].get()
            for count in range(amountW):
                itemLabelW = Label(wallBinary, text=textW[i], font = ('Helvetiva', 10, 'bold'), padx=7, pady=5).grid(row=j, column=0, sticky=W+E)

                receiveInputsW = Show(wallBinary, j, i, "Wall")

                j = j + 2
        i = i + 1

    tallBinary = LabelFrame(workspace_frame, text="Tall", padx=5, pady=5)
    tallBinary.grid(row=2, column=0, padx=5, pady=5, sticky=W+E)

    i = 0
    j = 0
    for item in itemsT:
        if item.get() == 1:
            amountT = numT[i].get()
            for count in range(amountT):
                itemLabelT = Label(tallBinary, text=textT[i], font = ('Helvetiva', 10, 'bold'), padx=7, pady=5).grid(row=j, column=0, sticky=W+E)

                receiveInputsT = Show(tallBinary, j, i, "Tall")

                j = j + 2
        i = i + 1

    vanityBinary = LabelFrame(workspace_frame, text="Vanity", padx=5, pady=5)
    vanityBinary.grid(row=3, column=0, padx=5, pady=5, sticky=W+E)

    i = 0
    j = 0
    for item in itemsV:
        if item.get() == 1:
            amountV = numV[i].get()
            for count in range(amountV):
                itemLabelV = Label(vanityBinary, text=textV[i], font = ('Helvetiva', 10, 'bold'), padx=7, pady=5).grid(row=j, column=0, sticky=W+E)

                receiveInputsV = Show(vanityBinary, j, i, "Vanity")

                j = j + 2
        i = i + 1

    customBinary = LabelFrame(workspace_frame, text="Custom", padx=5, pady=5)
    customBinary.grid(row=3, column=0, padx=5, pady=5, sticky=W+E)

    i = 0
    j = 0
    amountC = numCustom.get()
    for count in range(amountC):
        itemLabelC = Label(customBinary, text = "Custom" + str(i + 1), font = ('Helvetiva', 10, 'bold'), padx=7, pady=5).grid(row=j, column=0, sticky=W+E)

        receiveInputsC = Show(customBinary, j, i, "Custom")

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
# customB = IntVar()

fulldoorW = IntVar()
drawersW = IntVar()
microwaveW = IntVar()
# customW = IntVar()

fulldoorT = IntVar()
ovenT = IntVar()
# customT = IntVar()

fulldoorV = IntVar()
drawersV = IntVar()
linentowerV = IntVar()

custom = IntVar()
numCustom = IntVar()
numCustom.set(0)

numFullB = IntVar()
numFullB.set(0)
numDraB = IntVar()
numDraB.set(0)
num90B = IntVar()
num90B.set(0)
numDiaB = IntVar()
numDiaB.set(0)
# numCustB = IntVar()
# numCustB.set(0)

numFullW = IntVar()
numFullW.set(0)
numDraW = IntVar()
numDraW.set(0)
numMicW = IntVar()
numMicW.set(0)
# numCustW = IntVar()
# numCustW.set(0)

numFullT = IntVar()
numFullT.set(0)
numOvenT = IntVar()
numOvenT.set(0)
# numCustT = IntVar()
# numCustT.set(0)

numFullV = IntVar()
numFullV.set(0)
numDraV = IntVar()
numDraV.set(0)
numLinV = IntVar()
numLinV.set(0)
# numCustV = IntVar()
# numCustV.set(0)

materialThickness = 0.625
toekick = 4.5

newBase = Cabinet("null", "null", 0, 0, 0, 0, 0, 0, 0)

itemsB = [fulldoorB, drawersB, corner90B, cornerdiagonalB]
textB = ["Full Door", "Drawers", "Corner 90", "Corner Diagonal"]
numB = [numFullB, numDraB, num90B, numDiaB]
itemsW = [fulldoorW, drawersW, microwaveW]
textW = ["Full Door", "Corner 90", "Microwave Slot"]
numW = [numFullW, numDraW, numMicW]
itemsT = [fulldoorT, ovenT]
textT = ["Full Door", "Oven Slot"]
numT = [numFullT, numOvenT]
itemsV = [fulldoorV, drawersV, linentowerV]
textV = ["Full Door", "Drawers", "Linen Tower"]
numV = [numFullV, numDraV, numLinV]

#Base Frame
frameBase = LabelFrame(main_frame, text="Base", padx=5, pady=5)
frameBase.grid(row=1, column=0, padx=5, pady=5, sticky=W+E)
i = 0
for item in textB:
    newBL = Label(frameBase, text="0").grid(row=i, column=2, padx=5, sticky=E)
    i = i + 1

checkFullB = Checkbutton(frameBase, text=textB[0], variable = itemsB[0], onvalue=1, offvalue=0, command = lambda: checkedB(0)).grid(row=0, column=0, sticky=W)
check3DB = Checkbutton(frameBase, text=textB[1], variable = itemsB[1], onvalue=1, offvalue=0, command = lambda: checkedB(1)).grid(row=1, column=0, sticky=W)
check90B = Checkbutton(frameBase, text=textB[2], variable = itemsB[2], onvalue=1, offvalue=0, command = lambda: checkedB(2)).grid(row=2, column=0, sticky=W)
checkDiaB = Checkbutton(frameBase, text=textB[3], variable = itemsB[3], onvalue=1, offvalue=0, command = lambda: checkedB(3)).grid(row=3, column=0, sticky=W)
# checkCustB = Checkbutton(frameBase, text=textB[4], variable = itemsB[4], onvalue=1, offvalue=0, command = lambda: checkedB(4)).grid(row=4, column=0, sticky=W)

decFullB = Button(frameBase, text="-", command = lambda: decB(numB[0].get(), 0)).grid(row=0, column=1, sticky=E)
dec3DB = Button(frameBase, text="-", command = lambda: decB(numB[1].get(), 1)).grid(row=1, column=1, sticky=E)
dec90B = Button(frameBase, text="-", command = lambda: decB(numB[2].get(), 2)).grid(row=2, column=1, sticky=E)
decDiaB = Button(frameBase, text="-", command = lambda: decB(numB[3].get(), 3)).grid(row=3, column=1, sticky=E)
# decCustB = Button(frameBase, text="-", command = lambda: decB(numB[4].get(), 4)).grid(row=4, column=1, sticky=E)

incFullB = Button(frameBase, text="+", command = lambda: incB(numB[0].get(), 0)).grid(row=0, column=3, sticky=E)
inc3DB = Button(frameBase, text="+", command = lambda: incB(numB[1].get(), 1)).grid(row=1, column=3, sticky=E)
inc90B = Button(frameBase, text="+", command = lambda: incB(numB[2].get(), 2)).grid(row=2, column=3, sticky=E)
incDiaB = Button(frameBase, text="+", command = lambda: incB(numB[3].get(), 3)).grid(row=3, column=3, sticky=E)
# incCustB = Button(frameBase, text="+", command = lambda: incB(numB[4].get(), 4)).grid(row=4, column=3, sticky=E)

#Wall Frame
frameWall = LabelFrame(main_frame, text="Wall", padx=5, pady=5)
frameWall.grid(row=2, column=0, padx=5, pady=5, sticky=W+E)
i = 0
for item in textW:
    # wallCheckbutton = Checkbutton(frameWall, text=item, variable = itemsW[i], onvalue=1, offvalue=0).grid(row=i, column=0, sticky=W)
    newWL = Label(frameWall, text="0").grid(row=i, column=2, padx=5, sticky=E)
    # newB = Button(frameWall, text=">", command = lambda: clicked(numW[i].get())).grid(row=0, column=2, sticky=E)
    i = i + 1

checkFullW = Checkbutton(frameWall, text=textW[0], variable = itemsW[0], onvalue=1, offvalue=0, command = lambda: checkedW(0)).grid(row=0, column=0, sticky=W)
checkDraW = Checkbutton(frameWall, text=textW[1], variable = itemsW[1], onvalue=1, offvalue=0, command = lambda: checkedW(1)).grid(row=1, column=0, sticky=W)
checkMicW = Checkbutton(frameWall, text=textW[2], variable = itemsW[2], onvalue=1, offvalue=0, command = lambda: checkedW(2)).grid(row=2, column=0, sticky=W)
# checkCustW = Checkbutton(frameWall, text=textW[3], variable = itemsW[3], onvalue=1, offvalue=0, command = lambda: checkedW(3)).grid(row=3, column=0, sticky=W)

decFullW = Button(frameWall, text="-", command = lambda: decW(numW[0].get(), 0)).grid(row=0, column=1, sticky=W+E)
decDraW = Button(frameWall, text="-", command = lambda: decW(numW[1].get(), 1)).grid(row=1, column=1, sticky=W+E)
decMicW = Button(frameWall, text="-", command = lambda: decW(numW[2].get(), 2)).grid(row=2, column=1, sticky=W+E)
# decCustW = Button(frameWall, text="-", command = lambda: decW(numW[3].get(), 3)).grid(row=3, column=1, sticky=W+E)

incFullW = Button(frameWall, text="+", command = lambda: incW(numW[0].get(), 0)).grid(row=0, column=3, sticky=W+E)
incDraW = Button(frameWall, text="+", command = lambda: incW(numW[1].get(), 1)).grid(row=1, column=3, sticky=W+E)
incMicW = Button(frameWall, text="+", command = lambda: incW(numW[2].get(), 2)).grid(row=2, column=3, sticky=W+E)
# incCustW = Button(frameWall, text="+", command = lambda: incW(numW[3].get(), 3)).grid(row=3, column=3, sticky=W+E)

#Tall Frame
frameTall = LabelFrame(main_frame, text="Tall", padx=5, pady=5)
frameTall.grid(row=3, column=0, padx=5, pady=5, sticky=W+E)
i = 0
for item in textT:
    # tallCheckbutton = Checkbutton(frameTall, text=item, variable = itemsT[i], onvalue=1, offvalue=0).grid(row=i, column=0, sticky=W)
    newTL = Label(frameTall, text="0").grid(row=i, column=2, padx=5, sticky=E)
    i = i + 1

checkFullT = Checkbutton(frameTall, text=textT[0], variable = itemsT[0], onvalue=1, offvalue=0, command = lambda: checkedT(0)).grid(row=0, column=0, sticky=W)
checkOvenT = Checkbutton(frameTall, text=textT[1], variable = itemsT[1], onvalue=1, offvalue=0, command = lambda: checkedT(1)).grid(row=1, column=0, sticky=W)
# checkCustT = Checkbutton(frameTall, text=textT[2], variable = itemsT[2], onvalue=1, offvalue=0, command = lambda: checkedT(2)).grid(row=2, column=0, sticky=W)

decFullT = Button(frameTall, text="-", command = lambda: decT(numT[0].get(), 0)).grid(row=0, column=1, sticky=E)
decOvenT = Button(frameTall, text="-", command = lambda: decT(numT[1].get(), 1)).grid(row=1, column=1, sticky=E)
# decCustT = Button(frameTall, text="-", command = lambda: decT(numT[2].get(), 2)).grid(row=2, column=1, sticky=E)

incFullT = Button(frameTall, text="+", command = lambda: incT(numT[0].get(), 0)).grid(row=0, column=3, sticky=E)
incOvenT = Button(frameTall, text="+", command = lambda: incT(numT[1].get(), 1)).grid(row=1, column=3, sticky=E)
# incCustT = Button(frameTall, text="+", command = lambda: incT(numT[2].get(), 2)).grid(row=2, column=3, sticky=E)

#Vanity Frame
frameVanity = LabelFrame(main_frame, text="Vanity", padx=5, pady=5)
frameVanity.grid(row=4, column=0, padx=5, pady=5, sticky=W+E)
i = 0
for item in textV:
    # vanityCheckbutton = Checkbutton(frameVanity, text=item, variable = itemsV[i], onvalue=1, offvalue=0).grid(row=i, column=0, sticky=W)
    newVL = Label(frameVanity, text="0").grid(row=i, column=2, padx=5, sticky=E)
    i = i + 1

checkFullV = Checkbutton(frameVanity, text=textV[0], variable = itemsV[0], onvalue=1, offvalue=0, command = lambda: checkedV(0)).grid(row=0, column=0, sticky=W)
checkDraV = Checkbutton(frameVanity, text=textV[1], variable = itemsV[1], onvalue=1, offvalue=0, command = lambda: checkedV(1)).grid(row=1, column=0, sticky=W)
checkLinV = Checkbutton(frameVanity, text=textV[2], variable = itemsV[2], onvalue=1, offvalue=0, command = lambda: checkedV(2)).grid(row=2, column=0, sticky=W)
# checkCustV = Checkbutton(frameVanity, text=textV[3], variable = itemsV[3], onvalue=1, offvalue=0, command = lambda: checkedV(3)).grid(row=3, column=0, sticky=W)

decFullV = Button(frameVanity, text="-", command = lambda: decV(numV[0].get(), 0)).grid(row=0, column=1, sticky=E)
decDraV = Button(frameVanity, text="-", command = lambda: decV(numV[1].get(), 1)).grid(row=1, column=1, sticky=E)
decLinV = Button(frameVanity, text="-", command = lambda: decV(numV[2].get(), 2)).grid(row=2, column=1, sticky=E)
# decCustV = Button(frameVanity, text="-", command = lambda: decV(numV[3].get(), 3)).grid(row=3, column=1, sticky=E)

incFullV = Button(frameVanity, text="+", command = lambda: incV(numV[0].get(), 0)).grid(row=0, column=3, sticky=E)
incDraV = Button(frameVanity, text="+", command = lambda: incV(numV[1].get(), 1)).grid(row=1, column=3, sticky=E)
incLinV = Button(frameVanity, text="+", command = lambda: incV(numV[2].get(), 2)).grid(row=2, column=3, sticky=E)
# incCustV = Button(frameVanity, text="+", command = lambda: incV(numV[3].get(), 3)).grid(row=3, column=3, sticky=E)

#Custom Frame
frameCustom = LabelFrame(main_frame, text = "Custom", padx = 5, pady = 5)
frameCustom.grid(row=5, column=0, padx=5, pady=5, sticky=W+E)
checkCustom = Checkbutton(frameCustom, text="Custom Cabinet", variable = custom, onvalue=1, offvalue=0, command = lambda: checkedC()).grid(row=0, column=0, sticky=W)
numCustomLabel = Label(frameCustom, text="0").grid(row=0, column=2, padx=5, sticky=E)
decCustom = Button(frameCustom, text="-", command = lambda: decC(numCustom.get())).grid(row=0, column=1, sticky=E)
incCustom = Button(frameCustom, text="+", command = lambda: incC(numCustom.get())).grid(row=0, column=3, sticky=E)

submit_base_button = Button(main_frame, text="Submit", command=show).grid(row=6, column=0, sticky=W+E, pady=30)
submit_workspace_button = Button(main_frame, text="Generate Cutlist").grid(row=6, column=18, sticky=W+E, pady=30)

for dotthing in range(17):
    Label(main_frame, text="........ ").grid(row=7, column=dotthing)

root.mainloop()
