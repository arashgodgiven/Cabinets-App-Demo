from tkinter import *
# from tkinter import messagebox, filedialog
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font
from fpdf import FPDF
from datetime import date
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter import Scrollbar, Canvas
from tkinter import PhotoImage
import pickle
import ctypes
import datetime
import math


# Improve Graphics
ctypes.windll.shcore.SetProcessDpiAwareness(1)




#-------------------------------------------------- Classes for Cabinets --------------------------------------------------//
class Part:
    def __init__(self, qty, name, width, height, tape, drill, router):
        self.qty = qty
        self.name = name
        self.width = width
        self.height = height
        self.tape = tape
        self.drill = drill
        self.router = router

    def setQty(self, givenQty):
        self.qty = givenQty

class CabinetFullDoor: #15 ITEMS
    def __init__(self, category, name, count, width, height, depth, shelfQty, toeKick, sink, drill, router, materialThickness, materialType, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width = width
        self.height = height
        self.depth = depth
        self.shelfQty = shelfQty
        self.toeKick = toeKick
        self.sink = sink
        self.drill = drill
        self.router = router
        self.materialThickness = materialThickness
        self.materialType = materialType
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width) + ")"

        self.listParts = []

        if self.category == "Base":
            if self.name == "Full Door":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                self.bottom = Part(1, "Bottom", self.depth - self.materialThickness, self.width - 2 * self.materialThickness, "1S", False, False)
                self.listParts.append(self.bottom)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThickness, "-", False, False)  #TOEKICK -0.25
                self.listParts.append(self.kick)
                self.topStretcherFront = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.topStretcherFront)
                self.topStretcherBack = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.topStretcherBack)
                if self.shelfQty > 0:
                    self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThickness - 0.125, self.width - 2 * self.materialThickness - 0.0625, "1L", False, self.router)
                    self.listParts.append(self.shelf)

                if self.sink:
                    self.back = Part(2, "Back", self.width, "6", "1L", False, False)
                else:
                    if self.width >= 36:
                        self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", self.drill, False)
                    else:
                        self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", False, False)
                self.listParts.append(self.back)

        if self.category == "Vanity":
            if self.name == "Full Door":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                self.bottom = Part(1, "Bottom", self.depth - self.materialThickness, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.bottom)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThickness, "1L", False, False)
                # self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.kick)
                self.topStretcherFront = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.topStretcherFront)
                self.topStretcherBack = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.topStretcherBack)
                if self.shelfQty > 0:
                    self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThickness - 0.125, self.width - 2 * self.materialThickness - 0.0625, "1L", False, self.router)
                    self.listParts.append(self.shelf)

                if self.width >= 36:
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", self.drill, False)
                else:
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", False, False)
                self.listParts.append(self.back)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width, self.height, self.depth, self.shelfQty, self.toeKick, self.sink, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

    def setAttributes(self, attributes):
        self.category, self.name, self.count, self.width, self.height, self.depth, self.shelfQty, self.toeKick, self.sink, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus = attributes

class CabinetDrawers: #17 ITEMS
    def __init__(self, category, name, count, width, height, depth, drawerQty, drawerHeights, drawerDepth, toeKick, railType, drill, router, materialThickness, materialType, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width = width
        self.height = height
        self.depth = depth
        self.drawerQty = drawerQty
        self.drawerHeights = drawerHeights[:]
        self.drawerDepth = drawerDepth
        self.toeKick = toeKick
        self.railType = railType
        self.drill = drill
        self.router = router
        self.materialThickness = materialThickness
        self.materialType = materialType
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width) + ")"

        self.listParts = []

        self.railSpaceSides = 0
        self.railSpaceUnder = 0
        if self.railType == "Regular" or self.railType == "Side Mount" or self.railType == "P-2-O SM":
            self.railSpaceSides = 0.5
            self.railSpaceUnder = 0
        elif self.railType == "P-2-O UM" or self.railType == "Under Mount":
            self.railSpaceSides = 0.21875
            self.railSpaceUnder = 0.5

        if self.category == "Base":
            if name == "Drawers":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", self.drill, False)
                self.listParts.append(self.back)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.kick)

                self.tempDrawerHeights = self.drawerHeights[:]
                self.tempHeight = 0
                self.countedQty = 0
                self.partCount = 0

                self.tempHeight = self.tempDrawerHeights[0]
                while len(self.tempDrawerHeights) != 0:
                    if self.tempDrawerHeights[0] == self.tempHeight:
                        self.countedQty += 1
                        if len(self.tempDrawerHeights) == 1:
                            self.partCount += 1
                            self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThickness - self.railSpaceUnder, self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, "1L", False, False)
                            self.listParts.append(self.frontBack)
                            if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                            else:
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                            self.listParts.append(self.sides)
                        self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                    elif self.tempDrawerHeights[0] != self.tempHeight:
                        self.partCount += 1
                        self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThickness - self.railSpaceUnder, self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, "1L", False, False)
                        self.listParts.append(self.frontBack)
                        if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                            self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                        else:
                            self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                        self.listParts.append(self.sides)
                        self.countedQty = 1
                        self.tempHeight = self.tempDrawerHeights[0]

                        if len(self.tempDrawerHeights) == 1:
                            self.countedQty = 1
                            self.partCount += 1
                            self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempDrawerHeights[0] - self.materialThickness - self.railSpaceUnder, self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, "1L", False, False)
                            self.listParts.append(self.frontBack)
                            if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth - 5/8, "1L", False, False)
                            else:
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth, "1L", False, False)
                            self.listParts.append(self.sides)

                        self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                self.drawerBottom = Part(self.drawerQty, "Drawer Bottom", self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, self.drawerDepth - self.materialThickness, "-", False, False)
                self.listParts.append(self.drawerBottom)

                self.topStretcherFront = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.topStretcherFront)
                self.topStretcherBack = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.topStretcherBack)
                self.bottom = Part(1, "Bottom", self.width - 2 * self.materialThickness, self.depth - self.materialThickness, "1S", False, self.router)
                self.listParts.append(self.bottom)

        if self.category == "Vanity":
            if name == "Drawers":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                if self.width >= 36:
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", self.drill, False)
                else:
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", False, False)
                self.listParts.append(self.back)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.kick)

                self.tempDrawerHeights = self.drawerHeights[:]
                print("length is: " + str(len(self.tempDrawerHeights)))
                for height in self.tempDrawerHeights:
                    print("got here: " + str(height))
                self.tempHeight = 0
                self.countedQty = 0
                self.partCount = 0

                self.tempHeight = self.tempDrawerHeights[0]
                while len(self.tempDrawerHeights) != 0:
                    if self.tempDrawerHeights[0] == self.tempHeight:
                        self.countedQty += 1
                        if len(self.tempDrawerHeights) == 1:
                            self.partCount += 1
                            self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThickness - self.railSpaceUnder, self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, "1L", False, False)
                            self.listParts.append(self.frontBack)
                            if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                            else:
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                            self.listParts.append(self.sides)
                        self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                    elif self.tempDrawerHeights[0] != self.tempHeight:
                        self.partCount += 1
                        self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThickness - self.railSpaceUnder - 1.5, self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, "1L", False, False)
                        self.listParts.append(self.frontBack)
                        if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                            self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount),  self.tempHeight - 2 * self.materialThickness, self.drawerDepth - 5/8, "1L", False, False)
                        else:
                            self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount),  self.tempHeight - 2 * self.materialThickness, self.drawerDepth, "1L", False, False)
                        self.listParts.append(self.sides)
                        self.countedQty = 1
                        self.tempHeight = self.tempDrawerHeights[0]

                        if len(self.tempDrawerHeights) == 1:
                            self.countedQty = 1
                            self.partCount += 1
                            self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempDrawerHeights[0] - self.materialThickness - self.railSpaceUnder, self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, "1L", False, False)
                            self.listParts.append(self.frontBack)
                            if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth - 5/8, "1L", False, False)
                            else:
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth, "1L", False, False)
                            self.listParts.append(self.sides)

                        self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                self.drawerBottom = Part(self.drawerQty, "Drawer Bottom", self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, self.drawerDepth - self.materialThickness, "-", False, False)
                self.listParts.append(self.drawerBottom)

                self.topStretcherFront = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.topStretcherFront)
                self.topStretcherBack = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.topStretcherBack)
                self.bottom = Part(1, "Bottom", self.width - 2 * self.materialThickness, self.depth - self.materialThickness, "1S", False, self.router)
                self.listParts.append(self.bottom)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width, self.height, self.depth, self.drawerQty, self.drawerHeights, self.drawerDepth, self.toeKick, self.railType, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

    def setAttributes(self, attributes):
       self.category, self.name, self.count, self.width, self.height, self.depth, self.drawerQty, self.drawerHeights, self.drawerDepth, self.toeKick, self.railType, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus = attributes

class Cabinet1D1D: #17 ITEMS
    def __init__(self, category, name, count, width, height, depth, drawerHeight, drawerDepth, shelfQty, toeKick, railType, drill, router, materialThickness, materialType, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width = width
        self.height = height
        self.depth = depth
        self.drawerHeight = drawerHeight
        self.drawerDepth = drawerDepth
        self.shelfQty = shelfQty
        self.toeKick = toeKick
        self.railType = railType
        self.drill = drill
        self.router = router
        self.materialThickness = materialThickness
        self.materialType = materialType
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width) + ")"

        self.listParts = []

        self.railSpaceSides = 0
        self.railSpaceUnder = 0
        if self.railType == "Regular" or self.railType == "Side Mount" or self.railType == "P-2-O SM":
            self.railSpaceSides = 0.5
            self.railSpaceUnder = 0
        elif self.railType == "P-2-O UM" or self.railType == "Under Mount":
            self.railSpaceSides = 0.21875
            self.railSpaceUnder = 0.5

        if self.category == "Base":
            if name == "1Door 1Drawer":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.kick)

                if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                    self.drawerSides = Part(2, "Drawer Sides", self.drawerHeight, self.drawerDepth - 5/8, "1L", False, False)
                else:
                    self.drawerSides = Part(2, "Drawer Sides", self.drawerHeight, self.drawerDepth, "1L", False, False)
                self.listParts.append(self.drawerSides)

                self.drawerFrontBack = Part(2, "Front & Back", self.drawerHeight - self.materialThickness - self.railSpaceUnder, self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, "1L", False, False)
                self.listParts.append(self.drawerFrontBack)

                self.drawerBottom = Part(1, "Drawer Bottom", self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, self.drawerDepth - self.materialThickness, "-", False, False)
                self.listParts.append(self.drawerBottom)

                self.topStretcherFront = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.topStretcherFront)
                self.topStretcherBack = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.topStretcherBack)
                if self.shelfQty > 0:
                    self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThickness - 0.125, self.width - 2 * self.materialThickness - 0.0625, "1L", False, self.router)
                    self.listParts.append(self.shelf)

                if self.width >= 36:
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", self.drill, False)
                else:
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", False, False)
                self.listParts.append(self.back)
                self.bottom = Part(1, "Bottom", self.width - 2 * self.materialThickness, self.depth - self.materialThickness, "1S", False, False)
                self.listParts.append(self.bottom)

        if self.category == "Vanity":
            if name == "1Door 1Drawer":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.kick)

                if self.railType == "P-2-O UM" or self.railType == "Under Mount":
                    self.drawerSides = Part(2, "Drawer Sides", self.drawerHeight, self.drawerDepth - 5/8, "1L", False, False)
                else:
                    self.drawerSides = Part(2, "Drawer Sides", self.drawerHeight, self.drawerDepth, "1L", False, False)
                self.listParts.append(self.drawerSides)

                self.drawerFrontBack = Part(2, "Front & Back", self.drawerHeight - self.materialThickness - self.railSpaceUnder, self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, "1L", False, False)
                self.listParts.append(self.drawerFrontBack)

                self.drawerBottom = Part(1, "Drawer Bottom", self.width - 4 * self.materialThickness - 2 * self.railSpaceSides, self.drawerDepth - self.materialThickness, "-", False, False)
                self.listParts.append(self.drawerBottom)

                self.topStretcherFront = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.topStretcherFront)
                self.topStretcherBack = Part(1, "Top Stretcher", 4, self.width - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.topStretcherBack)
                if self.shelfQty > 0:
                    self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThickness - 0.125, self.width - 2 * self.materialThickness - 0.0625, "1L", False, self.router)
                    self.listParts.append(self.shelf)

                if self.width >= 36:
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", self.drill, False)
                else:
                    self.back = Part(1, "Back", self.width, self.height - self.toeKick, "-", False, False)
                self.listParts.append(self.back)
                self.bottom = Part(1, "Bottom", self.width - 2 * self.materialThickness, self.depth - self.materialThickness, "1S", False, False)
                self.listParts.append(self.bottom)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width, self.height, self.depth, self.drawerHeight, self.drawerDepth, self.shelfQty, self.toeKick, self.railType, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

    def setAttributes(self, attributes):
        self.category, self.name, self.count, self.width, self.height, self.depth, self.drawerHeight, self.drawerDepth, self.shelfQty, self.toeKick, self.railType, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus = attributes

class CabinetCorner: #16 ITEMS
    def __init__(self, category, name, count, width1, width2, height, depth, shelfQty, fillerWidth, toeKick, drill, router, materialThickness, materialType, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width1 = width1 # Width Left
        self.width2 = width2 # Width Left
        self.height = height
        self.depth = depth
        self.shelfQty = shelfQty
        self.fillerWidth = fillerWidth
        self.toeKick = toeKick
        self.drill = drill
        self.router = router
        self.materialThickness = materialThickness
        self.materialType = materialType
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width1) + ")"

        self.listParts = []

        if self.category == "Base":
            if name == "Corner 90":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                self.deck = Part(2, "Deck", self.width2 - 2 * self.materialThickness, self.width1 - 2 * self.materialThickness, "1S", False, False) #1S 90°
                self.listParts.append(self.deck)
                self.kick1 = Part(1, "Kick#1", self.toeKick - 0.25, self.width2 - self.depth, "-", False, False)
                self.listParts.append(self.kick1)
                self.kick2 = Part(1, "Kick#2", self.toeKick - 0.25, self.width1 - self.depth + self.materialThickness, "-", False, False)
                self.listParts.append(self.kick2)
                self.shelf = Part(self.shelfQty, "Shelf", self.width2 - 2 * self.materialThickness - 0.0625, self.width1 - 2 * self.materialThickness - 0.0625, "1S", False, self.router) #1S 90°
                self.listParts.append(self.shelf)
                self.back = Part(1, "Back", "17.0695", self.height, "-", False, False)
                self.listParts.append(self.back)
                self.side1 = Part(1, "Side#1", self.width2 - 12 + 0.1875, self.height - self.toeKick, "-", self.drill, False)    #changesssss
                # self.side1 = Part(1, "Side#1", self.width2 - 12.06996, self.height - self.toeKick, "-", self.drill, False)    #changesssss
                self.listParts.append(self.side1)
                self.side2 = Part(1, "Side#2", self.width1 - 12 + 0.1875, self.height - self.toeKick, "-", self.drill, False)    #changesssss
                # self.side2 = Part(1, "Side#2", self.width1 - 12.06996, self.height - self.toeKick, "-", self.drill, False)    #changesssss
                self.listParts.append(self.side2)

            elif name == "Corner Diagonal":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                self.deck = Part(2, "Deck", self.width2 - 2 * self.materialThickness,  self.width1 - 2 * self.materialThickness, "1S 90°", False, False)
                self.listParts.append(self.deck)
                # self.kick1 = Part(1, "Kick#1", self.toeKick - 0.25, self.width2 - self.depth + 2.5, "-", False, False)
                # self.listParts.append(self.kick1)
                # self.kick2 = Part(1, "Kick#2", self.toeKick - 0.25, self.width1 - self.depth + 2.5 + self.materialThickness, "-", False, False)
                # self.listParts.append(self.kick2)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, round(math.sqrt((self.depth - self.width1)**2 + (self.depth - self.width2)**2), 5), "-", False, False)
                self.listParts.append(self.kick)
                self.shelf = Part(self.shelfQty, "Shelf", self.width2 - 2 * self.materialThickness - 0.0625, self.width1 - 2 * self.materialThickness - 0.0625, "1S 90°", False, self.router)
                self.listParts.append(self.shelf)
                self.back = Part(1, "Back", "17.0695", self.height, "-", False, False)
                self.listParts.append(self.back)
                self.side1 = Part(1, "Side#1", self.width2 - 12 + 0.1875, self.height - self.toeKick, "-", self.drill, False)
                # self.side1 = Part(1, "Side#1", self.width2 - 12.06996, self.height - self.toeKick, "-", self.drill, False)
                self.listParts.append(self.side1)
                self.side2 = Part(1, "Side#2", self.width1 - 12 + 0.1875, self.height - self.toeKick, "-", self.drill, False)
                # self.side2 = Part(1, "Side#2", self.width1 - 12.06996, self.height - self.toeKick, "-", self.drill, False)
                self.listParts.append(self.side2)

            elif name == "Corner Blind":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                self.bottom = Part(1, "Bottom", self.depth - self.materialThickness, self.width1 - 2 * self.materialThickness, "1S", False, self.router)
                self.listParts.append(self.bottom)
                self.kick = Part(1, "Kick", self.toeKick - 0.25, (self.width1/2) - 2 * self.materialThickness, "-", False, False)
                self.listParts.append(self.kick)
                if self.shelfQty > 0:
                    self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThickness - 0.125, self.width1 - 2 * self.materialThickness - 0.0625, "1L", False, self.router)
                    self.listParts.append(self.shelf)
                if self.width1 >= 36:
                    self.back = Part(1, "Back", self.width1, self.height - self.toeKick, "-", self.drill, False)
                else:
                    self.back = Part(1, "Back", self.width1, self.height - self.toeKick, "-", False, False)
                self.listParts.append(self.back)
                # if self.fillerWidth > 0:
                    # self.filler = Part(1, "Filler", self.fillerWidth, self.height - self.toeKick, "1L", False, False)
                    # self.listParts.append(self.filler)
                self.topStretcher = Part(2, "Top Stretcher", 4, self.width1 - 2 * self.materialThickness, "2L", False, False)
                self.listParts.append(self.topStretcher)
                self.backPanel = Part(1, "Blank Panel", (self.width1/2) - (self.fillerWidth/2), self.height - self.toeKick, "-", False, False)
                self.listParts.append(self.backPanel)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width1, self.width2, self.height, self.depth, self.shelfQty, self.fillerWidth, self.toeKick, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

class CabinetFullDoorWall: #14 ITEMS
    def __init__(self, category, name, count, width, height, depth, shelfQty, lightShelf, drill, router, materialThickness, materialType, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width = width
        self.height = height
        self.depth = depth
        self.shelfQty = shelfQty
        self.lightShelf = lightShelf
        self.drill = drill
        self.router = router
        self.materialThickness = materialThickness
        self.materialType = materialType
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width) + ")"

        self.listParts = []

        if self.category == "Wall":
            if self.name == "Full Door":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L + 2S", self.drill, False)
                self.listParts.append(self.gable)
                if self.lightShelf:
                    self.deck = Part(3, "Deck", self.depth - self.materialThickness, self.width - 2 * self.materialThickness, "1L", False, False)
                else:
                    self.deck = Part(2, "Deck", self.depth - self.materialThickness, self.width - 2 * self.materialThickness, "1L", False, False)
                self.listParts.append(self.deck)
                if self.shelfQty > 0:
                    self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThickness - 0.125, self.width - 2 * self.materialThickness - 0.0625, "1L", False, self.router)
                    self.listParts.append(self.shelf)

                if self.width >= 36:
                    self.back = Part(1, "Back", self.width, self.height, "2S", self.drill, False)
                else:
                    self.back = Part(1, "Back", self.width, self.height, "2S", False, False)
                self.listParts.append(self.back)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width, self.height, self.depth, self.shelfQty, self.lightShelf, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

    def setAttributes(self, attributes):
        self.category, self.name, self.count, self.width, self.height, self.depth, self.shelfQty, self.lightShelf, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus = attributes

class CabinetCornerWall: #15 ITEMS
    def __init__(self, category, name, count, width1, width2, height, depth, shelfQty, lightShelf, drill, router, materialThickness, materialType, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width1 = width1 # Width Left
        self.width2 = width2 # Width Left
        self.height = height
        self.depth = depth   # defaultt 11 3/4
        self.shelfQty = shelfQty
        self.lightShelf = lightShelf
        self.drill = drill
        self.router = router
        self.materialThickness = materialThickness
        self.materialType = materialType
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width1) + ")"

        self.listParts = []

        if self.category == "Wall":
            if self.name == "Corner 90": #No kick for Corner 90?
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                # self.side1 = Part(1, "Side#1", self.width2 - 12, self.height, "-", self.drill, False)
                self.side1 = Part(1, "Back#1", self.width2, self.height, "-", self.drill, False) # no more back
                self.listParts.append(self.side1)
                # self.side2 = Part(1, "Side#2", self.width1 - 12, self.height, "-", self.drill, False)
                self.side2 = Part(1, "Back#2", self.width1 - self.materialThickness, self.height, "-", self.drill, False)
                self.listParts.append(self.side2)
                if self.lightShelf:
                    self.deck = Part(3, "Deck", self.width2 - 2 * self.materialThickness, self.width2 - 2 * self.materialThickness, "1S", False, False) #1S 90°
                else:
                    self.deck = Part(2, "Deck", self.width2 - 2 * self.materialThickness, self.width2 - 2 * self.materialThickness, "1S", False, False)
                self.listParts.append(self.deck)
                self.shelf = Part(self.shelfQty, "Shelf", self.width2 - 2 * self.materialThickness - 0.0625, self.width1 - 2 * self.materialThickness - 0.0625, "1S", False, self.router) #1S 90°
                self.listParts.append(self.shelf)
                # self.back = Part(1, "Back", "18", self.height, "-", False, False)
                # self.listParts.append(self.back)

            elif self.name == "Corner Diagonal":
                self.gable = Part(2, "Gable", self.depth - self.materialThickness, self.height, "1L", self.drill, False)
                self.listParts.append(self.gable)
                # self.side1 = Part(1, "Side#1", self.width2 - 12 - self.materialThickness - 0.25, self.height, "-", self.drill, False)
                self.side1 = Part(1, "Back#1", self.width2, self.height, "-", self.drill, False)
                self.listParts.append(self.side1)
                # self.side2 = Part(1, "Side#2", self.width1 - 12 - self.materialThickness - 0.25, self.height, "-", self.drill, False)
                self.side2 = Part(1, "Back#2", self.width1 - self.materialThickness, self.height, "-", self.drill, False)
                self.listParts.append(self.side2)
                if self.lightShelf:
                    self.deck = Part(3, "Deck", self.width2 - 2 * self.materialThickness, self.width2 - 2 * self.materialThickness, "1S 90°", False, False)
                else:
                    self.deck = Part(2, "Deck", self.width2 - 2 * self.materialThickness, self.width2 - 2 * self.materialThickness, "1S 90°", False, False)
                self.listParts.append(self.deck)
                self.shelf = Part(self.shelfQty, "Shelf", self.width2 - 2 * self.materialThickness - 0.0625, self.width1 - 2 * self.materialThickness - 0.0625, "1S 90°", False, self.router)
                self.listParts.append(self.shelf)
                # self.back = Part(1, "Back", "18", self.height, "-", False, False)
                # self.listParts.append(self.back)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width1, self.width2, self.height, self.depth, self.shelfQty, self.lightShelf, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

    def setAttributes(self, attributes):
        self.category, self.name, self.count, self.width1, self.width2, self.height, self.depth, self.shelfQty, self.lightShelf, self.drill, self.router, self.materialThickness, self.materialType, self.editable, self.completionStatus = attributes

class CabinetMicrowaveSlot: #19 ITEMS
    def __init__(self, category, name, count, width, heightTop, heightBottom, depthTop, depthBottom, shelfQty, twoPiece, lightShelf, drill, router, materialThicknessTop, materialThicknessBottom, materialTypeTop, materialTypeBottom, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width = width
        self.heightTop = heightTop
        self.heightBottom = heightBottom
        self.depthTop = depthTop
        self.depthBottom = depthBottom
        self.shelfQty = shelfQty
        self.twoPiece = twoPiece
        self.lightShelf = lightShelf
        self.drill = drill
        self.router = router
        self.materialThicknessTop = materialThicknessTop
        self.materialThicknessBottom = materialThicknessBottom
        self.materialTypeTop = materialTypeTop
        self.materialTypeBottom = materialTypeBottom
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width) + ")"   # lightshelf - 1/16

        self.listParts = []

        if self.category == "Wall":
            if self.name == "Microwave Slot":
                if self.heightBottom == 0 and self.depthBottom == 0:
                    self.gable = Part(2, "Gable", self.depthTop - 0.625, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gable)
                    if self.lightShelf:
                        self.deck = Part(3, "Deck", self.depthTop - 0.625, self.width - 2 * 0.625, "1L", False, self.router)
                    else:
                        self.deck = Part(2, "Deck", self.depthTop - 0.625, self.width - 2 * 0.625, "1L", False, self.router)
                    self.listParts.append(self.deck)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depthTop -0.625 - 0.125, self.width - 2 * 0.625- 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)

                    if self.width >= 36:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", False, False)
                    self.listParts.append(self.back)
                else:
                    self.gableBottom = Part(2, "Gable Bottom", self.depthBottom - self.materialThicknessBottom, self.heightBottom, "1L", self.drill, False)
                    self.listParts.append(self.gableBottom)
                    self.gableTop = Part(2, "Gable Top", self.depthTop - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gableTop)

                    if self.lightShelf:
                        self.deckTop = Part(3, "Deck-Top", self.depthTop - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    else:
                        self.deckTop = Part(2, "Deck-Top", self.depthTop - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.deckTop)

                    if self.lightShelf:
                        self.deckBottom = Part(3, "Deck-Bottom", self.depthBottom - self.materialThicknessBottom, self.width - 2 * self.materialThicknessBottom, "1S", False, self.router)
                    else:
                        self.deckBottom = Part(2, "Deck-Bottom", self.depthBottom - self.materialThicknessBottom, self.width - 2 * self.materialThicknessBottom, "1S", False, self.router)
                    self.listParts.append(self.deckBottom)

                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depthTop - self.materialThicknessTop - 0.125, self.width - 2 * self.materialThicknessTop - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)

                    if self.width >= 36:
                        self.backBottom = Part(1, "Back Bottom", self.width, self.heightBottom, "-", self.drill, False)
                    else:
                        self.backBottom = Part(1, "Back Bottom", self.width, self.heightBottom, "-", False, False)
                    self.listParts.append(self.backBottom)

                    if self.width >= 36:
                        self.backTop = Part(1, "Back Top", self.width, self.heightTop, "-", False, False)
                    else:
                        self.backTop = Part(1, "Back Top", self.width, self.heightTop, "-", self.drill, False)
                    self.listParts.append(self.backTop)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width, self.heightTop, self.heightBottom, self.depthTop, self.depthBottom, self.shelfQty, self.twoPiece, self.lightShelf, self.drill, self.router, self.materialThicknessTop, self.materialThicknessBottom, self.materialTypeTop, self.materialTypeBottom, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

    def setAttributes(self, attributes):
        self.category, self.name, self.count, self.width, self.heightBottom, self.heightTop, self.depthBottom, self.depthTop, self.shelfQty, self.twoPiece, self.lightShelf, self.drill, self.router, self.materialThicknessTop, self.materialThicknessBottom, self.materialTypeTop, self.materialTypeBottom, self.editable, self.completionStatus = attributes

class CabinetTall: #18 ITEMS
    def __init__(self, category, name, count, width, heightTop, heightBottom, depth, shelfQty, toeKick, twoPiece, drill, router, materialThicknessTop, materialThicknessBottom, materialTypeTop, materialTypeBottom, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width = width
        self.heightTop = heightTop
        self.heightBottom = heightBottom
        self.depth = depth
        self.shelfQty = shelfQty
        self.toeKick = toeKick
        self.twoPiece = twoPiece
        self.drill = drill
        self.router = router
        self.materialThicknessTop = materialThicknessTop
        self.materialThicknessBottom = materialThicknessBottom
        self.materialTypeTop = materialTypeTop
        self.materialTypeBottom = materialTypeBottom
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width) + ")"

        self.listParts = []

        if self.category == "Tall":
            if self.name == "Full Door":
                if self.heightBottom == 0:
                    self.gable = Part(2, "Gable", self.depth - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gable)
                    self.bottom = Part(2, "Bottom",  self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.bottom)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessTop, "-", False, False)
                    self.listParts.append(self.kick)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThicknessTop - 0.125, self.width - 2 * self.materialThicknessTop - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)

                    if self.width >= 36:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", False, False)
                    self.listParts.append(self.back)
                else:
                    self.gableBottom = Part(2, "Gable Bottom", self.depth - self.materialThicknessBottom, self.heightBottom, "1L", self.drill, False)
                    self.listParts.append(self.gableBottom)
                    self.gableTop = Part(2, "Gable Top", self.depth - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gableTop)
                    self.lowerBottom = Part(2, "Lower Bottom",  self.depth - self.materialThicknessBottom, self.width - 2 * self.materialThicknessBottom, "1S", False, False)
                    self.listParts.append(self.lowerBottom)
                    self.upperBottom = Part(2, "Upper Bottom",  self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, False)
                    self.listParts.append(self.upperBottom)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessBottom, "-", False, False)
                    self.listParts.append(self.kick)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThicknessTop - 0.125, self.width - 2 * self.materialThicknessTop - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)
                    if self.width >= 36:
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", self.drill, False)
                        self.backLower = Part(1, "Back Lower", self.width, self.heightBottom - self.toeKick, "-", self.drill, False)
                    else:
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", False, False)
                        self.backLower = Part(1, "Back Lower", self.width, self.heightBottom - self.toeKick, "-", False, False)
                    self.listParts.append(self.backUpper)
                    self.listParts.append(self.backLower)

            if self.name == "Oven Slot":
                if self.heightBottom == 0:
                    self.gable = Part(2, "Gable", self.depth - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gable)
                    self.bottom = Part(2, "Bottom",  self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.bottom)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThicknessTop - 0.125, self.width - 2 * self.materialThicknessTop - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)

                    if self.width >= 36:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", False, False)         #Might be: self.heightTop - OVEN HEIGHT, MIGHT HAVE TO ASK FOR OVEN HEIGHT**
                    self.listParts.append(self.back)
                    self.backPieceOven = Part(2, "Oven Slot Back", self.width, "6", "-", False, False)
                    self.listParts.append(self.backPieceOven)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessTop, "-", False, False)
                    self.listParts.append(self.kick)

                else:
                    self.gableBottom = Part(2, "Gable Bottom", self.depth - self.materialThicknessBottom, self.heightBottom, "1L", self.drill, False)
                    self.listParts.append(self.gableBottom)
                    self.gableTop = Part(2, "Gable Top", self.depth - self.materialThicknessBottom, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gableTop)
                    self.bottom = Part(2, "Bottom",  self.depth - self.materialThicknessBottom, self.width - 2 * self.materialThicknessBottom, "1S", False, self.router)
                    self.listParts.append(self.bottom)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessBottom, self.width - 2 * self.materialThicknessBottom, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThicknessBottom - 0.125, self.width - 2 * self.materialThicknessBottom - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)

                    if self.width >= 36:
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", False, False)
                    self.listParts.append(self.backUpper)
                    self.backPieceOven = Part(2, "Oven Slot Back", self.width, "6", "-", False, False)
                    self.listParts.append(self.backPieceOven)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessBottom, "-", False, False)
                    self.listParts.append(self.kick)

        if self.category == "Vanity":
            if self.name == "Linen Tower":
                if self.heightBottom == 0:
                    self.gable = Part(2, "Gable", self.depth - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gable)
                    self.bottom = Part(2, "Bottom",  self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.bottom)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessTop, "-", False, False)
                    self.listParts.append(self.kick)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThicknessTop - 0.125, self.width - 2 * self.materialThicknessTop - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)

                    if self.width >= 36:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", False, False)
                    self.listParts.append(self.back)

                else:
                    self.gableBottom = Part(2, "Gable Bottom", self.depth - self.materialThicknessBottom, self.heightBottom, "1L", self.drill, False)
                    self.listParts.append(self.gableBottom)
                    self.gableTop = Part(2, "Gable Top", self.depth - self.materialThicknessBottom, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gableTop)
                    self.bottom = Part(2, "Bottom",  self.depth - self.materialThicknessBottom, self.width - 2 * self.materialThicknessBottom, "1S", False, False)
                    self.listParts.append(self.bottom)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessBottom, self.width - 2 * self.materialThicknessBottom, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessBottom, "-", False, False)
                    self.listParts.append(self.kick)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThicknessBottom - 0.125, self.width - 2 * self.materialThicknessBottom - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)

                    if self.width >= 36:
                        self.backLower = Part(1, "Back Lower", self.width, self.heightBottom - self.toeKick, "-", self.drill, False)
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.backLower = Part(1, "Back Lower", self.width, self.heightBottom - self.toeKick, "-", False, False)
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", False, False)
                    self.listParts.append(self.backLower)
                    self.listParts.append(self.backUpper)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width, self.heightTop, self.heightBottom, self.depth, self.shelfQty, self.toeKick, self.twoPiece, self.drill, self.router, self.materialThicknessTop, self.materialThicknessBottom, self.materialTypeTop, self.materialTypeBottom, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

    def setAttributes(self, attributes):
        self.category, self.name, self.count, self.width, self.heightTop, self.heightBottom, self.depth, self.shelfQty, self.toeKick, self.twoPiece, self.drill, self.router, self.materialThicknessTop, self.materialThicknessBottom, self.materialTypeTop, self.materialTypeBottom, self.editable, self.completionStatus = attributes

class CabinetTallDrawer: # 23 ITEMS
    def __init__(self, category, name, count, width, heightTop, heightBottom, depth, shelfQty, drawerQty, drawerHeights, drawerDepth, toeKick, railTypeTop, railTypeBottom, twoPiece, drill, router, materialThicknessTop, materialThicknessBottom, materialTypeTop, materialTypeBottom, editable, completionStatus):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName
        self.width = width
        self.heightTop = heightTop
        self.heightBottom = heightBottom
        self.depth = depth
        self.shelfQty = shelfQty
        self.drawerQty = drawerQty
        self.drawerHeights = drawerHeights[:]
        self.drawerDepth = drawerDepth
        self.toeKick = toeKick
        self.railTypeTop = railTypeTop
        self.railTypeBottom = railTypeBottom
        self.twoPiece = twoPiece
        self.drill = drill
        self.router = router
        self.materialThicknessTop = materialThicknessTop
        self.materialThicknessBottom = materialThicknessBottom
        self.materialTypeTop = materialTypeTop
        self.materialTypeBottom = materialTypeBottom
        self.editable = editable
        self.completionStatus = completionStatus
        self.displayName = self.category + ", " + self.name + " #" + str(self.count + 1) + " (" + str(self.width) + ")"

        self.listParts = []

        self.railSpaceSidesTop = 0
        self.railSpaceUnderTop = 0
        if self.railTypeTop == "Regular" or self.railTypeTop == "Side Mount" or self.railTypeTop == "P-2-O SM":
            self.railSpaceSidesTop = 0.5
            self.railSpaceUnderTop = 0
        elif self.railTypeTop == "P-2-O UM" or self.railTypeTop == "Under Mount":
            self.railSpaceSidesTop = 0.21875
            self.railSpaceUnderTop = 0.5

        self.railSpaceSidesBottom = 0
        self.railSpaceUnderBottom = 0
        if self.railTypeBottom == "Regular" or self.railTypeBottom == "Side Mount" or self.railTypeBottom == "P-2-O SM":
            self.railSpaceSidesBottom = 0.5
            self.railSpaceUnderBottom = 0
        elif self.railTypeBottom == "P-2-O UM" or self.railTypeBottom == "Under Mount":
            self.railSpaceSidesBottom = 0.21875
            self.railSpaceUnderBottom = 0.5

        if self.category == "Tall":
            if self.name == "Pantry":
                if self.heightBottom == 0:
                    self.gable = Part(2, "Gable", self.depth - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gable)
                    self.bottom = Part(2, "Bottom",  self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.bottom)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThicknessTop - 0.125, self.width - 2 * self.materialThicknessTop - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)

                    if self.width >= 36:
                        self.back = Part(1, "Back", self.width, self.heightTop - self.toeKick, "-", self.drill, False)
                    else:
                        self.back = Part(1, "Back", self.width, self.heightTop - self.toeKick, "-", False, False)
                    self.listParts.append(self.back)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessTop, "-", False, False)
                    self.listParts.append(self.kick)

                    self.tempDrawerHeights = self.drawerHeights[:]
                    self.tempHeight = 0
                    self.countedQty = 0
                    self.partCount = 0

                    print("-------------------------------------------------------")
                    self.tempHeight = self.tempDrawerHeights[0]
                    while len(self.tempDrawerHeights) != 0:
                        if self.tempDrawerHeights[0] == self.tempHeight:
                            self.countedQty += 1
                            if len(self.tempDrawerHeights) == 1:
                                self.partCount += 1
                                self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThicknessTop - self.railSpaceUnderTop, self.width - 4 * self.materialThicknessTop - 2 * self.railSpaceSidesTop, "1L", False, False)
                                self.listParts.append(self.frontBack)
                                if self.railTypeTop == "P-2-O UM" or self.railTypeTop == "Under Mount":
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                                else:
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                                self.listParts.append(self.sides)
                            self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                        elif self.tempDrawerHeights[0] != self.tempHeight:
                            self.partCount += 1
                            self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThicknessTop - self.railSpaceUnderTop, self.width - 4 * self.materialThicknessTop - 2 * self.railSpaceSidesTop, "1L", False, False)
                            self.listParts.append(self.frontBack)
                            if self.railTypeTop == "P-2-O UM" or self.railTypeTop == "Under Mount":
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                            else:
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                            self.listParts.append(self.sides)
                            self.countedQty = 1
                            self.tempHeight = self.tempDrawerHeights[0]

                            if len(self.tempDrawerHeights) == 1:
                                self.countedQty = 1
                                self.partCount += 1
                                self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempDrawerHeights[0] - self.materialThicknessTop - self.railSpaceUnderTop, self.width - 4 * self.materialThicknessTop - 2 * self.railSpaceSidesTop, "1L", False, False)
                                self.listParts.append(self.frontBack)
                                if self.railTypeTop == "P-2-O UM" or self.railTypeTop == "Under Mount":
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth - 5/8, "1L", False, False)
                                else:
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth, "1L", False, False)
                                self.listParts.append(self.sides)

                            self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                    print("-------------------------------------------------------")

                    self.drawerBottom = Part(self.drawerQty, "Drawer Bottom", self.width - 4 * self.materialThicknessTop - 2 * self.railSpaceSidesTop, self.drawerDepth, "-", False, False)
                    self.listParts.append(self.drawerBottom)

                else:
                    self.gableBottom = Part(2, "Gable Bottom", self.depth - self.materialThicknessBottom, self.heightBottom, "1L", self.drill, False)
                    self.listParts.append(self.gableBottom)
                    self.gableTop = Part(2, "Gable Top", self.depth - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gableTop)
                    self.bottom = Part(2, "Bottom",  self.depth - self.materialThicknessBottom, self.width - 2 * self.materialThicknessBottom, "1S", False, self.router)
                    self.listParts.append(self.bottom)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    if self.shelfQty > 0:
                        self.shelf = Part(self.shelfQty, "Shelf", self.depth - self.materialThicknessTop - 0.125, self.width - 2 * self.materialThicknessTop - 0.0625, "1L", False, self.router)
                        self.listParts.append(self.shelf)
                    if self.width >= 36:
                        self.backLower = Part(1, "Back Lower", self.width, self.heightBottom - self.toeKick, "-", self.drill, False)
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.backLower = Part(1, "Back Lower", self.width, self.heightBottom - self.toeKick, "-", False, False)
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", False, False)
                    self.listParts.append(self.backLower)
                    self.listParts.append(self.backUpper)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessBottom, "-", False, False)
                    self.listParts.append(self.kick)

                    self.tempDrawerHeights = self.drawerHeights[:]
                    self.tempHeight = 0
                    self.countedQty = 0
                    self.partCount = 0

                    print("-------------------------------------------------------")
                    self.tempHeight = self.tempDrawerHeights[0]
                    while len(self.tempDrawerHeights) != 0:
                        if self.tempDrawerHeights[0] == self.tempHeight:
                            self.countedQty += 1
                            if len(self.tempDrawerHeights) == 1:
                                self.partCount += 1
                                self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThicknessBottom - self.railSpaceUnderBottom, self.width - 4 * self.materialThicknessBottom - 2 * self.railSpaceSidesBottom, "1L", False, False)
                                self.listParts.append(self.frontBack)
                                if self.railTypeBottom == "P-2-O UM" or self.railTypeBottom == "Under Mount":
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                                else:
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                                self.listParts.append(self.sides)
                            self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                        elif self.tempDrawerHeights[0] != self.tempHeight:
                            self.partCount += 1
                            self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThicknessBottom - self.railSpaceUnderBottom, self.width - 4 * self.materialThicknessBottom - 2 * self.railSpaceSidesBottom, "1L", False, False)
                            self.listParts.append(self.frontBack)
                            if self.railTypeBottom == "P-2-O UM" or self.railTypeBottom == "Under Mount":
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                            else:
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                            self.listParts.append(self.sides)
                            self.countedQty = 1
                            self.tempHeight = self.tempDrawerHeights[0]

                            if len(self.tempDrawerHeights) == 1:
                                self.countedQty = 1
                                self.partCount += 1
                                self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempDrawerHeights[0] - self.materialThicknessBottom - self.railSpaceUnderBottom, self.width - 4 * self.materialThicknessBottom - 2 * self.railSpaceSidesBottom, "1L", False, False)
                                self.listParts.append(self.frontBack)
                                if self.railTypeBottom == "P-2-O UM" or self.railTypeBottom == "Under Mount":
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth - 5/8, "1L", False, False)
                                else:
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth, "1L", False, False)
                                self.listParts.append(self.sides)

                            self.tempDrawerHeights.remove(self.tempDrawerHeights[0])
                    print("-------------------------------------------------------")

                    self.drawerBottom = Part(self.drawerQty, "Drawer Bottom", self.width - 4 * self.materialThicknessBottom - 2 * self.railSpaceSidesBottom, self.drawerDepth, "-", False, False)
                    self.listParts.append(self.drawerBottom)


            if name == "Pull Out":
                if self.heightBottom == 0:
                    self.gable = Part(2, "Gable", self.depth - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gable)
                    if self.width >= 36:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.back = Part(1, "Back", self.width, self.heightTop, "-", False, False)
                    self.listParts.append(self.back)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    self.bottom = Part(2, "Bottom", self.width - 2 * self.materialThicknessTop, self.depth - self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.bottom)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessTop, "-", False, False)
                    self.listParts.append(self.kick)

                    self.tempDrawerHeights = self.drawerHeights[:]
                    self.tempHeight = 0
                    self.countedQty = 0
                    self.partCount = 0

                    print("-------------------------------------------------------")
                    self.tempHeight = self.tempDrawerHeights[0]
                    while len(self.tempDrawerHeights) != 0:
                        if self.tempDrawerHeights[0] == self.tempHeight:
                            self.countedQty += 1
                            if len(self.tempDrawerHeights) == 1:
                                self.partCount += 1
                                self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThicknessTop - self.railSpaceUnderTop, self.width - 4 * self.materialThicknessTop - 2 * self.railSpaceSidesTop, "1L", False, False)
                                self.listParts.append(self.frontBack)
                                if self.railTypeTop == "P-2-O UM" or self.railTypeTop == "Under Mount":
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                                else:
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                                self.listParts.append(self.sides)
                            self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                        elif self.tempDrawerHeights[0] != self.tempHeight:
                            self.partCount += 1
                            self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThicknessTop - self.railSpaceUnderTop, self.width - 4 * self.materialThicknessTop - 2 * self.railSpaceSidesTop, "1L", False, False)
                            self.listParts.append(self.frontBack)
                            if self.railTypeTop == "P-2-O UM" or self.railTypeTop == "Under Mount":
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                            else:
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                            self.listParts.append(self.sides)
                            self.countedQty = 1
                            self.tempHeight = self.tempDrawerHeights[0]

                            if len(self.tempDrawerHeights) == 1:
                                self.countedQty = 1
                                self.partCount += 1
                                self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempDrawerHeights[0] - self.materialThicknessTop - self.railSpaceUnderTop, self.width - 4 * self.materialThicknessTop - 2 * self.railSpaceSidesTop, "1L", False, False)
                                self.listParts.append(self.frontBack)
                                if self.railTypeTop == "P-2-O UM" or self.railTypeTop == "Under Mount":
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth - 5/8, "1L", False, False)
                                else:
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth, "1L", False, False)
                                self.listParts.append(self.sides)

                            self.tempDrawerHeights.remove(self.tempDrawerHeights[0])
                    print("-------------------------------------------------------")

                    self.drawerBottom = Part(self.drawerQty, "Drawer Bottom", self.width - 4 * self.materialThicknessTop - 2 * self.railSpaceSidesTop - 0.75, self.drawerDepth, "-", False, False)
                    self.listParts.append(self.drawerBottom)

                else:
                    self.gableBottom = Part(2, "Gable Bottom", self.depth - self.materialThicknessBottom, self.heightBottom, "1L", self.drill, False)
                    self.listParts.append(self.gableBottom)
                    self.gableTop = Part(2, "Gable Top", self.depth - self.materialThicknessTop, self.heightTop, "1L", self.drill, False)
                    self.listParts.append(self.gableTop)

                    if self.width >= 36:
                        self.backLower = Part(1, "Back Lower", self.width, self.heightBottom - self.toeKick, "-", self.drill, False)
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", self.drill, False)
                    else:
                        self.backLower = Part(1, "Back Lower", self.width, self.heightBottom - self.toeKick, "-", False, False)
                        self.backUpper = Part(1, "Back Upper", self.width, self.heightTop, "-", False, False)
                    self.listParts.append(self.backLower)
                    self.listParts.append(self.backUpper)
                    self.roof = Part(2, "Roof", self.depth - self.materialThicknessTop, self.width - 2 * self.materialThicknessTop, "1S", False, self.router)
                    self.listParts.append(self.roof)
                    self.bottom = Part(2, "Bottom", self.width - 2 * self.materialThicknessBottom, self.depth - self.materialThicknessBottom, "1S", False, self.router)
                    self.listParts.append(self.bottom)
                    self.kick = Part(1, "Kick", self.toeKick - 0.25, self.width - 2 * self.materialThicknessBottom, "-", False, False)
                    self.listParts.append(self.kick)

                    self.tempDrawerHeights = self.drawerHeights[:]
                    self.tempHeight = 0
                    self.countedQty = 0
                    self.partCount = 0

                    print("-------------------------------------------------------")
                    self.tempHeight = self.tempDrawerHeights[0]
                    while len(self.tempDrawerHeights) != 0:
                        if self.tempDrawerHeights[0] == self.tempHeight:
                            self.countedQty += 1
                            if len(self.tempDrawerHeights) == 1:
                                self.partCount += 1
                                self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThicknessBottom - self.railSpaceUnderBottom, self.width - 4 * self.materialThicknessBottom - 2 * self.railSpaceSidesBottom, "1L", False, False)
                                self.listParts.append(self.frontBack)
                                if self.railTypeBottom == "P-2-O UM" or self.railTypeBottom == "Under Mount":
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                                else:
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                                self.listParts.append(self.sides)
                            self.tempDrawerHeights.remove(self.tempDrawerHeights[0])

                        elif self.tempDrawerHeights[0] != self.tempHeight:
                            self.partCount += 1
                            self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempHeight - self.materialThicknessBottom - self.railSpaceUnderBottom, self.width - 4 * self.materialThicknessBottom - 2 * self.railSpaceSidesBottom, "1L", False, False)
                            self.listParts.append(self.frontBack)
                            if self.railTypeBottom == "P-2-O UM" or self.railTypeBottom == "Under Mount":
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth - 5/8, "1L", False, False)
                            else:
                                self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempHeight, self.drawerDepth, "1L", False, False)
                            self.listParts.append(self.sides)
                            self.countedQty = 1
                            self.tempHeight = self.tempDrawerHeights[0]

                            if len(self.tempDrawerHeights) == 1:
                                self.countedQty = 1
                                self.partCount += 1
                                self.frontBack = Part(self.countedQty * 2, "Front & Back" + str(self.partCount), self.tempDrawerHeights[0] - self.materialThicknessBottom - self.railSpaceUnderBottom, self.width - 4 * self.materialThicknessBottom - 2 * self.railSpaceSidesBottom, "1L", False, False)
                                self.listParts.append(self.frontBack)
                                if self.railTypeBottom == "P-2-O UM" or self.railTypeBottom == "Under Mount":
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth - 5/8, "1L", False, False)
                                else:
                                    self.sides = Part(self.countedQty * 2, "Sides" + str(self.partCount), self.tempDrawerHeights[0], self.drawerDepth, "1L", False, False)
                                self.listParts.append(self.sides)

                            self.tempDrawerHeights.remove(self.tempDrawerHeights[0])
                    print("-------------------------------------------------------")

                    self.drawerBottom = Part(self.drawerQty, "Drawer Bottom", self.width - 4 * self.materialThicknessBottom - 2 * self.railSpaceSidesBottom - 0.75, self.drawerDepth, "-", False, False)
                    self.listParts.append(self.drawerBottom)

    def setFullName(self, category, name, count):
        self.category = category
        self.name = name
        self.count = count
        self.fullName = self.name + " " + str(self.count + 1)
        self.cabinetID = self.category + ", " + self.fullName

    def setCompletionStatus(self, completionStatus):
        self.completionStatus = completionStatus

    def setEditable(self, editable):
        self.editable = editable

    def getAttributes(self):
        self.cabinetAttributes = [self.category, self.name, self.count, self.width, self.heightTop, self.heightBottom, self.depth, self.shelfQty, self.drawerQty, self.drawerHeights, self.drawerDepth, self.toeKick, self.railTypeTop, self.railTypeBottom, self.twoPiece, self.drill, self.router, self.materialThicknessTop, self.materialThicknessBottom, self.materialTypeTop, self.materialTypeBottom, self.editable, self.completionStatus]
        cabinet_properties_list.append(self.cabinetAttributes)

    def setAttributes(self, attributes):
        self.category, self.name, self.count, self.width, self.heightTop, self.heightBottom, self.depth, self.shelfQty, self.drawerQty, self.drawerHeights, self.drawerDepth, self.toeKick, self.railTypeTop, self.railTypeBottom, self.twoPiece, self.drill, self.router, self.materialThicknessTop, self.materialThicknessBottom, self.materialTypeTop, self.materialTypeBottom, self.editable, self.completionStatus = attributes




#-------------------------------------------------- Defining functions for bottom-page bottons --------------------------------------------------//
def to_page2():

    def is_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    project_name.set(project_name_entry.get())
    po_number.set(po_number_entry.get())
    date_year.set(date_year_combobox.get())
    date_month.set(date_month_combobox.get())
    date_day.set(date_day_combobox.get())

    if project_name.get() == "":
        messagebox.showwarning("Missing Information", "Please fill in Project Name field.")
    elif po_number.get() == "":
        messagebox.showwarning("Missing Information", "Please fill in P.O. Number field.")
    elif date_year.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a date (year).")
    elif not is_number(date_year.get()):
        messagebox.showwarning("Missing Information", "Please specify a valid year.")
    elif date_month.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a date (month).")
    elif date_day.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a date (day).")
    elif not is_number(date_day.get()):
        messagebox.showwarning("Missing Information", "Please specify a valid day.")
    elif settings_var.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a measurement type.")
    elif rail_type_var.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a rail type.")
    elif kitchen_rail_size_var.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a rail size for kitchen drawers.")
    elif vanity_rail_size_var.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a rail size for vanity drawers.")
    elif material_type_var.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a material type.")
    elif material_thickness_var.get() == "":
        messagebox.showwarning("Missing Information", "Please choose a material thickness.")
    elif cabinet_height_entry.get() == "":
        messagebox.showwarning("Missing Information", "Please specify a cabinet height.")
    elif not is_number(cabinet_height_entry.get()):
        messagebox.showwarning("Missing Information", "Please enter a valid number for cabinet height.")
    elif has_crown_var.get() == "Yes" and crown_height_entry.get() == "":
        messagebox.showwarning("Missing Information", "Please specify a crown height.")
    elif has_crown_var.get() == "Yes" and not is_number(cabinet_height_entry.get()):
        messagebox.showwarning("Missing Information", "Please enter a valid number for crown height.")
    else:
        page1_frame.pack_forget()
        page2_frame.pack(fill=BOTH)

        for i, cabinet_type in enumerate(base_cabinet_types):
            regenerate_base_count(cabinet_type, len(base_cabinets_list[i]), base_cabinets_list[i])
        for i, cabinet_type in enumerate(wall_cabinet_types):
            regenerate_wall_count(cabinet_type, len(wall_cabinets_list[i]), wall_cabinets_list[i])
        for i, cabinet_type in enumerate(tall_cabinet_types):
            regenerate_tall_count(cabinet_type, len(tall_cabinets_list[i]), tall_cabinets_list[i])
        for i, cabinet_type in enumerate(vanity_cabinet_types):
            regenerate_vanity_count(cabinet_type, len(vanity_cabinets_list[i]), vanity_cabinets_list[i])

    projectNameLabelP2 = Label(project_detail_frame, text = project_name.get(), font = fontSegoeBold, bg = plainWhite, fg = textGray).grid(row=0, column=1, padx=10)
    sep = ttk.Separator(project_detail_frame, orient='vertical').grid(row=0, column=2, padx=2, pady=(3, 0), sticky="nsew")
    railTypeLabelP2 = Label(project_detail_frame, text = "Rail Type: " + rail_type_var.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=3, padx=10)
    sep = ttk.Separator(project_detail_frame, orient='vertical').grid(row=0, column=4, padx=2, pady=(3, 0), sticky="nsew")
    railSizeKitcehLabelP2 = Label(project_detail_frame, text = "Kitchen Rail: " + kitchen_rail_size_var.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=5, padx=10)
    sep = ttk.Separator(project_detail_frame, orient='vertical').grid(row=0, column=6, padx=2, pady=(3, 0), sticky="nsew")
    railSizeVanityLabelP2 = Label(project_detail_frame, text = "Vanity Rail: " + vanity_rail_size_var.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=7, padx=10)
    sep = ttk.Separator(project_detail_frame, orient='vertical').grid(row=0, column=8, padx=2, pady=(3, 0), sticky="nsew")
    materialLabelP2 = Label(project_detail_frame, text = "Material: " + material_type_var.get() + " " + material_thickness_var.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=9, padx=10)
    sep = ttk.Separator(project_detail_frame, orient='vertical').grid(row=0, column=10, padx=2, pady=(3, 0), sticky="nsew")
    cabinetHeightLabelP2 = Label(project_detail_frame, text = "Cabinet Height: " + total_cabinet_height.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=11, padx=10)

def back_to_page1():
    page2_frame.pack_forget()
    page1_frame.pack(fill=BOTH)

def to_page3():
    page2_frame.pack_forget()
    page3_frame.pack(fill=BOTH)
    for cabinet_type in base_cabinet_types:
        send_cabinets_to_page3_cutlists("Base", cabinet_type)
    populate_cutlist_total("Base", all_base_parts_list, cutlist_Total_base_frame)
    for cabinet_type in wall_cabinet_types:
        send_cabinets_to_page3_cutlists("Wall", cabinet_type)
    populate_cutlist_total("Wall", all_wall_parts_list, cutlist_Total_wall_frame)
    for cabinet_type in tall_cabinet_types:
        send_cabinets_to_page3_cutlists("Tall", cabinet_type)
    populate_cutlist_total("Tall", all_tall_parts_list, cutlist_Total_tall_frame)
    for cabinet_type in vanity_cabinet_types:
        send_cabinets_to_page3_cutlists("Vanity", cabinet_type)
    populate_cutlist_total("Vanity", all_vanity_parts_list, cutlist_Total_vanity_frame)

    projectNameLabelP3 = Label(project_detail_frame_p3, text = project_name.get(), font = fontSegoeBold, bg = plainWhite, fg = textGray).grid(row=0, column=1, padx=10)
    sep = ttk.Separator(project_detail_frame_p3, orient='vertical').grid(row=0, column=2, padx=2, pady=(3, 0), sticky="nsew")
    railTypeLabelP3 = Label(project_detail_frame_p3, text = "Rail Type: " + rail_type_var.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=3, padx=10)
    sep = ttk.Separator(project_detail_frame_p3, orient='vertical').grid(row=0, column=4, padx=2, pady=(3, 0), sticky="nsew")
    railSizeKitcehLabelP3 = Label(project_detail_frame_p3, text = "Kitchen Rail: " + kitchen_rail_size_var.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=5, padx=10)
    sep = ttk.Separator(project_detail_frame_p3, orient='vertical').grid(row=0, column=6, padx=2, pady=(3, 0), sticky="nsew")
    railSizeVanityLabelP3 = Label(project_detail_frame_p3, text = "Vanity Rail: " + vanity_rail_size_var.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=7, padx=10)
    sep = ttk.Separator(project_detail_frame_p3, orient='vertical').grid(row=0, column=8, padx=2, pady=(3, 0), sticky="nsew")
    materialLabelP3 = Label(project_detail_frame_p3, text = "Material: " + material_type_var.get() + " " + material_thickness_var.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=9, padx=10)
    sep = ttk.Separator(project_detail_frame_p3, orient='vertical').grid(row=0, column=10, padx=2, pady=(3, 0), sticky="nsew")
    cabinetHeightLabelP3 = Label(project_detail_frame_p3, text = "Cabinet Height: " + total_cabinet_height.get(), font = fontSegoe, bg = plainWhite, fg = textGray).grid(row=0, column=11, padx=10)

def back_to_page2():
    page3_frame.pack_forget()
    page2_frame.pack(fill=BOTH)

def resetWorkspace():
    length=len(base_FullDoor_cabinets)
    for i in range(length):
        delete_base_count("Full Door", 0, base_FullDoor_cabinets, "reset")
    length=len(base_Drawers_cabinets)
    for i in range(length):
        delete_base_count("Drawers", 0, base_Drawers_cabinets, "reset")
    length=len(base_1D1D_cabinets)
    for i in range(length):
        delete_base_count("1Door 1Drawer", 0, base_1D1D_cabinets, "reset")
    length=len(base_Corner90_cabinets)
    for i in range(length):
        delete_base_count("Corner 90", i, base_Corner90_cabinets, "reset")
    length=len(base_CornerDiagonal_cabinets)
    for i in range(length):
        delete_base_count("Corner Diagonal", 0, base_CornerDiagonal_cabinets, "reset")
    length=len(base_CornerBlind_cabinets)
    for i in range(length):
        delete_base_count("Corner Blind", 0, base_CornerBlind_cabinets, "reset")

    length=len(wall_FullDoor_cabinets)
    for i in range(length):
        delete_wall_count("Full Door", 0, wall_FullDoor_cabinets, "reset")
    length=len(wall_Corner90_cabinets)
    for i in range(length):
        delete_wall_count("Corner 90", 0, wall_Corner90_cabinets, "reset")
    length=len(wall_CornerDiagonal_cabinets)
    for i in range(length):
        delete_wall_count("Corner Diagonal", 0, wall_CornerDiagonal_cabinets, "reset")
    length=len(wall_MicowaveSlot_cabinets)
    for i in range(length):
        delete_wall_count("Microwave Slot", 0, wall_MicowaveSlot_cabinets, "reset")

    length=len(tall_FullDoor_cabinets)
    for i in range(length):
        delete_tall_count("Full Door", 0, tall_FullDoor_cabinets, "reset")
    length=len(tall_Pantry_cabinets)
    for i in range(length):
        delete_tall_count("Pantry", 0, tall_Pantry_cabinets, "reset")
    length=len(tall_OvenSlot_cabinets)
    for i in range(length):
        delete_tall_count("Oven Slot", 0, tall_OvenSlot_cabinets, "reset")
    length=len(tall_PullOut_cabinets)
    for i in range(length):
        delete_tall_count("Pull Out", 0, tall_PullOut_cabinets, "reset")

    length=len(vanity_FullDoor_cabinets)
    for i in range(length):
        delete_vanity_count("Full Door", 0, vanity_FullDoor_cabinets, "reset")
    length=len(vanity_Drawers_cabinets)
    for i in range(length):
        delete_vanity_count("Drawers", 0, vanity_Drawers_cabinets, "reset")
    length=len(vanity_1Door1Drawer_cabinets)
    for i in range(length):
        delete_vanity_count("1Door 1Drawer", 0, vanity_1Door1Drawer_cabinets, "reset")
    length=len(vanity_LinenTower_cabinets)
    for i in range(length):
        delete_vanity_count("Linen Tower", 0, vanity_LinenTower_cabinets, "reset")


#-------------------------------------------------- Defining save_project function --------------------------------------------------//
def save_project():
    cabinet_properties_list.clear()

    for cabinet_lists in all_cabinet_lists:
        for cabinet_list in cabinet_lists:
            for cabinet in cabinet_list:
                cabinet.getAttributes()

    project_properties_list = [project_name_entry.get(),
        po_number_entry.get(),
        date_year_combobox.get(),
        date_month_combobox.get(),
        date_day_combobox.get(),
        settings_var.get(),
        rail_type_var.get(),
        kitchen_rail_size_var.get(),
        vanity_rail_size_var.get(),
        material_type_var.get(),
        material_thickness_var.get(),
        to_ceiling_var.get(),
        has_crown_var.get(),
        cabinet_height_entry.get(),
        crown_height_entry.get(),
        total_cabinet_height.get()]

    cabinet_properties_list.append(project_properties_list)

    savedData = cabinet_properties_list[:]

    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/arash/OneDrive/Desktop/Cabinets-App/cabinetsAppData",
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
        )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        # Open the file
        output_file = open(file_name, 'wb')
        # Actually add the stuff to the file
        pickle.dump(savedData, output_file)


#-------------------------------------------------- Defining open_project function --------------------------------------------------//
def open_project():
    file_name = filedialog.askopenfilename(
        initialdir="C:/Users/arash/OneDrive/Desktop/Cabinets-App/cabinetsAppData",
        title="Open File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
        )
    if file_name:
        cabinet_properties_list.clear()
        for cabinet_lists in all_cabinet_lists:
            for cabinet_list in cabinet_lists:
                cabinet_list.clear()

        #Open the file
        input_file = open(file_name, 'rb')
        #Load the data from the file
        loadedItems = pickle.load(input_file)
        #Output stuff to the screen
        for item in loadedItems:
            cabinet_properties_list.append(item)

        project_properties_list = cabinet_properties_list[-1][:]
        cabinet_properties_list.pop()

        project_name_entry.delete(0,  END)
        project_name_entry.insert(0, project_properties_list[0])
        po_number_entry.delete(0,  END)
        po_number_entry.insert(0, project_properties_list[1])
        date_year_combobox.set(project_properties_list[2])
        date_month_combobox.set(project_properties_list[3])
        date_day_combobox.set(project_properties_list[4])
        if project_properties_list[5] == "":
            settings_var.set("Standard")
        else:
            settings_var.set(project_properties_list[5])
        if project_properties_list[6] == "":
            rail_type_var.set("Regular")
        else:
            rail_type_var.set(project_properties_list[6])
            print(rail_type_var.get())
        if project_properties_list[7] == "":
            kitchen_rail_size_var.set("22")
        else:
            kitchen_rail_size_var.set(project_properties_list[7])
        if project_properties_list[8] == "":
            vanity_rail_size_var.set("20")
        else:
            vanity_rail_size_var.set(project_properties_list[8])
        if project_properties_list[9] == "":
            material_type_var.set("Ply Wood")
        else:
            material_type_var.set(project_properties_list[9])
        if project_properties_list[10] == "":
            material_thickness_var.set("0.625")
        else:
            material_thickness_var.set(project_properties_list[10])
        if project_properties_list[11] == "":
            to_ceiling_var.set("No")
        else:
            to_ceiling_var.set(project_properties_list[11])
        if project_properties_list[12] == "":
            has_crown_var.set("Yes")
        else:
            has_crown_var.set(project_properties_list[12])
        if project_properties_list[13] == "":
            #create error function for cabinet_height_entry
            cabinet_height_entry.delete(0, END)
            cabinet_height_entry.insert(0, "100")
            # calculate_total_cabinet_height()
        else:
            cabinet_height_entry.delete(0, END)
            cabinet_height_entry.insert(0, project_properties_list[13])
        if project_properties_list[14] == "":
            #create error function for cabinet_height_entry
            crown_height_entry.delete(0, END)
            crown_height_entry.insert(0, "2")
        else:
            crown_height_entry.delete(0, END)
            crown_height_entry.insert(0, project_properties_list[14])
        if project_properties_list[15] == "":
            total_cabinet_height.set("")
            total_height_label.config(text="Total Cabinet Height: " + total_cabinet_height.get())
        else:
            total_cabinet_height.set(project_properties_list[15])
            total_height_label.config(text="Total Cabinet Height: " + total_cabinet_height.get())

        for list in cabinet_properties_list:
            if list[0] == "Base":
                if list[1] == "Full Door":
                    newCabinet = CabinetFullDoor(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14])
                    base_FullDoor_cabinets.append(newCabinet)
                elif list[1] == "Drawers":
                    newCabinet = CabinetDrawers(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16])
                    base_Drawers_cabinets.append(newCabinet)
                elif list[1] == "1Door 1Drawer":
                    newCabinet = Cabinet1D1D(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16])
                    base_1D1D_cabinets.append(newCabinet)
                elif list[1] == "Corner 90":
                    newCabinet = CabinetCorner(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15])
                    base_Corner90_cabinets.append(newCabinet)
                elif list[1] == "Corner Diagonal":
                    newCabinet = CabinetCorner(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15])
                    base_CornerDiagonal_cabinets.append(newCabinet)
                elif list[1] == "Corner Blind":
                    newCabinet = CabinetCorner(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15])
                    base_CornerBlind_cabinets.append(newCabinet)
            elif list[0] == "Wall":
                if list[1] == "Full Door":
                    newCabinet = CabinetFullDoorWall(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13])
                    wall_FullDoor_cabinets.append(newCabinet)
                elif list[1] == "Corner 90":
                    newCabinet = CabinetCornerWall(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14])
                    wall_Corner90_cabinets.append(newCabinet)
                elif list[1] == "Corner Diagonal":
                    newCabinet = CabinetCornerWall(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14])
                    wall_CornerDiagonal_cabinets.append(newCabinet)
                elif list[1] == "Microwave Slot":
                    newCabinet = CabinetMicrowaveSlot(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16], list[17], list[18])
                    wall_MicowaveSlot_cabinets.append(newCabinet)
            elif list[0] == "Tall":
                if list[1] == "Full Door":
                    newCabinet = CabinetTall(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16], list[17])
                    tall_FullDoor_cabinets.append(newCabinet)
                elif list[1] == "Pantry":
                    newCabinet = CabinetTallDrawer(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16], list[17], list[18], list[19], list[20], list[21], list[22])
                    tall_Pantry_cabinets.append(newCabinet)
                elif list[1] == "Oven Slot":
                    newCabinet = CabinetTall(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16], list[17])
                    tall_OvenSlot_cabinets.append(newCabinet)
                elif list[1] == "Pull Out":
                    newCabinet = CabinetTallDrawer(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16], list[17], list[18], list[19], list[20], list[21], list[22])
                    tall_PullOut_cabinets.append(newCabinet)
            elif list[0] == "Vanity":
                if list[1] == "Full Door":
                    newCabinet = CabinetFullDoor(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14])
                    vanity_FullDoor_cabinets.append(newCabinet)
                elif list[1] == "Drawers":
                    newCabinet = CabinetDrawers(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16])
                    vanity_Drawers_cabinets.append(newCabinet)
                elif list[1] == "1Door 1Drawer":
                    newCabinet = Cabinet1D1D(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16])
                    vanity_1Door1Drawer_cabinets.append(newCabinet)
                elif list[1] == "Linen Tower":
                    newCabinet = CabinetTall(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10], list[11], list[12], list[13], list[14], list[15], list[16], list[17])
                    vanity_LinenTower_cabinets.append(newCabinet)

        selected_rail_type = rail_type_var.get()
        for i, rail_type in enumerate(rail_type_options.keys()):
            if rail_type == selected_rail_type:
                buttons[i].config(fg=textGray)
                labels[i].config(fg=textGray)
            else:
                buttons[i].config(fg=lightTextGray)
                labels[i].config(fg=lightTextGray)

        for i, cabinet_type in enumerate(base_cabinet_types):
            regenerate_base_count(cabinet_type, len(base_cabinets_list[i]), base_cabinets_list[i])
            send_cabinet_to_cutlist("Base", len(base_cabinets_list[i]), cabinet_type)
        all_base_parts_list.clear()
        base_cabinets_list_copy = base_cabinets_list[:]
        merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)
        for cabinet_type in base_cabinet_types:
            send_cabinets_to_page3_cutlists("Base", cabinet_type)
        populate_cutlist_total("Base", all_base_parts_list, cutlist_Total_base_frame)

        for i, cabinet_type in enumerate(wall_cabinet_types):
            regenerate_wall_count(cabinet_type, len(wall_cabinets_list[i]), wall_cabinets_list[i])
            send_cabinet_to_cutlist("Wall", len(base_cabinets_list[i]), cabinet_type)
        all_wall_parts_list.clear()
        wall_cabinets_list_copy = wall_cabinets_list[:]
        merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)
        for cabinet_type in wall_cabinet_types:
            send_cabinets_to_page3_cutlists("Wall", cabinet_type)
        populate_cutlist_total("Wall", all_wall_parts_list, cutlist_Total_wall_frame)

        for i, cabinet_type in enumerate(tall_cabinet_types):
            regenerate_tall_count(cabinet_type, len(tall_cabinets_list[i]), tall_cabinets_list[i])
            send_cabinet_to_cutlist("Tall", len(base_cabinets_list[i]), cabinet_type)
        all_tall_parts_list.clear()
        tall_cabinets_list_copy = tall_cabinets_list[:]
        merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
        for cabinet_type in tall_cabinet_types:
            send_cabinets_to_page3_cutlists("Tall", cabinet_type)
        populate_cutlist_total("Tall", all_tall_parts_list, cutlist_Total_tall_frame)

        for i, cabinet_type in enumerate(vanity_cabinet_types):
            regenerate_vanity_count(cabinet_type, len(vanity_cabinets_list[i]), vanity_cabinets_list[i])
            send_cabinet_to_cutlist("Vall", len(base_cabinets_list[i]), cabinet_type)
        all_vanity_parts_list.clear()
        vanity_cabinets_list_copy = vanity_cabinets_list[:]
        merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)
        for cabinet_type in vanity_cabinet_types:
            send_cabinets_to_page3_cutlists("Vanity", cabinet_type)
        populate_cutlist_total("Vanity", all_vanity_parts_list, cutlist_Total_vanity_frame)


#-------------------------------------------------- Root --------------------------------------------------//
# Create the main application window
root = Tk()
root.title("Cabinets App V3")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(str(screen_width - 30) + "x" + str(screen_height - 60))


#-------------------------------------------------- Fonts --------------------------------------------------//
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
        size=8,
        overstrike=0)
font4 = Font(
        family="Arial Rounded MT Bold",
        size=11,
        overstrike=0)
fontAlien = Font(
        family = "Alien League II",
        size = 30)
fontBauhausHeader = Font(
        family = "Bauhaus 93",
        size = 25)
fontSegoe = Font(
        family = "Segoe UI Variable Display",
        size=10
        )
fontSegoeBold = Font(
        family = "Segoe UI Variable Display Bold",
        size=10
        #or size = 11
        )
fontSegoeSmall = Font(
        family = "Segoe UI Variable Display",
        size=9
        )
fontSegoeExtraSmall = Font(
        family = "Segoe UI Variable Display",
        size=9
        )
fontSegoeXXSmall = Font(
        family = "Segoe UI Variable Display",
        size=6
        )
fontSegoeBig = Font(
        family = "Segoe UI Variable Display",
        size=15
        )


#-------------------------------------------------- Colors --------------------------------------------------//
plainWhite = "#ffffff"
textGray = "#464646"
lightTextGray = "#b5adad"
backHighlightGray = "#b9b9b9"
frontHighlightGray = "#0f6772"
labelFrameBlue = "#125fc7"
logoBlue = "#40b0e5"
errorRed = "#ef1a10"


#-------------------------------------------------- Loading Images --------------------------------------------------//
edit_image = Image.open('edit-66-32.png')
edit_image = ImageTk.PhotoImage(edit_image)
send_image = Image.open('send-11-32.png')
send_image = ImageTk.PhotoImage(send_image)
delete_image = Image.open('delete-151-32.png')
delete_image = ImageTk.PhotoImage(delete_image)
arrowDown_image = Image.open('down-arrow-10-32.png')
arrowDown_image = ImageTk.PhotoImage(arrowDown_image)
arrowUp_image = Image.open('up-arrow-10-32.png')
arrowUp_image = ImageTk.PhotoImage(arrowUp_image)
arrowLeft_image = Image.open('arrow-left-35-32.png')
arrowLeft_image = ImageTk.PhotoImage(arrowLeft_image)

original_image = Image.open('submit-button.png')
new_width = 200  # Replace with your desired width
new_height = 100  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
submit_image = ImageTk.PhotoImage(resized_image)

original_image = Image.open('submit-button-dark.png')
new_width = 200  # Replace with your desired width
new_height = 100  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
submit_image_dark = ImageTk.PhotoImage(resized_image)

original_image = Image.open('print-button.png')
new_width = 140  # Replace with your desired width
new_height = 55  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
print_image = ImageTk.PhotoImage(resized_image)

original_image = Image.open('print-button-dark.png')
new_width = 140  # Replace with your desired width
new_height = 55  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
print_image_dark = ImageTk.PhotoImage(resized_image)

original_image = Image.open('reset-button.png')
new_width = 140  # Replace with your desired width
new_height = 55  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
reset_image = ImageTk.PhotoImage(resized_image)

original_image = Image.open('reset-button-dark.png')
new_width = 140  # Replace with your desired width
new_height = 55  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
reset_image_dark = ImageTk.PhotoImage(resized_image)

original_image = Image.open('get-pdf.png')
new_width =620  # Replace with your desired width
new_height = 55  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
get_pdf_image = ImageTk.PhotoImage(resized_image)

original_image = Image.open('get-pdf-dark.png')
new_width =620  # Replace with your desired width
new_height = 55  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
get_pdf_image_dark = ImageTk.PhotoImage(resized_image)

original_image = Image.open('get-pdf-green.png')
new_width =620  # Replace with your desired width
new_height = 55  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
get_pdf_green_image = ImageTk.PhotoImage(resized_image)

original_image = Image.open('get-pdf-green-dark.png')
new_width =620  # Replace with your desired width
new_height = 55  # Replace with your desired height
resized_image = original_image.resize((new_width, new_height))
get_pdf_green_image_dark = ImageTk.PhotoImage(resized_image)


#-------------------------------------------------- First Page Variables --------------------------------------------------//
project_name = StringVar()
project_name.set("")
po_number = StringVar()
po_number.set("")
date_year = StringVar()
date_year.set("")
date_month = StringVar()
date_month.set("")
date_day = StringVar()
date_day.set("")


#-------------------------------------------------- Lists for Cabinets --------------------------------------------------//
# project_properties_list = []
cabinet_properties_list = []

base_FullDoor_cabinets = []
base_Drawers_cabinets = []
base_1D1D_cabinets = []
base_Corner90_cabinets = []
base_CornerDiagonal_cabinets = []
base_CornerBlind_cabinets = []
base_cabinets_list = [base_FullDoor_cabinets, base_Drawers_cabinets, base_1D1D_cabinets, base_Corner90_cabinets, base_CornerDiagonal_cabinets, base_CornerBlind_cabinets]

wall_FullDoor_cabinets = []
wall_Corner90_cabinets = []
wall_CornerDiagonal_cabinets = []
wall_MicowaveSlot_cabinets = []
wall_cabinets_list = [wall_FullDoor_cabinets, wall_Corner90_cabinets, wall_CornerDiagonal_cabinets, wall_MicowaveSlot_cabinets]

tall_FullDoor_cabinets = []
tall_Pantry_cabinets = []
tall_OvenSlot_cabinets = []
tall_PullOut_cabinets = []
tall_cabinets_list = [tall_FullDoor_cabinets, tall_Pantry_cabinets, tall_OvenSlot_cabinets, tall_PullOut_cabinets]

vanity_FullDoor_cabinets = []
vanity_Drawers_cabinets = []
vanity_1Door1Drawer_cabinets = []
vanity_LinenTower_cabinets = []
vanity_cabinets_list = [vanity_FullDoor_cabinets, vanity_Drawers_cabinets, vanity_1Door1Drawer_cabinets, vanity_LinenTower_cabinets]

custom_cabinets = []

#------------------------------- Defining all_cabinets list and function -------------------------------//
all_cabinet_lists = [base_cabinets_list, wall_cabinets_list, tall_cabinets_list, vanity_cabinets_list]
all_cabinets = []
total_cabinets = 0

def update_allCabinets_list():
    all_cabinets.clear()
    in_cutlist_count = 0
    for cabinets_list in all_cabinet_lists:
        for cabinet_list in cabinets_list:
            for cabinet in cabinet_list:
                all_cabinets.append(cabinet)
                if cabinet.completionStatus == True:
                    in_cutlist_count += 1
    total_cabinets = len(all_cabinets)
    total_cabinets_label.config(text="Total Cabinets: " + str(total_cabinets))
    total_cutlist_label.config(text="In Cutlist: " + str(in_cutlist_count))
    total_cabinets_label_P3.config(text="Total Cabinets: " + str(total_cabinets))
    total_cutlist_label_P3.config(text="In Cutlist: " + str(in_cutlist_count))


#------------------------------- Defining all_parts list and function -------------------------------//
all_base_parts_list = []
all_wall_parts_list = []
all_tall_parts_list = []
all_vanity_parts_list = []
all_parts_list = [all_base_parts_list, all_wall_parts_list, all_tall_parts_list, all_vanity_parts_list]

def merge_cabinet_parts(given_cabinet_Lists, given_parts_list):
    for cabinet_list in given_cabinet_Lists:
        for cabinet in cabinet_list:
            # print(cabinet.cabinetID)
            for part in cabinet.listParts:
                status = "not added"
                if not given_parts_list:
                    newPart = Part(part.qty, part.name, part.width, part.height, part.tape, part.drill, part.router)
                    given_parts_list.append(newPart)
                else:
                    for addedPart in given_parts_list:
                        if addedPart.name == part.name and addedPart.width == part.width and addedPart.height == part.height and addedPart.tape == part.tape and addedPart.drill == part.drill  and addedPart.router == part.router:
                            addedPart.setQty(addedPart.qty + part.qty)
                            # print("addedPart: " + str(addedPart.qty) + " " + addedPart.name + " " + str(addedPart.width) + " " + str(addedPart.height) + " " + addedPart.tape + " " + str(addedPart.drill) + " " + str(addedPart.router))
                            # print("part: " + str(part.qty) + " " + part.name + " " + str(part.width) + " " + str(part.height) + " " + part.tape + " " + str(part.drill) + " " + str(part.router))
                            status = "added"
                    if status == "not added":
                        newPart = Part(part.qty, part.name, part.width, part.height, part.tape, part.drill, part.router)
                        given_parts_list.append(newPart)


#--------------------------------------------------------------------------------------------- Page 1 ---------------------------------------------------------------------------------------------//
#-------------------------------------------------- Page 1: Defining page1_frame --------------------------------------------------//
page1_frame = Frame(root, bg = plainWhite)
page1_frame.pack(fill=BOTH, expand=True)


#-------------------------------------------------- Page 1: Status, Save, and Open Buttons --------------------------------------------------//
status_frame = Frame(page1_frame, bg = plainWhite)
status_frame.pack(fill=BOTH)

status = Label(status_frame, text="Cabinets App - V3", font = fontBauhausHeader, bg = plainWhite, fg = logoBlue, bd=2, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, pady=10)
status.grid(row = 0, column=0, sticky="ew")
status_frame.grid_columnconfigure(0,weight=1)

saveBtnFrame = Frame(status_frame, highlightthickness=0, bg = plainWhite)
saveBtnFrame.grid(row=0, column=0, sticky=E)

sep = ttk.Separator(saveBtnFrame, orient='vertical')
sep.grid(row=0, column=0, padx=2, pady=7, sticky=N+S)

open_button = Button(saveBtnFrame, text="Open", command=open_project, highlightthickness = 0, bd = 0, highlightcolor = textGray, font=fontSegoeBold, activebackground = plainWhite, bg = plainWhite, fg = textGray)
open_button.grid(row=0, column=1, ipadx=18, ipady=18)

sep = ttk.Separator(saveBtnFrame, orient='vertical')
sep.grid(row=0, column=2, padx=2, pady=7, sticky=N+S)

save_button = Button(saveBtnFrame, text="Save", command=save_project, highlightthickness = 0, bd = 0, highlightcolor = textGray, font=fontSegoeBold, activebackground = plainWhite, bg = plainWhite, fg = textGray)
save_button.grid(row=0, column=3, ipadx=18, ipady=18)

sep = ttk.Separator(saveBtnFrame, orient='vertical')
sep.grid(row=0, column=4, padx=2, pady=7, sticky=N+S)

emptyLabel = Label(saveBtnFrame, text = "--", fg='#fff', bg = plainWhite)
emptyLabel.grid(row=0, column=5)


#-------------------------------------------------- Defining menu_frame --------------------------------------------------//
menu_frame = Frame(page1_frame, bg = plainWhite)
menu_frame.pack(fill=BOTH, padx=100, pady=15)


#-------------------------------------------------- Project Info: Name, PO, Date --------------------------------------------------//
project_info_frame = Frame(menu_frame, bg = plainWhite)
project_info_frame.pack(anchor=W, padx=0, pady=(40, 20), ipadx=10, ipady=5)

top_horizontal_frame = Frame(project_info_frame, bg = plainWhite)
top_horizontal_frame.grid(row=0, column=0, sticky="w")

# Create and place labels and entry fields for project information
project_name_label = Label(top_horizontal_frame, text="Project Name:", font=fontSegoe, bg=plainWhite, fg=textGray)
project_name_label.grid(row=0, column=0, sticky="nsew")
project_name_entry = Entry(top_horizontal_frame, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
project_name_entry.grid(row=0, column=1, padx=(10, 40), sticky="w")

po_number_label = Label(top_horizontal_frame, text="PO #:", font=fontSegoe, bg=plainWhite, fg=textGray)
po_number_label.grid(row=0, column=2)
po_number_entry = Entry(top_horizontal_frame, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
po_number_entry.grid(row=0, column=3, padx=(10, 40), sticky="w")

date_label = Label(top_horizontal_frame, text="Date:", font=fontSegoe, bg=plainWhite, fg=textGray)
date_label.grid(row=0, column=4)

current_date = datetime.datetime.now()
current_day = str(current_date.day)
current_month = current_date.strftime("%b")  # Get the month abbreviation
current_year = str(current_date.year)

date_day_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

def update_date(event):
    date_day = date_day_combobox.get()
    date_month = date_month_combobox.get()
    date_year = date_year_combobox.get()
    if date_month == "Jan" or date_month == "Mar" or date_month == "May" or date_month == "Jul" or date_month == "Aug" or date_month == "Oct" or date_month == "Dec":
        date_day_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        date_day_combobox.config(values=date_day_options)
    elif date_month == "Feb":
        date_day_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
        date_day_combobox.config(values=date_day_options)
    else:
        date_day_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
        date_day_combobox.config(values=date_day_options)

date_year_options = ["2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2033", "2034"]
date_year_combobox = ttk.Combobox(top_horizontal_frame, width=4, values=date_year_options)
date_year_combobox.grid(row=0, column=5, padx=(10, 0), sticky="w")
date_year_combobox.bind("<<ComboboxSelected>>", update_date)
date_year_combobox.set(current_year)

date_separator_label = Label(top_horizontal_frame, text="/", font=fontSegoe, bg=plainWhite, fg=textGray)
date_separator_label.grid(row=0, column=6, padx=0, sticky="w")

date_month_options = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
date_month_combobox = ttk.Combobox(top_horizontal_frame, width=4, values=date_month_options)
date_month_combobox.grid(row=0, column=7, padx=0, sticky="w")
date_month_combobox.bind("<<ComboboxSelected>>", update_date)
date_month_combobox.set(current_month)

date_separator_label = Label(top_horizontal_frame, text="/", font=fontSegoe, bg=plainWhite, fg=textGray)
date_separator_label.grid(row=0, column=8, padx=0, sticky="w")

date_day_combobox = ttk.Combobox(top_horizontal_frame, width=2, values=date_day_options)
date_day_combobox.grid(row=0, column=9, padx=0, sticky="w")
date_day_combobox.bind("<<ComboboxSelected>>", update_date)
date_day_combobox.set(current_day)


#-------------------------------------------------- Standard or Custom Measurements --------------------------------------------------//
# Create and place radio buttons for settings selection
settings_var = StringVar()
settings_var.set("Standard")

measurement_type_frame = Frame(menu_frame, bg = plainWhite)
measurement_type_frame.pack(anchor=N+W, pady=20)

settings_label = Label(measurement_type_frame, text="Standard or Custom measurements?", font=fontSegoe, bg=plainWhite, fg=textGray)
settings_label.grid(row=0, column=0, padx=10, pady=5)

standard_radio = Radiobutton(measurement_type_frame, text="Standard", variable=settings_var, value="Standard", font=fontSegoe, bg=plainWhite, fg=textGray)
standard_radio.grid(row=0, column=1, padx=10, pady=5)

custom_radio = Radiobutton(measurement_type_frame, text="Custom", variable=settings_var, value="Custom", font=fontSegoe, bg=plainWhite, fg=textGray)
custom_radio.grid(row=0, column=2, padx=10, pady=5)


#-------------------------------------------------- Slides and Railing for Drawers --------------------------------------------------//
# All railing options frame
railings_frame = LabelFrame(menu_frame, text=" Railing & Slides:  ", borderwidth=2, relief="groove", font=fontSegoe, bg = plainWhite, fg = labelFrameBlue)
railings_frame.pack(anchor=W, padx=10, pady=10, ipadx=10, ipady=5, fill=BOTH)

rail_type_label_frame = Frame(railings_frame, bg = plainWhite)
rail_type_label_frame.pack(anchor=N+W, padx=(20, 0), pady=(15,0), ipadx=10, ipady=7, side="left")

rail_space_instruction_label = Label(rail_type_label_frame, text="Choose one of the railing options: ", font=fontSegoe, bg=plainWhite, fg=textGray)
rail_space_instruction_label.pack(anchor=N+W)

# Create a frame for the rail type selection
rail_type_frame = LabelFrame(rail_type_label_frame, text=" Rail Types:  ", borderwidth=2, relief="groove", font=fontSegoeSmall, bg = plainWhite, fg = labelFrameBlue)
rail_type_frame.pack(anchor=N+W)

# Define rail types and their corresponding rail space
railList = ["Regular", "Side Mount", "P-2-O SM", "P-2-O UM", "Under Mount"]
railSpaceSidesList = [0.5, 0.5, 0.5, 0.21875, 0.21875]
railSpaceUnderList = [0, 0, 0, 0.5, 0.5]

rail_type_options = {
    "Regular": 0.5,
    "Side Mount": 0.5,
    "P-2-O SM": 0.5,
    "P-2-O UM": 0.21875,
    "Under Mount": 0.21875
}

# Create and place a rolling menu for Rail Types
rail_type_var = StringVar()
rail_type_var.set("Regular")

def select_rail_type(rail_type, i):
    rail_type_var.set(rail_type)
    button.config(fg=textGray)  # Change the color of the clicked button
    for j in range(len(buttons)):
        if j == i:
            buttons[j].config(fg=textGray)  # Dim down other buttons
            labels[j].config(fg=textGray)
        elif j != i:
            buttons[j].config(fg=lightTextGray)  # Dim down other buttons
            labels[j].config(fg=lightTextGray)

# Create and place separate buttons for each Rail Type
buttons = []
labels = []

for i, rail_type in enumerate(rail_type_options.keys()):
    button = Button(rail_type_frame, text=rail_type, command=lambda rt=rail_type, idx=i: select_rail_type(rt, idx), font=fontSegoe, fg=textGray)
    button.grid(row=0, column=i, padx=10, pady=5)
    buttons.append(button)

    rail_space_label = Label(rail_type_frame, text=f"Rail Space: {rail_type_options[rail_type]}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    rail_space_label.grid(row=1, column=i, padx=10, pady=(5,9))
    labels.append(rail_space_label)

# Choose railtype regular as default option
selected_rail_type = rail_type_var.get()
for i, rail_type in enumerate(rail_type_options.keys()):
    if rail_type == selected_rail_type:
        buttons[i].config(fg=textGray)
        labels[i].config(fg=textGray)
    else:
        buttons[i].config(fg=lightTextGray)
        labels[i].config(fg=lightTextGray)

#-------------------------------------------------- Rail Size for Kitchen and Vanity --------------------------------------------------//
rail_size_label_frame = Frame(railings_frame, bg = plainWhite)
rail_size_label_frame.pack(anchor=N+W, padx=45, pady=(15,0), ipadx=10, ipady=5)

rail_size_instruction_label = Label(rail_size_label_frame, text="Choose a size option for kitchen and vanity: ", font=fontSegoe, bg=plainWhite, fg=textGray)
rail_size_instruction_label.pack(anchor=N+W)

# Create a frame for the kitchen rail size selection
rail_size_frame = LabelFrame(rail_size_label_frame, text=" Rail Sizes:  ", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
rail_size_frame.pack(anchor=N+W, ipadx=20)

kitchen_rail_size_label = Label(rail_size_frame, text="Kitchen Rail Size:", font=fontSegoe, bg=plainWhite, fg=textGray)
kitchen_rail_size_label.grid(row=0, column=0, padx=10, pady=5)

kitchen_rail_size_var = StringVar()
kitchen_rail_size_var.set("22")

kitchen_rail_size_options = ["22", "20", "18"]
for i, size in enumerate(kitchen_rail_size_options):
    kitchen_rail_radio = Radiobutton(rail_size_frame, text=size, variable=kitchen_rail_size_var, value=size, font=fontSegoe, fg=textGray)
    kitchen_rail_radio.grid(row=0, column=i + 1, padx=10, pady=5)

# Create and place radio buttons for Vanity Rail Size
vanity_rail_size_var = StringVar()
vanity_rail_size_var.set("20")

vanity_rail_size_label = Label(rail_size_frame, text="Vanity Rail Size:", font=fontSegoe, bg=plainWhite, fg=textGray)
vanity_rail_size_label.grid(row=1, column=0, padx=10, pady=5)

vanity_rail_size_options = ["20", "18"]
for i, size in enumerate(vanity_rail_size_options):
    vanity_rail_radio = Radiobutton(rail_size_frame, text=size, variable=vanity_rail_size_var, value=size, font=fontSegoe, fg=textGray)
    vanity_rail_radio.grid(row=1, column=i + 1, padx=10, pady=5)


#-------------------------------------------------- Material Type and Thickness --------------------------------------------------//
mid_row_frame = Frame(menu_frame, bg = plainWhite)
mid_row_frame.pack(anchor=W, padx=10, pady=10, fill=BOTH)
# Materials frame
material_frame = LabelFrame(mid_row_frame, text=" Material:  ", borderwidth=2, relief="groove", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
material_frame.pack(anchor=W, padx=0, pady=10, ipadx=10, ipady=5, side="left")

rail_size_instruction_label = Label(material_frame, text="Choose a material type and thickness: ", font=fontSegoe, bg=plainWhite, fg=textGray)
rail_size_instruction_label.pack(anchor=N+W, padx=15, pady=(15, 10))


# Material types frame
material_type_frame = Frame(material_frame)
material_type_frame.pack(anchor=W)

# Create and place radio buttons for Material Type
material_type_var = StringVar()
material_type_var.set("Ply Wood")

material_type_label = Label(material_type_frame, text="Material Type:", font=fontSegoe, bg=plainWhite, fg=textGray)
material_type_label.grid(row=0, column=0, padx=20, pady=5)

material_type_options = ["Ply Wood", "White Melamin", "Custom"]
for i, size in enumerate(material_type_options):
    material_type_radio = Radiobutton(material_type_frame, text=size, variable=material_type_var, value=size, font=fontSegoe, fg=textGray)
    material_type_radio.grid(row=0, column=i + 1, padx=5, pady=5)

# Material thickness frame
material_thickness_frame = Frame(material_frame)
material_thickness_frame.pack(anchor=W)

# Create and place radio buttons for Material Thickness
material_thickness_var = StringVar()
material_thickness_var.set("0.625")

material_thickness_label = Label(material_thickness_frame, text="Material Thickness:", font=fontSegoe, bg=plainWhite, fg=textGray)
material_thickness_label.grid(row=1, column=0, padx=20, pady=(0, 5))

material_thickness_options = ["0.625", "0.75"]
for i, size in enumerate(material_thickness_options):
    material_thickness_radio = Radiobutton(material_thickness_frame, text=size, variable=material_thickness_var, value=size, font=fontSegoe, fg=textGray)
    material_thickness_radio.grid(row=1, column=i + 1, padx=10, pady=5)


#-------------------------------------------------- Ceiling Options --------------------------------------------------//
# Ceiling Options frame
ceiling_options_frame = LabelFrame(mid_row_frame, text=" Ceiling:  ", borderwidth=2, relief="groove", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue, width=1050, height=189)
ceiling_options_frame.pack(anchor=W, padx=0, pady=0, ipadx=5, ipady=5, side="right")
ceiling_options_frame.pack_propagate(False)

rail_size_instruction_label = Label(ceiling_options_frame, text="Choose a ceiling option: ", font=fontSegoe, bg=plainWhite, fg=textGray)
rail_size_instruction_label.pack(anchor=N+W, padx=15, pady=(15, 10))

# Create a frame for the ceiling radio buttons
ceiling_radio_buttons_frame = Frame(ceiling_options_frame, borderwidth=2)
ceiling_radio_buttons_frame.pack(anchor=W, padx=10, ipadx=10)

# Create and place radio buttons for "to the ceiling?"
to_ceiling_var = StringVar()
to_ceiling_var.set("No")

to_ceiling_label = Label(ceiling_radio_buttons_frame, text="To the ceiling?", font=fontSegoe, bg=plainWhite, fg=textGray)
to_ceiling_label.grid(row=0, column=0, padx=10, pady=5)

to_ceiling_options = ["No", "Yes"]
for i, size in enumerate(to_ceiling_options):
    to_ceiling_radio = Radiobutton(ceiling_radio_buttons_frame, text=size, variable=to_ceiling_var, value=size, font=fontSegoe, fg=textGray)
    to_ceiling_radio.grid(row=0, column=i + 1, padx=10, pady=5)

# Create and place radio buttons for Crown Options
has_crown_var = StringVar()
has_crown_var.set("Yes")

has_crown_label = Label(ceiling_radio_buttons_frame, text="Does this cabinet have a crown?", font=fontSegoe, bg=plainWhite, fg=textGray)
has_crown_label.grid(row=0, column=3, columnspan=4, padx=10, pady=5)

has_crown_options = ["No", "Yes"]
for j, size in enumerate(to_ceiling_options):
    has_crown_radio = Radiobutton(ceiling_radio_buttons_frame, text=size, variable=has_crown_var, value=size, font=fontSegoe, fg=textGray)
    has_crown_radio.grid(row=0, column=j + 7, padx=10, pady=5)

# Create a frame for the ceiling enteries
ceiling_enteries_frame = Frame(ceiling_options_frame, borderwidth=2)
ceiling_enteries_frame.pack(anchor=W, padx=10, ipadx=10)

cabinet_height_label = Label(ceiling_enteries_frame, text="Cabinet Height:", font=fontSegoe, bg=plainWhite, fg=textGray)
cabinet_height_label.grid(row=0, column=0, padx=(10, 5), pady=5)

cabinet_height_entry = Entry(ceiling_enteries_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
cabinet_height_entry.grid(row=0, column=1, padx=(5, 10), pady=5)

# Function to toggle the label of cabinet height entry
def toggle_ceiling_height_label():
    if to_ceiling_var.get() == "Yes":
        cabinet_height_label.config(text="Ceiling Height:")
    else:
        cabinet_height_label.config(text="Cabinet Height:")
    calculate_total_cabinet_height()

# Bind the function to the radio button variable
to_ceiling_var.trace_add("write", lambda *args: toggle_ceiling_height_label())

empty_label = Label(ceiling_enteries_frame, text="------", font=fontSegoe, bg=plainWhite, fg=plainWhite)
empty_label.grid(row=0, column=2, columnspan=2, padx=10, pady=5)

crown_height_label = Label(ceiling_enteries_frame, text="Crown Height:", font=fontSegoe, bg=plainWhite, fg=textGray)
crown_height_label.grid(row=0, column=4, padx=(10, 5), pady=5)

crown_height_entry = Entry(ceiling_enteries_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
crown_height_entry.grid(row=0, column=5, padx=(5, 10), pady=5)
crown_height = 2
crown_height_entry.insert(0, crown_height)

# Function to toggle the visibility of crown height label and entry
def toggle_crown_visibility():
    if has_crown_var.get() == "Yes":
        crown_height_label.grid(row=0, column=4, padx=10, pady=5)
        crown_height_entry.grid(row=0, column=5, padx=10, pady=5)
    else:
        crown_height_label.grid_forget()
        crown_height_entry.grid_forget()
    calculate_total_cabinet_height()

# Bind the function to the radio button variable
has_crown_var.trace_add("write", lambda *args: toggle_crown_visibility())

empty_label = Label(ceiling_enteries_frame, text="------", font=fontSegoe, bg=plainWhite, fg=plainWhite)
empty_label.grid(row=0, column=6, columnspan=2, padx=10, pady=5)

total_height_label = Label(ceiling_enteries_frame, text="Total Cabinet Height: ", font=fontSegoe, bg=plainWhite, fg=textGray)
total_height_label.grid(row=0, column=8, padx=10, pady=5)
total_cabinet_height = StringVar()
total_cabinet_height.set("")

# Function to calculate and update the total cabinet height
def calculate_total_cabinet_height():
    try:
        cabinet_height = float(cabinet_height_entry.get())
        crown_height = float(crown_height_entry.get())
        if has_crown_var.get() == "Yes" and crown_height < 2:
            crown_height = 2  # Minimum crown height of 2 inches
            crown_height_entry.delete(0, END)
            crown_height_entry.insert(0, crown_height)
        if to_ceiling_var.get() == "Yes":
            total_height = cabinet_height - crown_height + 2
            total_height_label.config(text=f"Total Cabinet Height: {total_height:.2f}")
        else:
            total_height = cabinet_height
            total_height_label.config(text=f"Total Cabinet Height: {total_height:.2f}")
        total_cabinet_height.set(f"{total_height:.2f}")
    except ValueError:
        total_height_label.config(text="Total Cabinet Height: Invalid Input")
        total_cabinet_height.set("")

# Bind the function to the cabinet height and crown height entries
# to_ceiling_radio.bind("<KeyRelease>", lambda event: calculate_total_cabinet_height())
# has_crown_radio.bind("<KeyRelease>", lambda event: calculate_total_cabinet_height())
cabinet_height_entry.bind("<KeyRelease>", lambda event: calculate_total_cabinet_height())
crown_height_entry.bind("<KeyRelease>", lambda event: calculate_total_cabinet_height())
cabinet_height_entry.insert(0, "100")
cabinet_height_entry.delete(0, END)


#-------------------------------------------------- to_page2 Button --------------------------------------------------//
to_page2_button_frame = Frame(menu_frame, bg = plainWhite)
to_page2_button_frame.pack(anchor=S+E, padx=10, pady=10, side="right")

def on_submit_button_press(event):
    to_page2_button.config(image=submit_image_dark)

def on_submit_button_release(event):
    to_page2_button.config(image=submit_image)

to_page2_button = Button(to_page2_button_frame, image=submit_image, command=to_page2, bd=0, relief="solid")
to_page2_button.pack(anchor=E, padx=0, pady=0)

to_page2_button.bind("<Button-1>", on_submit_button_press)
to_page2_button.bind("<ButtonRelease-1>", on_submit_button_release)




#--------------------------------------------------------------------------------------------- Page 2 ---------------------------------------------------------------------------------------------//
#-------------------------------------------------- Page 2: Defining page2_frame --------------------------------------------------//
page2_frame = Frame(root, bg = plainWhite)
# page2_frame.pack(fill=BOTH, expand=True)

#-------------------------------------------------- Page 2: Status, Save, and Open Buttons --------------------------------------------------//
status_frame = Frame(page2_frame, bg = plainWhite)
status_frame.pack(fill=BOTH)

status = Label(status_frame, text="Cabinets App - V3", font = fontBauhausHeader, bg = plainWhite, fg = logoBlue, bd=2, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, pady=10)
status.grid(row=0, column=0, sticky="ew")
status_frame.grid_columnconfigure(0,weight=1)

switchFrame = Frame(status_frame, highlightthickness=0, bg = plainWhite)
switchFrame.grid(row=0, column=0, sticky=W)

arrow_Button = Button(switchFrame, image=arrowLeft_image, width=11, height=36, command=back_to_page1, font=fontSegoeSmall, bd=0, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
arrow_Button.grid(row=0, column=0, padx=(30, 0), pady=(3,0), ipady=19, sticky=S)
backButton = Button(switchFrame, text="Back", width=4, command=back_to_page1, font=fontSegoeBold, bd=0, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
backButton.grid(row=0, column=1, padx=0, ipady=18)
emptyButton = Button(switchFrame, text="", width=1, command=back_to_page1, font=fontSegoeBold, bd=0, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
emptyButton.grid(row=0, column=2, padx=0, ipady=18)
sep = ttk.Separator(switchFrame, orient='vertical')
sep.grid(row=0, column=3, padx=5, pady=7, sticky=N+S)

total_cabinets_label = Label(switchFrame, text="Total Cabinets: 0", font=fontSegoe, bg=plainWhite, fg=textGray)
total_cabinets_label.grid(row=0, column=4, padx=(10, 5))
comma_label = Label(switchFrame, text="|", font=fontSegoeBig, bg=plainWhite, fg=textGray)
comma_label.grid(row=0, column=5)
total_cutlist_label = Label(switchFrame, text="In Cutlist: 0", font=fontSegoe, bg=plainWhite, fg=textGray)
total_cutlist_label.grid(row=0, column=6, padx=(5, 10))

saveBtnFrame = Frame(status_frame, highlightthickness=0, bg = plainWhite)
saveBtnFrame.grid(row=0, column=0, sticky=E)

sep = ttk.Separator(saveBtnFrame, orient='vertical')
sep.grid(row=0, column=0, padx=2, pady=7, sticky=N+S)

open_button = Button(saveBtnFrame, text="Open", command=open_project, highlightthickness=0, bd=0, highlightcolor=textGray, font=fontSegoeBold, activebackground=plainWhite, bg=plainWhite, fg=textGray)
open_button.grid(row=0, column=1, ipadx=18, ipady=18)

sep = ttk.Separator(saveBtnFrame, orient='vertical')
sep.grid(row=0, column=2, padx=2, pady=7, sticky=N+S)

save_button = Button(saveBtnFrame, text="Save", command=save_project, highlightthickness=0, bd=0, highlightcolor=textGray, font=fontSegoeBold, activebackground=plainWhite, bg=plainWhite, fg=textGray)
save_button.grid(row=0, column=3, ipadx=18, ipady=18)

sep = ttk.Separator(saveBtnFrame, orient='vertical')
sep.grid(row=0, column=4, padx=2, pady=7, sticky=N+S)

emptyLabel = Label(saveBtnFrame, text="--", bg=plainWhite, fg=plainWhite)
emptyLabel.grid(row=0, column=5)


#-------------------------------------------------- Project Details Frame --------------------------------------------------//
project_detail_frame = Frame(page2_frame, highlightthickness=0, bg = plainWhite)
project_detail_frame.pack(fill=BOTH)

# Contents of this frame are defined in to_page2() function
project_detail_frame.grid_columnconfigure(0, weight=1)
project_detail_frame.grid_columnconfigure(12, weight=1)


#-------------------------------------------------- Defining page2_app_frame --------------------------------------------------//
page2_app_frame = Frame(page2_frame, bg = plainWhite)
page2_app_frame.pack(fill=BOTH, padx=50)


#-------------------------------------------------- Defining page2 scrollbars --------------------------------------------------//
#----------------------------------------- Select Cabinets Scrollbar -----------------------------------------//
selectCabinets_backFrame = LabelFrame(page2_app_frame, text="Types", font = fontSegoe, padx=0, pady=5, bg = plainWhite, fg = labelFrameBlue)
selectCabinets_backFrame.grid(row=0, rowspan = 26, column=0, padx=5, pady=5, sticky=W+E+N+S)
selectCabinets_canvas = Canvas(selectCabinets_backFrame, bg = plainWhite, borderwidth=0, highlightthickness=0, width=250, height=screen_height-320)
selectCabinets_canvas.pack(side=LEFT, fill=BOTH, expand=1)
selectCabinets_scrollbar = ttk.Scrollbar(selectCabinets_backFrame, orient=VERTICAL, command=selectCabinets_canvas.yview)
selectCabinets_scrollbar.pack(side=RIGHT, fill=Y)
selectCabinets_canvas.configure(yscrollcommand=selectCabinets_scrollbar.set)
selectCabinets_canvas.bind('<Configure>', lambda e: selectCabinets_canvas.configure(scrollregion = selectCabinets_canvas.bbox("all")))
selectCabinets_frame = Frame(selectCabinets_canvas, bg = plainWhite)
selectCabinets_canvas.create_window((0,0), window=selectCabinets_frame, anchor="nw")

# Configure the canvas to update the scrollbar's view
selectCabinets_canvas.configure(yscrollcommand=selectCabinets_scrollbar.set)
# Bind the MouseWheel event to the canvas
selectCabinets_canvas.bind("<MouseWheel>", lambda event: selectCabinets_canvas.yview_scroll(-1 * (event.delta // 120), "units"))
# Bind the MouseWheel event to the canvas and its children
selectCabinets_frame.bind("<MouseWheel>", lambda event: selectCabinets_canvas.yview_scroll(-1 * (event.delta // 120), "units"))
# selectCabinets_frame.bind_all("<MouseWheel>", lambda event: selectCabinets_canvas.yview_scroll(-1 * (event.delta // 120), "units"))


#----------------------------------------- Workspace Scrollbar and Frames-----------------------------------------//
#------------------------- Workspace Scrollbar -------------------------//
workspace_backFrame = LabelFrame(page2_app_frame, text="Workspace", font = fontSegoe, padx=0, pady=5, bg = plainWhite, fg = labelFrameBlue)
workspace_backFrame.grid(row=0, rowspan = 26, column=1, padx=5, pady=5, sticky=W+E+N+S)
workspace_canvas = Canvas(workspace_backFrame, bg = plainWhite, borderwidth=0, highlightthickness=0, width=screen_width-1080, height=screen_height-320)
# workspace_canvas = Canvas(workspace_backFrame, bg = plainWhite, borderwidth=0, highlightthickness=0, width=850, height=screen_height-320)
workspace_canvas.grid(row=0, column=0, sticky="nsew")
# Create vertical scrollbar and make it fill the height
workspace_scrollbar = ttk.Scrollbar(workspace_backFrame, orient=VERTICAL, command=workspace_canvas.yview)
workspace_scrollbar.grid(row=0, column=1, sticky="ns")
workspace_canvas.configure(yscrollcommand=workspace_scrollbar.set, yscrollincrement=2)
workspace_scrollbar.grid_rowconfigure(0, weight=1)  # Allow the scrollbar to fill the height
# Create horizontal scrollbar
workspace_x_scrollbar = ttk.Scrollbar(workspace_backFrame, orient=HORIZONTAL, command=workspace_canvas.xview)
workspace_x_scrollbar.grid(row=1, column=0, sticky="ew")
workspace_canvas.configure(xscrollcommand=workspace_x_scrollbar.set, scrollregion=workspace_canvas.bbox("all"))

workspace_canvas.bind('<Configure>', lambda e: workspace_canvas.configure(scrollregion = workspace_canvas.bbox("all")))
workspace_frame = Frame(workspace_canvas, bg = plainWhite)
workspace_canvas.create_window((0,0), window=workspace_frame, anchor="nw")

# workspace_backFrame = LabelFrame(page2_app_frame, text="Workspace", font = fontSegoe, padx=0, pady=5, bg = plainWhite, fg = labelFrameBlue)
# workspace_backFrame.grid(row=0, rowspan = 26, column=1, padx=5, pady=5, sticky=W+E+N+S)
# workspace_canvas = Canvas(workspace_backFrame, bg = plainWhite, borderwidth=0, highlightthickness=0, width=850, height=screen_height-320)
# workspace_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# workspace_scrollbar = ttk.Scrollbar(workspace_backFrame, orient=VERTICAL, command=workspace_canvas.yview)
# workspace_scrollbar.pack(side=RIGHT, fill=Y)
# workspace_canvas.configure(yscrollcommand=workspace_scrollbar.set)
# workspace_canvas.bind('<Configure>', lambda e: workspace_canvas.configure(scrollregion = workspace_canvas.bbox("all")))
# workspace_frame = Frame(workspace_canvas, bg = plainWhite)
# workspace_canvas.create_window((0,0), window=workspace_frame, anchor="nw")

# Enable scrolling with the mouse wheel
# def on_canvas_mousewheel(event):
#     workspace_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
# workspace_canvas.bind("<MouseWheel>", on_canvas_mousewheel)
# workspace_canvas.bind_all("<MouseWheel>", on_canvas_mousewheel)

# Enable scrolling with the mouse wheel only when the mouse is inside the workspace canvas
def on_canvas_mousewheel(event):
    if mouse_inside_workspace:
        workspace_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
# Function to set the mouse_inside_workspace variable
def set_mouse_inside_workspace(value):
    global mouse_inside_workspace
    mouse_inside_workspace = value
    # print("value: " + str(value))
# Add a variable to track whether the mouse is inside the workspace canvas
mouse_inside_workspace = False
# Bind the Enter event to set the mouse_inside_workspace variable to True
workspace_canvas.bind("<Enter>", lambda event: set_mouse_inside_workspace(True))
# Bind the Leave event to set the mouse_inside_workspace variable to False
workspace_canvas.bind("<Leave>", lambda event: set_mouse_inside_workspace(False))
# Bind the MouseWheel event to the canvas
workspace_canvas.bind("<MouseWheel>", on_canvas_mousewheel)


#------------------------- Workspace Frames -------------------------//
cabinets_in_workspace_frame = Frame(workspace_frame, bg = plainWhite)
cabinets_in_workspace_frame.pack(fill=BOTH)

# Base frames in workspace
workspace_base_frame = LabelFrame(cabinets_in_workspace_frame, text="Base", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
workspace_base_frame.grid(row=0, column=0, ipadx=3, ipady=2, sticky=W+E)
workspace_base_frame.bind("<MouseWheel>", on_canvas_mousewheel)
# workspace_base_frame.bind_all("<MouseWheel>", on_canvas_mousewheel)
workspace_base_FullDoor_frame = Frame(workspace_base_frame, bg = plainWhite)
workspace_base_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
workspace_base_FullDoor_frame.bind("<MouseWheel>", on_canvas_mousewheel)
workspace_base_Drawers_frame = Frame(workspace_base_frame, bg = plainWhite)
workspace_base_Drawers_frame.grid(row=1, column=0, sticky=W+E)
workspace_base_Drawers_frame.bind("<MouseWheel>", on_canvas_mousewheel)
workspace_base_1D1D_frame = Frame(workspace_base_frame, bg = plainWhite)
workspace_base_1D1D_frame.grid(row=2, column=0, sticky=W+E)
workspace_base_1D1D_frame.bind("<MouseWheel>", on_canvas_mousewheel)
workspace_base_Corner90_frame = Frame(workspace_base_frame, bg = plainWhite)
workspace_base_Corner90_frame.grid(row=3, column=0, sticky=W+E)
workspace_base_Corner90_frame.bind("<MouseWheel>", on_canvas_mousewheel)
workspace_base_CornerDiagonal_frame = Frame(workspace_base_frame, bg = plainWhite)
workspace_base_CornerDiagonal_frame.grid(row=4, column=0, sticky=W+E)
workspace_base_CornerDiagonal_frame.bind("<MouseWheel>", on_canvas_mousewheel)
workspace_base_CornerBlind_frame = Frame(workspace_base_frame, bg = plainWhite)
workspace_base_CornerBlind_frame.grid(row=5, column=0, sticky=W+E)
workspace_base_CornerBlind_frame.bind("<MouseWheel>", on_canvas_mousewheel)

# Wall frames in workspace
workspace_wall_frame = LabelFrame(cabinets_in_workspace_frame, text="Wall", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
workspace_wall_frame.grid(row=1, column=0, ipadx=3, ipady=2, sticky=W+E)
workspace_wall_FullDoor_frame = Frame(workspace_wall_frame, bg = plainWhite)
workspace_wall_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
workspace_wall_Corner90_frame = Frame(workspace_wall_frame, bg = plainWhite)
workspace_wall_Corner90_frame.grid(row=1, column=0, sticky=W+E)
workspace_wall_CornerDiagonal_frame = Frame(workspace_wall_frame, bg = plainWhite)
workspace_wall_CornerDiagonal_frame.grid(row=2, column=0, sticky=W+E)
workspace_wall_MicrowaveSlot_frame = Frame(workspace_wall_frame, bg = plainWhite)
workspace_wall_MicrowaveSlot_frame.grid(row=3, column=0, sticky=W+E)

# Tall frames in workspace
workspace_tall_frame = LabelFrame(cabinets_in_workspace_frame, text="Tall", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
workspace_tall_frame.grid(row=2, column=0, ipadx=3, ipady=2, sticky=W+E)
workspace_tall_FullDoor_frame = Frame(workspace_tall_frame, bg = plainWhite)
workspace_tall_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
workspace_tall_Pantry_frame = Frame(workspace_tall_frame, bg = plainWhite)
workspace_tall_Pantry_frame.grid(row=1, column=0, sticky=W+E)
workspace_tall_OvenSlot_frame = Frame(workspace_tall_frame, bg = plainWhite)
workspace_tall_OvenSlot_frame.grid(row=2, column=0, sticky=W+E)
workspace_tall_PullOut_frame = Frame(workspace_tall_frame, bg = plainWhite)
workspace_tall_PullOut_frame.grid(row=3, column=0, sticky=W+E)

# Vanity frames in workspace
workspace_vanity_frame = LabelFrame(cabinets_in_workspace_frame, text="Vanity", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
workspace_vanity_frame.grid(row=3, column=0, ipadx=3, ipady=2, sticky=W+E)
workspace_vanity_FullDoor_frame = Frame(workspace_vanity_frame, bg = plainWhite)
workspace_vanity_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
workspace_vanity_Drawers_frame = Frame(workspace_vanity_frame, bg = plainWhite)
workspace_vanity_Drawers_frame.grid(row=1, column=0, sticky=W+E)
workspace_vanity_1D1D_frame = Frame(workspace_vanity_frame, bg = plainWhite)
workspace_vanity_1D1D_frame.grid(row=2, column=0, sticky=W+E)
workspace_vanity_LinenTower_frame = Frame(workspace_vanity_frame, bg = plainWhite)
workspace_vanity_LinenTower_frame.grid(row=3, column=0, sticky=W+E)

# Custom frames in workspace
workspace_custom_frame = LabelFrame(cabinets_in_workspace_frame, text="Custom", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
workspace_custom_frame.grid(row=4, column=0, ipadx=3, ipady=2, sticky=W+E)


#----------------------------------------- Cutlist Scrollbar and Frames -----------------------------------------//
#------------------------- Cutlist Scrollbar -------------------------//
cutlist_backFrame = LabelFrame(page2_app_frame, text="Cutlist", font=fontSegoe, padx=5, pady=5, bg=plainWhite, fg=labelFrameBlue)
cutlist_backFrame.grid(row=0, rowspan=26, column=2, padx=5, pady=5, sticky="nsew")
cutlist_canvas = Canvas(cutlist_backFrame, bg=plainWhite, borderwidth=0, highlightthickness=0, width=screen_width-1080-240, height=screen_height-320)
# cutlist_canvas = Canvas(cutlist_backFrame, bg=plainWhite, borderwidth=0, highlightthickness=0, width=590, height=screen_height-320)
cutlist_canvas.grid(row=0, column=0, sticky="nsew")
# Create vertical scrollbar and make it fill the height
cutlist_scrollbar = ttk.Scrollbar(cutlist_backFrame, orient=VERTICAL, command=cutlist_canvas.yview)
cutlist_scrollbar.grid(row=0, column=1, sticky="ns")
cutlist_canvas.configure(yscrollcommand=cutlist_scrollbar.set, yscrollincrement=2)
cutlist_scrollbar.grid_rowconfigure(0, weight=1)  # Allow the scrollbar to fill the height
# Create horizontal scrollbar
cutlist_x_scrollbar = ttk.Scrollbar(cutlist_backFrame, orient=HORIZONTAL, command=cutlist_canvas.xview)
cutlist_x_scrollbar.grid(row=1, column=0, sticky="ew")
cutlist_canvas.configure(xscrollcommand=cutlist_x_scrollbar.set, scrollregion=cutlist_canvas.bbox("all"))

cutlist_canvas.bind('<Configure>', lambda e: cutlist_canvas.configure(scrollregion=cutlist_canvas.bbox("all")))
cutlist_frame = Frame(cutlist_canvas, bg=plainWhite)
cutlist_canvas.create_window((0, 0), window=cutlist_frame, anchor="nw")

# Enable scrolling with the mouse wheel
def on_canvas_mousewheel(event):
    cutlist_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
cutlist_canvas.bind("<MouseWheel>", on_canvas_mousewheel)
# cutlist_canvas.bind_all("<MouseWheel>", on_canvas_mousewheel)

#------------------------- Cutlist Frames -------------------------//
cabinets_in_cutlist_frame = Frame(cutlist_frame, bg = plainWhite)
cabinets_in_cutlist_frame.pack(fill=BOTH)

# Base frames in Cutlist
cutlist_base_frame = LabelFrame(cabinets_in_cutlist_frame, text="Base", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_base_frame.grid(row=0, column=0, ipadx=3, ipady=2, sticky=W+E)
cutlist_base_FullDoor_frame = Frame(cutlist_base_frame, bg = plainWhite)
cutlist_base_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
cutlist_base_Drawers_frame = Frame(cutlist_base_frame, bg = plainWhite)
cutlist_base_Drawers_frame.grid(row=1, column=0, sticky=W+E)
cutlist_base_1D1D_frame = Frame(cutlist_base_frame, bg = plainWhite)
cutlist_base_1D1D_frame.grid(row=2, column=0, sticky=W+E)
cutlist_base_Corner90_frame = Frame(cutlist_base_frame, bg = plainWhite)
cutlist_base_Corner90_frame.grid(row=3, column=0, sticky=W+E)
cutlist_base_CornerDiagonal_frame = Frame(cutlist_base_frame, bg = plainWhite)
cutlist_base_CornerDiagonal_frame.grid(row=4, column=0, sticky=W+E)
cutlist_base_CornerBlind_frame = Frame(cutlist_base_frame, bg = plainWhite)
cutlist_base_CornerBlind_frame.grid(row=5, column=0, sticky=W+E)

# Wall frames in Cutlist
cutlist_wall_frame = LabelFrame(cabinets_in_cutlist_frame, text="Wall", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_wall_frame.grid(row=1, column=0, ipadx=3, ipady=2, sticky=W+E)
cutlist_wall_FullDoor_frame = Frame(cutlist_wall_frame, bg = plainWhite)
cutlist_wall_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
cutlist_wall_Corner90_frame = Frame(cutlist_wall_frame, bg = plainWhite)
cutlist_wall_Corner90_frame.grid(row=1, column=0, sticky=W+E)
cutlist_wall_CornerDiagonal_frame = Frame(cutlist_wall_frame, bg = plainWhite)
cutlist_wall_CornerDiagonal_frame.grid(row=2, column=0, sticky=W+E)
cutlist_wall_MicrowaveSlot_frame = Frame(cutlist_wall_frame, bg = plainWhite)
cutlist_wall_MicrowaveSlot_frame.grid(row=3, column=0, sticky=W+E)

# Tall frames in Cutlist
cutlist_tall_frame = LabelFrame(cabinets_in_cutlist_frame, text="Tall", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_tall_frame.grid(row=2, column=0, ipadx=3, ipady=2, sticky=W+E)
cutlist_tall_FullDoor_frame = Frame(cutlist_tall_frame, bg = plainWhite)
cutlist_tall_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
cutlist_tall_Pantry_frame = Frame(cutlist_tall_frame, bg = plainWhite)
cutlist_tall_Pantry_frame.grid(row=1, column=0, sticky=W+E)
cutlist_tall_OvenSlot_frame = Frame(cutlist_tall_frame, bg = plainWhite)
cutlist_tall_OvenSlot_frame.grid(row=2, column=0, sticky=W+E)
cutlist_tall_PullOut_frame = Frame(cutlist_tall_frame, bg = plainWhite)
cutlist_tall_PullOut_frame.grid(row=3, column=0, sticky=W+E)

# Vanity frames in Cutlist
cutlist_vanity_frame = LabelFrame(cabinets_in_cutlist_frame, text="Vanity", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_vanity_frame.grid(row=3, column=0, ipadx=3, ipady=2, sticky=W+E)
cutlist_vanity_FullDoor_frame = Frame(cutlist_vanity_frame, bg = plainWhite)
cutlist_vanity_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
cutlist_vanity_Drawers_frame = Frame(cutlist_vanity_frame, bg = plainWhite)
cutlist_vanity_Drawers_frame.grid(row=1, column=0, sticky=W+E)
cutlist_vanity_1D1D_frame = Frame(cutlist_vanity_frame, bg = plainWhite)
cutlist_vanity_1D1D_frame.grid(row=2, column=0, sticky=W+E)
cutlist_vanity_LinenTower_frame = Frame(cutlist_vanity_frame, bg = plainWhite)
cutlist_vanity_LinenTower_frame.grid(row=3, column=0, sticky=W+E)

# Custom frames in Cutlist
cutlist_custom_frame = LabelFrame(cabinets_in_cutlist_frame, text="Custom", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_custom_frame.grid(row=4, column=0, ipadx=3, ipady=2, sticky=W+E)


#-------------------------------------------------- Function to Send Cabinet to Cutlist --------------------------------------------------//
# Function is triggered when the "Send" button is clicked
def send_cabinet_to_cutlist(category, givenCount, cabinet_type):

    #------------------------- Function to auto scroll -------------------------//
    def auto_scroll_cutlistScrollbar():
        index = 0
        for cabinets_list in all_cabinet_lists:
            for cabinet_list in cabinets_list:
                for cabinet in cabinet_list:
                    index += 1
                    if cabinet.cabinetID == category + ", " + cabinet_type + " " + str(givenCount + 1):
                        selected_item_position = index * 70
                        cutlist_canvas.update_idletasks()
                        cutlist_canvas.configure(scrollregion=cutlist_canvas.bbox("all"))
                        fraction = selected_item_position / cutlist_canvas.winfo_height()
                        # print("fraction is: " + str(fraction))
                        cutlist_canvas.yview_moveto(fraction)

    def populate_cutlist(cabinet, parent, row):
        #------------------------- Cutlist: Defining Buttons Frame and Buttons -------------------------//
        cutlist_button_frame = Frame(parent, bg=plainWhite)
        cutlist_button_frame.grid(row=row, column=1, pady=19, sticky="ne")  # Adjust the column number as needed
        #------------------------- Cutlist: Defining Cutlist Cabinet Frame and Populating cutlist -------------------------//
        cutlist_cabinet_details_frame = LabelFrame(parent, text=cabinet.fullName, borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
        cutlist_cabinet_details_frame.grid(row=row, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")
        # Creating cutlist labels
        quantity_label = Label(cutlist_cabinet_details_frame, text="Quantity", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        quantity_label.grid(row=0, column=0, padx=8, pady=10)
        name_label = Label(cutlist_cabinet_details_frame, text="Name", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        name_label.grid(row=0, column=1, padx=8, pady=10)
        width_label = Label(cutlist_cabinet_details_frame, text="Width", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        width_label.grid(row=0, column=2, padx=8, pady=10)
        length_label = Label(cutlist_cabinet_details_frame, text="Height", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        length_label.grid(row=0, column=3, padx=8, pady=10)
        tape_label = Label(cutlist_cabinet_details_frame, text="Tape", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        tape_label.grid(row=0, column=4, padx=8, pady=10)
        drill_label = Label(cutlist_cabinet_details_frame, text="Drill", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        drill_label.grid(row=0, column=5, padx=8, pady=10)
        router_label = Label(cutlist_cabinet_details_frame, text="Router", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        router_label.grid(row=0, column=6, padx=8, pady=10)
        # Inserting cabinet_object.parts

        row=1
        for part in cabinet.listParts:
            part_qty_label = Label(cutlist_cabinet_details_frame, text=f"{part.qty}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_qty_label.grid(row=row, column=0, padx=8, pady=5)
            part_name_label = Label(cutlist_cabinet_details_frame, text=f"{part.name}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_name_label.grid(row=row, column=1, padx=8, pady=5)
            part_width_label = Label(cutlist_cabinet_details_frame, text=f"{part.width}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_width_label.grid(row=row, column=2, padx=8, pady=5)
            part_length_label = Label(cutlist_cabinet_details_frame, text=f"{part.height}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_length_label.grid(row=row, column=3, padx=8, pady=5)
            part_tape_label = Label(cutlist_cabinet_details_frame, text=f"{part.tape}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_tape_label.grid(row=row, column=4, padx=8, pady=5)
            part_drill_label = Label(cutlist_cabinet_details_frame, text=f"{part.drill}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_drill_label.grid(row=row, column=5, padx=8, pady=5)
            part_router_label = Label(cutlist_cabinet_details_frame, text=f"{part.router}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_router_label.grid(row=row, column=6, padx=8, pady=5)
            row+=1

    if category == "Base":
        if cabinet_type == "Full Door":
            for widget in cutlist_base_FullDoor_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_base_FullDoor_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in base_FullDoor_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Drawers":
            for widget in cutlist_base_Drawers_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_base_Drawers_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in base_Drawers_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "1Door 1Drawer":
            for widget in cutlist_base_1D1D_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_base_1D1D_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in base_1D1D_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Corner 90":
            for widget in cutlist_base_Corner90_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_base_Corner90_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in base_Corner90_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Corner Diagonal":
            for widget in cutlist_base_CornerDiagonal_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_base_CornerDiagonal_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in base_CornerDiagonal_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Corner Blind":
            for widget in cutlist_base_CornerBlind_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_base_CornerBlind_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in base_CornerBlind_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

    elif category == "Wall":
        if cabinet_type == "Full Door":
            for widget in cutlist_wall_FullDoor_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_wall_FullDoor_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in wall_FullDoor_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Corner 90":
            for widget in cutlist_wall_Corner90_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_wall_Corner90_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in wall_Corner90_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Corner Diagonal":
            for widget in cutlist_wall_CornerDiagonal_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_wall_CornerDiagonal_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in wall_CornerDiagonal_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Microwave Slot":
            for widget in cutlist_wall_MicrowaveSlot_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_wall_MicrowaveSlot_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in wall_MicowaveSlot_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

    elif category == "Tall":
        if cabinet_type == "Full Door":
            for widget in cutlist_tall_FullDoor_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_tall_FullDoor_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in tall_FullDoor_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Pantry":
            for widget in cutlist_tall_Pantry_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_tall_Pantry_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in tall_Pantry_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Oven Slot":
            for widget in cutlist_tall_OvenSlot_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_tall_OvenSlot_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in tall_OvenSlot_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Pull Out":
            for widget in cutlist_tall_PullOut_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_tall_PullOut_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in tall_PullOut_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

    elif category == "Vanity":
        if cabinet_type == "Full Door":
            for widget in cutlist_vanity_FullDoor_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_vanity_FullDoor_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in vanity_FullDoor_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Drawers":
            for widget in cutlist_vanity_Drawers_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_vanity_Drawers_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in vanity_Drawers_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "1Door 1Drawer":
            for widget in cutlist_vanity_1D1D_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_vanity_1D1D_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in vanity_1Door1Drawer_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

        elif cabinet_type == "Linen Tower":
            for widget in cutlist_vanity_LinenTower_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_vanity_LinenTower_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in vanity_LinenTower_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

    elif category == "Custom":
        if cabinet_type == "Custom":
            for widget in cutlist_custom_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_custom_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in custom_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist(cabinet, cabinet_frame, row)
                    row+=1

    # Update the layout of the cutlist_canvas to include the new entry
    cutlist_canvas.update_idletasks()
    cutlist_canvas.configure(scrollregion=cutlist_canvas.bbox("all"))
    auto_scroll_cutlistScrollbar()


#-------------------------------------------------- Function to update workspace --------------------------------------------------//
# Function to update workspace frames based on the selected cabinet counts
def update_workspace_frames(cabinet_type, current_count, category, action):

    currentCount = current_count

    def make_cabinet_editable(category, given_cabinet_list):
        if given_cabinet_list[currentCount].completionStatus == False:
            messagebox.showwarning("Cabinet is Open!", "The cabinet is not submitted to cut-list yet.\nGo ahead and edit it.")
        else:
            given_cabinet_list[currentCount].setEditable(True)
            if category == "Base":
                regenerate_base_count(cabinet_type, current_count, given_cabinet_list)
            elif category == "Wall":
                regenerate_wall_count(cabinet_type, current_count, given_cabinet_list)
            elif category == "Tall":
                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
            elif category == "Vanity":
                regenerate_vanity_count(cabinet_type, current_count, given_cabinet_list)
            elif category == "Custom":
                regenerate_custom_count(cabinet_type, current_count, given_cabinet_list)

    def is_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def create_cabinet_object(given_cabinet_list):
        # print("currentCount in create object = " + str(currentCount))
        if category == "Base":
            if cabinet_type == "Full Door":
                if base_FullDoor_cabinets[currentCount].completionStatus == True and base_FullDoor_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + base_FullDoor_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                # elif base_FullDoor_cabinets[currentCount].completionStatus == False:
                elif base_FullDoor_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()

                    if not width or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    else:
                        new_cabinet = CabinetFullDoor(category, cabinet_type, currentCount, float(width_entry.get()), float(height_entry.get()), float(depth_entry.get()), int(shelfQty_entry.get()), float(toeKick_entry.get()), sinkBool.get(), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        base_FullDoor_cabinets[currentCount] = new_cabinet
                        all_base_parts_list.clear()
                        base_cabinets_list_copy = base_cabinets_list[:]
                        merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_base_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "Drawers":
                if base_Drawers_cabinets[currentCount].completionStatus == True and base_Drawers_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + base_Drawers_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif base_Drawers_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    drawerDepth = drawerDepth_entry_combobox.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()
                    railType = rail_type_combobox.get().strip()

                    drawerHeightsList = []
                    for drawerHeight in drawerHeights_entries:
                        if is_number(drawerHeight.get()) and float(drawerHeight.get()) != 0:
                            drawerHeightsList.append(float(drawerHeight.get()))

                    if not width or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not drawerDepth:
                        messagebox.showwarning("Missing Information", "Please specify a Drawer Depth.")
                    elif not is_number(drawerDepth):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Drawer Depth.")
                    elif int(drawerQty_var_label["text"]) == 0:
                        messagebox.showwarning("Invalid Input", "Drawer Quantity must be greater than 0.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif not railType:
                        messagebox.showwarning("Missing Information", "Please specify a Rail Type.")
                    else:
                        new_cabinet = CabinetDrawers(category, cabinet_type, currentCount, float(width_entry.get()), float(height_entry.get()), float(depth_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), rail_type_combobox.get(), False, False, float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        base_Drawers_cabinets[currentCount] = new_cabinet
                        all_base_parts_list.clear()
                        base_cabinets_list_copy = base_cabinets_list[:]
                        merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_base_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "1Door 1Drawer":
                if base_1D1D_cabinets[currentCount].completionStatus == True and base_1D1D_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + base_1D1D_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif base_1D1D_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    drawerDepth = drawerDepth_entry_combobox.get().strip()
                    drawerHeight = drawerHeight_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()
                    railType = rail_type_combobox.get().strip()

                    if not width or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not drawerDepth:
                        messagebox.showwarning("Missing Information", "Please specify a Drawer Depth.")
                    elif not is_number(drawerDepth):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Drawer Depth.")
                    elif not drawerHeight:
                        messagebox.showwarning("Missing Information", "Please specify a Drawer Height.")
                    elif not is_number(drawerHeight):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Drawer Height.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif not railType:
                        messagebox.showwarning("Missing Information", "Please specify a Rail Type.")
                    else:
                        new_cabinet = Cabinet1D1D(category, cabinet_type, currentCount, float(width_entry.get()), float(height_entry.get()), float(depth_entry.get()), float(drawerHeight_entry.get()), float(drawerDepth_entry_combobox.get()), int(shelfQty_entry.get()), float(toeKick_entry.get()), rail_type_combobox.get(), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        base_1D1D_cabinets[currentCount] = new_cabinet
                        all_base_parts_list.clear()
                        base_cabinets_list_copy = base_cabinets_list[:]
                        merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_base_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "Corner 90":
                if base_Corner90_cabinets[currentCount].completionStatus == True and base_Corner90_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + base_Corner90_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif base_Corner90_cabinets[currentCount].editable == True:
                    widthL = widthLeft_entry.get().strip()
                    widthR = widthRight_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()

                    if not widthL or not widthR or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(widthL) or not is_number(widthR) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    else:
                        new_cabinet = CabinetCorner(category, cabinet_type, currentCount, float(widthLeft_entry.get()),  float(widthRight_entry.get()), float(height_entry.get()), float(depth_entry.get()), float(shelfQty_entry.get()), 0, float(toeKick_entry.get()), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        base_Corner90_cabinets[currentCount] = new_cabinet
                        all_base_parts_list.clear()
                        base_cabinets_list_copy = base_cabinets_list[:]
                        merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_base_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "Corner Diagonal":
                if base_CornerDiagonal_cabinets[currentCount].completionStatus == True and base_CornerDiagonal_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + base_CornerDiagonal_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif base_CornerDiagonal_cabinets[currentCount].editable == True:
                    widthL = widthLeft_entry.get().strip()
                    widthR = widthRight_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()

                    if not widthL or not widthR or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(widthL) or not is_number(widthR) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    else:
                        new_cabinet = CabinetCorner(category, cabinet_type, currentCount, float(widthLeft_entry.get()),  float(widthRight_entry.get()), float(height_entry.get()), float(depth_entry.get()), float(shelfQty_entry.get()), 0, float(toeKick_entry.get()), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        base_CornerDiagonal_cabinets[currentCount] = new_cabinet
                        all_base_parts_list.clear()
                        base_cabinets_list_copy = base_cabinets_list[:]
                        merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_base_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "Corner Blind":
                if base_CornerBlind_cabinets[currentCount].completionStatus == True and base_CornerBlind_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + base_CornerBlind_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif base_CornerBlind_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    fillerWidth = fillerWidth_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()

                    if not width or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not fillerWidth:
                        fillerWidth_entry.insert(0, "0")
                        new_cabinet = CabinetCorner(category, cabinet_type, currentCount, float(width_entry.get()), 0, float(height_entry.get()), float(depth_entry.get()), float(shelfQty_entry.get()), float(fillerWidth_entry.get()), float(toeKick_entry.get()), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        base_CornerBlind_cabinets[currentCount] = new_cabinet
                        all_base_parts_list.clear()
                        base_cabinets_list_copy = base_cabinets_list[:]
                        merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_base_count(cabinet_type, current_count, given_cabinet_list)
                    elif not is_number(fillerWidth):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Filler Width.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    else:
                        new_cabinet = CabinetCorner(category, cabinet_type, currentCount, float(width_entry.get()), 0, float(height_entry.get()), float(depth_entry.get()), float(shelfQty_entry.get()), float(fillerWidth_entry.get()), float(toeKick_entry.get()), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        base_CornerBlind_cabinets[currentCount] = new_cabinet
                        all_base_parts_list.clear()
                        base_cabinets_list_copy = base_cabinets_list[:]
                        merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_base_count(cabinet_type, current_count, given_cabinet_list)

        if category == "Wall":
            if cabinet_type == "Full Door":
                if wall_FullDoor_cabinets[currentCount].completionStatus == True and wall_FullDoor_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + wall_FullDoor_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif wall_FullDoor_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()

                    if not width or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    else:
                        new_cabinet = CabinetFullDoorWall(category, cabinet_type, currentCount, float(width_entry.get()), float(height_entry.get()), float(depth_entry.get()), int(shelfQty_entry.get()), lightShelfBool.get(), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        wall_FullDoor_cabinets[currentCount] = new_cabinet
                        all_wall_parts_list.clear()
                        wall_cabinets_list_copy = wall_cabinets_list[:]
                        merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_wall_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "Corner 90":
                if wall_Corner90_cabinets[currentCount].completionStatus == True and wall_Corner90_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + wall_Corner90_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif wall_Corner90_cabinets[currentCount].editable == True:
                    widthL = widthLeft_entry.get().strip()
                    widthR = widthRight_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()

                if not widthL or not widthR or not height or not depth:
                    messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                elif not is_number(widthL) or not is_number(widthR) or not is_number(height) or not is_number(depth):
                    messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                elif not shelfQty:
                    messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                elif not is_number(shelfQty):
                    messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                elif not materialThickness:
                    messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                elif not is_number(materialThickness):
                    messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                elif not materialType:
                    messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                else:
                    new_cabinet = CabinetCornerWall(category, cabinet_type, currentCount, float(widthLeft_entry.get()),  float(widthRight_entry.get()), float(height_entry.get()), float(depth_entry.get()), float(shelfQty_entry.get()), lightShelfBool.get(), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                    wall_Corner90_cabinets[currentCount] = new_cabinet
                    all_wall_parts_list.clear()
                    wall_cabinets_list_copy = wall_cabinets_list[:]
                    merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)
                    send_cabinet_to_cutlist(category, current_count, cabinet_type)
                    regenerate_wall_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "Corner Diagonal":
                if wall_CornerDiagonal_cabinets[currentCount].completionStatus == True and wall_CornerDiagonal_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + wall_CornerDiagonal_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif wall_CornerDiagonal_cabinets[currentCount].editable == True:
                    widthL = widthLeft_combobox.get().strip()
                    widthR = widthRight_combobox.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()

                if not widthL or not widthR or not height or not depth:
                    messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                elif not is_number(widthL) or not is_number(widthR) or not is_number(height) or not is_number(depth):
                    messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                elif not shelfQty:
                    messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                elif not is_number(shelfQty):
                    messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                elif not materialThickness:
                    messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                elif not is_number(materialThickness):
                    messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                elif not materialType:
                    messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                else:
                    new_cabinet = CabinetCornerWall(category, cabinet_type, currentCount, float(widthLeft_combobox.get()),  float(widthRight_combobox.get()), float(height_entry.get()), float(depth_entry.get()), float(shelfQty_entry.get()), lightShelfBool.get(), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                    wall_CornerDiagonal_cabinets[currentCount] = new_cabinet
                    all_wall_parts_list.clear()
                    wall_cabinets_list_copy = wall_cabinets_list[:]
                    merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)
                    send_cabinet_to_cutlist(category, current_count, cabinet_type)
                    regenerate_wall_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "Microwave Slot":
                if wall_MicowaveSlot_cabinets[currentCount].completionStatus == True and wall_MicowaveSlot_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + wall_MicowaveSlot_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif wall_MicowaveSlot_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    if twoPieceBool.get() == False:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        heightTop = topPieceData[2].get().strip()
                        depthTop = topPieceData[3].get().strip()
                        materialThicknessBottom = 0
                        materialTypeBottom = ""
                        heightBottom = 0
                        depthBottom = 0
                    elif twoPieceBool.get() == True:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        heightTop = topPieceData[2].get().strip()
                        depthTop = topPieceData[3].get().strip()
                        materialThicknessBottom = bottomPieceData[0].get().strip()
                        materialTypeBottom = bottomPieceData[1].get()
                        heightBottom = bottomPieceData[2].get().strip()
                        depthBottom = bottomPieceData[3].get().strip()

                if not width or not heightTop or not depthTop:
                    messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                elif not is_number(width) or not is_number(heightTop) or not is_number(depthTop):
                    messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                elif not shelfQty:
                    messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                elif not is_number(shelfQty):
                    messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                elif not materialThicknessTop:
                    messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                elif not is_number(materialThicknessTop):
                    messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                elif not materialTypeTop:
                    messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                elif twoPieceBool.get() == True:
                    if not heightBottom or not depthBottom:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(heightBottom) or not is_number(depthBottom):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not materialThicknessBottom:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThicknessBottom):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialTypeBottom:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    else:
                        if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                            response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                            if response:  # If 'Yes' button is clicked
                                new_cabinet = CabinetMicrowaveSlot(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depthTop), float(depthBottom), float(shelfQty_entry.get()), twoPieceBool.get(), lightShelfBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                wall_MicowaveSlot_cabinets[currentCount] = new_cabinet
                                all_wall_parts_list.clear()
                                wall_cabinets_list_copy = wall_cabinets_list[:]
                                merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_wall_count(cabinet_type, current_count, given_cabinet_list)
                            else:
                                pass
                        else:
                            new_cabinet = CabinetMicrowaveSlot(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depthTop), float(depthBottom), float(shelfQty_entry.get()), twoPieceBool.get(), lightShelfBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                            wall_MicowaveSlot_cabinets[currentCount] = new_cabinet
                            all_wall_parts_list.clear()
                            wall_cabinets_list_copy = wall_cabinets_list[:]
                            merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)
                            send_cabinet_to_cutlist(category, current_count, cabinet_type)
                            regenerate_wall_count(cabinet_type, current_count, given_cabinet_list)
                else:
                    if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                        response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                        if response:  # If 'Yes' button is clicked
                            new_cabinet = CabinetMicrowaveSlot(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depthTop), float(depthBottom), float(shelfQty_entry.get()), twoPieceBool.get(), lightShelfBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                            wall_MicowaveSlot_cabinets[currentCount] = new_cabinet
                            all_wall_parts_list.clear()
                            wall_cabinets_list_copy = wall_cabinets_list[:]
                            merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)
                            send_cabinet_to_cutlist(category, current_count, cabinet_type)
                            regenerate_wall_count(cabinet_type, current_count, given_cabinet_list)
                        else:
                            pass
                    else:
                        new_cabinet = CabinetMicrowaveSlot(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depthTop), float(depthBottom), float(shelfQty_entry.get()), twoPieceBool.get(), lightShelfBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                        wall_MicowaveSlot_cabinets[currentCount] = new_cabinet
                        all_wall_parts_list.clear()
                        wall_cabinets_list_copy = wall_cabinets_list[:]
                        merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_wall_count(cabinet_type, current_count, given_cabinet_list)

        if category == "Tall":
            if cabinet_type == "Full Door":
                if tall_FullDoor_cabinets[currentCount].completionStatus == True and tall_FullDoor_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + tall_FullDoor_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif tall_FullDoor_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    if twoPieceBool.get() == False:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        heightTop = topPieceData[2].get().strip()
                        materialThicknessBottom = 0
                        materialTypeBottom = ""
                        heightBottom = 0
                    elif twoPieceBool.get() == True:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        heightTop = topPieceData[2].get().strip()
                        materialThicknessBottom = bottomPieceData[0].get().strip()
                        materialTypeBottom = bottomPieceData[1].get()
                        heightBottom = bottomPieceData[2].get().strip()

                    if not width or not heightTop or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(heightTop) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThicknessTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThicknessTop):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialTypeTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif twoPieceBool.get() == True:
                        if not heightBottom:
                            messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                        elif not is_number(heightBottom):
                            messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                        elif not materialThicknessBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                        elif not is_number(materialThicknessBottom):
                            messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                        elif not materialTypeBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                        else:
                            if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                                response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                                if response:  # If 'Yes' button is clicked
                                    new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                    tall_FullDoor_cabinets[currentCount] = new_cabinet
                                    all_tall_parts_list.clear()
                                    tall_cabinets_list_copy = tall_cabinets_list[:]
                                    merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                    send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                    regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                                else:
                                    pass
                            else:
                                new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                tall_FullDoor_cabinets[currentCount] = new_cabinet
                                all_tall_parts_list.clear()
                                tall_cabinets_list_copy = tall_cabinets_list[:]
                                merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)

                    else:
                        if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                            response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                            if response:  # If 'Yes' button is clicked
                                new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                tall_FullDoor_cabinets[currentCount] = new_cabinet
                                all_tall_parts_list.clear()
                                tall_cabinets_list_copy = tall_cabinets_list[:]
                                merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                            else:
                                pass
                        else:
                            new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                            tall_FullDoor_cabinets[currentCount] = new_cabinet
                            all_tall_parts_list.clear()
                            tall_cabinets_list_copy = tall_cabinets_list[:]
                            merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                            send_cabinet_to_cutlist(category, current_count, cabinet_type)
                            regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)

            if cabinet_type == "Pantry":
                if tall_Pantry_cabinets[currentCount].completionStatus == True and tall_Pantry_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + tall_Pantry_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif tall_Pantry_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    drawerDepth = drawerDepth_entry_combobox.get().strip()

                    drawerHeightsList = []
                    for drawerHeight in drawerHeights_entries:
                        if is_number(drawerHeight.get()) and float(drawerHeight.get()) != 0:
                            drawerHeightsList.append(float(drawerHeight.get()))

                    if twoPieceBool.get() == False:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        railTypeTop = topPieceData[2].get()
                        heightTop = topPieceData[3].get().strip()
                        materialThicknessBottom = 0
                        materialTypeBottom = ""
                        heightBottom = 0
                        railTypeBottom = ""
                    elif twoPieceBool.get() == True:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        railTypeTop = topPieceData[2].get()
                        heightTop = topPieceData[3].get().strip()
                        materialThicknessBottom = bottomPieceData[0].get().strip()
                        materialTypeBottom = bottomPieceData[1].get()
                        railTypeBottom = bottomPieceData[2].get()
                        heightBottom = bottomPieceData[3].get().strip()

                    if not width or not heightTop or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(heightTop) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThicknessTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThicknessTop):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialTypeTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif not railTypeTop:
                        messagebox.showwarning("Missing Information", "Please specify a Rail Type.")
                    elif not drawerDepth:
                        messagebox.showwarning("Missing Information", "Please specify a Drawer Depth.")
                    elif not is_number(drawerDepth):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Drawer Depth.")
                    elif int(drawerQty_var_label["text"]) == 0:
                        messagebox.showwarning("Invalid Input", "Drawer Quantity must be greater than 0.")
                    elif twoPieceBool.get() == True:
                        if not heightBottom:
                            messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                        # elif not is_number(heightBottom):
                        #     messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                        elif not materialThicknessBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                        elif not is_number(materialThicknessBottom):
                            messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                        elif not materialTypeBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                        elif not railTypeBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Rail Type.")
                        else:
                            if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                                response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                                if response:  # If 'Yes' button is clicked
                                    new_cabinet = CabinetTallDrawer(category, cabinet_type, currentCount, float(width_entry.get()), float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), railTypeTop, railTypeBottom, twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                    tall_Pantry_cabinets[currentCount] = new_cabinet
                                    all_tall_parts_list.clear()
                                    tall_cabinets_list_copy = tall_cabinets_list[:]
                                    merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                    send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                    regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                                else:
                                    pass
                            else:
                                new_cabinet = CabinetTallDrawer(category, cabinet_type, currentCount, float(width_entry.get()), float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), railTypeTop, railTypeBottom, twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                tall_Pantry_cabinets[currentCount] = new_cabinet
                                all_tall_parts_list.clear()
                                tall_cabinets_list_copy = tall_cabinets_list[:]
                                merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                    else:
                        if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                            response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                            if response:  # If 'Yes' button is clicked
                                new_cabinet = CabinetTallDrawer(category, cabinet_type, currentCount, float(width_entry.get()), float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), railTypeTop, railTypeBottom, twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                tall_Pantry_cabinets[currentCount] = new_cabinet
                                all_tall_parts_list.clear()
                                tall_cabinets_list_copy = tall_cabinets_list[:]
                                merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                            else:
                                pass
                        else:
                            new_cabinet = CabinetTallDrawer(category, cabinet_type, currentCount, float(width_entry.get()), float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), railTypeTop, railTypeBottom, twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                            tall_Pantry_cabinets[currentCount] = new_cabinet
                            all_tall_parts_list.clear()
                            tall_cabinets_list_copy = tall_cabinets_list[:]
                            merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                            send_cabinet_to_cutlist(category, current_count, cabinet_type)
                            regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)

            if cabinet_type == "Oven Slot":
                if tall_OvenSlot_cabinets[currentCount].completionStatus == True and tall_OvenSlot_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + tall_OvenSlot_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif tall_OvenSlot_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    if twoPieceBool.get() == False:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        heightTop = topPieceData[2].get().strip()
                        materialThicknessBottom = 0
                        materialTypeBottom = ""
                        heightBottom = 0
                    elif twoPieceBool.get() == True:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        heightTop = topPieceData[2].get().strip()
                        materialThicknessBottom = bottomPieceData[0].get().strip()
                        materialTypeBottom = bottomPieceData[1].get()
                        heightBottom = bottomPieceData[2].get().strip()

                    if not width or not heightTop or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(heightTop) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThicknessTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThicknessTop):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialTypeTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif twoPieceBool.get() == True:
                        if not heightBottom:
                            messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                        elif not is_number(heightBottom):
                            messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                        elif not materialThicknessBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                        elif not is_number(materialThicknessBottom):
                            messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                        elif not materialTypeBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                        else:
                            if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                                response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                                if response:  # If 'Yes' button is clicked
                                    new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                    tall_OvenSlot_cabinets[currentCount] = new_cabinet
                                    all_tall_parts_list.clear()
                                    tall_cabinets_list_copy = tall_cabinets_list[:]
                                    merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                    send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                    regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                                else:
                                    pass
                            else:
                                new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                tall_OvenSlot_cabinets[currentCount] = new_cabinet
                                all_tall_parts_list.clear()
                                tall_cabinets_list_copy = tall_cabinets_list[:]
                                merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                    else:
                        if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                            response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                            if response:  # If 'Yes' button is clicked
                                new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                tall_OvenSlot_cabinets[currentCount] = new_cabinet
                                all_tall_parts_list.clear()
                                tall_cabinets_list_copy = tall_cabinets_list[:]
                                merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                            else:
                                pass
                        else:
                            new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                            tall_OvenSlot_cabinets[currentCount] = new_cabinet
                            all_tall_parts_list.clear()
                            tall_cabinets_list_copy = tall_cabinets_list[:]
                            merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                            send_cabinet_to_cutlist(category, current_count, cabinet_type)
                            regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)

            if cabinet_type == "Pull Out":
                if tall_PullOut_cabinets[currentCount].completionStatus == True and tall_PullOut_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + tall_PullOut_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif tall_PullOut_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    drawerDepth = drawerDepth_entry_combobox.get().strip()

                    drawerHeightsList = []
                    for drawerHeight in drawerHeights_entries:
                        if is_number(drawerHeight.get()) and float(drawerHeight.get()) != 0:
                            drawerHeightsList.append(float(drawerHeight.get()))

                    if twoPieceBool.get() == False:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        railTypeTop = topPieceData[2].get()
                        heightTop = topPieceData[3].get().strip()
                        materialThicknessBottom = 0
                        materialTypeBottom = ""
                        heightBottom = 0
                        railTypeBottom = ""
                    elif twoPieceBool.get() == True:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        railTypeTop = topPieceData[2].get()
                        heightTop = topPieceData[3].get().strip()
                        materialThicknessBottom = bottomPieceData[0].get().strip()
                        materialTypeBottom = bottomPieceData[1].get()
                        railTypeBottom = bottomPieceData[2].get()
                        heightBottom = bottomPieceData[3].get().strip()

                    if not width or not heightTop or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(heightTop) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThicknessTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThicknessTop):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialTypeTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif not railTypeTop:
                        messagebox.showwarning("Missing Information", "Please specify a Rail Type.")
                    elif not drawerDepth:
                        messagebox.showwarning("Missing Information", "Please specify a Drawer Depth.")
                    elif not is_number(drawerDepth):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Drawer Depth.")
                    elif int(drawerQty_var_label["text"]) == 0:
                        messagebox.showwarning("Invalid Input", "Drawer Quantity must be greater than 0.")
                    elif twoPieceBool.get() == True:
                        if not heightBottom:
                            messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                        # elif not is_number(heightBottom):
                        #     messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                        elif not materialThicknessBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                        elif not is_number(materialThicknessBottom):
                            messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                        elif not materialTypeBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                        elif not railTypeBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Rail Type.")
                        else:
                            if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                                response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                                if response:  # If 'Yes' button is clicked
                                    new_cabinet = CabinetTallDrawer(category, cabinet_type, currentCount, float(width_entry.get()), float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), railTypeTop, railTypeBottom, twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                    tall_PullOut_cabinets[currentCount] = new_cabinet
                                    all_tall_parts_list.clear()
                                    tall_cabinets_list_copy = tall_cabinets_list[:]
                                    merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                    send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                    regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                                else:
                                    pass
                            else:
                                new_cabinet = CabinetTallDrawer(category, cabinet_type, currentCount, float(width_entry.get()), float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), railTypeTop, railTypeBottom, twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                tall_PullOut_cabinets[currentCount] = new_cabinet
                                all_tall_parts_list.clear()
                                tall_cabinets_list_copy = tall_cabinets_list[:]
                                merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                    else:
                        if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                            response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                            if response:  # If 'Yes' button is clicked
                                new_cabinet = CabinetTallDrawer(category, cabinet_type, currentCount, float(width_entry.get()), float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), railTypeTop, railTypeBottom, twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                tall_PullOut_cabinets[currentCount] = new_cabinet
                                all_tall_parts_list.clear()
                                tall_cabinets_list_copy = tall_cabinets_list[:]
                                merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)
                            else:
                                pass
                        else:
                            new_cabinet = CabinetTallDrawer(category, cabinet_type, currentCount, float(width_entry.get()), float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), railTypeTop, railTypeBottom, twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                            tall_PullOut_cabinets[currentCount] = new_cabinet
                            all_tall_parts_list.clear()
                            tall_cabinets_list_copy = tall_cabinets_list[:]
                            merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)
                            send_cabinet_to_cutlist(category, current_count, cabinet_type)
                            regenerate_tall_count(cabinet_type, current_count, given_cabinet_list)

        if category == "Vanity":
            if cabinet_type == "Full Door":
                if vanity_FullDoor_cabinets[currentCount].completionStatus == True and vanity_FullDoor_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + vanity_FullDoor_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif vanity_FullDoor_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()

                    if not width or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    else:
                        new_cabinet = CabinetFullDoor(category, cabinet_type, currentCount, float(width_entry.get()), float(height_entry.get()), float(depth_entry.get()), int(shelfQty_entry.get()), float(toeKick_entry.get()), False, drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        vanity_FullDoor_cabinets[currentCount] = new_cabinet
                        all_vanity_parts_list.clear()
                        vanity_cabinets_list_copy = vanity_cabinets_list[:]
                        merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_vanity_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "Drawers":
                if vanity_Drawers_cabinets[currentCount].completionStatus == True and vanity_Drawers_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + vanity_Drawers_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif vanity_Drawers_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    drawerDepth = drawerDepth_entry_combobox.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()
                    railType = rail_type_combobox.get().strip()

                    drawerHeightsList = []
                    for drawerHeight in drawerHeights_entries:
                        if is_number(drawerHeight.get()) and float(drawerHeight.get()) != 0:
                            drawerHeightsList.append(float(drawerHeight.get()))

                    if not width or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not drawerDepth:
                        messagebox.showwarning("Missing Information", "Please specify a Drawer Depth.")
                    elif not is_number(drawerDepth):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Drawer Depth.")
                    elif int(drawerQty_var_label["text"]) == 0:
                        messagebox.showwarning("Invalid Input", "Drawer Quantity must be greater than 0.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif not railType:
                        messagebox.showwarning("Missing Information", "Please specify a Rail Type.")
                    else:
                        new_cabinet = CabinetDrawers(category, cabinet_type, currentCount, float(width_entry.get()), float(height_entry.get()), float(depth_entry.get()), int(drawerQty_var_label["text"]), drawerHeightsList, float(drawerDepth_entry_combobox.get()), float(toeKick_entry.get()), rail_type_combobox.get(), False, False, float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        vanity_Drawers_cabinets[currentCount] = new_cabinet
                        all_vanity_parts_list.clear()
                        vanity_cabinets_list_copy = vanity_cabinets_list[:]
                        merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_vanity_count(cabinet_type, current_count, given_cabinet_list)

            elif cabinet_type == "1Door 1Drawer":
                if vanity_1Door1Drawer_cabinets[currentCount].completionStatus == True and vanity_1Door1Drawer_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + vanity_1Door1Drawer_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif vanity_1Door1Drawer_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    height = height_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    drawerDepth = drawerDepth_entry_combobox.get().strip()
                    drawerHeight = drawerHeight_entry.get().strip()
                    materialThickness = material_thickness_combobox.get().strip()
                    materialType = material_type_combobox.get().strip()
                    railType = rail_type_combobox.get().strip()

                    if not width or not height or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(height) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not drawerDepth:
                        messagebox.showwarning("Missing Information", "Please specify a Drawer Depth.")
                    elif not is_number(drawerDepth):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Drawer Depth.")
                    elif not drawerHeight:
                        messagebox.showwarning("Missing Information", "Please specify a Drawer Height.")
                    elif not is_number(drawerHeight):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Drawer Height.")
                    elif not materialThickness:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThickness):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialType:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif not railType:
                        messagebox.showwarning("Missing Information", "Please specify a Rail Type.")
                    else:
                        new_cabinet = Cabinet1D1D(category, cabinet_type, currentCount, float(width_entry.get()), float(height_entry.get()), float(depth_entry.get()), float(drawerHeight_entry.get()), float(drawerDepth_entry_combobox.get()), int(shelfQty_entry.get()), float(toeKick_entry.get()), rail_type_combobox.get(), drillBool.get(), routerBool.get(), float(material_thickness_combobox.get()), material_type_combobox.get(), False, True)
                        vanity_1Door1Drawer_cabinets[currentCount] = new_cabinet
                        all_vanity_parts_list.clear()
                        vanity_cabinets_list_copy = vanity_cabinets_list[:]
                        merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)
                        send_cabinet_to_cutlist(category, current_count, cabinet_type)
                        regenerate_vanity_count(cabinet_type, current_count, given_cabinet_list)

            if cabinet_type == "Linen Tower":
                if vanity_LinenTower_cabinets[currentCount].completionStatus == True and vanity_LinenTower_cabinets[currentCount].editable == False:
                    messagebox.showwarning("Invalid Input", "The cabinet is already in the cutlist as " + vanity_LinenTower_cabinets[current_count].fullName + ".\nUse the Edit button to edit the cabinet or create a new one.")

                elif vanity_LinenTower_cabinets[currentCount].editable == True:
                    width = width_entry.get().strip()
                    depth = depth_entry.get().strip()
                    shelfQty = shelfQty_entry.get().strip()
                    toeKick = toeKick_entry.get().strip()
                    if twoPieceBool.get() == False:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        heightTop = topPieceData[2].get().strip()
                        materialThicknessBottom = 0
                        materialTypeBottom = ""
                        heightBottom = 0
                    elif twoPieceBool.get() == True:
                        materialThicknessTop = topPieceData[0].get().strip()
                        materialTypeTop = topPieceData[1].get()
                        heightTop = topPieceData[2].get().strip()
                        materialThicknessBottom = bottomPieceData[0].get().strip()
                        materialTypeBottom = bottomPieceData[1].get()
                        heightBottom = bottomPieceData[2].get().strip()

                    if not width or not heightTop or not depth:
                        messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                    elif not is_number(width) or not is_number(heightTop) or not is_number(depth):
                        messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                    elif not shelfQty:
                        messagebox.showwarning("Missing Information", "Please specify number of Shelves.")
                    elif not is_number(shelfQty):
                        messagebox.showwarning("Invalid Input", "Please enter valid number for Shelf Quantity.")
                    elif not toeKick:
                        messagebox.showwarning("Missing Information", "Please specify a Toe Kick height.")
                    elif not is_number(toeKick):
                        messagebox.showwarning("Invalid Input", "Please enter a valid number for Toe Kick height.")
                    elif not materialThicknessTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                    elif not is_number(materialThicknessTop):
                        messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                    elif not materialTypeTop:
                        messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                    elif twoPieceBool.get() == True:
                        if not heightBottom:
                            messagebox.showwarning("Missing Information", "Please fill in all width, height, and depth fields.")
                        elif not is_number(heightBottom):
                            messagebox.showwarning("Invalid Input", "Please enter valid numbers for width, height, and depth.")
                        elif not materialThicknessBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Thickness.")
                        elif not is_number(materialThicknessBottom):
                            messagebox.showwarning("Invalid Input", "Please specify a valid number for Material Thickness.")
                        elif not materialTypeBottom:
                            messagebox.showwarning("Missing Information", "Please specify a Material Type.")
                        else:
                            if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                                response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\nWould you like to continue?")
                                if response:  # If 'Yes' button is clicked
                                    new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                    vanity_LinenTower_cabinets[currentCount] = new_cabinet
                                    all_vanity_parts_list.clear()
                                    vanity_cabinets_list_copy = vanity_cabinets_list[:]
                                    merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)
                                    send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                    regenerate_vanity_count(cabinet_type, current_count, given_cabinet_list)
                                else:
                                    pass
                            else:
                                new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                vanity_LinenTower_cabinets[currentCount] = new_cabinet
                                all_vanity_parts_list.clear()
                                vanity_cabinets_list_copy = vanity_cabinets_list[:]
                                merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_vanity_count(cabinet_type, current_count, given_cabinet_list)
                    else:
                        if (float(heightTop) + float(heightBottom)) > float(total_cabinet_height.get()):
                            response = messagebox.askyesno("Warning", "Cabinet: " + category + ", " + cabinet_type + " " + str(currentCount + 1) + " has a height greater than total cabinet height specified.\n\nWould you like to continue?")
                            if response:  # If 'Yes' button is clicked
                                new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                                vanity_LinenTower_cabinets[currentCount] = new_cabinet
                                all_vanity_parts_list.clear()
                                vanity_cabinets_list_copy = vanity_cabinets_list[:]
                                merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)
                                send_cabinet_to_cutlist(category, current_count, cabinet_type)
                                regenerate_vanity_count(cabinet_type, current_count, given_cabinet_list)
                            else:
                                pass
                        else:
                            new_cabinet = CabinetTall(category, cabinet_type, currentCount, float(width_entry.get()),  float(heightTop), float(heightBottom), float(depth_entry.get()), float(shelfQty_entry.get()), float(toeKick_entry.get()), twoPieceBool.get(), drillBool.get(), routerBool.get(), float(materialThicknessTop), float(materialThicknessBottom), materialTypeTop, materialTypeBottom, False, True)
                            vanity_LinenTower_cabinets[currentCount] = new_cabinet
                            all_vanity_parts_list.clear()
                            vanity_cabinets_list_copy = vanity_cabinets_list[:]
                            merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)
                            send_cabinet_to_cutlist(category, current_count, cabinet_type)
                            regenerate_vanity_count(cabinet_type, current_count, given_cabinet_list)

        # send_cabinet_to_cutlist(category, current_count, cabinet_type)
        # regenerate_base_count(cabinet_type, current_count, given_cabinet_list)

    if category == "Base": #----------------------------------------------------------------------------------- Base -----------------------------------------------------------------------------------//
        if cabinet_type == "Full Door": #------------------------------------------------------------- Base: FullDoor -------------------------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not base_FullDoor_cabinets:
                    workspace_base_FullDoor_frame.grid(row=0, column=0, sticky=W+E)
                    workspace_base_FullDoor_frame.bind("<MouseWheel>", on_canvas_mousewheel)

                if action == "add":
                    new_cabinet = CabinetFullDoor(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, False, False, False, 0, "", True, False)
                    base_FullDoor_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    base_FullDoor_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_base_FullDoor_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                cabinet_frame.bind("<MouseWheel>", on_canvas_mousewheel)

                #-------------------------------------------------- Base: FullDoor: Defining Buttons Frame and Buttons --------------------------------------------------//
                # Create a nested frame for the button
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed
                button_frame.bind("<MouseWheel>", on_canvas_mousewheel)

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, base_FullDoor_cabinets))
                edit_cabinet_button.bind("<MouseWheel>", on_canvas_mousewheel)

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(base_FullDoor_cabinets))
                send_cabinet_button.bind("<MouseWheel>", on_canvas_mousewheel)

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_base_count(cabinet_type, current_count, base_FullDoor_cabinets, "delete one"))
                delete_cabinet_button.bind("<MouseWheel>", on_canvas_mousewheel)

                #------------------------------------------------- Base: FullDoor: cabinet properties frame --------------------------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=base_FullDoor_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")
                cabinet_properties_frame.bind("<MouseWheel>", on_canvas_mousewheel)

                #-------------------------------------------------- Base: FullDoor: top frame --------------------------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)
                options_frame.bind("<MouseWheel>", on_canvas_mousewheel)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                materialThickness_label.bind("<MouseWheel>", on_canvas_mousewheel)
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                material_thickness_combobox.bind("<MouseWheel>", on_canvas_mousewheel)
                def update_material_thickness(event): # Unnecessary function, check if it can be removed.
                    selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(base_FullDoor_cabinets[current_count].materialThickness)
                if base_FullDoor_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                materialType_label.bind("<MouseWheel>", on_canvas_mousewheel)
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=3, sticky="w")
                material_type_combobox.set(material_type_var.get())
                material_type_combobox.bind("<MouseWheel>", on_canvas_mousewheel)
                def update_material_type(event): # Unnecessary function, check if it can be removed.
                    selected_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(base_FullDoor_cabinets[current_count].materialType)
                if base_FullDoor_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=4, padx = (279,5), sticky=N+E)
                completionStatus_label.bind("<MouseWheel>", on_canvas_mousewheel)
                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True and base_FullDoor_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=4, padx = (186,5), sticky=N+E)
                elif base_FullDoor_cabinets[current_count].completionStatus == True and base_FullDoor_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=4, padx = (220,5), sticky=N+E)

                #-------------------------------------------------- Base: FullDoor: mid frame --------------------------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)
                mid_frame.bind("<MouseWheel>", on_canvas_mousewheel)

                width_label = Label(mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_label.bind("<MouseWheel>", on_canvas_mousewheel)
                width_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                width_entry.bind("<MouseWheel>", on_canvas_mousewheel)
                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, base_FullDoor_cabinets[current_count].width)
                if base_FullDoor_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                height_label.bind("<MouseWheel>", on_canvas_mousewheel)
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=3, padx=10, sticky="w")
                height_entry.bind("<MouseWheel>", on_canvas_mousewheel)
                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, base_FullDoor_cabinets[current_count].height)
                elif action == "add" or base_FullDoor_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "34.75")
                if base_FullDoor_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                depth_label.bind("<MouseWheel>", on_canvas_mousewheel)
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=5, padx=10, sticky="w")
                depth_entry.bind("<MouseWheel>", on_canvas_mousewheel)
                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, base_FullDoor_cabinets[current_count].depth)
                elif action == "add" or base_FullDoor_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "23.75")
                if base_FullDoor_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                shelfQty_label.bind("<MouseWheel>", on_canvas_mousewheel)
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=1, column=1, padx=10, sticky="w")
                shelfQty_entry.bind("<MouseWheel>", on_canvas_mousewheel)
                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, base_FullDoor_cabinets[current_count].shelfQty)
                elif action == "add" or base_FullDoor_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if base_FullDoor_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                toeKick_label.bind("<MouseWheel>", on_canvas_mousewheel)
                toeKick_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=3, padx=10, sticky="w")
                toeKick_entry.bind("<MouseWheel>", on_canvas_mousewheel)
                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, base_FullDoor_cabinets[current_count].toeKick)
                elif action == "add" or base_FullDoor_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if base_FullDoor_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #-------------------------------------------------- Base: FullDoor: toggle buttons --------------------------------------------------//
                toggleButtons_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(20,0), pady=(0,10), sticky=W+E)
                toggleButtons_frame.bind("<MouseWheel>", on_canvas_mousewheel)

                sinkBool = BooleanVar()
                sinkBool.set(False)
                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_sink_button():
                    if sink_checkButton["text"] == "⬜ Sink":
                        sink_checkButton["text"] = "✅ Sink"
                        sinkBool.set(True)
                    else:
                        sink_checkButton["text"] = "⬜ Sink"
                        sinkBool.set(False)
                sink_checkButton = Button(toggleButtons_frame, text="⬜ Sink", command=toggle_sink_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                sink_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                sink_checkButton.bind("<MouseWheel>", on_canvas_mousewheel)
                if base_FullDoor_cabinets[current_count].editable == False:
                    sink_checkButton.config(state="disabled")

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=1, padx=10, pady=10)
                drill_checkButton.bind("<MouseWheel>", on_canvas_mousewheel)
                if base_FullDoor_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=2, padx=10, pady=10)
                router_checkButton.bind("<MouseWheel>", on_canvas_mousewheel)
                if base_FullDoor_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and base_FullDoor_cabinets[current_count].completionStatus == True:
                    if base_FullDoor_cabinets[current_count].sink == True:
                        toggle_sink_button()
                    if base_FullDoor_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if base_FullDoor_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Base: FullDoor: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if base_FullDoor_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_FullDoor_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    base_FullDoor_cabinets.pop()  # Remove the latest item in the list
                    if not base_FullDoor_cabinets:
                        workspace_base_FullDoor_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if base_FullDoor_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_FullDoor_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not base_FullDoor_cabinets:
                        workspace_base_FullDoor_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_base_FullDoor_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del base_FullDoor_cabinets[currentCount]
                for child in workspace_base_FullDoor_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not base_FullDoor_cabinets:
                    workspace_base_FullDoor_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Drawers": #------------------------------------------------------------- Base: Drawers -------------------------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not base_Drawers_cabinets:
                    workspace_base_Drawers_frame.grid(row=1, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetDrawers(category, cabinet_type, currentCount, 0, 0, 0, 0, [0,0], 0, 0, "", False, False, 0, "", True, False)
                    base_Drawers_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    base_Drawers_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_base_Drawers_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #-------------------------------------------------- Base: Drawers: Defining Buttons Frame and Buttons --------------------------------------------------//
                # Create a nested frame for the button
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, base_Drawers_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(base_Drawers_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_base_count(cabinet_type, current_count, base_Drawers_cabinets, "delete one"))

                #-------------------------------------------------- Base: Drawers: cabinet properties frame --------------------------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=base_Drawers_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #-------------------------------------------------- Base: Drawers: top frame --------------------------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_material_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(base_Drawers_cabinets[current_count].materialThickness)
                if base_Drawers_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=3, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=4, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_material_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(base_Drawers_cabinets[current_count].materialType)
                if base_Drawers_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                empty_label = Label(options_frame, text="-", font=fontSegoeSmall, bg=plainWhite, fg=plainWhite)
                empty_label.grid(row=0, column=5, padx=5, pady=10)

                railType_label = Label(options_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                railType_label.grid(row=0, column=6, padx=(10, 0), pady=10, sticky="e")
                rail_type_combobox = ttk.Combobox(options_frame, width=12, values=list(rail_type_options.keys()), state="readonly")
                rail_type_combobox.grid(row=0, column=7, sticky="w")
                rail_type_combobox.set(rail_type_var.get())
                def update_rail_type(event):
                    selected_rail_type = rail_type_combobox.get()
                rail_type_combobox.bind("<<ComboboxSelected>>", update_rail_type)
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    rail_type_combobox.set(base_Drawers_cabinets[current_count].railType)
                if base_Drawers_cabinets[current_count].editable == False:
                    rail_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=9, padx=(27,5), pady=(0,5), sticky=N+E)
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True and base_Drawers_cabinets[current_count].editable == False:
                    completionStatus_label.config(text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=7, padx=(85,5), pady=(0,5), sticky=N+E)

                    materialThickness_label.grid(row=1, column=0, padx=(10, 0), pady=(0,10), sticky="e")
                    material_thickness_combobox.grid(row=1, column=1, pady=(0,10), sticky="w")
                    materialType_label.grid(row=1, column=3, padx=(3, 0), pady=(0,10), sticky="e")
                    material_type_combobox.grid(row=1, column=4, pady=(0,10), sticky="w")
                    empty_label.grid(row=1, column=5, padx=5, pady=(0,10))
                    railType_label.grid(row=1, column=6, padx=(10, 0), pady=(0,10), sticky="e")
                    rail_type_combobox.grid(row=1, column=7, pady=(0,10), sticky="w")

                elif base_Drawers_cabinets[current_count].completionStatus == True and base_Drawers_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=7, padx=(119,5), pady=(0,5), sticky=N+E)

                    materialThickness_label.grid(row=1, column=0, padx=(10, 0), pady=(0,10), sticky="e")
                    material_thickness_combobox.grid(row=1, column=1, pady=(0,10), sticky="w")
                    materialType_label.grid(row=1, column=3, padx=(3, 0), pady=(0,10), sticky="e")
                    material_type_combobox.grid(row=1, column=4, pady=(0,10), sticky="w")
                    empty_label.grid(row=1, column=5, padx=5, pady=(0,10))
                    railType_label.grid(row=1, column=6, padx=(10, 0), pady=(0,10), sticky="e")
                    rail_type_combobox.grid(row=1, column=7, pady=(0,10), sticky="w")

                #-------------------------------------------------- Base: Drawers: mid frame --------------------------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                mid_top_frame = Frame(mid_frame, bg=plainWhite)
                mid_top_frame.grid(row=0, column=0, sticky=N+W+E)

                width_label = Label(mid_top_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, base_Drawers_cabinets[current_count].width)
                if base_Drawers_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_top_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, base_Drawers_cabinets[current_count].height)
                elif action == "add" or base_Drawers_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "34.75")
                if base_Drawers_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_top_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=5, columnspan=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, base_Drawers_cabinets[current_count].depth)
                elif action == "add" or base_Drawers_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "23.75")
                if base_Drawers_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_top_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, base_Drawers_cabinets[current_count].toeKick)
                elif action == "add" or base_Drawers_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if base_Drawers_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                drawerDepth_label = Label(mid_top_frame, text="Drawer Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerDepth_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                drawerDepth_entry_combobox = ttk.Combobox(mid_top_frame, width=5, values=kitchen_rail_size_options)
                drawerDepth_entry_combobox.grid(row=1, column=3, padx=10, sticky="w")
                drawerDepth_entry_combobox.set(kitchen_rail_size_var.get())
                def update_drawerDepth_entry_combobox(event):
                    selected_drawerDepth = drawerDepth_entry_combobox.get()  # Use get() to retrieve the selected value
                drawerDepth_entry_combobox.bind("<<ComboboxSelected>>", update_drawerDepth_entry_combobox)
                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    drawerDepth_entry_combobox.set(base_Drawers_cabinets[current_count].drawerDepth)
                if base_Drawers_cabinets[current_count].editable == False:
                    drawerDepth_entry_combobox.config(state="disabled")

                #-------------------------------------------------- Base: Drawers: drawerHeights frame --------------------------------------------------//
                drawerHeights_frame = LabelFrame(mid_frame, text="Drawer Heights", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                drawerHeights_frame.grid(row=1, column=0, padx=15, pady=(0,15), sticky=W+E)

                drawerHeights_entries = []

                def increment_drawer_qty(drawerHeight):
                    current_qty = int(drawerQty_var_label["text"])
                    new_qty = current_qty + 1
                    drawerQty_var_label["text"] = str(new_qty)
                    create_drawer_height_entry(new_qty, drawerHeight)  # Create a new drawer entry
                    update_drawer_height_entries()

                def decrement_drawer_qty():
                    current_qty = int(drawerQty_var_label["text"])
                    if current_qty > 1:
                        new_qty = current_qty - 1
                        drawerQty_var_label["text"] = str(new_qty)
                        remove_drawer_height_entry()  # Remove the last drawer entry
                        update_drawer_height_entries()

                def create_drawer_height_entry(entry_number, drawerHeight):
                    row = (entry_number-1) // 4  # Calculate the row based on the entry_number
                    column = (entry_number-1) % 4  # Calculate the column based on the entry_number

                    single_frame = Frame(drawerHeights_frame, bg=plainWhite)
                    single_frame.grid(row=row, column=column, sticky="w")

                    drawerNum_label = Label(single_frame, text="#" + str(entry_number), font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                    drawerNum_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                    drawer_height_entry = Entry(single_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                    drawer_height_entry.grid(row=0, column=1, padx=10, sticky="w")
                    drawer_height_entry.insert(0, drawerHeight)
                    if base_Drawers_cabinets[current_count].editable == False:
                        drawer_height_entry.config(state="readonly", fg=frontHighlightGray)

                    # Add the entry to the drawerHeights list if it's not empty. (this is checked in create_cabinet_object)
                    drawerHeights_entries.append(drawer_height_entry)

                def remove_drawer_height_entry():
                    last_entry = drawerHeights_frame.winfo_children()[-1]  # Get the last entry widget
                    last_entry.destroy()
                    # Remove the corresponding entry from the drawerHeights list
                    if drawerHeights_entries:
                        drawerHeights_entries.pop()

                def update_drawer_height_entries():
                    if action == "add" or base_Drawers_cabinets[current_count].completionStatus == False:
                        if len(drawerHeights_entries) == 1:
                            drawerHeights_entries[0].delete(0, 'end')
                            drawerHeights_entries[0].insert(0, "4.5")
                        elif len(drawerHeights_entries) > 1:
                            calculated_drawerHeight = (float(height_entry.get()) - 16.75) / (len(drawerHeights_entries) - 1)
                            for i in range(len(drawerHeights_entries)):
                                if i != 0:
                                    drawerHeights_entries[i].delete(0, 'end')
                                    drawerHeights_entries[i].insert(0, str(calculated_drawerHeight))

                drawerQty_label = Label(mid_top_frame, text="Drawer#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerQty_label.grid(row=1, column=4, padx=(10, 0), pady=10, sticky="e")

                drawerDecrement_button = Button(mid_top_frame, text="-", command=decrement_drawer_qty, width=3, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drawerDecrement_button.grid(row=1, column=5, padx=0, pady=10, sticky="e")

                drawerQty_var_label = Label(mid_top_frame, text="0", width=2, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerQty_var_label.grid(row=1, column=6, padx=0, pady=10)

                drawerIncrement_button = Button(mid_top_frame, text="+", command= lambda: increment_drawer_qty("0"), width=3, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drawerIncrement_button.grid(row=1, column=7, padx=0, pady=10, sticky="w")

                if action == "repopulate parent frame" and base_Drawers_cabinets[current_count].completionStatus == True:
                    for drawerHeight in base_Drawers_cabinets[current_count].drawerHeights:
                        increment_drawer_qty(drawerHeight)
                elif action == "add" or base_Drawers_cabinets[current_count].completionStatus == False:
                    increment_drawer_qty("4.5")
                    increment_drawer_qty("9")
                    increment_drawer_qty("9")
                if base_Drawers_cabinets[current_count].editable == False:
                    drawerDecrement_button.config(state="disabled")
                    drawerIncrement_button.config(state="disabled")

            #-------------------------------------------------- Base: Drawers: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if base_Drawers_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_Drawers_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    base_Drawers_cabinets.pop()  # Remove the latest item in the list
                    if not base_Drawers_cabinets:
                        workspace_base_Drawers_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if base_Drawers_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_Drawers_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not base_Drawers_cabinets:
                        workspace_base_Drawers_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_base_Drawers_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del base_Drawers_cabinets[currentCount]
                for child in workspace_base_Drawers_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not base_Drawers_cabinets:
                    workspace_base_Drawers_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "1Door 1Drawer": #------------------------------------------------------------- Base: 1D1D -------------------------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not base_1D1D_cabinets:
                    workspace_base_1D1D_frame.grid(row=2, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = Cabinet1D1D(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, 0, 0, "", False, False, 0, "", True, False)
                    base_1D1D_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    base_1D1D_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_base_1D1D_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Base: 1D1D: Defining Buttons Frame and Buttons --------------------------------------------------//
                # Create a nested frame for the button
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, base_1D1D_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(base_1D1D_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_base_count(cabinet_type, current_count, base_1D1D_cabinets, "delete one"))

                #------------------------------- Base: 1D1D: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=base_1D1D_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Base: 1D1D: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_material_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(base_1D1D_cabinets[current_count].materialThickness)
                if base_1D1D_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=3, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=4, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_material_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(base_1D1D_cabinets[current_count].materialType)
                if base_1D1D_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                empty_label = Label(options_frame, text="-", font=fontSegoeSmall, bg=plainWhite, fg=plainWhite)
                empty_label.grid(row=0, column=5, padx=5, pady=10)

                railType_label = Label(options_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                railType_label.grid(row=0, column=6, padx=(10, 0), pady=10, sticky="e")
                rail_type_combobox = ttk.Combobox(options_frame, width=12, values=list(rail_type_options.keys()), state="readonly")
                rail_type_combobox.grid(row=0, column=7, sticky="w")
                rail_type_combobox.set(rail_type_var.get())
                def update_rail_type(event):
                    selected_rail_type = rail_type_combobox.get()
                rail_type_combobox.bind("<<ComboboxSelected>>", update_rail_type)
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    rail_type_combobox.set(base_1D1D_cabinets[current_count].railType)
                if base_1D1D_cabinets[current_count].editable == False:
                    rail_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=9, padx=(27,5), pady=(0,5), sticky=N+E)
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True and base_1D1D_cabinets[current_count].editable == False:
                    completionStatus_label.config(text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=7, padx=(85,5), pady=(0,5), sticky=N+E)

                    materialThickness_label.grid(row=1, column=0, padx=(10, 0), pady=(0,10), sticky="e")
                    material_thickness_combobox.grid(row=1, column=1, pady=(0,10), sticky="w")
                    materialType_label.grid(row=1, column=3, padx=(3, 0), pady=(0,10), sticky="e")
                    material_type_combobox.grid(row=1, column=4, pady=(0,10), sticky="w")
                    empty_label.grid(row=1, column=5, padx=5, pady=(0,10))
                    railType_label.grid(row=1, column=6, padx=(10, 0), pady=(0,10), sticky="e")
                    rail_type_combobox.grid(row=1, column=7, pady=(0,10), sticky="w")

                elif base_1D1D_cabinets[current_count].completionStatus == True and base_1D1D_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=7, padx=(119,5), pady=(0,5), sticky=N+E)

                    materialThickness_label.grid(row=1, column=0, padx=(10, 0), pady=(0,10), sticky="e")
                    material_thickness_combobox.grid(row=1, column=1, pady=(0,10), sticky="w")
                    materialType_label.grid(row=1, column=3, padx=(3, 0), pady=(0,10), sticky="e")
                    material_type_combobox.grid(row=1, column=4, pady=(0,10), sticky="w")
                    empty_label.grid(row=1, column=5, padx=5, pady=(0,10))
                    railType_label.grid(row=1, column=6, padx=(10, 0), pady=(0,10), sticky="e")
                    rail_type_combobox.grid(row=1, column=7, pady=(0,10), sticky="w")

                #------------------------------- Base: 1D1D: mid frame -------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                width_label = Label(mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, base_1D1D_cabinets[current_count].width)
                if base_1D1D_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, base_1D1D_cabinets[current_count].height)
                if action == "add" or base_1D1D_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "34.75")
                if base_1D1D_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, base_1D1D_cabinets[current_count].depth)
                if action == "add" or base_1D1D_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "23.75")
                if base_1D1D_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, base_1D1D_cabinets[current_count].toeKick)
                if action == "add" or base_1D1D_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if base_1D1D_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                drawerDepth_label = Label(mid_frame, text="Drawer Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerDepth_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                drawerDepth_entry_combobox = ttk.Combobox(mid_frame, width=5, values=kitchen_rail_size_options)
                drawerDepth_entry_combobox.grid(row=1, column=3, padx=10, sticky="w")
                drawerDepth_entry_combobox.set(kitchen_rail_size_var.get())
                def update_drawerDepth_entry_combobox(event):
                    selected_drawerDepth = drawerDepth_entry_combobox.get()  # Use get() to retrieve the selected value
                drawerDepth_entry_combobox.bind("<<ComboboxSelected>>", update_drawerDepth_entry_combobox)
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    drawerDepth_entry_combobox.set(base_1D1D_cabinets[current_count].drawerDepth)
                if base_1D1D_cabinets[current_count].editable == False:
                    drawerDepth_entry_combobox.config(state="disabled")

                drawerHeight_label = Label(mid_frame, text="Drawer Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerHeight_label.grid(row=1, column=4, padx=(10, 0), pady=10, sticky="e")
                drawerHeight_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                drawerHeight_entry.grid(row=1, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    drawerHeight_entry.insert(0, base_1D1D_cabinets[current_count].drawerHeight)
                if action == "add" or base_1D1D_cabinets[current_count].completionStatus == False:
                    drawerHeight_entry.insert(0, "4.5")
                if base_1D1D_cabinets[current_count].editable == False:
                    drawerHeight_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=2, column=0, padx=(15, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=2, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, base_1D1D_cabinets[current_count].shelfQty)
                if action == "add" or base_1D1D_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if base_1D1D_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Base: 1D1D: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(20,0), pady=(0,10), sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if base_1D1D_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if base_1D1D_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and base_1D1D_cabinets[current_count].completionStatus == True:
                    if base_1D1D_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if base_1D1D_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Base: 1D1D: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if base_1D1D_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_1D1D_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    base_1D1D_cabinets.pop()  # Remove the latest item in the list
                    if not base_1D1D_cabinets:
                        workspace_base_1D1D_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if base_1D1D_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_1D1D_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not base_1D1D_cabinets:
                        workspace_base_1D1D_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_base_1D1D_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del base_1D1D_cabinets[currentCount]
                for child in workspace_base_1D1D_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not base_1D1D_cabinets:
                    workspace_base_1D1D_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Corner 90": #------------------------------------------ Base: Corner 90 ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not base_Corner90_cabinets:
                    workspace_base_Corner90_frame.grid(row=3, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetCorner(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, 0, 0, False, False, 0, "", True, False)
                    base_Corner90_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    base_Corner90_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_base_Corner90_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Base: Corner 90: Defining Buttons Frame and Buttons -------------------------------//
                # Create a nested frame for the button
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, base_Corner90_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(base_Corner90_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_base_count(cabinet_type, current_count, base_Corner90_cabinets, "delete one"))

                #------------------------------- Base: Corner 90: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=base_Corner90_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Base: Corner 90: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(base_Corner90_cabinets[current_count].materialThickness)
                if base_Corner90_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=3, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(base_Corner90_cabinets[current_count].materialType)
                if base_Corner90_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=4, padx = (279,5), sticky=N+E)
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True and base_Corner90_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=4, padx = (186,5), sticky=N+E)
                elif base_Corner90_cabinets[current_count].completionStatus == True and base_Corner90_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=4, padx = (220,5), sticky=N+E)

                #------------------------------- Base: Corner 90: mid frame -------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                widthLeft_label = Label(mid_frame, text="Width Left:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                widthLeft_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                widthLeft_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                widthLeft_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    widthLeft_entry.insert(0, base_Corner90_cabinets[current_count].width1)
                if base_Corner90_cabinets[current_count].editable == False:
                    widthLeft_entry.config(state="readonly", fg=frontHighlightGray)

                widthRight_label = Label(mid_frame, text="Width Right:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                widthRight_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                widthRight_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                widthRight_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    widthRight_entry.insert(0, base_Corner90_cabinets[current_count].width2)
                if base_Corner90_cabinets[current_count].editable == False:
                    widthRight_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, base_Corner90_cabinets[current_count].height)
                if action == "add" or base_Corner90_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "34.75")
                if base_Corner90_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, base_Corner90_cabinets[current_count].depth)
                if action == "add" or base_Corner90_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "23.75")
                if base_Corner90_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=1, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, base_Corner90_cabinets[current_count].shelfQty)
                if action == "add" or base_Corner90_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if base_Corner90_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=4, padx=(10, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, base_Corner90_cabinets[current_count].toeKick)
                if action == "add" or base_Corner90_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if base_Corner90_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Base: Corner 90: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(15,0), pady=5, sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if base_Corner90_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if base_Corner90_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and base_Corner90_cabinets[current_count].completionStatus == True:
                    if base_Corner90_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if base_Corner90_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Base: Corner 90: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if base_Corner90_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_Corner90_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    base_Corner90_cabinets.pop()  # Remove the latest item in the list
                    if not base_Corner90_cabinets:
                        workspace_base_Corner90_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if base_Corner90_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_Corner90_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not base_Corner90_cabinets:
                        workspace_base_Corner90_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_base_Corner90_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del base_Corner90_cabinets[currentCount]
                for child in workspace_base_Corner90_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not base_Corner90_cabinets:
                    workspace_base_Corner90_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Corner Diagonal": #------------------------------------------ Base: Corner Diagonal ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not base_CornerDiagonal_cabinets:
                    workspace_base_CornerDiagonal_frame.grid(row=4, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetCorner(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, 0, 0, False, False, 0, "", True, False)
                    base_CornerDiagonal_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    base_CornerDiagonal_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_base_CornerDiagonal_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Base: Corner Diagonal: Defining Buttons Frame and Buttons -------------------------------//
                # Create a nested frame for the button
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, base_CornerDiagonal_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(base_CornerDiagonal_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_base_count(cabinet_type, current_count, base_CornerDiagonal_cabinets, "delete one"))

                #------------------------------- Base: Corner Diagonal: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=base_CornerDiagonal_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Base: Corner Diagonal: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(base_CornerDiagonal_cabinets[current_count].materialThickness)
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=3, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(base_CornerDiagonal_cabinets[current_count].materialType)
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=4, padx = (279,5), sticky=N+E)
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True and base_CornerDiagonal_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=4, padx = (186,5), sticky=N+E)
                elif base_CornerDiagonal_cabinets[current_count].completionStatus == True and base_CornerDiagonal_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=4, padx = (220,5), sticky=N+E)

                #------------------------------- Base: Corner Diagonal: mid frame -------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                widthLeft_label = Label(mid_frame, text="Width Left:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                widthLeft_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                widthLeft_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                widthLeft_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    widthLeft_entry.insert(0, base_CornerDiagonal_cabinets[current_count].width1)
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    widthLeft_entry.config(state="readonly", fg=frontHighlightGray)

                widthRight_label = Label(mid_frame, text="Width Right:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                widthRight_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                widthRight_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                widthRight_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    widthRight_entry.insert(0, base_CornerDiagonal_cabinets[current_count].width2)
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    widthRight_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, base_CornerDiagonal_cabinets[current_count].height)
                if action == "add" or base_CornerDiagonal_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "34.75")
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, base_CornerDiagonal_cabinets[current_count].depth)
                if action == "add" or base_CornerDiagonal_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "23.75")
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=1, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, base_CornerDiagonal_cabinets[current_count].shelfQty)
                if action == "add" or base_CornerDiagonal_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=4, padx=(10, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, base_CornerDiagonal_cabinets[current_count].toeKick)
                if action == "add" or base_CornerDiagonal_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Base: Corner Diagonal: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(15,0), pady=5, sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if base_CornerDiagonal_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and base_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    if base_CornerDiagonal_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if base_CornerDiagonal_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Base: Corner Diagonal: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if base_CornerDiagonal_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_CornerDiagonal_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    base_CornerDiagonal_cabinets.pop()  # Remove the latest item in the list
                    if not base_CornerDiagonal_cabinets:
                        workspace_base_CornerDiagonal_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if base_CornerDiagonal_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_CornerDiagonal_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not base_CornerDiagonal_cabinets:
                        workspace_base_CornerDiagonal_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_base_CornerDiagonal_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del base_CornerDiagonal_cabinets[currentCount]
                for child in workspace_base_CornerDiagonal_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not base_CornerDiagonal_cabinets:
                    workspace_base_CornerDiagonal_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Corner Blind": #------------------------------------------ Base: Corner Blind ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not base_CornerBlind_cabinets:
                    workspace_base_CornerBlind_frame.grid(row=5, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetCorner(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, 0, 0, False, False, 0, "", True, False)
                    base_CornerBlind_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    base_CornerBlind_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_base_CornerBlind_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Base: Corner Blind: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, base_CornerBlind_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(base_CornerBlind_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_base_count(cabinet_type, current_count, base_CornerBlind_cabinets, "delete one"))

                #------------------------------- Base: Corner Blind: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=base_CornerBlind_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Base: Corner Blind: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(base_CornerBlind_cabinets[current_count].materialThickness)
                if base_CornerBlind_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=3, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(base_CornerBlind_cabinets[current_count].materialType)
                if base_CornerBlind_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=4, padx = (279,5), sticky=N+E)
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True and base_CornerBlind_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=4, padx = (186,5), sticky=N+E)
                elif base_CornerBlind_cabinets[current_count].completionStatus == True and base_CornerBlind_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=4, padx = (220,5), sticky=N+E)

                #------------------------------- Base: Corner Blind: mid frame -------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                width_label = Label(mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, base_CornerBlind_cabinets[current_count].width1)
                if base_CornerBlind_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, base_CornerBlind_cabinets[current_count].height)
                if action == "add" or base_CornerBlind_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "34.75")
                if base_CornerBlind_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, base_CornerBlind_cabinets[current_count].depth)
                if action == "add" or base_CornerBlind_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "23.75")
                if base_CornerBlind_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, base_CornerBlind_cabinets[current_count].shelfQty)
                if action == "add" or base_CornerBlind_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if base_CornerBlind_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, base_CornerBlind_cabinets[current_count].toeKick)
                if action == "add" or base_CornerBlind_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if base_CornerBlind_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                fillerWidth_label = Label(mid_frame, text="fillerWidth:\n(Optional)", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                fillerWidth_label.grid(row=1, column=4, padx=(10, 0), pady=10, sticky="e")
                fillerWidth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                fillerWidth_entry.grid(row=1, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    fillerWidth_entry.insert(0, base_CornerBlind_cabinets[current_count].fillerWidth)
                if action == "add" or base_CornerBlind_cabinets[current_count].completionStatus == False:
                    fillerWidth_entry.insert(0, "0")
                if base_CornerBlind_cabinets[current_count].editable == False:
                    fillerWidth_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Base: Corner Blind: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(15,0), pady=5, sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if base_CornerBlind_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if base_CornerBlind_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and base_CornerBlind_cabinets[current_count].completionStatus == True:
                    if base_CornerBlind_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if base_CornerBlind_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Base: Corner Blind: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if base_CornerBlind_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_CornerBlind_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    base_CornerBlind_cabinets.pop()  # Remove the latest item in the list
                    if not base_CornerBlind_cabinets:
                        workspace_base_CornerBlind_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if base_CornerBlind_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_base_CornerBlind_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not base_CornerBlind_cabinets:
                        workspace_base_CornerBlind_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_base_CornerBlind_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del base_CornerBlind_cabinets[currentCount]
                for child in workspace_base_CornerBlind_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not base_CornerBlind_cabinets:
                    workspace_base_CornerBlind_frame.grid_forget()  # Hide the frame

    elif category == "Wall": #---------------------------------------------------------------- Wall ----------------------------------------------------------------//
        if cabinet_type == "Full Door": #------------------------------------------ Wall: Full Door ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not wall_FullDoor_cabinets:
                    workspace_wall_FullDoor_frame.grid(row=0, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetFullDoorWall(category, cabinet_type, currentCount, 0, 0, 0, 0, False, False, False, 0, "", True, False)
                    wall_FullDoor_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    wall_FullDoor_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_wall_FullDoor_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Wall: Full Door: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, wall_FullDoor_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(wall_FullDoor_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_wall_count(cabinet_type, current_count, wall_FullDoor_cabinets, "delete one"))

                #------------------------------- Wall: Full Door: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=wall_FullDoor_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Wall: Full Door: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and wall_FullDoor_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(wall_FullDoor_cabinets[current_count].materialThickness)
                if wall_FullDoor_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=3, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and wall_FullDoor_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(wall_FullDoor_cabinets[current_count].materialType)
                if wall_FullDoor_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=4, padx = (279,5), sticky=N+E)
                if action == "repopulate parent frame" and wall_FullDoor_cabinets[current_count].completionStatus == True and wall_FullDoor_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=4, padx = (186,5), sticky=N+E)
                elif wall_FullDoor_cabinets[current_count].completionStatus == True and wall_FullDoor_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=4, padx = (220,5), sticky=N+E)

                #------------------------------- Wall: Full Door: mid frame -------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                width_label = Label(mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_FullDoor_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, wall_FullDoor_cabinets[current_count].width)
                if wall_FullDoor_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_FullDoor_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, wall_FullDoor_cabinets[current_count].height)
                if action == "add" or wall_FullDoor_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, str((float(total_cabinet_height.get()) - 54)))
                if wall_FullDoor_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_FullDoor_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, wall_FullDoor_cabinets[current_count].depth)
                if action == "add" or wall_FullDoor_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "11.75") # Change based on cabinet height
                if wall_FullDoor_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_FullDoor_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, wall_FullDoor_cabinets[current_count].shelfQty)
                if action == "add" or wall_FullDoor_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if wall_FullDoor_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Wall: Full Door: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(15,0), pady=5, sticky=W+E)

                lightShelfBool = BooleanVar()
                lightShelfBool.set(False)
                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_lightShelf_button():
                    if lightShelf_checkButton["text"] == "⬜ lightShelf":
                        lightShelf_checkButton["text"] = "✅ lightShelf"
                        lightShelfBool.set(True)
                    else:
                        lightShelf_checkButton["text"] = "⬜ lightShelf"
                        lightShelfBool.set(False)
                lightShelf_checkButton = Button(toggleButtons_frame, text="⬜ lightShelf", command=toggle_lightShelf_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                lightShelf_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if wall_FullDoor_cabinets[current_count].editable == False:
                    lightShelf_checkButton.config(state="disabled")

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if wall_FullDoor_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=2, padx=10, pady=10)
                if wall_FullDoor_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and wall_FullDoor_cabinets[current_count].completionStatus == True:
                    if wall_FullDoor_cabinets[current_count].lightShelf == True:
                        toggle_lightShelf_button()
                    if wall_FullDoor_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if wall_FullDoor_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Wall: FullDoor: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if wall_FullDoor_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_wall_FullDoor_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    wall_FullDoor_cabinets.pop()  # Remove the latest item in the list
                    if not wall_FullDoor_cabinets:
                        workspace_wall_FullDoor_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if wall_FullDoor_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_wall_FullDoor_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not wall_FullDoor_cabinets:
                        workspace_wall_FullDoor_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_wall_FullDoor_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del wall_FullDoor_cabinets[currentCount]
                for child in workspace_wall_FullDoor_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not wall_FullDoor_cabinets:
                    workspace_wall_FullDoor_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Corner 90": #------------------------------------------ Wall: Corner 90 ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not wall_Corner90_cabinets:
                    workspace_wall_Corner90_frame.grid(row=1, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetCornerWall(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, False, False, False, 0, "", True, False)
                    wall_Corner90_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    wall_Corner90_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_wall_Corner90_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Wall: Corner 90: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, wall_Corner90_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(wall_Corner90_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_wall_count(cabinet_type, current_count, wall_Corner90_cabinets, "delete one"))

                #------------------------------- Wall: Corner 90: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=wall_Corner90_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Wall: Corner 90: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(wall_Corner90_cabinets[current_count].materialThickness)
                if wall_Corner90_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=3, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(wall_Corner90_cabinets[current_count].materialType)
                if wall_Corner90_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=4, padx = (279,5), sticky=N+E)
                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True and wall_Corner90_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=4, padx = (186,5), sticky=N+E)
                elif wall_Corner90_cabinets[current_count].completionStatus == True and wall_Corner90_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=4, padx = (220,5), sticky=N+E)

                #------------------------------- Wall: Corner 90: mid frame -------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                widthLeft_label = Label(mid_frame, text="Width Left:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                widthLeft_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                widthLeft_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                widthLeft_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True:
                    widthLeft_entry.insert(0, wall_Corner90_cabinets[current_count].width1)
                if wall_Corner90_cabinets[current_count].editable == False:
                    widthLeft_entry.config(state="readonly", fg=frontHighlightGray)

                widthRight_label = Label(mid_frame, text="Width Right:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                widthRight_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                widthRight_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                widthRight_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True:
                    widthRight_entry.insert(0, wall_Corner90_cabinets[current_count].width2)
                if wall_Corner90_cabinets[current_count].editable == False:
                    widthRight_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, wall_Corner90_cabinets[current_count].height)
                if action == "add" or wall_Corner90_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, str((float(total_cabinet_height.get()) - 54)))
                if wall_Corner90_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, wall_Corner90_cabinets[current_count].depth)
                if action == "add" or wall_Corner90_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "11.75")
                if wall_Corner90_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=1, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, wall_Corner90_cabinets[current_count].shelfQty)
                if action == "add" or wall_Corner90_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if wall_Corner90_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Wall: Corner 90: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(15,0), pady=5, sticky=W+E)

                lightShelfBool = BooleanVar()
                lightShelfBool.set(False)
                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_lightShelf_button():
                    if lightShelf_checkButton["text"] == "⬜ lightShelf":
                        lightShelf_checkButton["text"] = "✅ lightShelf"
                        lightShelfBool.set(True)
                    else:
                        lightShelf_checkButton["text"] = "⬜ lightShelf"
                        lightShelfBool.set(False)
                lightShelf_checkButton = Button(toggleButtons_frame, text="⬜ lightShelf", command=toggle_lightShelf_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                lightShelf_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if wall_Corner90_cabinets[current_count].editable == False:
                    lightShelf_checkButton.config(state="disabled")

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if wall_Corner90_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=2, padx=10, pady=10)
                if wall_Corner90_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and wall_Corner90_cabinets[current_count].completionStatus == True:
                    if wall_Corner90_cabinets[current_count].lightShelf == True:
                        toggle_lightShelf_button()
                    if wall_Corner90_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if wall_Corner90_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Wall: Corner 90: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if wall_Corner90_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_wall_Corner90_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    wall_Corner90_cabinets.pop()  # Remove the latest item in the list
                    if not wall_Corner90_cabinets:
                        workspace_wall_Corner90_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if wall_Corner90_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_wall_Corner90_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not wall_Corner90_cabinets:
                        workspace_wall_Corner90_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_wall_Corner90_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del wall_Corner90_cabinets[currentCount]
                for child in workspace_wall_Corner90_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not wall_Corner90_cabinets:
                    workspace_wall_Corner90_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Corner Diagonal": #------------------------------------------ Wall: Corner Diagonal ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not wall_CornerDiagonal_cabinets:
                    workspace_wall_CornerDiagonal_frame.grid(row=2, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetCornerWall(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, False, False, False, 0, "", True, False)
                    wall_CornerDiagonal_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    wall_CornerDiagonal_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_wall_CornerDiagonal_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Wall: Corner Diagonal: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, wall_CornerDiagonal_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(wall_CornerDiagonal_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_wall_count(cabinet_type, current_count, wall_CornerDiagonal_cabinets, "delete one"))

                #------------------------------- Wall: Corner Diagonal: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=wall_CornerDiagonal_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Wall: Corner Diagonal: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(wall_CornerDiagonal_cabinets[current_count].materialThickness)
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=3, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(wall_CornerDiagonal_cabinets[current_count].materialType)
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=4, padx = (279,5), sticky=N+E)
                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True and wall_CornerDiagonal_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=4, padx = (186,5), sticky=N+E)
                elif wall_CornerDiagonal_cabinets[current_count].completionStatus == True and wall_CornerDiagonal_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=4, padx = (220,5), sticky=N+E)

                #------------------------------- Wall: Corner Diagonal: mid frame -------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                cornerDiagonal_widths_frame = Frame(mid_frame, bg=plainWhite)
                cornerDiagonal_widths_frame.grid(row=0, column=0, columnspan=4, padx=(0,10), sticky=W+E)

                wall_cornerDiagonal_width_options = ["21 & 21", "24 & 24", "21 & 24", "24 & 21"]

                width_label = Label(cornerDiagonal_widths_frame, text="Width:  Left:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                widthLeft_combobox = ttk.Combobox(cornerDiagonal_widths_frame, width=8, values=wall_cornerDiagonal_width_options)
                widthLeft_combobox.grid(row=0, column=1, padx=5, sticky="w")
                widthLeft_combobox.set("21")
                def update_width(event):
                    if widthLeft_combobox.get() == "21 & 21" or widthRight_combobox.get() == "21 & 21":
                        widthLeft_combobox.set("21")
                        widthRight_combobox.set("21")
                    elif widthLeft_combobox.get() == "24 & 24" or widthRight_combobox.get() == "24 & 24":
                        widthLeft_combobox.set("24")
                        widthRight_combobox.set("24")
                    elif widthLeft_combobox.get() == "21 & 24" or widthRight_combobox.get() == "21 & 24":
                        widthLeft_combobox.set("21")
                        widthRight_combobox.set("24")
                    elif widthLeft_combobox.get() == "24 & 21" or widthRight_combobox.get() == "24 & 21":
                        widthLeft_combobox.set("24")
                        widthRight_combobox.set("21")
                widthLeft_combobox.bind("<<ComboboxSelected>>", update_width)
                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    widthLeft_combobox.set(wall_CornerDiagonal_cabinets[current_count].width1)
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    widthLeft_combobox.config(state="disabled")

                right_label = Label(cornerDiagonal_widths_frame, text="Right:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                right_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                widthRight_combobox = ttk.Combobox(cornerDiagonal_widths_frame, width=8, values=wall_cornerDiagonal_width_options)
                widthRight_combobox.grid(row=0, column=3, padx=5, sticky="w")
                widthRight_combobox.set("21")
                widthRight_combobox.bind("<<ComboboxSelected>>", update_width)
                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    widthRight_combobox.set(wall_CornerDiagonal_cabinets[current_count].width2)
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    widthRight_combobox.config(state="disabled")

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, wall_CornerDiagonal_cabinets[current_count].height)
                if action == "add" or wall_CornerDiagonal_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, str((float(total_cabinet_height.get()) - 54)))
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, wall_CornerDiagonal_cabinets[current_count].depth)
                if action == "add" or wall_CornerDiagonal_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "11.75")
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=1, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, wall_CornerDiagonal_cabinets[current_count].shelfQty)
                if action == "add" or wall_CornerDiagonal_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Wall: Corner Diagonal: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(15,0), pady=5, sticky=W+E)

                lightShelfBool = BooleanVar()
                lightShelfBool.set(False)
                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_lightShelf_button():
                    if lightShelf_checkButton["text"] == "⬜ lightShelf":
                        lightShelf_checkButton["text"] = "✅ lightShelf"
                        lightShelfBool.set(True)
                    else:
                        lightShelf_checkButton["text"] = "⬜ lightShelf"
                        lightShelfBool.set(False)
                lightShelf_checkButton = Button(toggleButtons_frame, text="⬜ lightShelf", command=toggle_lightShelf_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                lightShelf_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    lightShelf_checkButton.config(state="disabled")

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=2, padx=10, pady=10)
                if wall_CornerDiagonal_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and wall_CornerDiagonal_cabinets[current_count].completionStatus == True:
                    if wall_CornerDiagonal_cabinets[current_count].lightShelf == True:
                        toggle_lightShelf_button()
                    if wall_CornerDiagonal_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if wall_CornerDiagonal_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Wall: Corner Diagonal: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if wall_CornerDiagonal_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_wall_CornerDiagonal_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    wall_CornerDiagonal_cabinets.pop()  # Remove the latest item in the list
                    if not wall_CornerDiagonal_cabinets:
                        workspace_wall_CornerDiagonal_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if wall_CornerDiagonal_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_wall_CornerDiagonal_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not wall_CornerDiagonal_cabinets:
                        workspace_wall_CornerDiagonal_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_wall_CornerDiagonal_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del wall_CornerDiagonal_cabinets[currentCount]
                for child in workspace_wall_CornerDiagonal_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not wall_CornerDiagonal_cabinets:
                    workspace_wall_CornerDiagonal_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Microwave Slot": #------------------------------------------ Wall: Microwave Slot ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not wall_MicowaveSlot_cabinets:
                    workspace_wall_MicrowaveSlot_frame.grid(row=3, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetMicrowaveSlot(category, cabinet_type, current_count, 0, 0, 0, 0, 0, 0, False, False, False, False, 0, 0, "", "", True, False)
                    wall_MicowaveSlot_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    wall_MicowaveSlot_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_wall_MicrowaveSlot_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Wall: Microwave Slot: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, wall_MicowaveSlot_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(wall_MicowaveSlot_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_wall_count(cabinet_type, current_count, wall_MicowaveSlot_cabinets, "delete one"))

                #------------------------------- Wall: Microwave Slot: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=wall_MicowaveSlot_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Wall: Microwave Slot: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=(5,20), sticky=W+E)

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=6, padx = (156,5), sticky=N+E)
                if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True and wall_MicowaveSlot_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=6, padx = (65,5), sticky=N+E)
                elif wall_MicowaveSlot_cabinets[current_count].completionStatus == True and wall_MicowaveSlot_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=6, padx = (98,5), sticky=N+E)

                #------------------------------- Wall: Microwave Slot: mid frame -------------------------------//
                #-------------------- Microwave Slot: Left mid frame --------------------//
                right_mid_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                #-------------------- Microwave Slot: Declaring twoPieceData frames --------------------//
                top_right_mid_frame = LabelFrame(right_mid_frame, text="Upper Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                materialThickness_label = Label(top_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                material_thickness_combobox = ttk.Combobox(top_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=material_type_options, state="readonly")
                height_frame = Frame(top_right_mid_frame, bg=plainWhite)
                height_entry = Entry(height_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry = Entry(height_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                bottom_right_mid_frame = LabelFrame(right_mid_frame, text="Lower Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                material_thickness_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=material_type_options, state="readonly")
                height_bottom_frame = Frame(bottom_right_mid_frame, bg=plainWhite)
                height_bottom_entry = Entry(height_bottom_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_bottom_entry = Entry(height_bottom_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                twoPieceBool = BooleanVar()
                twoPieceBool.set(False)

                topPieceData = []
                bottomPieceData = []

                def toggle_twoPiece_button():
                    for widget in right_mid_frame.winfo_children():
                        widget.grid_forget()
                    right_mid_frame.grid_forget()

                    topPieceData.clear()
                    bottomPieceData.clear()

                    if twoPiece_checkButton["text"] == "⬜ Two Piece ":
                        twoPiece_checkButton["text"] = "✅ Two Piece "
                        arrow_Button.config(image=arrowUp_image)
                        twoPieceBool.set(True)

                        #-------------------- Microwave Slot: Top mid LabelFrame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=0, sticky=N+W)
                        top_right_mid_frame.config(text="Upper Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(wall_MicowaveSlot_cabinets[current_count].materialThicknessTop)
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, padx=(0, 10), sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(wall_MicowaveSlot_cabinets[current_count].materialTypeTop)
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        height_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        height_label = Label(height_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=1, padx=10, sticky="w")
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, wall_MicowaveSlot_cabinets[current_count].heightTop)
                        if action == "add" or wall_MicowaveSlot_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, str((float(total_cabinet_height.get()) - 54)/2)) # Divide cabinet_height-54 by two
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                        depth_label = Label(height_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        depth_label.grid(row=0, column=2, padx=(20, 0), pady=10, sticky="e")
                        depth_entry.grid(row=0, column=3, padx=10, sticky="w")
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            depth_entry.delete(0, 'end')
                            depth_entry.insert(0, wall_MicowaveSlot_cabinets[current_count].depthTop)
                        if action == "add" or wall_MicowaveSlot_cabinets[current_count].completionStatus == False:
                            depth_entry.delete(0, 'end')
                            depth_entry.insert(0, "23.75")
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            depth_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(depth_entry)

                        #-------------------- Microwave Slot: Bottom mid frame --------------------//
                        bottom_right_mid_frame.grid(row=2, column=0, padx=(20,10), pady=5, sticky=N+W)

                        materialThickness_bottom_label = Label(bottom_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialThickness_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_bottom_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_bottom_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_bottom_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_bottom_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            if wall_MicowaveSlot_cabinets[current_count].twoPiece == False:
                                material_thickness_bottom_combobox.set(material_thickness_var.get())
                            else:
                                material_thickness_bottom_combobox.set(wall_MicowaveSlot_cabinets[current_count].materialThicknessBottom)
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            material_thickness_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_thickness_bottom_combobox)

                        materialType_bottom_label = Label(bottom_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_bottom_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_bottom_combobox.grid(row=0, column=3, padx=(0, 10), sticky="w")
                        material_type_bottom_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_bottom_combobox.get()
                        material_type_bottom_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            if wall_MicowaveSlot_cabinets[current_count].twoPiece == False:
                                material_type_bottom_combobox.set(material_type_var.get())
                            else:
                                material_type_bottom_combobox.set(wall_MicowaveSlot_cabinets[current_count].materialTypeBottom)
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            material_type_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_type_bottom_combobox)

                        height_bottom_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        height_bottom_label = Label(height_bottom_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        height_bottom_entry.grid(row=0, column=1, padx=10, sticky="w")
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            if wall_MicowaveSlot_cabinets[current_count].twoPiece == False:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, str((float(total_cabinet_height.get()) - 54)/2)) # Divide cabinet_height-54 by two
                            else:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, wall_MicowaveSlot_cabinets[current_count].heightBottom)
                        if action == "add" or wall_MicowaveSlot_cabinets[current_count].completionStatus == False:
                            height_bottom_entry.delete(0, 'end')
                            height_bottom_entry.insert(0, str((float(total_cabinet_height.get()) - 54)/2)) # Divide cabinet_height-54 by two
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            height_bottom_entry.config(state="readonly", fg=frontHighlightGray)

                        bottomPieceData.append(height_bottom_entry)

                        depth_bottom_label = Label(height_bottom_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        depth_bottom_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                        depth_bottom_entry.grid(row=0, column=3, padx=10, sticky="w")
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            if wall_MicowaveSlot_cabinets[current_count].twoPiece == False:
                                depth_bottom_entry.delete(0, 'end')
                                depth_bottom_entry.insert(0, "23.75")
                            else:
                                depth_bottom_entry.delete(0, 'end')
                                depth_bottom_entry.insert(0, wall_MicowaveSlot_cabinets[current_count].depthBottom)
                        if action == "add" or wall_MicowaveSlot_cabinets[current_count].completionStatus == False:
                            depth_bottom_entry.delete(0, 'end')
                            depth_bottom_entry.insert(0, "23.75")
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            depth_bottom_entry.config(state="readonly", fg=frontHighlightGray)

                        bottomPieceData.append(depth_bottom_entry)

                    else:
                        twoPiece_checkButton["text"] = "⬜ Two Piece "
                        arrow_Button.config(image=arrowDown_image)
                        twoPieceBool.set(False)

                        #-------------------- Microwave Slot: Single mid frame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=0, sticky=N+W)
                        top_right_mid_frame.config(text="One Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(wall_MicowaveSlot_cabinets[current_count].materialThicknessTop)
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, padx=(0, 10), sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(wall_MicowaveSlot_cabinets[current_count].materialTypeTop)
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        height_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        height_label = Label(height_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=1, padx=10, sticky="w")
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, wall_MicowaveSlot_cabinets[current_count].heightTop)
                        if action == "add" or wall_MicowaveSlot_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, str(float(total_cabinet_height.get())-54))
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                        depth_label = Label(height_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        depth_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                        depth_entry.grid(row=0, column=3, padx=10, sticky="w")
                        if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                            depth_entry.delete(0, 'end')
                            depth_entry.insert(0, wall_MicowaveSlot_cabinets[current_count].depthTop)
                        if action == "add" or wall_MicowaveSlot_cabinets[current_count].completionStatus == False:
                            depth_entry.delete(0, 'end')
                            depth_entry.insert(0, "23.75")
                        if wall_MicowaveSlot_cabinets[current_count].editable == False:
                            depth_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(depth_entry)

                twoPiece_checkButton = Button(options_frame, text="✅ Two Piece ", command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                twoPiece_checkButton.grid(row=0, column=0, padx=(15,0), pady=(10, 0))
                arrow_Button = Button(options_frame, image=arrowDown_image, height=36, command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                arrow_Button.grid(row=0, column=1, pady=(10, 0))
                toggle_twoPiece_button()
                if wall_MicowaveSlot_cabinets[current_count].editable == False:
                    twoPiece_checkButton.config(state="disabled")
                    arrow_Button.config(state="disabled")
                if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                    if wall_MicowaveSlot_cabinets[current_count].twoPiece == True:
                        toggle_twoPiece_button()

                #-------------------- Wall: Microwave Slot: Bottom mid frame --------------------//
                left_mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                left_mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=5, sticky=N+W+E)

                width_label = Label(left_mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, wall_MicowaveSlot_cabinets[current_count].width)
                if wall_MicowaveSlot_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(left_mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=0, column=2, padx=(15, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, wall_MicowaveSlot_cabinets[current_count].shelfQty)
                if action == "add" or wall_MicowaveSlot_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if wall_MicowaveSlot_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Wall: Microwave Slot: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=0, column=2, columnspan=3, padx=(45,0), pady=(0, 0), sticky=W+E)

                lightShelfBool = BooleanVar()
                lightShelfBool.set(False)
                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_lightShelf_button():
                    if lightShelf_checkButton["text"] == "⬜ lightShelf":
                        lightShelf_checkButton["text"] = "✅ lightShelf"
                        lightShelfBool.set(True)
                    else:
                        lightShelf_checkButton["text"] = "⬜ lightShelf"
                        lightShelfBool.set(False)
                lightShelf_checkButton = Button(toggleButtons_frame, text="⬜ lightShelf", command=toggle_lightShelf_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                lightShelf_checkButton.grid(row=0, column=0, padx=(25,10), pady=(10, 0))
                if wall_MicowaveSlot_cabinets[current_count].editable == False:
                    lightShelf_checkButton.config(state="disabled")

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=1, padx=10, pady=(10, 0))
                if wall_MicowaveSlot_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=2, padx=10, pady=(10, 0))
                if wall_MicowaveSlot_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and wall_MicowaveSlot_cabinets[current_count].completionStatus == True:
                    if wall_MicowaveSlot_cabinets[current_count].lightShelf == True:
                        toggle_lightShelf_button()
                    if wall_MicowaveSlot_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if wall_MicowaveSlot_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Wall: Microwave Slot: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if wall_MicowaveSlot_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_wall_MicrowaveSlot_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    wall_MicowaveSlot_cabinets.pop()  # Remove the latest item in the list
                    if not wall_MicowaveSlot_cabinets:
                        workspace_wall_MicrowaveSlot_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if wall_MicowaveSlot_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_wall_MicrowaveSlot_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not wall_MicowaveSlot_cabinets:
                        workspace_wall_MicrowaveSlot_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_wall_MicrowaveSlot_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del wall_MicowaveSlot_cabinets[currentCount]
                for child in workspace_wall_MicrowaveSlot_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not wall_MicowaveSlot_cabinets:
                    workspace_wall_MicrowaveSlot_frame.grid_forget()  # Hide the frame

    elif category == "Tall": #---------------------------------------------------------------- Tall ----------------------------------------------------------------//
        if cabinet_type == "Full Door": #------------------------------------------ Tall: Full Door ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not tall_FullDoor_cabinets:
                    workspace_tall_FullDoor_frame.grid(row=0, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetTall(category, cabinet_type, current_count, 0, 0, 0, 0, 0, 0, False, False, False, 0, 0, "", "", True, False)
                    tall_FullDoor_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    tall_FullDoor_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_tall_FullDoor_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Tall: Full Door: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, tall_FullDoor_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(tall_FullDoor_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_tall_count(cabinet_type, current_count, tall_FullDoor_cabinets, "delete one"))

                #------------------------------- Tall: Full Door: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=tall_FullDoor_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Tall: Full Door: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=6, padx = (292,5), sticky=N+E)
                if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True and tall_FullDoor_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=6, padx = (200,5), sticky=N+E)
                elif tall_FullDoor_cabinets[current_count].completionStatus == True and tall_FullDoor_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=6, padx = (233,5), sticky=N+E)

                #------------------------------- Tall: Full Door: mid frame -------------------------------//
                #-------------------- Tall: Full Door: Top mid frame --------------------//
                right_mid_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                #-------------------- Tall: Full Door: Declaring twoPieceData frames --------------------//
                top_right_mid_frame = LabelFrame(right_mid_frame, text="Upper Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                materialThickness_label = Label(top_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                material_thickness_combobox = ttk.Combobox(top_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=material_type_options, state="readonly")
                height_entry = Entry(top_right_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                bottom_right_mid_frame = LabelFrame(right_mid_frame, text="Lower Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                material_thickness_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=material_type_options, state="readonly")
                height_bottom_entry = Entry(bottom_right_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                twoPieceBool = BooleanVar()
                twoPieceBool.set(False)

                topPieceData = []
                bottomPieceData = []

                def toggle_twoPiece_button():
                    for widget in right_mid_frame.winfo_children():
                        widget.grid_forget()
                    right_mid_frame.grid_forget()

                    topPieceData.clear()
                    bottomPieceData.clear()

                    if twoPiece_checkButton["text"] == "⬜ Two Piece ":
                        twoPiece_checkButton["text"] = "✅ Two Piece "
                        arrow_Button.config(image=arrowUp_image)
                        twoPieceBool.set(True)

                        #-------------------- Tall: Full Door: top mid LabelFrame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="Upper Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(tall_FullDoor_cabinets[current_count].materialThicknessTop)
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(tall_FullDoor_cabinets[current_count].materialTypeTop)
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        height_label = Label(top_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, tall_FullDoor_cabinets[current_count].heightTop)
                        if action == "add" or tall_FullDoor_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, str(float(total_cabinet_height.get())/2))
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                        #-------------------- Tall: Full Door: Bottom mid frame --------------------//
                        bottom_right_mid_frame.grid(row=2, column=0, padx=(20,10), pady=5, sticky=N+W)

                        materialThickness_bottom_label = Label(bottom_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialThickness_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_bottom_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_bottom_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_bottom_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_bottom_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            if tall_FullDoor_cabinets[current_count].twoPiece == False:
                                material_thickness_bottom_combobox.set(material_thickness_var.get())
                            else:
                                material_thickness_bottom_combobox.set(tall_FullDoor_cabinets[current_count].materialThicknessBottom)
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            material_thickness_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_thickness_bottom_combobox)

                        materialType_bottom_label = Label(bottom_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_bottom_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_bottom_combobox.grid(row=0, column=3, sticky="w")
                        material_type_bottom_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_bottom_combobox.get()
                        material_type_bottom_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            if tall_FullDoor_cabinets[current_count].twoPiece == False:
                                material_type_bottom_combobox.set(material_type_var.get())
                            else:
                                material_type_bottom_combobox.set(tall_FullDoor_cabinets[current_count].materialTypeBottom)
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            material_type_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_type_bottom_combobox)

                        height_bottom_label = Label(bottom_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_bottom_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_bottom_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            if tall_FullDoor_cabinets[current_count].twoPiece == False:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                            else:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, tall_FullDoor_cabinets[current_count].heightBottom)
                        if action == "add" or tall_FullDoor_cabinets[current_count].completionStatus == False:
                            height_bottom_entry.delete(0, 'end')
                            height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            height_bottom_entry.config(state="readonly", fg=frontHighlightGray)

                        bottomPieceData.append(height_bottom_entry)

                    else:
                        twoPiece_checkButton["text"] = "⬜ Two Piece "
                        arrow_Button.config(image=arrowDown_image)
                        twoPieceBool.set(False)

                        #-------------------- Tall: Full Door: Top mid frame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="One Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(tall_FullDoor_cabinets[current_count].materialThicknessTop)
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(tall_FullDoor_cabinets[current_count].materialTypeTop)
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        height_label = Label(top_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, tall_FullDoor_cabinets[current_count].heightTop)
                        if action == "add" or tall_FullDoor_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, total_cabinet_height.get())
                        if tall_FullDoor_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                twoPiece_checkButton = Button(options_frame, text="✅ Two Piece ", command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                twoPiece_checkButton.grid(row=0, column=0, padx=(15,0), pady=(10, 0))
                arrow_Button = Button(options_frame, image=arrowDown_image, height=36, command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                arrow_Button.grid(row=0, column=1, pady=(10, 0))
                toggle_twoPiece_button()
                if tall_FullDoor_cabinets[current_count].editable == False:
                    twoPiece_checkButton.config(state="disabled")
                    arrow_Button.config(state="disabled")
                if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                    if tall_FullDoor_cabinets[current_count].twoPiece == True:
                        toggle_twoPiece_button()

                #-------------------- Tall: Full Door: Bottom mid frame --------------------//
                left_mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                left_mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=5, sticky=N+W+E)

                width_label = Label(left_mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                width_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, tall_FullDoor_cabinets[current_count].width)
                if tall_FullDoor_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(left_mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=2, padx=(20, 0), pady=10, sticky="e")
                depth_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, tall_FullDoor_cabinets[current_count].depth)
                if action == "add" or tall_FullDoor_cabinets[current_count].completionStatus == False:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, "23.75")
                if tall_FullDoor_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(left_mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=0, column=4, padx=(20, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, tall_FullDoor_cabinets[current_count].shelfQty)
                if action == "add" or tall_FullDoor_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if tall_FullDoor_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(left_mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(20, 0), pady=10, sticky="e")
                toeKick_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, tall_FullDoor_cabinets[current_count].toeKick)
                if action == "add" or tall_FullDoor_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if tall_FullDoor_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Tall: Full Door: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=0, column=2, columnspan=3, padx=(45,0), pady=(0, 5), sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(25,10), pady=(10, 0))
                if tall_FullDoor_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=(10, 0))
                if tall_FullDoor_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and tall_FullDoor_cabinets[current_count].completionStatus == True:
                    if tall_FullDoor_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if tall_FullDoor_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Tall: Full Door: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if tall_FullDoor_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_tall_FullDoor_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    tall_FullDoor_cabinets.pop()  # Remove the latest item in the list
                    if not tall_FullDoor_cabinets:
                        workspace_tall_FullDoor_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if tall_FullDoor_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_tall_FullDoor_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not tall_FullDoor_cabinets:
                        workspace_tall_FullDoor_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_tall_FullDoor_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del tall_FullDoor_cabinets[currentCount]
                for child in workspace_tall_FullDoor_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not tall_FullDoor_cabinets:
                    workspace_tall_FullDoor_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Pantry": #------------------------------------------ Tall: Pantry ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not tall_Pantry_cabinets:
                    workspace_tall_Pantry_frame.grid(row=1, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetTallDrawer(category, cabinet_type, current_count, 0, 0, 0, 0, 0, 0, [0,0], 0, 0, "", "", False, False, False, 0, 0, "", "", True, False)
                    tall_Pantry_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    tall_Pantry_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_tall_Pantry_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Tall: Pantry: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, tall_Pantry_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(tall_Pantry_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_tall_count(cabinet_type, current_count, tall_Pantry_cabinets, "delete one"))

                #------------------------------- Tall: Pantry: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=tall_Pantry_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Tall: Pantry: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=6, padx = (292,5), sticky=N+E)
                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True and tall_Pantry_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=6, padx = (200,5), sticky=N+E)
                elif tall_Pantry_cabinets[current_count].completionStatus == True and tall_Pantry_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=6, padx = (233,5), sticky=N+E)

                #------------------------------- Tall: Pantry: mid frame -------------------------------//
                #-------------------- Tall: Pantry: Top mid frame --------------------//
                right_mid_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                #-------------------- Tall: Pantry: Declaring twoPieceData frames --------------------//
                top_right_mid_frame = LabelFrame(right_mid_frame, text="Upper Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                materialThickness_label = Label(top_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                material_thickness_combobox = ttk.Combobox(top_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=material_type_options, state="readonly")
                rail_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=railList, state="readonly")
                height_frame = Frame(top_right_mid_frame, bg=plainWhite)
                height_entry = Entry(height_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                bottom_right_mid_frame = LabelFrame(right_mid_frame, text="Lower Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                material_thickness_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=material_type_options, state="readonly")
                rail_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=railList, state="readonly")
                height_bottom_frame = Frame(bottom_right_mid_frame, bg=plainWhite)
                height_bottom_entry = Entry(height_bottom_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                twoPieceBool = BooleanVar()
                twoPieceBool.set(False)

                topPieceData = []
                bottomPieceData = []

                def toggle_twoPiece_button():
                    materialThickness_label.grid_forget()

                    for widget in height_frame.winfo_children():
                        widget.grid_forget()
                    height_frame.grid_forget()

                    for widget in right_mid_frame.winfo_children():
                        widget.grid_forget()
                    right_mid_frame.grid_forget()

                    topPieceData.clear()
                    bottomPieceData.clear()

                    if twoPiece_checkButton["text"] == "⬜ Two Piece ":
                        twoPiece_checkButton["text"] = "✅ Two Piece "
                        arrow_Button.config(image=arrowUp_image)
                        twoPieceBool.set(True)

                        #-------------------- Tall: Pantry: Top mid LabelFrame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="Upper Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(tall_Pantry_cabinets[current_count].materialThicknessTop)
                        if tall_Pantry_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(tall_Pantry_cabinets[current_count].materialTypeTop)
                        if tall_Pantry_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        railType_label = Label(top_right_mid_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        railType_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                        rail_type_combobox.grid(row=0, column=5, padx=(0, 10), sticky="w")
                        rail_type_combobox.set(rail_type_var.get())
                        def update_rail_type(event):
                            selected_rail_type = rail_type_combobox.get()
                        rail_type_combobox.bind("<<ComboboxSelected>>", update_rail_type)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            rail_type_combobox.set(tall_Pantry_cabinets[current_count].railTypeTop)
                        if tall_Pantry_cabinets[current_count].editable == False:
                            rail_type_combobox.config(state="disabled")

                        topPieceData.append(rail_type_combobox)

                        height_frame.grid(row=1, column=0, columnspan=3, sticky=N+W)

                        height_label = Label(height_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=4, padx=(20, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, tall_Pantry_cabinets[current_count].heightTop)
                        if action == "add" or tall_Pantry_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                        if tall_Pantry_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                        #-------------------- Tall: Pantry: Bottom mid frame --------------------//
                        bottom_right_mid_frame.grid(row=2, column=0, padx=(20,10), pady=5, sticky=N+W)

                        materialThickness_bottom_label = Label(bottom_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialThickness_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_bottom_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_bottom_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_bottom_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_bottom_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            if tall_Pantry_cabinets[current_count].twoPiece == False:
                                material_thickness_bottom_combobox.set(material_thickness_var.get())
                            else:
                                material_thickness_bottom_combobox.set(tall_Pantry_cabinets[current_count].materialThicknessBottom)
                        if tall_Pantry_cabinets[current_count].editable == False:
                            material_thickness_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_thickness_bottom_combobox)

                        materialType_bottom_label = Label(bottom_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_bottom_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_bottom_combobox.grid(row=0, column=3, sticky="w")
                        material_type_bottom_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_bottom_combobox.get()
                        material_type_bottom_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            if tall_Pantry_cabinets[current_count].twoPiece == False:
                                material_type_bottom_combobox.set(material_type_var.get())
                            else:
                                material_type_bottom_combobox.set(tall_Pantry_cabinets[current_count].materialTypeBottom)
                        if tall_Pantry_cabinets[current_count].editable == False:
                            material_type_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_type_bottom_combobox)

                        railType_bottom_label = Label(bottom_right_mid_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        railType_bottom_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                        rail_type_bottom_combobox.grid(row=0, column=5, padx=(0, 10), sticky="w")
                        rail_type_bottom_combobox.set(rail_type_var.get())
                        def update_bottom_rail_type(event):
                            selected_rail_type = rail_type_bottom_combobox.get()
                        rail_type_bottom_combobox.bind("<<ComboboxSelected>>", update_bottom_rail_type)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            rail_type_bottom_combobox.set(tall_Pantry_cabinets[current_count].railTypeBottom)
                            if tall_Pantry_cabinets[current_count].railTypeBottom == "":
                                rail_type_bottom_combobox.set(rail_type_var.get())
                        if tall_Pantry_cabinets[current_count].editable == False:
                            rail_type_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(rail_type_bottom_combobox)

                        height_bottom_frame.grid(row=1, column=0, columnspan=3, sticky=N+W)

                        height_bottom_label = Label(height_bottom_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        height_bottom_entry.grid(row=0, column=1, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            if tall_Pantry_cabinets[current_count].twoPiece == False:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                            else:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, tall_Pantry_cabinets[current_count].heightBottom)
                        if action == "add" or tall_Pantry_cabinets[current_count].completionStatus == False:
                            height_bottom_entry.delete(0, 'end')
                            height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                        if tall_Pantry_cabinets[current_count].editable == False:
                            height_bottom_entry.config(state="readonly", fg=frontHighlightGray)

                        bottomPieceData.append(height_bottom_entry)

                    else:
                        twoPiece_checkButton["text"] = "⬜ Two Piece "
                        arrow_Button.config(image=arrowDown_image)
                        twoPieceBool.set(False)

                        #-------------------- Tall: Pantry: Single mid frame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="One Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(tall_Pantry_cabinets[current_count].materialThicknessTop)
                        if tall_Pantry_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(tall_Pantry_cabinets[current_count].materialTypeTop)
                        if tall_Pantry_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        railType_label = Label(top_right_mid_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        railType_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                        rail_type_combobox.grid(row=0, column=5, padx=(0, 10), sticky="w")
                        rail_type_combobox.set(rail_type_var.get())
                        def update_rail_type(event):
                            selected_rail_type = rail_type_combobox.get()
                        rail_type_combobox.bind("<<ComboboxSelected>>", update_rail_type)
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            rail_type_combobox.set(tall_Pantry_cabinets[current_count].railTypeTop)
                        if tall_Pantry_cabinets[current_count].editable == False:
                            rail_type_combobox.config(state="disabled")

                        topPieceData.append(rail_type_combobox)

                        height_frame.grid(row=1, column=0, columnspan=3, sticky=N+W)

                        height_label = Label(height_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=1, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, tall_Pantry_cabinets[current_count].heightTop)
                        if action == "add" or tall_Pantry_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, total_cabinet_height.get())
                        if tall_Pantry_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                twoPiece_checkButton = Button(options_frame, text="✅ Two Piece ", command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                twoPiece_checkButton.grid(row=0, column=0, padx=(15,0), pady=(10, 0))
                arrow_Button = Button(options_frame, image=arrowDown_image, height=36, command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                arrow_Button.grid(row=0, column=1, pady=(10, 0))
                toggle_twoPiece_button()
                if tall_Pantry_cabinets[current_count].editable == False:
                    twoPiece_checkButton.config(state="disabled")
                    arrow_Button.config(state="disabled")
                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                    if tall_Pantry_cabinets[current_count].twoPiece == True:
                        toggle_twoPiece_button()

                #-------------------- Tall: Pantry: Bottom mid frame --------------------//
                left_mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                left_mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=5, sticky=N+W+E)

                mid_top_frame = Frame(left_mid_frame, bg=plainWhite)
                mid_top_frame.grid(row=0, column=0, sticky=N+W+E)

                width_label = Label(mid_top_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, tall_Pantry_cabinets[current_count].width)
                if tall_Pantry_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_top_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=2, padx=(15, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, tall_Pantry_cabinets[current_count].depth)
                if action == "add" or tall_Pantry_cabinets[current_count].completionStatus == False:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, "23.75")
                if tall_Pantry_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_top_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=0, column=4, padx=(35, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, tall_Pantry_cabinets[current_count].shelfQty)
                if action == "add" or tall_Pantry_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if tall_Pantry_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_top_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, tall_Pantry_cabinets[current_count].toeKick)
                if action == "add" or tall_Pantry_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if tall_Pantry_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #-------------------- Tall: Pantry: Drawer Inc Dec frame --------------------//
                drawerIncDec_frame = Frame(mid_top_frame, bg=plainWhite)
                drawerIncDec_frame.grid(row=1, column=2, columnspan=9, padx=5, pady=5, sticky="w")

                drawerDepth_label = Label(drawerIncDec_frame, text="Drawer Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerDepth_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                drawerDepth_entry_combobox = ttk.Combobox(drawerIncDec_frame, width=5, values=kitchen_rail_size_options)
                drawerDepth_entry_combobox.grid(row=0, column=1, padx=10, sticky="w")
                drawerDepth_entry_combobox.set(kitchen_rail_size_var.get())
                def update_drawerDepth_entry_combobox(event):
                    selected_drawerDepth = drawerDepth_entry_combobox.get()  # Use get() to retrieve the selected value
                drawerDepth_entry_combobox.bind("<<ComboboxSelected>>", update_drawerDepth_entry_combobox)
                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                    drawerDepth_entry_combobox.set(tall_Pantry_cabinets[current_count].drawerDepth)
                if tall_Pantry_cabinets[current_count].editable == False:
                    drawerDepth_entry_combobox.config(state="disabled")

                #-------------------------------------------------- Tall: Pantry:: Drawers: drawerHeights frame --------------------------------------------------//
                drawerHeights_frame = LabelFrame(left_mid_frame, text="Drawer Heights", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                drawerHeights_frame.grid(row=1, column=0, padx=15, pady=(0,15), sticky="w")

                drawerHeights_entries = []

                def increment_drawer_qty(drawerHeight):
                    current_qty = int(drawerQty_var_label["text"])
                    new_qty = current_qty + 1
                    drawerQty_var_label["text"] = str(new_qty)
                    create_drawer_height_entry(new_qty, drawerHeight)  # Create a new drawer entry
                    update_drawer_height_entries()

                def decrement_drawer_qty():
                    current_qty = int(drawerQty_var_label["text"])
                    if current_qty > 1:
                        new_qty = current_qty - 1
                        drawerQty_var_label["text"] = str(new_qty)
                        remove_drawer_height_entry()  # Remove the last drawer entry
                        update_drawer_height_entries()

                def create_drawer_height_entry(entry_number, drawerHeight):
                    row = (entry_number-1) // 4  # Calculate the row based on the entry_number
                    column = (entry_number-1) % 4  # Calculate the column based on the entry_number

                    single_frame = Frame(drawerHeights_frame, bg=plainWhite)
                    single_frame.grid(row=row, column=column, sticky="w")

                    drawerNum_label = Label(single_frame, text="#" + str(entry_number), font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                    drawerNum_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                    drawer_height_entry = Entry(single_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                    drawer_height_entry.grid(row=0, column=1, padx=10, sticky="w")
                    drawer_height_entry.insert(0, drawerHeight)
                    if tall_Pantry_cabinets[current_count].editable == False:
                        drawer_height_entry.config(state="readonly", fg=frontHighlightGray)

                    # Add the entry to the drawerHeights list if it's not empty. (this is checked in create_cabinet_object)
                    drawerHeights_entries.append(drawer_height_entry)

                def remove_drawer_height_entry():
                    last_entry = drawerHeights_frame.winfo_children()[-1]  # Get the last entry widget
                    last_entry.destroy()
                    # Remove the corresponding entry from the drawerHeights list
                    if drawerHeights_entries:
                        drawerHeights_entries.pop()

                def update_drawer_height_entries():
                    if action == "add" or tall_Pantry_cabinets[current_count].completionStatus == False:
                        if len(drawerHeights_entries) == 1:
                            drawerHeights_entries[0].delete(0, 'end')
                            drawerHeights_entries[0].insert(0, "4.5")
                        elif len(drawerHeights_entries) > 1:
                            calculated_drawerHeight = (float(height_entry.get()) - 16.75) / (len(drawerHeights_entries) - 1)
                            for i in range(len(drawerHeights_entries)):
                                if i != 0:
                                    drawerHeights_entries[i].delete(0, 'end')
                                    drawerHeights_entries[i].insert(0, str(calculated_drawerHeight))

                drawerQty_label = Label(drawerIncDec_frame, text="Drawer#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerQty_label.grid(row=0, column=2, padx=(5, 10), pady=10, sticky="e")

                drawerDecrement_button = Button(drawerIncDec_frame, text="-", command=decrement_drawer_qty, width=3, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drawerDecrement_button.grid(row=0, column=3, padx=0, pady=10, sticky="e")

                drawerQty_var_label = Label(drawerIncDec_frame, text="0", width=2, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerQty_var_label.grid(row=0, column=4, padx=0, pady=10)

                drawerIncrement_button = Button(drawerIncDec_frame, text="+", command= lambda: increment_drawer_qty("0"), width=3, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drawerIncrement_button.grid(row=0, column=5, padx=0, pady=10, sticky="w")

                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                    for drawerHeight in tall_Pantry_cabinets[current_count].drawerHeights:
                        increment_drawer_qty(drawerHeight)
                elif action == "add" or tall_Pantry_cabinets[current_count].completionStatus == False:
                    increment_drawer_qty("4.5")
                    increment_drawer_qty("9")
                    increment_drawer_qty("9")
                if tall_Pantry_cabinets[current_count].editable == False:
                    drawerDecrement_button.config(state="disabled")
                    drawerIncrement_button.config(state="disabled")

                #------------------------------- Tall: Pantry: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=0, column=2, columnspan=3, padx=(45,0), pady=(0, 5), sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(25,10), pady=(10, 0))
                if tall_Pantry_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=(10, 0))
                if tall_Pantry_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and tall_Pantry_cabinets[current_count].completionStatus == True:
                    if tall_Pantry_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if tall_Pantry_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Tall: Pantry: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if tall_Pantry_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_tall_Pantry_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    tall_Pantry_cabinets.pop()  # Remove the latest item in the list
                    if not tall_Pantry_cabinets:
                        workspace_tall_Pantry_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if tall_Pantry_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_tall_Pantry_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not tall_Pantry_cabinets:
                        workspace_tall_Pantry_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_tall_Pantry_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del tall_Pantry_cabinets[currentCount]
                for child in workspace_tall_Pantry_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not tall_Pantry_cabinets:
                    workspace_tall_Pantry_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Oven Slot": #------------------------------------------ Tall: Oven Slot ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not tall_OvenSlot_cabinets:
                    workspace_tall_OvenSlot_frame.grid(row=2, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetTall(category, cabinet_type, current_count, 0, 0, 0, 0, 0, 0, False, False, False, 0, 0, "", "", True, False)
                    tall_OvenSlot_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    tall_OvenSlot_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_tall_OvenSlot_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Tall: Oven Slot: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, tall_OvenSlot_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(tall_OvenSlot_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_tall_count(cabinet_type, current_count, tall_OvenSlot_cabinets, "delete one"))

                #------------------------------- Tall: Oven Slot: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=tall_OvenSlot_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Tall: Oven Slot: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=6, padx = (292,5), sticky=N+E)
                if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True and tall_OvenSlot_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=6, padx = (200,5), sticky=N+E)
                elif tall_OvenSlot_cabinets[current_count].completionStatus == True and tall_OvenSlot_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=6, padx = (233,5), sticky=N+E)

                #------------------------------- Tall: Oven Slot: mid frame -------------------------------//
                #-------------------- Tall: Oven Slot: Top mid frame --------------------//
                right_mid_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                #-------------------- Tall: Oven Slot: Declaring twoPieceData frames --------------------//
                top_right_mid_frame = LabelFrame(right_mid_frame, text="Upper Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                materialThickness_label = Label(top_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                material_thickness_combobox = ttk.Combobox(top_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=material_type_options, state="readonly")
                rail_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=railList, state="readonly")
                height_entry = Entry(top_right_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                bottom_right_mid_frame = LabelFrame(right_mid_frame, text="Lower Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                material_thickness_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=material_type_options, state="readonly")
                rail_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=railList, state="readonly")
                height_bottom_entry = Entry(bottom_right_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                twoPieceBool = BooleanVar()
                twoPieceBool.set(False)

                topPieceData = []
                bottomPieceData = []

                def toggle_twoPiece_button():
                    for widget in right_mid_frame.winfo_children():
                        widget.grid_forget()
                    right_mid_frame.grid_forget()

                    topPieceData.clear()
                    bottomPieceData.clear()

                    if twoPiece_checkButton["text"] == "⬜ Two Piece ":
                        twoPiece_checkButton["text"] = "✅ Two Piece "
                        arrow_Button.config(image=arrowUp_image)
                        twoPieceBool.set(True)

                        #-------------------- Tall: Oven Slot: top mid LabelFrame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="Upper Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(tall_OvenSlot_cabinets[current_count].materialThicknessTop)
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(tall_OvenSlot_cabinets[current_count].materialTypeTop)
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        height_label = Label(top_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, tall_OvenSlot_cabinets[current_count].heightTop)
                        if action == "add" or tall_OvenSlot_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                        #-------------------- Tall: Oven Slot: Bottom mid frame --------------------//
                        bottom_right_mid_frame.grid(row=2, column=0, padx=(20,10), pady=5, sticky=N+W)

                        materialThickness_bottom_label = Label(bottom_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialThickness_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_bottom_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_bottom_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_bottom_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_bottom_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            if tall_OvenSlot_cabinets[current_count].twoPiece == False:
                                material_thickness_bottom_combobox.set(material_thickness_var.get())
                            else:
                                material_thickness_bottom_combobox.set(tall_OvenSlot_cabinets[current_count].materialThicknessBottom)
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            material_thickness_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_thickness_bottom_combobox)

                        materialType_bottom_label = Label(bottom_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_bottom_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_bottom_combobox.grid(row=0, column=3, sticky="w")
                        material_type_bottom_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_bottom_combobox.get()
                        material_type_bottom_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            if tall_OvenSlot_cabinets[current_count].twoPiece == False:
                                material_type_bottom_combobox.set(material_type_var.get())
                            else:
                                material_type_bottom_combobox.set(tall_OvenSlot_cabinets[current_count].materialTypeBottom)
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            material_type_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_type_bottom_combobox)

                        height_bottom_label = Label(bottom_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_bottom_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_bottom_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            if tall_OvenSlot_cabinets[current_count].twoPiece == False:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                            else:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, tall_OvenSlot_cabinets[current_count].heightBottom)
                        if action == "add" or tall_OvenSlot_cabinets[current_count].completionStatus == False:
                            height_bottom_entry.delete(0, 'end')
                            height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            height_bottom_entry.config(state="readonly", fg=frontHighlightGray)

                        bottomPieceData.append(height_bottom_entry)

                    else:
                        twoPiece_checkButton["text"] = "⬜ Two Piece "
                        arrow_Button.config(image=arrowDown_image)
                        twoPieceBool.set(False)

                        #-------------------- Tall: Oven Slot: Top mid frame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="One Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(tall_OvenSlot_cabinets[current_count].materialThicknessTop)
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(tall_OvenSlot_cabinets[current_count].materialTypeTop)
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        height_label = Label(top_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, tall_OvenSlot_cabinets[current_count].heightTop)
                        if action == "add" or tall_OvenSlot_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, total_cabinet_height.get())
                        if tall_OvenSlot_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                twoPiece_checkButton = Button(options_frame, text="✅ Two Piece ", command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                twoPiece_checkButton.grid(row=0, column=0, padx=(15,0), pady=(10, 0))
                arrow_Button = Button(options_frame, image=arrowDown_image, height=36, command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                arrow_Button.grid(row=0, column=1, pady=(10, 0))
                toggle_twoPiece_button()
                if tall_OvenSlot_cabinets[current_count].editable == False:
                    twoPiece_checkButton.config(state="disabled")
                    arrow_Button.config(state="disabled")
                if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                    if tall_OvenSlot_cabinets[current_count].twoPiece == True:
                        toggle_twoPiece_button()

                #-------------------- Tall: Oven Slot: Bottom mid frame --------------------//
                left_mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                left_mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=5, sticky=N+W+E)

                mid_top_frame = Frame(left_mid_frame, bg=plainWhite)
                mid_top_frame.grid(row=0, column=0, sticky=N+W+E)

                width_label = Label(mid_top_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, tall_OvenSlot_cabinets[current_count].width)
                if tall_OvenSlot_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_top_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=2, padx=(15, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, tall_OvenSlot_cabinets[current_count].depth)
                if action == "add" or tall_OvenSlot_cabinets[current_count].completionStatus == False:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, "23.75")
                if tall_OvenSlot_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_top_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=0, column=4, padx=(35, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, tall_OvenSlot_cabinets[current_count].shelfQty)
                if action == "add" or tall_OvenSlot_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if tall_OvenSlot_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_top_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, tall_OvenSlot_cabinets[current_count].toeKick)
                if action == "add" or tall_OvenSlot_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if tall_OvenSlot_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Tall: Oven Slot: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=0, column=2, columnspan=3, padx=(45,0), pady=(0, 5), sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(25,10), pady=(10, 0))
                if tall_OvenSlot_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=(10, 0))
                if tall_OvenSlot_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and tall_OvenSlot_cabinets[current_count].completionStatus == True:
                    if tall_OvenSlot_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if tall_OvenSlot_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Tall: Oven Slot: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if tall_OvenSlot_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_tall_OvenSlot_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    tall_OvenSlot_cabinets.pop()  # Remove the latest item in the list
                    if not tall_OvenSlot_cabinets:
                        workspace_tall_OvenSlot_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if tall_OvenSlot_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_tall_OvenSlot_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not tall_OvenSlot_cabinets:
                        workspace_tall_OvenSlot_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_tall_OvenSlot_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del tall_OvenSlot_cabinets[currentCount]
                for child in workspace_tall_OvenSlot_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not tall_OvenSlot_cabinets:
                    workspace_tall_OvenSlot_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Pull Out": #------------------------------------------ Tall: Pull Out ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not tall_PullOut_cabinets:
                    workspace_tall_PullOut_frame.grid(row=3, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetTallDrawer(category, cabinet_type, current_count, 0, 0, 0, 0, 0, 0, [0,0], 0, 0, "", "", False, False, False, 0, 0, "", "", True, False)
                    tall_PullOut_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    tall_PullOut_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_tall_PullOut_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Tall: Pull Out: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, tall_PullOut_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(tall_PullOut_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_tall_count(cabinet_type, current_count, tall_PullOut_cabinets, "delete one"))

                #------------------------------- Tall: Pull Out: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=tall_PullOut_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Tall: Pull Out: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=6, padx = (292,5), sticky=N+E)
                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True and tall_PullOut_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=6, padx = (200,5), sticky=N+E)
                elif tall_PullOut_cabinets[current_count].completionStatus == True and tall_PullOut_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=6, padx = (233,5), sticky=N+E)

                #------------------------------- Tall: Pull Out: mid frame -------------------------------//
                #-------------------- Tall: Pull Out: Top mid frame --------------------//
                right_mid_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                #-------------------- Tall: Pull Out: Declaring twoPieceData frames --------------------//
                top_right_mid_frame = LabelFrame(right_mid_frame, text="Upper Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                materialThickness_label = Label(top_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                material_thickness_combobox = ttk.Combobox(top_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=material_type_options, state="readonly")
                rail_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=railList, state="readonly")
                height_frame = Frame(top_right_mid_frame, bg=plainWhite)
                height_entry = Entry(height_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                bottom_right_mid_frame = LabelFrame(right_mid_frame, text="Lower Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                material_thickness_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=material_type_options, state="readonly")
                rail_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=railList, state="readonly")
                height_bottom_frame = Frame(bottom_right_mid_frame, bg=plainWhite)
                height_bottom_entry = Entry(height_bottom_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                twoPieceBool = BooleanVar()
                twoPieceBool.set(False)

                topPieceData = []
                bottomPieceData = []

                def toggle_twoPiece_button():
                    materialThickness_label.grid_forget()

                    for widget in height_frame.winfo_children():
                        widget.grid_forget()
                    height_frame.grid_forget()

                    for widget in right_mid_frame.winfo_children():
                        widget.grid_forget()
                    right_mid_frame.grid_forget()

                    topPieceData.clear()
                    bottomPieceData.clear()

                    if twoPiece_checkButton["text"] == "⬜ Two Piece ":
                        twoPiece_checkButton["text"] = "✅ Two Piece "
                        arrow_Button.config(image=arrowUp_image)
                        twoPieceBool.set(True)

                        #-------------------- Tall: Pull Out: Top mid LabelFrame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="Upper Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(tall_PullOut_cabinets[current_count].materialThicknessTop)
                        if tall_PullOut_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(tall_PullOut_cabinets[current_count].materialTypeTop)
                        if tall_PullOut_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        railType_label = Label(top_right_mid_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        railType_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                        rail_type_combobox.grid(row=0, column=5, padx=(0, 10), sticky="w")
                        rail_type_combobox.set(rail_type_var.get())
                        def update_rail_type(event):
                            selected_rail_type = rail_type_combobox.get()
                        rail_type_combobox.bind("<<ComboboxSelected>>", update_rail_type)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            rail_type_combobox.set(tall_PullOut_cabinets[current_count].railTypeTop)
                        if tall_PullOut_cabinets[current_count].editable == False:
                            rail_type_combobox.config(state="disabled")

                        topPieceData.append(rail_type_combobox)

                        height_frame.grid(row=1, column=0, columnspan=3, sticky=N+W)

                        height_label = Label(height_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=4, padx=(20, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, tall_PullOut_cabinets[current_count].heightTop)
                        if action == "add" or tall_PullOut_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                        if tall_PullOut_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                        #-------------------- Tall: Pull Out: Bottom mid frame --------------------//
                        bottom_right_mid_frame.grid(row=2, column=0, padx=(20,10), pady=5, sticky=N+W)

                        materialThickness_bottom_label = Label(bottom_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialThickness_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_bottom_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_bottom_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_bottom_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_bottom_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            if tall_PullOut_cabinets[current_count].twoPiece == False:
                                material_thickness_bottom_combobox.set(material_thickness_var.get())
                            else:
                                material_thickness_bottom_combobox.set(tall_PullOut_cabinets[current_count].materialThicknessBottom)
                        if tall_PullOut_cabinets[current_count].editable == False:
                            material_thickness_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_thickness_bottom_combobox)

                        materialType_bottom_label = Label(bottom_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_bottom_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_bottom_combobox.grid(row=0, column=3, sticky="w")
                        material_type_bottom_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_bottom_combobox.get()
                        material_type_bottom_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            if tall_PullOut_cabinets[current_count].twoPiece == False:
                                material_type_bottom_combobox.set(material_type_var.get())
                            else:
                                material_type_bottom_combobox.set(tall_PullOut_cabinets[current_count].materialTypeBottom)
                        if tall_PullOut_cabinets[current_count].editable == False:
                            material_type_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_type_bottom_combobox)

                        railType_bottom_label = Label(bottom_right_mid_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        railType_bottom_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                        rail_type_bottom_combobox.grid(row=0, column=5, padx=(0, 10), sticky="w")
                        rail_type_bottom_combobox.set(rail_type_var.get())
                        def update_bottom_rail_type(event):
                            selected_rail_type = rail_type_bottom_combobox.get()
                        rail_type_bottom_combobox.bind("<<ComboboxSelected>>", update_bottom_rail_type)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            rail_type_bottom_combobox.set(tall_PullOut_cabinets[current_count].railTypeBottom)
                            if tall_PullOut_cabinets[current_count].railTypeBottom == "":
                                rail_type_bottom_combobox.set(rail_type_var.get())
                        if tall_PullOut_cabinets[current_count].editable == False:
                            rail_type_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(rail_type_bottom_combobox)

                        height_bottom_frame.grid(row=1, column=0, columnspan=3, sticky=N+W)

                        height_bottom_label = Label(height_bottom_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        height_bottom_entry.grid(row=0, column=1, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            if tall_PullOut_cabinets[current_count].twoPiece == False:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                            else:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, tall_PullOut_cabinets[current_count].heightBottom)
                        if action == "add" or tall_PullOut_cabinets[current_count].completionStatus == False:
                            height_bottom_entry.delete(0, 'end')
                            height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide total height by two
                        if tall_PullOut_cabinets[current_count].editable == False:
                            height_bottom_entry.config(state="readonly", fg=frontHighlightGray)

                        bottomPieceData.append(height_bottom_entry)

                    else:
                        twoPiece_checkButton["text"] = "⬜ Two Piece "
                        arrow_Button.config(image=arrowDown_image)
                        twoPieceBool.set(False)

                        #-------------------- Tall: Pull Out: Single mid frame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="One Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(tall_PullOut_cabinets[current_count].materialThicknessTop)
                        if tall_PullOut_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(tall_PullOut_cabinets[current_count].materialTypeTop)
                        if tall_PullOut_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        railType_label = Label(top_right_mid_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        railType_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                        rail_type_combobox.grid(row=0, column=5, padx=(0, 10), sticky="w")
                        rail_type_combobox.set(rail_type_var.get())
                        def update_rail_type(event):
                            selected_rail_type = rail_type_combobox.get()
                        rail_type_combobox.bind("<<ComboboxSelected>>", update_rail_type)
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            rail_type_combobox.set(tall_PullOut_cabinets[current_count].railTypeTop)
                        if tall_PullOut_cabinets[current_count].editable == False:
                            rail_type_combobox.config(state="disabled")

                        topPieceData.append(rail_type_combobox)

                        height_frame.grid(row=1, column=0, columnspan=3, sticky=N+W)

                        height_label = Label(height_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=1, padx=10, sticky="w")
                        if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, tall_PullOut_cabinets[current_count].heightTop)
                        if action == "add" or tall_PullOut_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, total_cabinet_height.get())
                        if tall_PullOut_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                twoPiece_checkButton = Button(options_frame, text="✅ Two Piece ", command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                twoPiece_checkButton.grid(row=0, column=0, padx=(15,0), pady=(10, 0))
                arrow_Button = Button(options_frame, image=arrowDown_image, height=36, command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                arrow_Button.grid(row=0, column=1, pady=(10, 0))
                toggle_twoPiece_button()
                if tall_PullOut_cabinets[current_count].editable == False:
                    twoPiece_checkButton.config(state="disabled")
                    arrow_Button.config(state="disabled")
                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                    if tall_PullOut_cabinets[current_count].twoPiece == True:
                        toggle_twoPiece_button()

                #-------------------- Tall: Pull Out: Bottom mid frame --------------------//
                left_mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                left_mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=5, sticky=N+W+E)

                mid_top_frame = Frame(left_mid_frame, bg=plainWhite)
                mid_top_frame.grid(row=0, column=0, sticky=N+W+E)

                width_label = Label(mid_top_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, tall_PullOut_cabinets[current_count].width)
                if tall_PullOut_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_top_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=2, padx=(15, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, tall_PullOut_cabinets[current_count].depth)
                if action == "add" or tall_PullOut_cabinets[current_count].completionStatus == False:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, "23.75")
                if tall_PullOut_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_top_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=0, column=4, padx=(35, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, tall_PullOut_cabinets[current_count].shelfQty)
                if action == "add" or tall_PullOut_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if tall_PullOut_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_top_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, tall_PullOut_cabinets[current_count].toeKick)
                if action == "add" or tall_PullOut_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4.5")
                if tall_PullOut_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #-------------------- Tall: Pull Out: Drawer Inc Dec frame --------------------//
                drawerIncDec_frame = Frame(mid_top_frame, bg=plainWhite)
                drawerIncDec_frame.grid(row=1, column=2, columnspan=9, padx=5, pady=5, sticky="w")

                drawerDepth_label = Label(drawerIncDec_frame, text="Drawer Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerDepth_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                drawerDepth_entry_combobox = ttk.Combobox(drawerIncDec_frame, width=5, values=kitchen_rail_size_options)
                drawerDepth_entry_combobox.grid(row=0, column=1, padx=10, sticky="w")
                drawerDepth_entry_combobox.set(kitchen_rail_size_var.get())
                def update_drawerDepth_entry_combobox(event):
                    selected_drawerDepth = drawerDepth_entry_combobox.get()  # Use get() to retrieve the selected value
                drawerDepth_entry_combobox.bind("<<ComboboxSelected>>", update_drawerDepth_entry_combobox)
                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                    drawerDepth_entry_combobox.set(tall_PullOut_cabinets[current_count].drawerDepth)
                if tall_PullOut_cabinets[current_count].editable == False:
                    drawerDepth_entry_combobox.config(state="disabled")

                #-------------------------------------------------- Tall: Pull Out: Drawers: drawerHeights frame --------------------------------------------------//
                drawerHeights_frame = LabelFrame(left_mid_frame, text="Drawer Heights", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                drawerHeights_frame.grid(row=1, column=0, padx=15, pady=(0,15), sticky="w")

                drawerHeights_entries = []

                def increment_drawer_qty(drawerHeight):
                    current_qty = int(drawerQty_var_label["text"])
                    new_qty = current_qty + 1
                    drawerQty_var_label["text"] = str(new_qty)
                    create_drawer_height_entry(new_qty, drawerHeight)  # Create a new drawer entry
                    update_drawer_height_entries()

                def decrement_drawer_qty():
                    current_qty = int(drawerQty_var_label["text"])
                    if current_qty > 1:
                        new_qty = current_qty - 1
                        drawerQty_var_label["text"] = str(new_qty)
                        remove_drawer_height_entry()  # Remove the last drawer entry
                        update_drawer_height_entries()

                def create_drawer_height_entry(entry_number, drawerHeight):
                    row = (entry_number-1) // 4  # Calculate the row based on the entry_number
                    column = (entry_number-1) % 4  # Calculate the column based on the entry_number

                    single_frame = Frame(drawerHeights_frame, bg=plainWhite)
                    single_frame.grid(row=row, column=column, sticky="w")

                    drawerNum_label = Label(single_frame, text="#" + str(entry_number), font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                    drawerNum_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                    drawer_height_entry = Entry(single_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                    drawer_height_entry.grid(row=0, column=1, padx=10, sticky="w")
                    drawer_height_entry.insert(0, drawerHeight)
                    if tall_PullOut_cabinets[current_count].editable == False:
                        drawer_height_entry.config(state="readonly", fg=frontHighlightGray)

                    # Add the entry to the drawerHeights list if it's not empty. (this is checked in create_cabinet_object)
                    drawerHeights_entries.append(drawer_height_entry)

                def remove_drawer_height_entry():
                    last_entry = drawerHeights_frame.winfo_children()[-1]  # Get the last entry widget
                    last_entry.destroy()
                    # Remove the corresponding entry from the drawerHeights list
                    if drawerHeights_entries:
                        drawerHeights_entries.pop()

                def update_drawer_height_entries():
                    if action == "add" or tall_PullOut_cabinets[current_count].completionStatus == False:
                        if len(drawerHeights_entries) == 1:
                            drawerHeights_entries[0].delete(0, 'end')
                            drawerHeights_entries[0].insert(0, "4.5")
                        elif len(drawerHeights_entries) > 1:
                            calculated_drawerHeight = (float(height_entry.get()) - 16.75) / (len(drawerHeights_entries) - 1)
                            for i in range(len(drawerHeights_entries)):
                                if i != 0:
                                    drawerHeights_entries[i].delete(0, 'end')
                                    drawerHeights_entries[i].insert(0, str(calculated_drawerHeight))

                drawerQty_label = Label(drawerIncDec_frame, text="Drawer#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerQty_label.grid(row=0, column=2, padx=(5, 10), pady=10, sticky="e")

                drawerDecrement_button = Button(drawerIncDec_frame, text="-", command=decrement_drawer_qty, width=3, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drawerDecrement_button.grid(row=0, column=3, padx=0, pady=10, sticky="e")

                drawerQty_var_label = Label(drawerIncDec_frame, text="0", width=2, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerQty_var_label.grid(row=0, column=4, padx=0, pady=10)

                drawerIncrement_button = Button(drawerIncDec_frame, text="+", command= lambda: increment_drawer_qty("0"), width=3, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drawerIncrement_button.grid(row=0, column=5, padx=0, pady=10, sticky="w")

                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                    for drawerHeight in tall_PullOut_cabinets[current_count].drawerHeights:
                        increment_drawer_qty(drawerHeight)
                elif action == "add" or tall_PullOut_cabinets[current_count].completionStatus == False:
                    increment_drawer_qty("4.5")
                    increment_drawer_qty("9")
                    increment_drawer_qty("9")
                if tall_PullOut_cabinets[current_count].editable == False:
                    drawerDecrement_button.config(state="disabled")
                    drawerIncrement_button.config(state="disabled")

                #------------------------------- Tall: Pull Out: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=0, column=2, columnspan=3, padx=(45,0), pady=(0, 5), sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(25,10), pady=(10, 0))
                if tall_PullOut_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=(10, 0))
                if tall_PullOut_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and tall_PullOut_cabinets[current_count].completionStatus == True:
                    if tall_PullOut_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if tall_PullOut_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Tall: Pull Out: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if tall_PullOut_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_tall_PullOut_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    tall_PullOut_cabinets.pop()  # Remove the latest item in the list
                    if not tall_PullOut_cabinets:
                        workspace_tall_PullOut_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if tall_PullOut_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_tall_PullOut_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not tall_PullOut_cabinets:
                        workspace_tall_PullOut_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_tall_PullOut_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del tall_PullOut_cabinets[currentCount]
                for child in workspace_tall_PullOut_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not tall_PullOut_cabinets:
                    workspace_tall_PullOut_frame.grid_forget()  # Hide the frame

    elif category == "Vanity": #----------------------------------------------------------------------------------- Vanity -----------------------------------------------------------------------------------//
        if cabinet_type == "Full Door": #------------------------------------------------------------- Vanity: FullDoor -------------------------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not vanity_FullDoor_cabinets:
                    workspace_vanity_FullDoor_frame.grid(row=0, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetFullDoor(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, False, False, False, 0, "", True, False)
                    vanity_FullDoor_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    vanity_FullDoor_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_vanity_FullDoor_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #-------------------------------------------------- Vanity: FullDoor: Defining Buttons Frame and Buttons --------------------------------------------------//
                # Create a nested frame for the button
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, vanity_FullDoor_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(vanity_FullDoor_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_vanity_count(cabinet_type, current_count, vanity_FullDoor_cabinets, "delete one"))

                #------------------------------------------------- Vanity: FullDoor: cabinet properties frame --------------------------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=vanity_FullDoor_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #-------------------------------------------------- Vanity: FullDoor: top frame --------------------------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event): # Unnecessary function, check if it can be removed.
                    selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(vanity_FullDoor_cabinets[current_count].materialThickness)
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=3, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event): # Unnecessary function, check if it can be removed.
                    selected_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(vanity_FullDoor_cabinets[current_count].materialType)
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=4, padx = (279,5), sticky=N+E)
                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True and vanity_FullDoor_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=4, padx = (186,5), sticky=N+E)
                elif vanity_FullDoor_cabinets[current_count].completionStatus == True and vanity_FullDoor_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=4, padx = (220,5), sticky=N+E)

                #-------------------------------------------------- Vanity: FullDoor: mid frame --------------------------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                width_label = Label(mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, vanity_FullDoor_cabinets[current_count].width)
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, vanity_FullDoor_cabinets[current_count].height)
                elif action == "add" or vanity_FullDoor_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "30.25")
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, vanity_FullDoor_cabinets[current_count].depth)
                elif action == "add" or vanity_FullDoor_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "20.75")
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, vanity_FullDoor_cabinets[current_count].shelfQty)
                elif action == "add" or vanity_FullDoor_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, vanity_FullDoor_cabinets[current_count].toeKick)
                elif action == "add" or vanity_FullDoor_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4")
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #-------------------------------------------------- Vanity: FullDoor: toggle buttons --------------------------------------------------//
                toggleButtons_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(20,0), pady=(0,10), sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if vanity_FullDoor_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and vanity_FullDoor_cabinets[current_count].completionStatus == True:
                    if vanity_FullDoor_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if vanity_FullDoor_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Vanity: FullDoor: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if vanity_FullDoor_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_vanity_FullDoor_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    vanity_FullDoor_cabinets.pop()  # Remove the latest item in the list
                    if not vanity_FullDoor_cabinets:
                        workspace_vanity_FullDoor_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if vanity_FullDoor_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_vanity_FullDoor_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not vanity_FullDoor_cabinets:
                        workspace_vanity_FullDoor_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_vanity_FullDoor_frame.winfo_children(): # Delete all children in workspace_vanity_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del vanity_FullDoor_cabinets[currentCount]
                for child in workspace_vanity_FullDoor_frame.winfo_children(): # Delete all children in workspace_vanity_FullDoor_frame
                    child.destroy()
                if not vanity_FullDoor_cabinets:
                    workspace_vanity_FullDoor_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Drawers": #------------------------------------------------------------- Vanity: Drawers -------------------------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not vanity_Drawers_cabinets:
                    workspace_vanity_Drawers_frame.grid(row=1, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetDrawers(category, cabinet_type, currentCount, 0, 0, 0, 0, [0,0], 0, 0, "", False, False, 0, "", True, False)
                    vanity_Drawers_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    vanity_Drawers_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_vanity_Drawers_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #-------------------------------------------------- Vanity: Drawers: Defining Buttons Frame and Buttons --------------------------------------------------//
                # Create a nested frame for the button
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, vanity_Drawers_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(vanity_Drawers_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_vanity_count(cabinet_type, current_count, vanity_Drawers_cabinets, "delete one"))

                #-------------------------------------------------- Vanity: Drawers: cabinet properties frame --------------------------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=vanity_Drawers_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #-------------------------------------------------- Vanity: Drawers: top frame --------------------------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_material_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(vanity_Drawers_cabinets[current_count].materialThickness)
                if vanity_Drawers_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=3, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=4, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_material_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(vanity_Drawers_cabinets[current_count].materialType)
                if vanity_Drawers_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                empty_label = Label(options_frame, text="-", font=fontSegoeSmall, bg=plainWhite, fg=plainWhite)
                empty_label.grid(row=0, column=5, padx=5, pady=10)

                railType_label = Label(options_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                railType_label.grid(row=0, column=6, padx=(10, 0), pady=10, sticky="e")
                rail_type_combobox = ttk.Combobox(options_frame, width=12, values=list(rail_type_options.keys()), state="readonly")
                rail_type_combobox.grid(row=0, column=7, sticky="w")
                rail_type_combobox.set(rail_type_var.get())
                def update_rail_type(event):
                    selected_rail_type = rail_type_combobox.get()
                rail_type_combobox.bind("<<ComboboxSelected>>", update_rail_type)
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    rail_type_combobox.set(vanity_Drawers_cabinets[current_count].railType)
                if vanity_Drawers_cabinets[current_count].editable == False:
                    rail_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=9, padx=(27,5), pady=(0,5), sticky=N+E)
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True and vanity_Drawers_cabinets[current_count].editable == False:
                    completionStatus_label.config(text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=7, padx=(85,5), pady=(0,5), sticky=N+E)

                    materialThickness_label.grid(row=1, column=0, padx=(10, 0), pady=(0,10), sticky="e")
                    material_thickness_combobox.grid(row=1, column=1, pady=(0,10), sticky="w")
                    materialType_label.grid(row=1, column=3, padx=(3, 0), pady=(0,10), sticky="e")
                    material_type_combobox.grid(row=1, column=4, pady=(0,10), sticky="w")
                    empty_label.grid(row=1, column=5, padx=5, pady=(0,10))
                    railType_label.grid(row=1, column=6, padx=(10, 0), pady=(0,10), sticky="e")
                    rail_type_combobox.grid(row=1, column=7, pady=(0,10), sticky="w")

                elif vanity_Drawers_cabinets[current_count].completionStatus == True and vanity_Drawers_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=7, padx=(119,5), pady=(0,5), sticky=N+E)

                    materialThickness_label.grid(row=1, column=0, padx=(10, 0), pady=(0,10), sticky="e")
                    material_thickness_combobox.grid(row=1, column=1, pady=(0,10), sticky="w")
                    materialType_label.grid(row=1, column=3, padx=(3, 0), pady=(0,10), sticky="e")
                    material_type_combobox.grid(row=1, column=4, pady=(0,10), sticky="w")
                    empty_label.grid(row=1, column=5, padx=5, pady=(0,10))
                    railType_label.grid(row=1, column=6, padx=(10, 0), pady=(0,10), sticky="e")
                    rail_type_combobox.grid(row=1, column=7, pady=(0,10), sticky="w")

                #-------------------------------------------------- Vanity: Drawers: mid frame --------------------------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=1, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                mid_top_frame = Frame(mid_frame, bg=plainWhite)
                mid_top_frame.grid(row=0, column=0, sticky=N+W+E)

                width_label = Label(mid_top_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, vanity_Drawers_cabinets[current_count].width)
                if vanity_Drawers_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_top_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, vanity_Drawers_cabinets[current_count].height)
                elif action == "add" or vanity_Drawers_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "30.25")
                if vanity_Drawers_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_top_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=5, columnspan=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, vanity_Drawers_cabinets[current_count].depth)
                elif action == "add" or vanity_Drawers_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "20.75")
                if vanity_Drawers_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_top_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_top_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, vanity_Drawers_cabinets[current_count].toeKick)
                elif action == "add" or vanity_Drawers_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4")
                if vanity_Drawers_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                drawerDepth_label = Label(mid_top_frame, text="Drawer Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerDepth_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                drawerDepth_entry_combobox = ttk.Combobox(mid_top_frame, width=5, values=vanity_rail_size_options)
                drawerDepth_entry_combobox.grid(row=1, column=3, padx=10, sticky="w")
                drawerDepth_entry_combobox.set(vanity_rail_size_var.get())
                def update_drawerDepth_entry_combobox(event):
                    selected_drawerDepth = drawerDepth_entry_combobox.get()  # Use get() to retrieve the selected value
                drawerDepth_entry_combobox.bind("<<ComboboxSelected>>", update_drawerDepth_entry_combobox)
                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    drawerDepth_entry_combobox.set(vanity_Drawers_cabinets[current_count].drawerDepth)
                if vanity_Drawers_cabinets[current_count].editable == False:
                    drawerDepth_entry_combobox.config(state="disabled")

                #-------------------------------------------------- Vanity: Drawers: drawerHeights frame --------------------------------------------------//
                drawerHeights_frame = LabelFrame(mid_frame, text="Drawer Heights", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                drawerHeights_frame.grid(row=1, column=0, padx=15, pady=(0,15), sticky=W+E)

                drawerHeights_entries = []

                drawerHeights_entries = []

                def increment_drawer_qty(drawerHeight):
                    current_qty = int(drawerQty_var_label["text"])
                    new_qty = current_qty + 1
                    drawerQty_var_label["text"] = str(new_qty)
                    create_drawer_height_entry(new_qty, drawerHeight)  # Create a new drawer entry
                    update_drawer_height_entries()

                def decrement_drawer_qty():
                    current_qty = int(drawerQty_var_label["text"])
                    if current_qty > 1:
                        new_qty = current_qty - 1
                        drawerQty_var_label["text"] = str(new_qty)
                        remove_drawer_height_entry()  # Remove the last drawer entry
                        update_drawer_height_entries()

                def create_drawer_height_entry(entry_number, drawerHeight):
                    row = (entry_number-1) // 4  # Calculate the row based on the entry_number
                    column = (entry_number-1) % 4  # Calculate the column based on the entry_number

                    single_frame = Frame(drawerHeights_frame, bg=plainWhite)
                    single_frame.grid(row=row, column=column, sticky="w")

                    drawerNum_label = Label(single_frame, text="#" + str(entry_number), font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                    drawerNum_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                    drawer_height_entry = Entry(single_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                    drawer_height_entry.grid(row=0, column=1, padx=10, sticky="w")
                    drawer_height_entry.insert(0, drawerHeight)
                    if vanity_Drawers_cabinets[current_count].editable == False:
                        drawer_height_entry.config(state="readonly", fg=frontHighlightGray)

                    # Add the entry to the drawerHeights list if it's not empty. (this is checked in create_cabinet_object)
                    drawerHeights_entries.append(drawer_height_entry)

                def remove_drawer_height_entry():
                    last_entry = drawerHeights_frame.winfo_children()[-1]  # Get the last entry widget
                    last_entry.destroy()
                    # Remove the corresponding entry from the drawerHeights list
                    if drawerHeights_entries:
                        drawerHeights_entries.pop()

                def update_drawer_height_entries():
                    if action == "add" or vanity_Drawers_cabinets[current_count].completionStatus == False:
                        if len(drawerHeights_entries) == 1:
                            drawerHeights_entries[0].delete(0, 'end')
                            drawerHeights_entries[0].insert(0, "4.5")
                        elif len(drawerHeights_entries) > 1:
                            calculated_drawerHeight = (float(height_entry.get()) - 16.75) / (len(drawerHeights_entries) - 1)
                            for i in range(len(drawerHeights_entries)):
                                if i != 0:
                                    drawerHeights_entries[i].delete(0, 'end')
                                    drawerHeights_entries[i].insert(0, str(calculated_drawerHeight))

                drawerQty_label = Label(mid_top_frame, text="Drawer#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerQty_label.grid(row=1, column=4, padx=(10, 0), pady=10, sticky="e")

                drawerDecrement_button = Button(mid_top_frame, text="-", command=decrement_drawer_qty, width=3, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drawerDecrement_button.grid(row=1, column=5, padx=0, pady=10, sticky="e")

                drawerQty_var_label = Label(mid_top_frame, text="0", width=2, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerQty_var_label.grid(row=1, column=6, padx=0, pady=10)

                drawerIncrement_button = Button(mid_top_frame, text="+", command= lambda: increment_drawer_qty("0"), width=3, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drawerIncrement_button.grid(row=1, column=7, padx=0, pady=10, sticky="w")

                if action == "repopulate parent frame" and vanity_Drawers_cabinets[current_count].completionStatus == True:
                    for drawerHeight in vanity_Drawers_cabinets[current_count].drawerHeights:
                        increment_drawer_qty(drawerHeight)
                elif action == "add" or vanity_Drawers_cabinets[current_count].completionStatus == False:
                    increment_drawer_qty("4.5")
                    increment_drawer_qty("9")
                    increment_drawer_qty("9")
                if vanity_Drawers_cabinets[current_count].editable == False:
                    drawerDecrement_button.config(state="disabled")
                    drawerIncrement_button.config(state="disabled")

            #-------------------------------------------------- Vanity: Drawers: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if vanity_Drawers_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_vanity_Drawers_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    vanity_Drawers_cabinets.pop()  # Remove the latest item in the list
                    if not vanity_Drawers_cabinets:
                        workspace_vanity_Drawers_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if vanity_Drawers_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_vanity_Drawers_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not vanity_Drawers_cabinets:
                        workspace_vanity_Drawers_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_vanity_Drawers_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del vanity_Drawers_cabinets[currentCount]
                for child in workspace_vanity_Drawers_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not vanity_Drawers_cabinets:
                    workspace_vanity_Drawers_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "1Door 1Drawer": #------------------------------------------------------------- Vanity: 1D1D -------------------------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not vanity_1Door1Drawer_cabinets:
                    workspace_vanity_1D1D_frame.grid(row=2, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = Cabinet1D1D(category, cabinet_type, currentCount, 0, 0, 0, 0, 0, 0, 0, "", False, False, 0, "", True, False)
                    vanity_1Door1Drawer_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    vanity_1Door1Drawer_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_vanity_1D1D_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Vanity: 1D1D: Defining Buttons Frame and Buttons --------------------------------------------------//
                # Create a nested frame for the button
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, vanity_1Door1Drawer_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(vanity_1Door1Drawer_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_vanity_count(cabinet_type, current_count, vanity_1Door1Drawer_cabinets, "delete one"))

                #------------------------------- Vanity: 1D1D: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=vanity_1Door1Drawer_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")
                #------------------------------- Vanity: 1D1D: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                materialThickness_label = Label(options_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialThickness_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")
                material_thickness_combobox = ttk.Combobox(options_frame, width=5, values=material_thickness_options, state="readonly")
                material_thickness_combobox.grid(row=0, column=1, sticky="w")
                material_thickness_combobox.set(material_thickness_var.get())
                def update_material_thickness(event):
                    selected_material_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    material_thickness_combobox.set(vanity_1Door1Drawer_cabinets[current_count].materialThickness)
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    material_thickness_combobox.config(state="disabled")

                materialType_label = Label(options_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                materialType_label.grid(row=0, column=3, padx=(3, 0), pady=10, sticky="e")
                material_type_combobox = ttk.Combobox(options_frame, width=12, values=material_type_options, state="readonly")
                material_type_combobox.grid(row=0, column=4, sticky="w")
                material_type_combobox.set(material_type_var.get())
                def update_material_type(event):
                    selected_material_type = material_type_combobox.get()
                material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    material_type_combobox.set(vanity_1Door1Drawer_cabinets[current_count].materialType)
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    material_type_combobox.config(state="disabled")

                empty_label = Label(options_frame, text="-", font=fontSegoeSmall, bg=plainWhite, fg=plainWhite)
                empty_label.grid(row=0, column=5, padx=5, pady=10)

                railType_label = Label(options_frame, text="Railing: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                railType_label.grid(row=0, column=6, padx=(10, 0), pady=10, sticky="e")
                rail_type_combobox = ttk.Combobox(options_frame, width=12, values=list(rail_type_options.keys()), state="readonly")
                rail_type_combobox.grid(row=0, column=7, sticky="w")
                rail_type_combobox.set(rail_type_var.get())
                def update_rail_type(event):
                    selected_rail_type = rail_type_combobox.get()
                rail_type_combobox.bind("<<ComboboxSelected>>", update_rail_type)
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    rail_type_combobox.set(vanity_1Door1Drawer_cabinets[current_count].railType)
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    rail_type_combobox.config(state="disabled")

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=9, padx=(27,5), pady=(0,5), sticky=N+E)
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True and vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    completionStatus_label.config(text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=7, padx=(85,5), pady=(0,5), sticky=N+E)

                    materialThickness_label.grid(row=1, column=0, padx=(10, 0), pady=(0,10), sticky="e")
                    material_thickness_combobox.grid(row=1, column=1, pady=(0,10), sticky="w")
                    materialType_label.grid(row=1, column=3, padx=(3, 0), pady=(0,10), sticky="e")
                    material_type_combobox.grid(row=1, column=4, pady=(0,10), sticky="w")
                    empty_label.grid(row=1, column=5, padx=5, pady=(0,10))
                    railType_label.grid(row=1, column=6, padx=(10, 0), pady=(0,10), sticky="e")
                    rail_type_combobox.grid(row=1, column=7, pady=(0,10), sticky="w")

                elif vanity_1Door1Drawer_cabinets[current_count].completionStatus == True and vanity_1Door1Drawer_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=7, padx=(119,5), pady=(0,5), sticky=N+E)

                    materialThickness_label.grid(row=1, column=0, padx=(10, 0), pady=(0,10), sticky="e")
                    material_thickness_combobox.grid(row=1, column=1, pady=(0,10), sticky="w")
                    materialType_label.grid(row=1, column=3, padx=(3, 0), pady=(0,10), sticky="e")
                    material_type_combobox.grid(row=1, column=4, pady=(0,10), sticky="w")
                    empty_label.grid(row=1, column=5, padx=5, pady=(0,10))
                    railType_label.grid(row=1, column=6, padx=(10, 0), pady=(0,10), sticky="e")
                    rail_type_combobox.grid(row=1, column=7, pady=(0,10), sticky="w")

                #------------------------------- Vanity: 1D1D: mid frame -------------------------------//
                mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=(0,5), sticky=N+W+E)

                width_label = Label(mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(15, 0), pady=10, sticky="e")
                width_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, vanity_1Door1Drawer_cabinets[current_count].width)
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                height_label = Label(mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                height_label.grid(row=0, column=2, padx=(10, 0), pady=10, sticky="e")
                height_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                height_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    height_entry.insert(0, vanity_1Door1Drawer_cabinets[current_count].height)
                if action == "add" or vanity_1Door1Drawer_cabinets[current_count].completionStatus == False:
                    height_entry.insert(0, "30.25")
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    height_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=4, padx=(10, 0), pady=10, sticky="e")
                depth_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    depth_entry.insert(0, vanity_1Door1Drawer_cabinets[current_count].depth)
                if action == "add" or vanity_1Door1Drawer_cabinets[current_count].completionStatus == False:
                    depth_entry.insert(0, "20.75")
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(15, 0), pady=10, sticky="e")
                toeKick_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, vanity_1Door1Drawer_cabinets[current_count].toeKick)
                if action == "add" or vanity_1Door1Drawer_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4")
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                drawerDepth_label = Label(mid_frame, text="Drawer Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerDepth_label.grid(row=1, column=2, padx=(10, 0), pady=10, sticky="e")
                drawerDepth_entry_combobox = ttk.Combobox(mid_frame, width=5, values=vanity_rail_size_options)
                drawerDepth_entry_combobox.grid(row=1, column=3, padx=10, sticky="w")
                drawerDepth_entry_combobox.set(vanity_rail_size_var.get())
                def update_drawerDepth_entry_combobox(event):
                    selected_drawerDepth = drawerDepth_entry_combobox.get()  # Use get() to retrieve the selected value
                drawerDepth_entry_combobox.bind("<<ComboboxSelected>>", update_drawerDepth_entry_combobox)
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    drawerDepth_entry_combobox.set(vanity_1Door1Drawer_cabinets[current_count].drawerDepth)
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    drawerDepth_entry_combobox.config(state="disabled")

                drawerHeight_label = Label(mid_frame, text="Drawer Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                drawerHeight_label.grid(row=1, column=4, padx=(10, 0), pady=10, sticky="e")
                drawerHeight_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                drawerHeight_entry.grid(row=1, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    drawerHeight_entry.insert(0, vanity_1Door1Drawer_cabinets[current_count].drawerHeight)
                if action == "add" or vanity_1Door1Drawer_cabinets[current_count].completionStatus == False:
                    drawerHeight_entry.insert(0, "4.5")
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    drawerHeight_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=2, column=0, padx=(15, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=2, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, vanity_1Door1Drawer_cabinets[current_count].shelfQty)
                if action == "add" or vanity_1Door1Drawer_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Vanity: 1D1D: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=1, column=0, columnspan=4, padx=(20,0), pady=(0,10), sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(0,10), pady=10)
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=10)
                if vanity_1Door1Drawer_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and vanity_1Door1Drawer_cabinets[current_count].completionStatus == True:
                    if vanity_1Door1Drawer_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if vanity_1Door1Drawer_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Vanity: 1D1D: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if vanity_1Door1Drawer_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_vanity_1D1D_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    vanity_1Door1Drawer_cabinets.pop()  # Remove the latest item in the list
                    if not vanity_1Door1Drawer_cabinets:
                        workspace_vanity_1D1D_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if vanity_1Door1Drawer_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_vanity_1D1D_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not vanity_1Door1Drawer_cabinets:
                        workspace_vanity_1D1D_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_vanity_1D1D_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del vanity_1Door1Drawer_cabinets[currentCount]
                for child in workspace_vanity_1D1D_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not vanity_1Door1Drawer_cabinets:
                    workspace_vanity_1D1D_frame.grid_forget()  # Hide the frame

        elif cabinet_type == "Linen Tower": #------------------------------------------ Vanity: Linen Tower ------------------------------------------//
            if action == "add" or action == "repopulate parent frame":
                if not vanity_LinenTower_cabinets:
                    workspace_vanity_LinenTower_frame.grid(row=3, column=0, sticky=W+E)

                if action == "add":
                    new_cabinet = CabinetTall(category, cabinet_type, current_count, 0, 0, 0, 0, 0, 0, False, False, False, 0, 0, "", "", True, False)
                    vanity_LinenTower_cabinets.append(new_cabinet)
                if action == "repopulate parent frame":
                    vanity_LinenTower_cabinets[current_count].setFullName(category, cabinet_type, current_count)

                cabinet_frame = Frame(workspace_vanity_LinenTower_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)

                #------------------------------- Vanity: Linen Tower: Defining Buttons Frame and Buttons -------------------------------//
                button_frame = Frame(cabinet_frame, bg=plainWhite)
                button_frame.grid(row=0, column=1, pady=19, sticky="ne")

                # Create the button within the button_frame
                edit_cabinet_button = Button(button_frame, image=edit_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                edit_cabinet_button.image = edit_image  # Store a reference to the image
                edit_cabinet_button.grid(row=0, column=0, sticky="w")
                edit_cabinet_button.configure(command= lambda: make_cabinet_editable(category, vanity_LinenTower_cabinets))

                send_cabinet_button = Button(button_frame, image=send_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                send_cabinet_button.image = send_image
                send_cabinet_button.grid(row=1, column=0, pady=5, sticky="w")
                send_cabinet_button.configure(command= lambda: create_cabinet_object(vanity_LinenTower_cabinets))

                delete_cabinet_button = Button(button_frame, image=delete_image, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                delete_cabinet_button.image = delete_image
                delete_cabinet_button.grid(row=2, column=0, pady=(78,0), sticky="sw")
                delete_cabinet_button.configure(command= lambda: delete_vanity_count(cabinet_type, current_count, vanity_LinenTower_cabinets, "delete one"))

                #------------------------------- Vanity: Linen Tower: cabinet properties frame -------------------------------//
                cabinet_properties_frame = LabelFrame(cabinet_frame, text=vanity_LinenTower_cabinets[current_count].fullName, borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_properties_frame.grid(row=0, column=0, padx=(5,0), pady=5, ipadx=5, ipady=5, sticky="nw")

                #------------------------------- Vanity: Linen Tower: top frame -------------------------------//
                options_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                options_frame.grid(row=0, column=0, columnspan=20, padx=5, pady=5, sticky=W+E)

                completionStatus_label = Label(options_frame, text = "⬜", font = fontSegoeSmall, bg = plainWhite, fg = textGray)
                completionStatus_label.grid(row = 0, column=6, padx = (292,5), sticky=N+E)
                if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True and vanity_LinenTower_cabinets[current_count].editable == False:
                    completionStatus_label.config( text = "Completed ✅")
                    completionStatus_label.grid(row = 0, column=6, padx = (200,5), sticky=N+E)
                elif vanity_LinenTower_cabinets[current_count].completionStatus == True and vanity_LinenTower_cabinets[current_count].editable == True:
                    completionStatus_label.config( text = "Editing ⬜")
                    completionStatus_label.grid(row = 0, column=6, padx = (233,5), sticky=N+E)

                #------------------------------- Vanity: Linen Tower: mid frame -------------------------------//
                #-------------------- Vanity: Linen Tower: Top mid frame --------------------//
                right_mid_frame = Frame(cabinet_properties_frame, bg=plainWhite)
                right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                #-------------------- Vanity: Linen Tower: Declaring twoPieceData frames --------------------//
                top_right_mid_frame = LabelFrame(right_mid_frame, text="Upper Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                materialThickness_label = Label(top_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                material_thickness_combobox = ttk.Combobox(top_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_combobox = ttk.Combobox(top_right_mid_frame, width=12, values=material_type_options, state="readonly")
                height_entry = Entry(top_right_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                bottom_right_mid_frame = LabelFrame(right_mid_frame, text="Lower Piece", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                material_thickness_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=5, values=material_thickness_options, state="readonly")
                material_type_bottom_combobox = ttk.Combobox(bottom_right_mid_frame, width=12, values=material_type_options, state="readonly")
                height_bottom_entry = Entry(bottom_right_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)

                twoPieceBool = BooleanVar()
                twoPieceBool.set(False)

                topPieceData = []
                bottomPieceData = []

                def toggle_twoPiece_button():
                    for widget in right_mid_frame.winfo_children():
                        widget.grid_forget()
                    right_mid_frame.grid_forget()

                    topPieceData.clear()
                    bottomPieceData.clear()

                    if twoPiece_checkButton["text"] == "⬜ Two Piece ":
                        twoPiece_checkButton["text"] = "✅ Two Piece "
                        arrow_Button.config(image=arrowUp_image)
                        twoPieceBool.set(True)

                        #-------------------- Vanity: Linen Tower: top mid LabelFrame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="Upper Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(vanity_LinenTower_cabinets[current_count].materialThicknessTop)
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(vanity_LinenTower_cabinets[current_count].materialTypeTop)
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        height_label = Label(top_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, vanity_LinenTower_cabinets[current_count].heightTop)
                        if action == "add" or vanity_LinenTower_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, str(float(total_cabinet_height.get())/2)) # Divide cabinet height by two
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                        #-------------------- Vanity: Linen Tower: Bottom mid frame --------------------//
                        bottom_right_mid_frame.grid(row=2, column=0, padx=(20,10), pady=5, sticky=N+W)

                        materialThickness_bottom_label = Label(bottom_right_mid_frame, text="Material Thickness: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialThickness_bottom_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_bottom_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_bottom_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_bottom_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_bottom_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            if vanity_LinenTower_cabinets[current_count].twoPiece == False:
                                material_thickness_bottom_combobox.set(material_thickness_var.get())
                            else:
                                material_thickness_bottom_combobox.set(vanity_LinenTower_cabinets[current_count].materialThicknessBottom)
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            material_thickness_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_thickness_bottom_combobox)

                        materialType_bottom_label = Label(bottom_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_bottom_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_bottom_combobox.grid(row=0, column=3, sticky="w")
                        material_type_bottom_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_bottom_combobox.get()
                        material_type_bottom_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            if vanity_LinenTower_cabinets[current_count].twoPiece == False:
                                material_type_bottom_combobox.set(material_type_var.get())
                            else:
                                material_type_bottom_combobox.set(vanity_LinenTower_cabinets[current_count].materialTypeBottom)
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            material_type_bottom_combobox.config(state="disabled")

                        bottomPieceData.append(material_type_bottom_combobox)

                        height_bottom_label = Label(bottom_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_bottom_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_bottom_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            if vanity_LinenTower_cabinets[current_count].twoPiece == False:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2))  # Divide cabinet height by two
                            else:
                                height_bottom_entry.delete(0, 'end')
                                height_bottom_entry.insert(0, vanity_LinenTower_cabinets[current_count].heightBottom)
                        if action == "add" or vanity_LinenTower_cabinets[current_count].completionStatus == False:
                            height_bottom_entry.delete(0, 'end')
                            height_bottom_entry.insert(0, str(float(total_cabinet_height.get())/2))  # Divide cabinet height by two
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            height_bottom_entry.config(state="readonly", fg=frontHighlightGray)

                        bottomPieceData.append(height_bottom_entry)

                    else:
                        twoPiece_checkButton["text"] = "⬜ Two Piece "
                        arrow_Button.config(image=arrowDown_image)
                        twoPieceBool.set(False)

                        #-------------------- Vanity: Linen Tower: Top mid frame --------------------//
                        right_mid_frame.grid(row=1, column=0, columnspan=5, sticky=N+W)

                        top_right_mid_frame.grid(row=0, column=0, padx=(20,10), pady=(10, 0), sticky=N+W)
                        top_right_mid_frame.config(text="One Piece", borderwidth=2, relief="groove")

                        materialThickness_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                        material_thickness_combobox.grid(row=0, column=1, sticky="w")
                        material_thickness_combobox.set(material_thickness_var.get())
                        def update_material_thickness(event):
                            selected_thickness = material_thickness_combobox.get()  # Use get() to retrieve the selected value
                        material_thickness_combobox.bind("<<ComboboxSelected>>", update_material_thickness)
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            material_thickness_combobox.set(vanity_LinenTower_cabinets[current_count].materialThicknessTop)
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            material_thickness_combobox.config(state="disabled")

                        topPieceData.append(material_thickness_combobox)

                        materialType_label = Label(top_right_mid_frame, text="Type: ", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        materialType_label.grid(row=0, column=2, padx=(3, 0), pady=10, sticky="e")
                        material_type_combobox.grid(row=0, column=3, sticky="w")
                        material_type_combobox.set(material_type_var.get())
                        def update_material_type(event):
                            selected_type = material_type_combobox.get()
                        material_type_combobox.bind("<<ComboboxSelected>>", update_material_type)
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            material_type_combobox.set(vanity_LinenTower_cabinets[current_count].materialTypeTop)
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            material_type_combobox.config(state="disabled")

                        topPieceData.append(material_type_combobox)

                        height_label = Label(top_right_mid_frame, text="Height:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                        height_label.grid(row=0, column=4, padx=(30, 0), pady=10, sticky="e")
                        height_entry.grid(row=0, column=5, padx=10, sticky="w")
                        if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, vanity_LinenTower_cabinets[current_count].heightTop)
                        if action == "add" or vanity_LinenTower_cabinets[current_count].completionStatus == False:
                            height_entry.delete(0, 'end')
                            height_entry.insert(0, total_cabinet_height.get())
                        if vanity_LinenTower_cabinets[current_count].editable == False:
                            height_entry.config(state="readonly", fg=frontHighlightGray)

                        topPieceData.append(height_entry)

                twoPiece_checkButton = Button(options_frame, text="✅ Two Piece ", command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                twoPiece_checkButton.grid(row=0, column=0, padx=(15,0), pady=(10, 0))
                arrow_Button = Button(options_frame, image=arrowDown_image, height=36, command=toggle_twoPiece_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                arrow_Button.grid(row=0, column=1, pady=(10, 0))
                toggle_twoPiece_button()
                if vanity_LinenTower_cabinets[current_count].editable == False:
                    twoPiece_checkButton.config(state="disabled")
                    arrow_Button.config(state="disabled")
                if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                    if vanity_LinenTower_cabinets[current_count].twoPiece == True:
                        toggle_twoPiece_button()

                #-------------------- Vanity: Linen Tower: Bottom mid frame --------------------//
                left_mid_frame = LabelFrame(cabinet_properties_frame, text="Main Components", borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
                left_mid_frame.grid(row=2, column=0, columnspan=2, padx=(20,0), pady=5, sticky=N+W+E)

                width_label = Label(left_mid_frame, text="Width:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                width_label.grid(row=0, column=0, padx=(20, 0), pady=10, sticky="e")
                width_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                width_entry.grid(row=0, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                    width_entry.insert(0, vanity_LinenTower_cabinets[current_count].width)
                if vanity_LinenTower_cabinets[current_count].editable == False:
                    width_entry.config(state="readonly", fg=frontHighlightGray)

                depth_label = Label(left_mid_frame, text="Depth:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                depth_label.grid(row=0, column=2, padx=(20, 0), pady=10, sticky="e")
                depth_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                depth_entry.grid(row=0, column=3, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, vanity_LinenTower_cabinets[current_count].depth)
                if action == "add" or vanity_LinenTower_cabinets[current_count].completionStatus == False:
                    depth_entry.delete(0, 'end')
                    depth_entry.insert(0, "20.75")
                if vanity_LinenTower_cabinets[current_count].editable == False:
                    depth_entry.config(state="readonly", fg=frontHighlightGray)

                shelfQty_label = Label(left_mid_frame, text="Shelves#:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                shelfQty_label.grid(row=0, column=4, padx=(20, 0), pady=10, sticky="e")
                shelfQty_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                shelfQty_entry.grid(row=0, column=5, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                    shelfQty_entry.insert(0, vanity_LinenTower_cabinets[current_count].shelfQty)
                if action == "add" or vanity_LinenTower_cabinets[current_count].completionStatus == False:
                    shelfQty_entry.insert(0, "1")
                if vanity_LinenTower_cabinets[current_count].editable == False:
                    shelfQty_entry.config(state="readonly", fg=frontHighlightGray)

                toeKick_label = Label(left_mid_frame, text="Toe Kick:", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
                toeKick_label.grid(row=1, column=0, padx=(20, 0), pady=10, sticky="e")
                toeKick_entry = Entry(left_mid_frame, width=10, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, highlightcolor=frontHighlightGray)
                toeKick_entry.grid(row=1, column=1, padx=10, sticky="w")
                if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                    toeKick_entry.insert(0, vanity_LinenTower_cabinets[current_count].toeKick)
                if action == "add" or vanity_LinenTower_cabinets[current_count].completionStatus == False:
                    toeKick_entry.insert(0, "4")
                if vanity_LinenTower_cabinets[current_count].editable == False:
                    toeKick_entry.config(state="readonly", fg=frontHighlightGray)

                #------------------------------- Vanity: Linen Tower: toggle buttons -------------------------------//
                toggleButtons_frame = Frame(options_frame, bg=plainWhite)
                toggleButtons_frame.grid(row=0, column=2, columnspan=3, padx=(45,0), pady=(0, 5), sticky=W+E)

                drillBool = BooleanVar()
                drillBool.set(False)
                routerBool = BooleanVar()
                routerBool.set(False)

                def toggle_drill_button():
                    if drill_checkButton["text"] == "⬜ Drill":
                        drill_checkButton["text"] = "✅ Drill"
                        drillBool.set(True)
                    else:
                        drill_checkButton["text"] = "⬜ Drill"
                        drillBool.set(False)
                drill_checkButton = Button(toggleButtons_frame, text="⬜ Drill", command=toggle_drill_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                drill_checkButton.grid(row=0, column=0, padx=(25,10), pady=(10, 0))
                if vanity_LinenTower_cabinets[current_count].editable == False:
                    drill_checkButton.config(state="disabled")

                def toggle_router_button():
                    if router_checkButton["text"] == "⬜ Router":
                        router_checkButton["text"] = "✅ Router"
                        routerBool.set(True)
                    else:
                        router_checkButton["text"] = "⬜ Router"
                        routerBool.set(False)
                router_checkButton = Button(toggleButtons_frame, text="⬜ Router", command=toggle_router_button, font=fontSegoeSmall, bd=1, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
                router_checkButton.grid(row=0, column=1, padx=10, pady=(10, 0))
                if vanity_LinenTower_cabinets[current_count].editable == False:
                    router_checkButton.config(state="disabled")

                if action == "repopulate parent frame" and vanity_LinenTower_cabinets[current_count].completionStatus == True:
                    if vanity_LinenTower_cabinets[current_count].drill == True:
                        toggle_drill_button()
                    if vanity_LinenTower_cabinets[current_count].router == True:
                        toggle_router_button()

            #-------------------------------------------------- Vanity: Linen Tower: functions --------------------------------------------------//
            elif action == "remove last frame": # Remove the last frame
                if vanity_LinenTower_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_vanity_LinenTower_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    vanity_LinenTower_cabinets.pop()  # Remove the latest item in the list
                    if not vanity_LinenTower_cabinets:
                        workspace_vanity_LinenTower_frame.grid_forget()  # Hide the frame

            elif action == "remove specific frame": # Remove the last frame
                if vanity_LinenTower_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_vanity_LinenTower_frame.winfo_children()[current_count]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    if not vanity_LinenTower_cabinets:
                        workspace_vanity_LinenTower_frame.grid_forget()  # Hide the frame

            elif action == "empty parent frame":
                for child in workspace_vanity_LinenTower_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()

            elif action == "delete i and empty parent frame":
                del vanity_LinenTower_cabinets[currentCount]
                for child in workspace_vanity_LinenTower_frame.winfo_children(): # Delete all children in workspace_base_FullDoor_frame
                    child.destroy()
                if not vanity_LinenTower_cabinets:
                    workspace_vanity_LinenTower_frame.grid_forget()  # Hide the frame

    elif category == "Custom": #---------------------------------------------------------------- Custom ----------------------------------------------------------------//
        if cabinet_type == "Custom": #------------------------------------------ Custom ------------------------------------------//
            if action == "add":
                if not custom_cabinets:
                    workspace_custom_frame.grid(row=4, column=0, sticky=W+E)
                new_cabinet = CabinetCorner(category, cabinet_type, current_count, 0, 0, 0, 0, 0, 0, 0, False, False, material_thickness_var.get(), False)
                custom_cabinets.append(new_cabinet)
                cabinet_frame = LabelFrame(workspace_custom_frame, text=cabinet_type + " " + str(current_count), borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
                cabinet_frame.pack(anchor=W, padx=5, pady=5, ipadx=3, ipady=5)
                submit_button = Button(cabinet_frame, text="Submit")
                submit_button.grid(row=0, column=0, padx=5, pady=5, sticky=W+S)
            elif action == "remove last frame": # Remove the last frame
                if custom_cabinets:  # Check if the list is not empty
                    removed_cabinet_frame = workspace_custom_frame.winfo_children()[-1]  # Get the last frame
                    removed_cabinet_frame.destroy()  # Remove the last frame
                    custom_cabinets.pop()  # Remove the latest item in the list
                    if not custom_cabinets:
                        workspace_custom_frame.grid_forget()  # Hide the frame


#-------------------------------------------------- Function to auto scroll --------------------------------------------------//
def auto_scroll_workspaceScrollbar(category, cabinet_type, givenCount):
    index = 0
    for cabinets_list in all_cabinet_lists:
        for cabinet_list in cabinets_list:
            for cabinet in cabinet_list:
                index += 1
                if cabinet.cabinetID == category + ", " + cabinet_type + " " + str(givenCount + 1):
                    selected_item_position = index *60
                    workspace_canvas.update_idletasks()
                    workspace_canvas.configure(scrollregion=workspace_canvas.bbox("all"))
                    fraction = selected_item_position / workspace_canvas.winfo_height()
                    workspace_canvas.yview_moveto(fraction)


#-------------------------------------------------- Base Cabinets --------------------------------------------------//
# Create a label frame inside page1_frame for "Base Cabinets"
base_cabinets_frame = LabelFrame(selectCabinets_frame, text=" Base:  ", borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
base_cabinets_frame.pack(anchor=W, padx=5, pady=5, ipadx=3, ipady=5, fill=BOTH)

# List of base cabinet types
base_cabinet_types = [
    "Full Door",
    "Drawers",
    "1Door 1Drawer",
    "Corner 90",
    "Corner Diagonal",
    "Corner Blind"
]

# Create buttons to increase and decrease the amount of each cabinet type
base_cabinet_counts = {cabinet_type: IntVar(value=0) for cabinet_type in base_cabinet_types}

for i, cabinet_type in enumerate(base_cabinet_types):
    cabinet_label = Label(base_cabinets_frame, text=cabinet_type, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    cabinet_label.grid(row=i, column=0, padx=4, pady=5, sticky=W)

    decrease_button = Button(base_cabinets_frame, text="-", font=fontSegoeSmall, command=lambda ct=cabinet_type: decrement_base_count(ct), bg=plainWhite, fg=textGray)
    decrease_button.grid(row=i, column=1, padx=1, ipadx=2, sticky=E)

    count_label = Label(base_cabinets_frame, textvariable=base_cabinet_counts[cabinet_type], font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    count_label.grid(row=i, column=2, padx=5, sticky=E)

    increase_button = Button(base_cabinets_frame, text="+", font=fontSegoeSmall, command=lambda ct=cabinet_type: increment_base_count(ct), bg=plainWhite, fg=textGray)
    increase_button.grid(row=i, column=3, padx=(1,7), sticky=E)

base_cabinets_frame.columnconfigure(0, weight=1)

# Function to increment cabinet count
def increment_base_count(cabinet_type):
    current_count = base_cabinet_counts[cabinet_type].get()
    base_cabinet_counts[cabinet_type].set(current_count + 1)
    update_workspace_frames(cabinet_type, current_count, "Base", "add")
    update_allCabinets_list()
    auto_scroll_workspaceScrollbar("Base", cabinet_type, current_count)

# Function to decrement cabinet count
def decrement_base_count(cabinet_type):
    current_count = base_cabinet_counts[cabinet_type].get()

    completed_cabinets = 0
    base_cabinet_object_list = []

    if cabinet_type == "Full Door":
        base_cabinet_object_list = base_FullDoor_cabinets
    elif cabinet_type == "Drawers":
        base_cabinet_object_list = base_Drawers_cabinets
    elif cabinet_type == "1Door 1Drawer":
        base_cabinet_object_list = base_1D1D_cabinets
    elif cabinet_type == "Corner 90":
        base_cabinet_object_list = base_Corner90_cabinets
    elif cabinet_type == "Corner Diagonal":
        base_cabinet_object_list = base_CornerDiagonal_cabinets
    elif cabinet_type == "Corner Blind":
        base_cabinet_object_list = base_CornerBlind_cabinets

    for i in range(len(base_cabinet_object_list)):
        if base_cabinet_object_list[i].completionStatus == True:
            completed_cabinets += 1

    if current_count > 0 and current_count > completed_cabinets:
        if base_cabinet_object_list[current_count-1].completionStatus == True:
            messagebox.showwarning("Invalid Input", "Can not decrement completed cabinets.\nTo remove cabinets, use the delete button.")
        else:
            base_cabinet_counts[cabinet_type].set(current_count - 1)
            update_workspace_frames(cabinet_type, current_count, "Base", "remove last frame")
            update_allCabinets_list()

    elif current_count == completed_cabinets:
        messagebox.showwarning("Invalid Input", "Can not decrement completed cabinets.\nTo remove completed cabinets, use the delete button.")

    workspace_canvas.update_idletasks()
    workspace_canvas.configure(scrollregion=workspace_canvas.bbox("all"))

def delete_base_count(cabinet_type, given_count, base_cabinet_object_list, action):
    current_count = base_cabinet_counts[cabinet_type].get()

    if base_cabinet_object_list[given_count].completionStatus == True:
        if action == "reset":
            if current_count > 0:
                base_cabinet_counts[cabinet_type].set(current_count - 1)
                update_workspace_frames(cabinet_type, given_count, "Base", "delete i and empty parent frame")
                update_allCabinets_list()

                base_cabinet_counts[cabinet_type].set(0)
                for i in range(len(base_cabinet_object_list)):
                    current_count = base_cabinet_counts[cabinet_type].get()
                    base_cabinet_counts[cabinet_type].set(current_count + 1)
                    update_workspace_frames(cabinet_type, current_count, "Base", "repopulate parent frame")
                    update_allCabinets_list()

                send_cabinet_to_cutlist("Base", current_count, cabinet_type)
        elif action == "delete one":
            response = messagebox.askyesno("Warning", "Do you want to delete " + base_cabinet_object_list[given_count].fullName + "?\nThis will also delete the item from the Cutlist.")
            if response:  # If 'Yes' button is clicked
                if current_count > 0:
                    base_cabinet_counts[cabinet_type].set(current_count - 1)
                    update_workspace_frames(cabinet_type, given_count, "Base", "delete i and empty parent frame")
                    update_allCabinets_list()

                    base_cabinet_counts[cabinet_type].set(0)
                    for i in range(len(base_cabinet_object_list)):
                        current_count = base_cabinet_counts[cabinet_type].get()
                        base_cabinet_counts[cabinet_type].set(current_count + 1)
                        update_workspace_frames(cabinet_type, current_count, "Base", "repopulate parent frame")
                        update_allCabinets_list()

                    send_cabinet_to_cutlist("Base", current_count, cabinet_type)

            else:  # If 'No' button is clicked
                pass

    elif base_cabinet_object_list[given_count].completionStatus == False:
        if action == "reset":
            if current_count > 0:
                base_cabinet_counts[cabinet_type].set(current_count - 1)
                update_workspace_frames(cabinet_type, given_count, "Base", "delete i and empty parent frame")
                update_allCabinets_list()

                base_cabinet_counts[cabinet_type].set(0)
                for i in range(len(base_cabinet_object_list)):
                    current_count = base_cabinet_counts[cabinet_type].get()
                    base_cabinet_counts[cabinet_type].set(current_count + 1)
                    update_workspace_frames(cabinet_type, current_count, "Base", "repopulate parent frame")
                    update_allCabinets_list()

                send_cabinet_to_cutlist("Base", current_count, cabinet_type)
        elif action == "delete one":
            response = messagebox.askyesno("Warning", "Do you want to delete " + base_cabinet_object_list[given_count].fullName + "?")
            if response:  # If 'Yes' button is clicked
                if current_count > 0:
                    base_cabinet_counts[cabinet_type].set(current_count - 1)
                    update_workspace_frames(cabinet_type, given_count, "Base", "delete i and empty parent frame")
                    update_allCabinets_list()

                    base_cabinet_counts[cabinet_type].set(0)
                    for i in range(len(base_cabinet_object_list)):
                        current_count = base_cabinet_counts[cabinet_type].get()
                        base_cabinet_counts[cabinet_type].set(current_count + 1)
                        update_workspace_frames(cabinet_type, current_count, "Base", "repopulate parent frame")
                        update_allCabinets_list()

                    send_cabinet_to_cutlist("Base", current_count, cabinet_type)

            else:  # If 'No' button is clicked
                pass
    all_base_parts_list.clear()
    base_cabinets_list_copy = base_cabinets_list[:]
    merge_cabinet_parts(base_cabinets_list_copy, all_base_parts_list)

    workspace_canvas.update_idletasks()
    workspace_canvas.configure(scrollregion=workspace_canvas.bbox("all"))

def regenerate_base_count(cabinet_type, given_count, base_cabinet_object_list):
    update_workspace_frames(cabinet_type, given_count, "Base", "empty parent frame")
    update_allCabinets_list()

    base_cabinet_counts[cabinet_type].set(0)
    for i in range(len(base_cabinet_object_list)):
        # print("in regen, len(base_cabinet_object_list): " + str(len(base_cabinet_object_list)))
        current_count = base_cabinet_counts[cabinet_type].get()
        base_cabinet_counts[cabinet_type].set(current_count + 1)
        update_workspace_frames(cabinet_type, current_count, "Base", "repopulate parent frame")
        update_allCabinets_list()

    workspace_canvas.update_idletasks()
    workspace_canvas.configure(scrollregion=workspace_canvas.bbox("all"))

#-------------------------------------------------- Wall Cabinets --------------------------------------------------//
# Create a label frame inside page2_app_frame for "Wall Cabinets"
wall_cabinets_frame = LabelFrame(selectCabinets_frame, text=" Wall:  ", borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
wall_cabinets_frame.pack(anchor=W, padx=5, pady=5, ipadx=3, ipady=5, fill=BOTH)

# List of wall cabinet types
wall_cabinet_types = [
    "Full Door",
    "Corner 90",
    "Corner Diagonal",
    "Microwave Slot"
]

# Create buttons to increase and decrease the amount of each wall cabinet type
wall_cabinet_counts = {cabinet_type: IntVar(value=0) for cabinet_type in wall_cabinet_types}

for i, cabinet_type in enumerate(wall_cabinet_types):
    cabinet_label = Label(wall_cabinets_frame, text=cabinet_type, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    cabinet_label.grid(row=i, column=0, padx=5, pady=5, sticky=W)

    decrease_button = Button(wall_cabinets_frame, text="-", font=fontSegoeSmall, command=lambda ct=cabinet_type: decrement_wall_count(ct), bg=plainWhite, fg=textGray)
    decrease_button.grid(row=i, column=1, padx=1, ipadx=2, sticky=E)

    count_label = Label(wall_cabinets_frame, textvariable=wall_cabinet_counts[cabinet_type], font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    count_label.grid(row=i, column=2, padx=5, sticky=E)

    increase_button = Button(wall_cabinets_frame, text="+", font=fontSegoeSmall, command=lambda ct=cabinet_type: increment_wall_count(ct), bg=plainWhite, fg=textGray)
    increase_button.grid(row=i, column=3, padx=(1,7), sticky=E)

wall_cabinets_frame.columnconfigure(0, weight=1)

# Function to increment wall cabinet count
def increment_wall_count(cabinet_type):
    current_count = wall_cabinet_counts[cabinet_type].get()
    wall_cabinet_counts[cabinet_type].set(current_count + 1)
    update_workspace_frames(cabinet_type, current_count, "Wall", "add")
    update_allCabinets_list()
    auto_scroll_workspaceScrollbar("Wall", cabinet_type, current_count)

# Function to decrement wall cabinet count
def decrement_wall_count(cabinet_type):
    current_count = wall_cabinet_counts[cabinet_type].get()

    completed_cabinets = 0
    wall_cabinet_object_list = []

    if cabinet_type == "Full Door":
        wall_cabinet_object_list = wall_FullDoor_cabinets
    elif cabinet_type == "Corner 90":
        wall_cabinet_object_list = wall_Corner90_cabinets
    elif cabinet_type == "Corner Diagonal":
        wall_cabinet_object_list = wall_CornerDiagonal_cabinets
    elif cabinet_type == "Microwave Slot":
        wall_cabinet_object_list = wall_MicowaveSlot_cabinets

    for i in range(len(wall_cabinet_object_list)):
        if wall_cabinet_object_list[i].completionStatus == True:
            completed_cabinets += 1

    if current_count > 0 and current_count > completed_cabinets:
        if wall_cabinet_object_list[current_count-1].completionStatus == True:
            messagebox.showwarning("Invalid Input", "Can not decrement completed cabinets.\nTo remove cabinets, use the delete button.")
        else:
            wall_cabinet_counts[cabinet_type].set(current_count - 1)
            update_workspace_frames(cabinet_type, current_count, "Wall", "remove last frame")
            update_allCabinets_list()

    elif current_count == completed_cabinets:
        messagebox.showwarning("Invalid Input", "Can not decrement completed cabinets.\nTo remove completed cabinets, use the delete button.")

    workspace_canvas.update_idletasks()
    workspace_canvas.configure(scrollregion=workspace_canvas.bbox("all"))

def delete_wall_count(cabinet_type, given_count, wall_cabinet_object_list, action):
    current_count = wall_cabinet_counts[cabinet_type].get()

    if wall_cabinet_object_list[given_count].completionStatus == True:
        if action == "reset":
            if current_count > 0:
                wall_cabinet_counts[cabinet_type].set(current_count - 1)
                update_workspace_frames(cabinet_type, given_count, "Wall", "delete i and empty parent frame")
                update_allCabinets_list()

                wall_cabinet_counts[cabinet_type].set(0)
                for i in range(len(wall_cabinet_object_list)):
                    current_count = wall_cabinet_counts[cabinet_type].get()
                    wall_cabinet_counts[cabinet_type].set(current_count + 1)
                    update_workspace_frames(cabinet_type, current_count, "Wall", "repopulate parent frame")
                    update_allCabinets_list()

                send_cabinet_to_cutlist("Wall", current_count, cabinet_type)
        elif action == "delete one":
            response = messagebox.askyesno("Warning", "Do you want to delete " + wall_cabinet_object_list[given_count].fullName + "?\nThis will also delete the item from the Cutlist.")
            if response:  # If 'Yes' button is clicked
                if current_count > 0:
                    wall_cabinet_counts[cabinet_type].set(current_count - 1)
                    update_workspace_frames(cabinet_type, given_count, "Wall", "delete i and empty parent frame")
                    update_allCabinets_list()

                    wall_cabinet_counts[cabinet_type].set(0)
                    for i in range(len(wall_cabinet_object_list)):
                        current_count = wall_cabinet_counts[cabinet_type].get()
                        wall_cabinet_counts[cabinet_type].set(current_count + 1)
                        update_workspace_frames(cabinet_type, current_count, "Wall", "repopulate parent frame")
                        update_allCabinets_list()

                    send_cabinet_to_cutlist("Wall", current_count, cabinet_type)

            else:  # If 'No' button is clicked
                pass

    elif wall_cabinet_object_list[given_count].completionStatus == False:
        if action == "reset":
            if current_count > 0:
                wall_cabinet_counts[cabinet_type].set(current_count - 1)
                update_workspace_frames(cabinet_type, given_count, "Wall", "delete i and empty parent frame")
                update_allCabinets_list()

                wall_cabinet_counts[cabinet_type].set(0)
                for i in range(len(wall_cabinet_object_list)):
                    current_count = wall_cabinet_counts[cabinet_type].get()
                    wall_cabinet_counts[cabinet_type].set(current_count + 1)
                    update_workspace_frames(cabinet_type, current_count, "Wall", "repopulate parent frame")
                    update_allCabinets_list()

                send_cabinet_to_cutlist("Wall", current_count, cabinet_type)
        elif action == "delete one":
            response = messagebox.askyesno("Warning", "Do you want to delete " + wall_cabinet_object_list[given_count].fullName + "?")
            if response:  # If 'Yes' button is clicked
                if current_count > 0:
                    wall_cabinet_counts[cabinet_type].set(current_count - 1)
                    update_workspace_frames(cabinet_type, given_count, "Wall", "delete i and empty parent frame")
                    update_allCabinets_list()

                    wall_cabinet_counts[cabinet_type].set(0)
                    for i in range(len(wall_cabinet_object_list)):
                        current_count = wall_cabinet_counts[cabinet_type].get()
                        wall_cabinet_counts[cabinet_type].set(current_count + 1)
                        update_workspace_frames(cabinet_type, current_count, "Wall", "repopulate parent frame")
                        update_allCabinets_list()

                    send_cabinet_to_cutlist("Wall", current_count, cabinet_type)

            else:  # If 'No' button is clicked
                pass
    all_wall_parts_list.clear()
    wall_cabinets_list_copy = wall_cabinets_list[:]
    merge_cabinet_parts(wall_cabinets_list_copy, all_wall_parts_list)

def regenerate_wall_count(cabinet_type, given_count, wall_cabinet_object_list):
    update_workspace_frames(cabinet_type, given_count, "Wall", "empty parent frame")
    update_allCabinets_list()
    wall_cabinet_counts[cabinet_type].set(0)
    for i in range(len(wall_cabinet_object_list)):
        current_count = wall_cabinet_counts[cabinet_type].get()
        wall_cabinet_counts[cabinet_type].set(current_count + 1)
        update_workspace_frames(cabinet_type, current_count, "Wall", "repopulate parent frame")
        update_allCabinets_list()

#-------------------------------------------------- Tall Cabinets --------------------------------------------------//
# Create a label frame inside page2_app_frame for "Tall Cabinets"
tall_cabinets_frame = LabelFrame(selectCabinets_frame, text=" Tall:  ", borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
tall_cabinets_frame.pack(anchor=W, padx=5, pady=5, ipadx=3, ipady=5, fill=BOTH)

# List of tall cabinet types
tall_cabinet_types = [
    "Full Door",
    "Pantry",
    "Oven Slot",
    "Pull Out"
]

# Create buttons to increase and decrease the amount of each tall cabinet type
tall_cabinet_counts = {cabinet_type: IntVar(value=0) for cabinet_type in tall_cabinet_types}

for i, cabinet_type in enumerate(tall_cabinet_types):
    cabinet_label = Label(tall_cabinets_frame, text=cabinet_type, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    cabinet_label.grid(row=i, column=0, padx=7, pady=5, sticky=W)

    decrease_button = Button(tall_cabinets_frame, text="-", font=fontSegoeSmall, command=lambda ct=cabinet_type: decrement_tall_count(ct), bg=plainWhite, fg=textGray)
    decrease_button.grid(row=i, column=1, padx=1, ipadx=2, sticky=E)

    count_label = Label(tall_cabinets_frame, textvariable=tall_cabinet_counts[cabinet_type], font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    count_label.grid(row=i, column=2, padx=5, sticky=E)

    increase_button = Button(tall_cabinets_frame, text="+", font=fontSegoeSmall, command=lambda ct=cabinet_type: increment_tall_count(ct), bg=plainWhite, fg=textGray)
    increase_button.grid(row=i, column=3, padx=(1,7), sticky=E)

tall_cabinets_frame.columnconfigure(0, weight=1)

# Function to increment tall cabinet count
def increment_tall_count(cabinet_type):
    current_count = tall_cabinet_counts[cabinet_type].get()
    tall_cabinet_counts[cabinet_type].set(current_count + 1)
    update_workspace_frames(cabinet_type, current_count, "Tall", "add")
    update_allCabinets_list()
    auto_scroll_workspaceScrollbar("Tall", cabinet_type, current_count)

# Function to decrement tall cabinet count
def decrement_tall_count(cabinet_type):
    current_count = tall_cabinet_counts[cabinet_type].get()

    completed_cabinets = 0
    tall_cabinet_object_list = []

    if cabinet_type == "Full Door":
        tall_cabinet_object_list = tall_FullDoor_cabinets
    elif cabinet_type == "Pantry":
        tall_cabinet_object_list = tall_Pantry_cabinets
    elif cabinet_type == "Oven Slot":
        tall_cabinet_object_list = tall_OvenSlot_cabinets
    elif cabinet_type == "Pull Out":
        tall_cabinet_object_list = tall_PullOut_cabinets

    for i in range(len(tall_cabinet_object_list)):
        if tall_cabinet_object_list[i].completionStatus == True:
            completed_cabinets += 1

    if current_count > 0 and current_count > completed_cabinets:
        if tall_cabinet_object_list[current_count-1].completionStatus == True:
            messagebox.showwarning("Invalid Input", "Can not decrement completed cabinets.\nTo remove cabinets, use the delete button.")
        else:
            tall_cabinet_counts[cabinet_type].set(current_count - 1)
            update_workspace_frames(cabinet_type, current_count, "Tall", "remove last frame")
            update_allCabinets_list()

    elif current_count == completed_cabinets:
        messagebox.showwarning("Invalid Input", "Can not decrement completed cabinets.\nTo remove completed cabinets, use the delete button.")

    workspace_canvas.update_idletasks()
    workspace_canvas.configure(scrollregion=workspace_canvas.bbox("all"))

def delete_tall_count(cabinet_type, given_count, tall_cabinet_object_list, action):
    current_count = tall_cabinet_counts[cabinet_type].get()

    if tall_cabinet_object_list[given_count].completionStatus == True:
        if action == "reset":
            if current_count > 0:
                tall_cabinet_counts[cabinet_type].set(current_count - 1)
                update_workspace_frames(cabinet_type, given_count, "Tall", "delete i and empty parent frame")
                update_allCabinets_list()

                tall_cabinet_counts[cabinet_type].set(0)
                for i in range(len(tall_cabinet_object_list)):
                    current_count = tall_cabinet_counts[cabinet_type].get()
                    tall_cabinet_counts[cabinet_type].set(current_count + 1)
                    update_workspace_frames(cabinet_type, current_count, "Tall", "repopulate parent frame")
                    update_allCabinets_list()

                send_cabinet_to_cutlist("Tall", current_count, cabinet_type)
        elif action == "delete one":
            response = messagebox.askyesno("Warning", "Do you want to delete " + tall_cabinet_object_list[given_count].fullName + "?\nThis will also delete the item from the Cutlist.")
            if response:  # If 'Yes' button is clicked
                if current_count > 0:
                    tall_cabinet_counts[cabinet_type].set(current_count - 1)
                    update_workspace_frames(cabinet_type, given_count, "Tall", "delete i and empty parent frame")
                    update_allCabinets_list()

                    tall_cabinet_counts[cabinet_type].set(0)
                    for i in range(len(tall_cabinet_object_list)):
                        current_count = tall_cabinet_counts[cabinet_type].get()
                        tall_cabinet_counts[cabinet_type].set(current_count + 1)
                        update_workspace_frames(cabinet_type, current_count, "Tall", "repopulate parent frame")
                        update_allCabinets_list()

                    send_cabinet_to_cutlist("Tall", current_count, cabinet_type)

            else:  # If 'No' button is clicked
                pass

    elif tall_cabinet_object_list[given_count].completionStatus == False:
        if action == "reset":
            if current_count > 0:
                tall_cabinet_counts[cabinet_type].set(current_count - 1)
                update_workspace_frames(cabinet_type, given_count, "Tall", "delete i and empty parent frame")
                update_allCabinets_list()

                tall_cabinet_counts[cabinet_type].set(0)
                for i in range(len(tall_cabinet_object_list)):
                    current_count = tall_cabinet_counts[cabinet_type].get()
                    tall_cabinet_counts[cabinet_type].set(current_count + 1)
                    update_workspace_frames(cabinet_type, current_count, "Tall", "repopulate parent frame")
                    update_allCabinets_list()

                send_cabinet_to_cutlist("Tall", current_count, cabinet_type)
        elif action == "delete one":
            response = messagebox.askyesno("Warning", "Do you want to delete " + tall_cabinet_object_list[given_count].fullName + "?")
            if response:  # If 'Yes' button is clicked
                if current_count > 0:
                    tall_cabinet_counts[cabinet_type].set(current_count - 1)
                    update_workspace_frames(cabinet_type, given_count, "Tall", "delete i and empty parent frame")
                    update_allCabinets_list()

                    tall_cabinet_counts[cabinet_type].set(0)
                    for i in range(len(tall_cabinet_object_list)):
                        current_count = tall_cabinet_counts[cabinet_type].get()
                        tall_cabinet_counts[cabinet_type].set(current_count + 1)
                        update_workspace_frames(cabinet_type, current_count, "Tall", "repopulate parent frame")
                        update_allCabinets_list()

                    send_cabinet_to_cutlist("Tall", current_count, cabinet_type)

            else:  # If 'No' button is clicked
                pass
    all_tall_parts_list.clear()
    tall_cabinets_list_copy = tall_cabinets_list[:]
    merge_cabinet_parts(tall_cabinets_list_copy, all_tall_parts_list)

def regenerate_tall_count(cabinet_type, given_count, tall_cabinet_object_list):
    update_workspace_frames(cabinet_type, given_count, "Tall", "empty parent frame")
    update_allCabinets_list()
    tall_cabinet_counts[cabinet_type].set(0)
    for i in range(len(tall_cabinet_object_list)):
        current_count = tall_cabinet_counts[cabinet_type].get()
        tall_cabinet_counts[cabinet_type].set(current_count + 1)
        update_workspace_frames(cabinet_type, current_count, "Tall", "repopulate parent frame")
        update_allCabinets_list()

#-------------------------------------------------- Vanity Cabinets --------------------------------------------------//
# Create a label frame inside page2_app_frame for "Vanity Cabinets"
vanity_cabinets_frame = LabelFrame(selectCabinets_frame, text=" Vanity:  ", borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
vanity_cabinets_frame.pack(anchor=W, padx=5, pady=5, ipadx=3, ipady=5, fill=BOTH)

# List of vanity cabinet types
vanity_cabinet_types = [
    "Full Door",
    "Drawers",
    "1Door 1Drawer",
    "Linen Tower"
]

# Create buttons to increase and decrease the amount of each vanity cabinet type
vanity_cabinet_counts = {cabinet_type: IntVar(value=0) for cabinet_type in vanity_cabinet_types}

for i, cabinet_type in enumerate(vanity_cabinet_types):
    cabinet_label = Label(vanity_cabinets_frame, text=cabinet_type, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    cabinet_label.grid(row=i, column=0, padx=7, pady=5, sticky=W)

    decrease_button = Button(vanity_cabinets_frame, text="-", font=fontSegoeSmall, command=lambda ct=cabinet_type: decrement_vanity_count(ct), bg=plainWhite, fg=textGray)
    decrease_button.grid(row=i, column=1, padx=1, ipadx=2, sticky=E)

    count_label = Label(vanity_cabinets_frame, textvariable=vanity_cabinet_counts[cabinet_type], font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    count_label.grid(row=i, column=2, padx=5, sticky=E)

    increase_button = Button(vanity_cabinets_frame, text="+", font=fontSegoeSmall, command=lambda ct=cabinet_type: increment_vanity_count(ct), bg=plainWhite, fg=textGray)
    increase_button.grid(row=i, column=3, padx=(1,7), sticky=E)

vanity_cabinets_frame.columnconfigure(0, weight=1)

# Function to increment vanity cabinet count
def increment_vanity_count(cabinet_type):
    current_count = vanity_cabinet_counts[cabinet_type].get()
    vanity_cabinet_counts[cabinet_type].set(current_count + 1)
    update_workspace_frames(cabinet_type, current_count, "Vanity", "add")
    update_allCabinets_list()
    auto_scroll_workspaceScrollbar("Vanity", cabinet_type, current_count)

# Function to decrement Vanity cabinet count
def decrement_vanity_count(cabinet_type):
    current_count = vanity_cabinet_counts[cabinet_type].get()

    completed_cabinets = 0
    vanity_cabinet_object_list = []

    if cabinet_type == "Full Door":
        vanity_cabinet_object_list = vanity_FullDoor_cabinets
    elif cabinet_type == "Drawers":
        vanity_cabinet_object_list = vanity_Drawers_cabinets
    elif cabinet_type == "1Door 1Drawer":
        vanity_cabinet_object_list = vanity_1Door1Drawer_cabinets
    elif cabinet_type == "Linen Tower":
        vanity_cabinet_object_list = vanity_LinenTower_cabinets

    for i in range(len(vanity_cabinet_object_list)):
        if vanity_cabinet_object_list[i].completionStatus == True:
            completed_cabinets += 1

    if current_count > 0 and current_count > completed_cabinets:
        if vanity_cabinet_object_list[current_count-1].completionStatus == True:
            messagebox.showwarning("Invalid Input", "Can not decrement completed cabinets.\nTo remove cabinets, use the delete button.")
        else:
            vanity_cabinet_counts[cabinet_type].set(current_count - 1)
            update_workspace_frames(cabinet_type, current_count, "Vanity", "remove last frame")
            update_allCabinets_list()

    elif current_count == completed_cabinets:
        messagebox.showwarning("Invalid Input", "Can not decrement completed cabinets.\nTo remove completed cabinets, use the delete button.")

    workspace_canvas.update_idletasks()
    workspace_canvas.configure(scrollregion=workspace_canvas.bbox("all"))

def delete_vanity_count(cabinet_type, given_count, vanity_cabinet_object_list, action):
    current_count = vanity_cabinet_counts[cabinet_type].get()

    if vanity_cabinet_object_list[given_count].completionStatus == True:
        if action == "reset":
            if current_count > 0:
                vanity_cabinet_counts[cabinet_type].set(current_count - 1)
                update_workspace_frames(cabinet_type, given_count, "Vanity", "delete i and empty parent frame")
                update_allCabinets_list()

                vanity_cabinet_counts[cabinet_type].set(0)
                for i in range(len(vanity_cabinet_object_list)):
                    current_count = vanity_cabinet_counts[cabinet_type].get()
                    vanity_cabinet_counts[cabinet_type].set(current_count + 1)
                    update_workspace_frames(cabinet_type, current_count, "Vanity", "repopulate parent frame")
                    update_allCabinets_list()

                send_cabinet_to_cutlist("Vanity", current_count, cabinet_type)
        elif action == "delete one":
            response = messagebox.askyesno("Warning", "Do you want to delete " + vanity_cabinet_object_list[given_count].fullName + "?\nThis will also delete the item from the Cutlist.")
            if response:  # If 'Yes' button is clicked
                if current_count > 0:
                    vanity_cabinet_counts[cabinet_type].set(current_count - 1)
                    update_workspace_frames(cabinet_type, given_count, "Vanity", "delete i and empty parent frame")
                    update_allCabinets_list()

                    vanity_cabinet_counts[cabinet_type].set(0)
                    for i in range(len(vanity_cabinet_object_list)):
                        current_count = vanity_cabinet_counts[cabinet_type].get()
                        vanity_cabinet_counts[cabinet_type].set(current_count + 1)
                        update_workspace_frames(cabinet_type, current_count, "Vanity", "repopulate parent frame")
                        update_allCabinets_list()

                    send_cabinet_to_cutlist("Vanity", current_count, cabinet_type)

            else:  # If 'No' button is clicked
                pass

    elif vanity_cabinet_object_list[given_count].completionStatus == False:
        if action == "reset":
            if current_count > 0:
                vanity_cabinet_counts[cabinet_type].set(current_count - 1)
                update_workspace_frames(cabinet_type, given_count, "Vanity", "delete i and empty parent frame")
                update_allCabinets_list()

                vanity_cabinet_counts[cabinet_type].set(0)
                for i in range(len(vanity_cabinet_object_list)):
                    current_count = vanity_cabinet_counts[cabinet_type].get()
                    vanity_cabinet_counts[cabinet_type].set(current_count + 1)
                    update_workspace_frames(cabinet_type, current_count, "Vanity", "repopulate parent frame")
                    update_allCabinets_list()

                send_cabinet_to_cutlist("Vanity", current_count, cabinet_type)
        elif action == "delete one":
            response = messagebox.askyesno("Warning", "Do you want to delete " + vanity_cabinet_object_list[given_count].fullName + "?")
            if response:  # If 'Yes' button is clicked
                if current_count > 0:
                    vanity_cabinet_counts[cabinet_type].set(current_count - 1)
                    update_workspace_frames(cabinet_type, given_count, "Vanity", "delete i and empty parent frame")
                    update_allCabinets_list()

                    vanity_cabinet_counts[cabinet_type].set(0)
                    for i in range(len(vanity_cabinet_object_list)):
                        current_count = vanity_cabinet_counts[cabinet_type].get()
                        vanity_cabinet_counts[cabinet_type].set(current_count + 1)
                        update_workspace_frames(cabinet_type, current_count, "Vanity", "repopulate parent frame")
                        update_allCabinets_list()

                    send_cabinet_to_cutlist("Vanity", current_count, cabinet_type)

            else:  # If 'No' button is clicked
                pass
    all_vanity_parts_list.clear()
    vanity_cabinets_list_copy = vanity_cabinets_list[:]
    merge_cabinet_parts(vanity_cabinets_list_copy, all_vanity_parts_list)

def regenerate_vanity_count(cabinet_type, given_count, vanity_cabinet_object_list):
    update_workspace_frames(cabinet_type, given_count, "Vanity", "empty parent frame")
    update_allCabinets_list()
    vanity_cabinet_counts[cabinet_type].set(0)
    for i in range(len(vanity_cabinet_object_list)):
        current_count = vanity_cabinet_counts[cabinet_type].get()
        vanity_cabinet_counts[cabinet_type].set(current_count + 1)
        update_workspace_frames(cabinet_type, current_count, "Vanity", "repopulate parent frame")
        update_allCabinets_list()


#-------------------------------------------------- Custom Cabinets --------------------------------------------------//
# Create a label frame inside page2_app_frame for "Custom Cabinets"
custom_cabinets_frame = LabelFrame(selectCabinets_frame, text=" Custom:  ", borderwidth=2, relief="groove", font=fontSegoe, bg=plainWhite, fg=labelFrameBlue)
custom_cabinets_frame.pack(anchor=W, padx=5, pady=5, ipadx=3, ipady=5, fill=BOTH)

# List of custom cabinet types
custom_cabinet_types = [
    "Custom Cabinet"
]

# Create buttons to increase and decrease the amount of the custom cabinet type
custom_cabinet_counts = {cabinet_type: IntVar(value=0) for cabinet_type in custom_cabinet_types}
# update_workspace_frames(custom_cabinet_counts, workspace_custom_frame)  # Initial call for custom cabinets

for i, cabinet_type in enumerate(custom_cabinet_types):
    cabinet_label = Label(custom_cabinets_frame, text=cabinet_type, font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    cabinet_label.grid(row=i, column=0, padx=6, pady=5, sticky=W)

    decrease_button = Button(custom_cabinets_frame, text="-", font=fontSegoeSmall, command=lambda ct=cabinet_type: decrement_custom_count(ct), bg=plainWhite, fg=textGray)
    decrease_button.grid(row=i, column=1, padx=1, ipadx=2, sticky=E)

    count_label = Label(custom_cabinets_frame, textvariable=custom_cabinet_counts[cabinet_type], font=fontSegoeSmall, bg=plainWhite, fg=textGray)
    count_label.grid(row=i, column=2, padx=5, sticky=E)

    increase_button = Button(custom_cabinets_frame, text="+", font=fontSegoeSmall, command=lambda ct=cabinet_type: increment_custom_count(ct), bg=plainWhite, fg=textGray)
    increase_button.grid(row=i, column=3, padx=(1,7), sticky=E)

custom_cabinets_frame.columnconfigure(0, weight=1)

# Function to increment custom cabinet count
def increment_custom_count(cabinet_type):
    current_count = custom_cabinet_counts[cabinet_type].get()
    custom_cabinet_counts[cabinet_type].set(current_count + 1)
    update_workspace_frames(cabinet_type, current_count, "Custom", "add")
    # update_allCabinets_list()

# Function to decrement custom cabinet count
def decrement_custom_count(cabinet_type):
    current_count = custom_cabinet_counts[cabinet_type].get()
    if current_count > 0:
        custom_cabinet_counts[cabinet_type].set(current_count - 1)
        update_workspace_frames(cabinet_type, current_count, "Custom", "remove last frame")
        # update_allCabinets_list()


#-------------------------------------------------- Buttons for page2_app_frame --------------------------------------------------//
rail_size_label_frame = Frame(page2_app_frame, bg = plainWhite)
rail_size_label_frame.grid(row=26, column=0, columnspan=3, padx=(70,250), pady=0, sticky=W+E+S)
# rail_size_label_frame.grid(row=26, column=0, columnspan=3, padx=5, pady=0, sticky=W+E+S)

def on_reset_button_press(event):
    reset_workspace_button.config(image=reset_image_dark)

def on_reset_button_release(event):
    reset_workspace_button.config(image=reset_image)

# Reset Workspace button for Workspace
reset_workspace_button = Button(rail_size_label_frame, image=reset_image, command=resetWorkspace, bd=0, relief="solid")
reset_workspace_button.pack(anchor=W, side="left")

reset_workspace_button.bind("<Button-1>", on_reset_button_press)
reset_workspace_button.bind("<ButtonRelease-1>", on_reset_button_release)


def on_print_button_press(event):
    print_cutlist_button.config(image=print_image_dark)

def on_print_button_release(event):
    print_cutlist_button.config(image=print_image)

# Print Cutlist button for Cutlist
print_cutlist_button = Button(rail_size_label_frame, image=print_image, command=to_page3, bd=0, relief="solid")
print_cutlist_button.pack(anchor=E, side="right")

print_cutlist_button.bind("<Button-1>", on_print_button_press)
print_cutlist_button.bind("<ButtonRelease-1>", on_print_button_release)




#--------------------------------------------------------------------------------------------- Page 3 ---------------------------------------------------------------------------------------------//
#-------------------------------------------------- Page 3: Defining page3_frame --------------------------------------------------//
page3_frame = Frame(root, bg = plainWhite)
# page3_frame.pack(fill=BOTH, expand=True)


#-------------------------------------------------- Page 3: Status, Save, and Open Buttons --------------------------------------------------//
status_frame_P3 = Frame(page3_frame, bg = plainWhite)
status_frame_P3.pack(fill=BOTH)

status_P3 = Label(status_frame_P3, text="Cabinets App - V3", font = fontBauhausHeader, bg = plainWhite, fg = logoBlue, bd=2, relief=FLAT, highlightthickness=1, highlightbackground=backHighlightGray, pady=10)
status_P3.grid(row=0, column=0, sticky="ew")
status_frame_P3.grid_columnconfigure(0,weight=1)

switchFrame_P3 = Frame(status_frame_P3, highlightthickness=0, bg = plainWhite)
switchFrame_P3.grid(row=0, column=0, sticky=W)

arrow_Button_P3 = Button(switchFrame_P3, image=arrowLeft_image, width=11, height=36, command=back_to_page2, font=fontSegoeSmall, bd=0, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
arrow_Button_P3.grid(row=0, column=0, padx=(30, 0), pady=(3,0), ipady=19, sticky=S)
backButton_P3 = Button(switchFrame_P3, text="Back", width=4, command=back_to_page2, font=fontSegoeBold, bd=0, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
backButton_P3.grid(row=0, column=1, padx=0, ipady=18)
emptyButton_P3 = Button(switchFrame_P3, text="", width=1, command=back_to_page2, font=fontSegoeBold, bd=0, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
emptyButton_P3.grid(row=0, column=2, padx=0, ipady=18)
sep = ttk.Separator(switchFrame_P3, orient='vertical')
sep.grid(row=0, column=3, padx=5, pady=7, sticky=N+S)

total_cabinets_label_P3 = Label(switchFrame_P3, text="Total Cabinets: 0", font=fontSegoe, bg=plainWhite, fg=textGray)
total_cabinets_label_P3.grid(row=0, column=4, padx=(10, 5))
comma_label = Label(switchFrame_P3, text="|", font=fontSegoeBig, bg=plainWhite, fg=textGray)
comma_label.grid(row=0, column=5)
total_cutlist_label_P3 = Label(switchFrame_P3, text="In Cutlist: 0", font=fontSegoe, bg=plainWhite, fg=textGray)
total_cutlist_label_P3.grid(row=0, column=6, padx=(5, 10))

saveBtnFrame_P3 = Frame(status_frame_P3, highlightthickness=0, bg = plainWhite)
saveBtnFrame_P3.grid(row=0, column=0, sticky=E)

sep = ttk.Separator(saveBtnFrame_P3, orient='vertical')
sep.grid(row=0, column=0, padx=2, pady=7, sticky=N+S)

open_button_P3 = Button(saveBtnFrame_P3, text="Open", command=open_project, highlightthickness=0, bd=0, highlightcolor=textGray, font=fontSegoeBold, activebackground=plainWhite, bg=plainWhite, fg=textGray)
open_button_P3.grid(row=0, column=1, ipadx=18, ipady=18)

sep = ttk.Separator(saveBtnFrame_P3, orient='vertical')
sep.grid(row=0, column=2, padx=2, pady=7, sticky=N+S)

save_button_P3 = Button(saveBtnFrame_P3, text="Save", command=save_project, highlightthickness=0, bd=0, highlightcolor=textGray, font=fontSegoeBold, activebackground=plainWhite, bg=plainWhite, fg=textGray)
save_button_P3.grid(row=0, column=3, ipadx=18, ipady=18)

sep = ttk.Separator(saveBtnFrame_P3, orient='vertical')
sep.grid(row=0, column=4, padx=2, pady=7, sticky=N+S)

emptyLabel = Label(saveBtnFrame_P3, text="--", fg='#fff', bg=plainWhite)
emptyLabel.grid(row=0, column=5)


#-------------------------------------------------- Project Details Frame Page 3 --------------------------------------------------//
project_detail_frame_p3 = Frame(page3_frame, highlightthickness=0, bg = plainWhite)
project_detail_frame_p3.pack(fill=BOTH)

project_detail_frame_p3.grid_columnconfigure(0, weight=1)
project_detail_frame_p3.grid_columnconfigure(12, weight=1)


#-------------------------------------------------- Defining page3_app_frame --------------------------------------------------//
page3_app_frame = Frame(page3_frame, bg = plainWhite)
page3_app_frame.pack(fill=BOTH, padx=100)


#----------------------------------------- Cutlist Results Scrollbar and Frames -----------------------------------------//
#------------------------- Cutlist Results Scrollbar -------------------------//
cutlist_results_backFrame = LabelFrame(page3_app_frame, text="Sorted Cabinets by Category", font=fontSegoe, padx=5, pady=5, bg=plainWhite, fg=labelFrameBlue)
cutlist_results_backFrame.grid(row=0, rowspan=27, column=0, padx=55, pady=5, sticky=N+W+E)
cutlist_results_canvas = Canvas(cutlist_results_backFrame, bg=plainWhite, borderwidth=0, highlightthickness=0, width=710, height=screen_height-300)
cutlist_results_canvas.grid(row=0, column=0, sticky="nsew")
cutlist_results_scrollbar = ttk.Scrollbar(cutlist_results_backFrame, orient=VERTICAL, command=cutlist_results_canvas.yview)
cutlist_results_scrollbar.grid(row=0, column=1, sticky="ns")
cutlist_results_canvas.configure(yscrollcommand=cutlist_results_scrollbar.set, yscrollincrement=2)
cutlist_results_scrollbar.grid_rowconfigure(0, weight=1)  # Allow the scrollbar to fill the height

cutlist_results_canvas.bind('<Configure>', lambda e: cutlist_results_canvas.configure(scrollregion=cutlist_results_canvas.bbox("all")))
cutlist_results_frame = Frame(cutlist_results_canvas, bg=plainWhite)
cutlist_results_canvas.create_window((0, 0), window=cutlist_results_frame, anchor="nw")

# Enable scrolling with the mouse wheel
def on_canvas_mousewheel(event):
    cutlist_results_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
cutlist_results_canvas.bind("<MouseWheel>", on_canvas_mousewheel)
# cutlist_canvas.bind_all("<MouseWheel>", on_canvas_mousewheel)

#------------------------- Cutlist Results Frames -------------------------//
cabinets_in_cutlist_results_frame = Frame(cutlist_results_frame, bg = plainWhite)
cabinets_in_cutlist_results_frame.pack(fill=BOTH)
# Base frames in Cutlist
cutlist_results_base_frame = LabelFrame(cabinets_in_cutlist_results_frame, text="Base", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
# cutlist_results_base_frame.grid(row=0, column=0, padx=10, ipadx=3, ipady=2, sticky=W+E)
cutlist_results_base_FullDoor_frame = Frame(cutlist_results_base_frame, bg = plainWhite)
# cutlist_results_base_FullDoor_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_base_Drawers_frame = Frame(cutlist_results_base_frame, bg = plainWhite)
# cutlist_results_base_Drawers_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_base_1D1D_frame = Frame(cutlist_results_base_frame, bg = plainWhite)
# cutlist_results_base_1D1D_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_base_Corner90_frame = Frame(cutlist_results_base_frame, bg = plainWhite)
# cutlist_results_base_Corner90_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_base_CornerDiagonal_frame = Frame(cutlist_results_base_frame, bg = plainWhite)
# cutlist_results_base_CornerDiagonal_frame.grid(row=4, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_base_CornerBlind_frame = Frame(cutlist_results_base_frame, bg = plainWhite)
cutlist_results_base_CornerBlind_frame.grid(row=5, column=0, padx=10, pady=5, sticky=W+E)
# Wall frames in Cutlist
cutlist_results_wall_frame = LabelFrame(cabinets_in_cutlist_results_frame, text="Wall", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
# cutlist_results_wall_frame.grid(row=1, column=0, padx=10, pady=5, ipadx=3, ipady=2, sticky=W+E)
cutlist_results_wall_FullDoor_frame = Frame(cutlist_results_wall_frame, bg = plainWhite)
# cutlist_results_wall_FullDoor_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_wall_Corner90_frame = Frame(cutlist_results_wall_frame, bg = plainWhite)
# cutlist_results_wall_Corner90_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_wall_CornerDiagonal_frame = Frame(cutlist_results_wall_frame, bg = plainWhite)
# cutlist_results_wall_CornerDiagonal_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_wall_MicrowaveSlot_frame = Frame(cutlist_results_wall_frame, bg = plainWhite)
# cutlist_results_wall_MicrowaveSlot_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W+E)
# Tall frames in Cutlist
cutlist_results_tall_frame = LabelFrame(cabinets_in_cutlist_results_frame, text="Tall", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
# cutlist_results_tall_frame.grid(row=2, column=0, padx=10, pady=5, ipadx=3, ipady=2, sticky=W+E)
cutlist_results_tall_FullDoor_frame = Frame(cutlist_results_tall_frame, bg = plainWhite)
# cutlist_results_tall_FullDoor_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_tall_Pantry_frame = Frame(cutlist_results_tall_frame, bg = plainWhite)
# cutlist_results_tall_Pantry_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_tall_OvenSlot_frame = Frame(cutlist_results_tall_frame, bg = plainWhite)
# cutlist_results_tall_OvenSlot_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_tall_PullOut_frame = Frame(cutlist_results_tall_frame, bg = plainWhite)
# cutlist_results_tall_PullOut_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W+E)
# Vanity frames in Cutlist
cutlist_results_vanity_frame = LabelFrame(cabinets_in_cutlist_results_frame, text="Vanity", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
# cutlist_results_vanity_frame.grid(row=3, column=0, padx=10, pady=5, ipadx=3, ipady=2, sticky=W+E)
cutlist_results_vanity_FullDoor_frame = Frame(cutlist_results_vanity_frame, bg = plainWhite)
# cutlist_results_vanity_FullDoor_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_vanity_Drawers_frame = Frame(cutlist_results_vanity_frame, bg = plainWhite)
# cutlist_results_vanity_Drawers_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_vanity_1D1D_frame = Frame(cutlist_results_vanity_frame, bg = plainWhite)
# cutlist_results_vanity_1D1D_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W+E)
cutlist_results_vanity_LinenTower_frame = Frame(cutlist_results_vanity_frame, bg = plainWhite)
# cutlist_results_vanity_LinenTower_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W+E)
# Custom frames in Cutlist
cutlist_results_custom_frame = LabelFrame(cabinets_in_cutlist_results_frame, text="Custom", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_results_custom_frame.grid(row=4, column=0, padx=10, pady=5, ipadx=3, ipady=2, sticky=W+E)


#----------------------------------------- Cutlist Total Scrollbar and Frames -----------------------------------------//
#------------------------- Cutlist Total Total Scrollbar -------------------------//
cutlist_Total_backFrame = LabelFrame(page3_app_frame, text="Sorted Parts by Category", font=fontSegoe, padx=5, pady=5, bg=plainWhite, fg=labelFrameBlue)
cutlist_Total_backFrame.grid(row=0, rowspan=27, column=2, padx=55, pady=5, sticky=N+E)
cutlist_Total_canvas = Canvas(cutlist_Total_backFrame, bg=plainWhite, borderwidth=0, highlightthickness=0, width=710, height=screen_height-300)
cutlist_Total_canvas.grid(row=0, column=0, sticky="nsew")
cutlist_Total_scrollbar = ttk.Scrollbar(cutlist_Total_backFrame, orient=VERTICAL, command=cutlist_Total_canvas.yview)
cutlist_Total_scrollbar.grid(row=0, column=1, sticky="ns")
cutlist_Total_canvas.configure(yscrollcommand=cutlist_Total_scrollbar.set, yscrollincrement=2)
cutlist_Total_scrollbar.grid_rowconfigure(0, weight=1)  # Allow the scrollbar to fill the height
cutlist_Total_canvas.bind('<Configure>', lambda e: cutlist_Total_canvas.configure(scrollregion=cutlist_Total_canvas.bbox("all")))
cutlist_Total_frame = Frame(cutlist_Total_canvas, bg=plainWhite)
cutlist_Total_canvas.create_window((0, 0), window=cutlist_Total_frame, anchor="nw")

cutlist_Total_canvas.bind('<Configure>', lambda e: cutlist_Total_canvas.configure(scrollregion=cutlist_Total_canvas.bbox("all")))
cutlist_Total_frame = Frame(cutlist_Total_canvas, bg=plainWhite)
cutlist_Total_canvas.create_window((0, 0), window=cutlist_Total_frame, anchor="nw")

# Enable scrolling with the mouse wheel
def on_canvas_mousewheel(event):
    cutlist_Total_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
cutlist_Total_canvas.bind("<MouseWheel>", on_canvas_mousewheel)
# cutlist_canvas.bind_all("<MouseWheel>", on_canvas_mousewheel)

#------------------------- Cutlist Total Frames -------------------------//
cabinets_in_cutlist_Total_frame = Frame(cutlist_Total_frame, bg = plainWhite)
cabinets_in_cutlist_Total_frame.pack(fill=BOTH)
# Base frames in Cutlist
cutlist_Total_base_frame = LabelFrame(cabinets_in_cutlist_Total_frame, text="Base", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_Total_base_frame.grid(row=0, column=0, padx=(10,0), ipadx=3, ipady=2, sticky=W+E)
# Wall frames in Cutlist
cutlist_Total_wall_frame = LabelFrame(cabinets_in_cutlist_Total_frame, text="Wall", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_Total_wall_frame.grid(row=1, column=0, padx=(10,0), ipadx=3, ipady=2, sticky=W+E)
# Tall frames in Cutlist
cutlist_Total_tall_frame = LabelFrame(cabinets_in_cutlist_Total_frame, text="Tall", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_Total_tall_frame.grid(row=2, column=0, padx=(10,0), ipadx=3, ipady=2, sticky=W+E)
# Vanity frames in Cutlist
cutlist_Total_vanity_frame = LabelFrame(cabinets_in_cutlist_Total_frame, text="Vanity", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_Total_vanity_frame.grid(row=3, column=0, padx=(10,0), ipadx=3, ipady=2, sticky=W+E)
# Custom frames in Cutlist
cutlist_Total_custom_frame = LabelFrame(cabinets_in_cutlist_Total_frame, text="Custom", font = fontSegoe, bg = plainWhite, fg = labelFrameBlue)
cutlist_Total_custom_frame.grid(row=4, column=0, padx=(10,0), ipadx=3, ipady=2, sticky=W+E)


#-------------------------------------------------- Function to Send Cabinet to Cutlist Results --------------------------------------------------//
# Function is triggered when the "Send" button is clicked
def send_cabinets_to_page3_cutlists(category, cabinet_type):
    def populate_cutlist_results(cabinet, parent, row):
        cutlist_cabinet_details_frame = LabelFrame(parent, text=cabinet.fullName, borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
        cutlist_cabinet_details_frame.grid(row=row, column=0, padx=(5,0), ipadx=5, ipady=5, sticky=N+W+E)
        # Creating cutlist labels
        quantity_label = Label(cutlist_cabinet_details_frame, text="Quantity", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        quantity_label.grid(row=0, column=0, padx=(8,0), pady=10)
        name_label = Label(cutlist_cabinet_details_frame, text="Name", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        name_label.grid(row=0, column=1, padx=(0,8), pady=10)
        width_label = Label(cutlist_cabinet_details_frame, text="Width", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        width_label.grid(row=0, column=2, padx=8, pady=10)
        length_label = Label(cutlist_cabinet_details_frame, text="Height", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        length_label.grid(row=0, column=3, padx=8, pady=10)
        tape_label = Label(cutlist_cabinet_details_frame, text="Tape", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        tape_label.grid(row=0, column=4, padx=8, pady=10)
        drill_label = Label(cutlist_cabinet_details_frame, text="Drill", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        drill_label.grid(row=0, column=5, padx=8, pady=10)
        router_label = Label(cutlist_cabinet_details_frame, text="Router", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        router_label.grid(row=0, column=6, padx=8, pady=10)
        # Inserting cabinet_object.parts
        row=1
        for part in cabinet.listParts:
            part_qty_label = Label(cutlist_cabinet_details_frame, text=f"{part.qty}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_qty_label.grid(row=row, column=0, padx=8, pady=5)
            part_name_label = Label(cutlist_cabinet_details_frame, text=f"{part.name}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_name_label.grid(row=row, column=1, padx=8, pady=5)
            part_width_label = Label(cutlist_cabinet_details_frame, text=f"{part.width}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_width_label.grid(row=row, column=2, padx=8, pady=5)
            part_length_label = Label(cutlist_cabinet_details_frame, text=f"{part.height}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_length_label.grid(row=row, column=3, padx=8, pady=5)
            part_tape_label = Label(cutlist_cabinet_details_frame, text=f"{part.tape}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_tape_label.grid(row=row, column=4, padx=8, pady=5)
            part_drill_label = Label(cutlist_cabinet_details_frame, text=f"{part.drill}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_drill_label.grid(row=row, column=5, padx=8, pady=5)
            part_router_label = Label(cutlist_cabinet_details_frame, text=f"{part.router}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_router_label.grid(row=row, column=6, padx=8, pady=5)
            row+=1

    if category == "Base":
        if base_FullDoor_cabinets or base_Drawers_cabinets or base_1D1D_cabinets or base_Corner90_cabinets or base_CornerDiagonal_cabinets or base_CornerBlind_cabinets:
            cutlist_results_base_frame.grid(row=0, column=0, padx=10, ipadx=3, ipady=2, sticky=W+E)
        if base_FullDoor_cabinets:
            if cabinet_type == "Full Door":
                for widget in cutlist_results_base_FullDoor_frame.winfo_children():
                    widget.destroy()
                cutlist_results_base_FullDoor_frame.grid_forget()
                cutlist_results_base_FullDoor_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_base_FullDoor_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in base_FullDoor_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if base_Drawers_cabinets:
            if cabinet_type == "Drawers":
                for widget in cutlist_results_base_Drawers_frame.winfo_children():
                    widget.destroy()
                cutlist_results_base_Drawers_frame.grid_forget()
                cutlist_results_base_Drawers_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_base_Drawers_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in base_Drawers_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if base_1D1D_cabinets:
            if cabinet_type == "1Door 1Drawer":
                for widget in cutlist_results_base_1D1D_frame.winfo_children():
                    widget.destroy()
                cutlist_results_base_1D1D_frame.grid_forget()
                cutlist_results_base_1D1D_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_base_1D1D_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in base_1D1D_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if base_Corner90_cabinets:
            if cabinet_type == "Corner 90":
                for widget in cutlist_results_base_Corner90_frame.winfo_children():
                    widget.destroy()
                cutlist_results_base_Corner90_frame.grid_forget()
                cutlist_results_base_Corner90_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_base_Corner90_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in base_Corner90_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if base_CornerDiagonal_cabinets:
            if cabinet_type == "Corner Diagonal":
                for widget in cutlist_results_base_CornerDiagonal_frame.winfo_children():
                    widget.destroy()
                cutlist_results_base_CornerDiagonal_frame.grid_forget()
                cutlist_results_base_CornerDiagonal_frame.grid(row=4, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_base_CornerDiagonal_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in base_CornerDiagonal_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if base_CornerBlind_cabinets:
            if cabinet_type == "Corner Blind":
                for widget in cutlist_results_base_CornerBlind_frame.winfo_children():
                    widget.destroy()
                cutlist_results_base_CornerBlind_frame.grid_forget()
                cutlist_results_base_CornerBlind_frame.grid(row=5, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_base_CornerBlind_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in base_CornerBlind_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

    elif category == "Wall":
        if wall_FullDoor_cabinets or wall_Corner90_cabinets or wall_CornerDiagonal_cabinets or wall_MicowaveSlot_cabinets:
            cutlist_results_wall_frame.grid(row=1, column=0, padx=10, pady=5, ipadx=3, ipady=2, sticky=W+E)
        if wall_FullDoor_cabinets:
            if cabinet_type == "Full Door":
                for widget in cutlist_results_wall_FullDoor_frame.winfo_children():
                    widget.destroy()
                cutlist_results_wall_FullDoor_frame.grid_forget()
                cutlist_results_wall_FullDoor_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_wall_FullDoor_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in wall_FullDoor_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if wall_Corner90_cabinets:
            if cabinet_type == "Corner 90":
                for widget in cutlist_results_wall_Corner90_frame.winfo_children():
                    widget.destroy()
                cutlist_results_wall_Corner90_frame.grid_forget()
                cutlist_results_wall_Corner90_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_wall_Corner90_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in wall_Corner90_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if wall_CornerDiagonal_cabinets:
            if cabinet_type == "Corner Diagonal":
                for widget in cutlist_results_wall_CornerDiagonal_frame.winfo_children():
                    widget.destroy()
                cutlist_results_wall_CornerDiagonal_frame.grid_forget()
                cutlist_results_wall_CornerDiagonal_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_wall_CornerDiagonal_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in wall_CornerDiagonal_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if wall_MicowaveSlot_cabinets:
            if cabinet_type == "Microwave Slot":
                for widget in cutlist_results_wall_MicrowaveSlot_frame.winfo_children():
                    widget.destroy()
                cutlist_results_wall_MicrowaveSlot_frame.grid_forget()
                cutlist_results_wall_MicrowaveSlot_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_wall_MicrowaveSlot_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in wall_MicowaveSlot_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

    elif category == "Tall":
        if tall_FullDoor_cabinets or tall_Pantry_cabinets or tall_OvenSlot_cabinets or tall_PullOut_cabinets:
            cutlist_results_tall_frame.grid(row=2, column=0, padx=10, pady=5, ipadx=3, ipady=2, sticky=W+E)
        if tall_FullDoor_cabinets:
            if cabinet_type == "Full Door":
                for widget in cutlist_results_tall_FullDoor_frame.winfo_children():
                    widget.destroy()
                cutlist_results_tall_FullDoor_frame.grid_forget()
                cutlist_results_tall_FullDoor_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_tall_FullDoor_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in tall_FullDoor_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if tall_Pantry_cabinets:
            if cabinet_type == "Pantry":
                for widget in cutlist_results_tall_Pantry_frame.winfo_children():
                    widget.destroy()
                cutlist_results_tall_Pantry_frame.grid_forget()
                cutlist_results_tall_Pantry_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_tall_Pantry_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in tall_Pantry_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if tall_OvenSlot_cabinets:
            if cabinet_type == "Oven Slot":
                for widget in cutlist_results_tall_OvenSlot_frame.winfo_children():
                    widget.destroy()
                cutlist_results_tall_OvenSlot_frame.grid_forget()
                cutlist_results_tall_OvenSlot_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_tall_OvenSlot_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in tall_OvenSlot_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if tall_PullOut_cabinets:
            if cabinet_type == "Pull Out":
                for widget in cutlist_results_tall_PullOut_frame.winfo_children():
                    widget.destroy()
                cutlist_results_tall_PullOut_frame.grid_forget()
                cutlist_results_tall_PullOut_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_tall_PullOut_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in tall_PullOut_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

    elif category == "Vanity":
        if vanity_FullDoor_cabinets or vanity_Drawers_cabinets or vanity_1Door1Drawer_cabinets or vanity_LinenTower_cabinets:
            cutlist_results_vanity_frame.grid(row=3, column=0, padx=10, pady=5, ipadx=3, ipady=2, sticky=W+E)
        if vanity_FullDoor_cabinets:
            if cabinet_type == "Full Door":
                for widget in cutlist_results_vanity_FullDoor_frame.winfo_children():
                    widget.destroy()
                cutlist_results_vanity_FullDoor_frame.grid_forget()
                cutlist_results_vanity_FullDoor_frame.grid(row=0, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_vanity_FullDoor_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in vanity_FullDoor_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if vanity_Drawers_cabinets:
            if cabinet_type == "Drawers":
                for widget in cutlist_results_vanity_Drawers_frame.winfo_children():
                    widget.destroy()
                cutlist_results_vanity_Drawers_frame.grid_forget()
                cutlist_results_vanity_Drawers_frame.grid(row=1, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_vanity_Drawers_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in vanity_Drawers_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if vanity_1Door1Drawer_cabinets:
            if cabinet_type == "1Door 1Drawer":
                for widget in cutlist_results_vanity_1D1D_frame.winfo_children():
                    widget.destroy()
                cutlist_results_vanity_1D1D_frame.grid_forget()
                cutlist_results_vanity_1D1D_frame.grid(row=2, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_vanity_1D1D_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in vanity_1Door1Drawer_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

        if vanity_LinenTower_cabinets:
            if cabinet_type == "Linen Tower":
                for widget in cutlist_results_vanity_LinenTower_frame.winfo_children():
                    widget.destroy()
                cutlist_results_vanity_LinenTower_frame.grid_forget()
                cutlist_results_vanity_LinenTower_frame.grid(row=3, column=0, padx=10, pady=5, sticky=W+E)
                cabinet_frame = Frame(cutlist_results_vanity_LinenTower_frame, bg=plainWhite)
                cabinet_frame.pack(anchor=W)
                row=0
                for cabinet in vanity_LinenTower_cabinets:
                    if cabinet.completionStatus == True:
                        populate_cutlist_results(cabinet, cabinet_frame, row)
                        row+=1

    elif category == "Custom":
        if cabinet_type == "Custom":
            for widget in cutlist_results_custom_frame.winfo_children():
                widget.destroy()
            cabinet_frame = Frame(cutlist_results_custom_frame, bg=plainWhite)
            cabinet_frame.pack(anchor=W)
            row=0
            for cabinet in custom_cabinets:
                if cabinet.completionStatus == True:
                    populate_cutlist_results(cabinet, cabinet_frame, row)
                    row+=1

    # Update the layout of the cutlist_canvas to include the new entry
    cutlist_Total_canvas.update_idletasks()
    cutlist_Total_canvas.configure(scrollregion=cutlist_Total_canvas.bbox("all"))


#-------------------------------------------------- Function to Send Cabinet to Cutlist Total --------------------------------------------------//
def populate_cutlist_total(category, given_cabinet_Lists, parent):

    if given_cabinet_Lists:
        #------------------------- Cutlist: Defining Buttons Frame and Buttons -------------------------//
        cutlist_button_frame = Frame(parent, bg=plainWhite)
        cutlist_button_frame.grid(row=0, column=1, pady=19, sticky="ne")  # Adjust the column number as needed
        #------------------------- Cutlist: Defining Cutlist Cabinet Frame and Populating cutlist -------------------------//
        # cutlist_cabinet_details_frame = LabelFrame(parent, text=category, borderwidth=2, relief="groove", font=fontSegoeSmall, bg=plainWhite, fg=labelFrameBlue)
        cutlist_cabinet_details_frame = Frame(parent, bg=plainWhite)
        cutlist_cabinet_details_frame.grid(row=0, column=0, padx=(5,0), ipadx=5, ipady=5, sticky=N+W+E)
        # Creating cutlist labels
        quantity_label = Label(cutlist_cabinet_details_frame, text="Quantity", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        quantity_label.grid(row=0, column=0, padx=(8,0), pady=10)
        name_label = Label(cutlist_cabinet_details_frame, text="Name", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        name_label.grid(row=0, column=1, padx=(0,8), pady=10)
        width_label = Label(cutlist_cabinet_details_frame, text="Width", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        width_label.grid(row=0, column=2, padx=8, pady=10)
        length_label = Label(cutlist_cabinet_details_frame, text="Height", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        length_label.grid(row=0, column=3, padx=8, pady=10)
        tape_label = Label(cutlist_cabinet_details_frame, text="Tape", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        tape_label.grid(row=0, column=4, padx=8, pady=10)
        drill_label = Label(cutlist_cabinet_details_frame, text="Drill", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        drill_label.grid(row=0, column=5, padx=8, pady=10)
        router_label = Label(cutlist_cabinet_details_frame, text="Router", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
        router_label.grid(row=0, column=6, padx=8, pady=10)
        # Inserting cabinet_object.parts
        row=1
        for part in given_cabinet_Lists:
            part_qty_label = Label(cutlist_cabinet_details_frame, text=f"{part.qty}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_qty_label.grid(row=row, column=0, padx=8, pady=5)
            part_name_label = Label(cutlist_cabinet_details_frame, text=f"{part.name}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_name_label.grid(row=row, column=1, padx=8, pady=5)
            part_width_label = Label(cutlist_cabinet_details_frame, text=f"{part.width}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_width_label.grid(row=row, column=2, padx=8, pady=5)
            part_length_label = Label(cutlist_cabinet_details_frame, text=f"{part.height}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_length_label.grid(row=row, column=3, padx=8, pady=5)
            part_tape_label = Label(cutlist_cabinet_details_frame, text=f"{part.tape}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_tape_label.grid(row=row, column=4, padx=8, pady=5)
            part_drill_label = Label(cutlist_cabinet_details_frame, text=f"{part.drill}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_drill_label.grid(row=row, column=5, padx=8, pady=5)
            part_router_label = Label(cutlist_cabinet_details_frame, text=f"{part.router}", font=fontSegoeSmall, bg=plainWhite, fg=textGray)
            part_router_label.grid(row=row, column=6, padx=8, pady=5)
            row+=1

    # Update the layout of the cutlist_canvas to include the new entry
    cutlist_results_canvas.update_idletasks()
    cutlist_results_canvas.configure(scrollregion=cutlist_results_canvas.bbox("all"))


#-------------------------------------------------- Defining PDF class --------------------------------------------------//
class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 20)
        self.cell(0, 10, project_name_entry.get(), border=True, ln=True, align='C')
        self.set_font('helvetica', '', 10)
        self.cell(0, 5, str(project_name_entry.get()))
        self.cell(0, 5, str(date_day_combobox.get()) + "/" + str(date_month_combobox.get()) + "/" + str(date_year_combobox.get()), ln=True, align='R')
        # self.cell(0, 5, str(date_entry.get()))
        self.cell(0, 5, "P.O.#: " + str(po_number_entry.get()), ln=True)
        self.ln(10)
        self.set_font('helvetica', 'B', 10)
        self.cell(30, 3, '')
        self.cell(25, 3, "Quantity")
        self.cell(25, 3, "Name")
        self.cell(25, 3, "Width")
        self.cell(25, 3, "Length")
        self.cell(25, 3, "Tape")
        self.cell(25, 3, "Drill")
        self.cell(25, 3, "Router")
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

def createPDF(givenString):
    newPDF = PDF('P', 'mm', 'Letter')
    newPDF.set_auto_page_break(auto=True, margin = 15)
    newPDF.add_page()

    if givenString == "CABINETS":

        for categoryList in all_cabinet_lists:
            if categoryList == base_cabinets_list and len(categoryList) != 0:
                newPDF.set_font('helvetica', 'B', 13)
                newPDF.cell(10, 10, "Base,", ln=True)
                newPDF.set_font('helvetica', '', 10)
            elif categoryList  == wall_cabinets_list and len(categoryList) != 0:
                newPDF.set_font('helvetica', 'B', 13)
                newPDF.cell(10, 10, "Wall,", ln=True)
                newPDF.set_font('helvetica', '', 10)
            elif categoryList == tall_cabinets_list and len(categoryList) != 0:
                newPDF.set_font('helvetica', 'B', 13)
                newPDF.cell(10, 10, "Tall,", ln=True)
                newPDF.set_font('helvetica', '', 10)
            elif categoryList == vanity_cabinets_list and len(categoryList) != 0:
                newPDF.set_font('helvetica', 'B', 13)
                newPDF.cell(10, 10, "Vanity,", ln=True)
                newPDF.set_font('helvetica', '', 10)
            # elif categoryList == tempListC and len(categoryList) != 0:
            #     newPDF.set_font('helvetica', 'B', 13)
            #     newPDF.cell(10, 10, "Custom,", ln=True)
            #     newPDF.set_font('helvetica', '', 10)

            for list in categoryList:
                for item in list:
                    newPDF.cell(5, 3, '')
                    newPDF.cell(0, 12, item.displayName, ln=True)
                    for part in item.listParts:
                        newPDF.cell(30, 0, '')
                        newPDF.cell(25, 0, str(part.qty))
                        newPDF.cell(25, 0, str(part.name))
                        newPDF.cell(25, 0, str(part.width))
                        newPDF.cell(25, 0, str(part.height))
                        newPDF.cell(25, 0, str(part.tape))
                        if part.drill == True:
                            newPDF.cell(25, 0, "Yes")
                        else:
                            newPDF.cell(25, 0, "-")

                        if part.router == True:
                            newPDF.cell(25, 0, "Yes", ln=True)
                        else:
                            newPDF.cell(25, 0, "-", ln=True)
                        newPDF.ln(5)

        file_name_path = filedialog.asksaveasfilename(
            initialdir="C:/Users/arash/OneDrive/Desktop/Cabinets-App/cabinetsAppData",
            initialfile= str(project_name_entry.get()) + "_Cabinets",
            title="Save PDF File",
            filetypes=(
                ("PDF Files", "*.pdf"),
                ("All Files", "*.*"))
            )

        if file_name_path:
            if file_name_path.endswith(".pdf"):
                pass
            else:
                file_name_path = f'{file_name_path}.pdf'

        newPDF.output(file_name_path, 'F')

    elif givenString == "ADD_CATEGORY_PARTS":

        for list in all_parts_list:
            if list == all_base_parts_list and len(list) != 0:
                newPDF.set_font('helvetica', 'B', 13)
                newPDF.cell(10, 10, "Base Total Parts,", ln=True)
                newPDF.set_font('helvetica', '', 10)
            elif list  == all_wall_parts_list and len(list) != 0:
                newPDF.set_font('helvetica', 'B', 13)
                newPDF.cell(10, 10, "Wall Total Parts,", ln=True)
                newPDF.set_font('helvetica', '', 10)
            elif list == all_tall_parts_list and len(list) != 0:
                newPDF.set_font('helvetica', 'B', 13)
                newPDF.cell(10, 10, "Tall Total Parts,", ln=True)
                newPDF.set_font('helvetica', '', 10)
            elif list == all_vanity_parts_list and len(list) != 0:
                newPDF.set_font('helvetica', 'B', 13)
                newPDF.cell(10, 10, "Vanity Total Parts,", ln=True)
                newPDF.set_font('helvetica', '', 10)
            # elif list == totalPartsListC and len(list) != 0:
            #     newPDF.set_font('helvetica', 'B', 13)
            #     newPDF.cell(10, 10, "Custom Total Parts,", ln=True)
            #     newPDF.set_font('helvetica', '', 10)

            for part in list:
                newPDF.cell(30, 0, '')
                newPDF.cell(25, 0, str(part.qty))
                newPDF.cell(25, 0, str(part.name))
                newPDF.cell(25, 0, str(part.width))
                newPDF.cell(25, 0, str(part.height))
                newPDF.cell(25, 0, str(part.tape))
                if part.drill == True:
                    newPDF.cell(25, 0, "Yes")
                else:
                    newPDF.cell(25, 0, "-")
                if part.router == True:
                    newPDF.cell(25, 0, "Yes", ln=True)
                else:
                    newPDF.cell(25, 0, "-", ln=True)
                newPDF.ln(5)

        file_name_path = filedialog.asksaveasfilename(
            initialdir="C:/Users/arash/OneDrive/Desktop/Cabinets-App/cabinetsAppData",
            initialfile= str(project_name_entry.get()) + "_Parts",
            title="Save PDF File",
            filetypes=(
                ("PDF Files", "*.pdf"),
                ("All Files", "*.*"))
            )

        if file_name_path:
            if file_name_path.endswith(".pdf"):
                pass
            else:
                file_name_path = f'{file_name_path}.pdf'

        newPDF.output(file_name_path, 'F')


#-------------------------------------------------- Get PDF Buttons --------------------------------------------------//
rail_size_label_frame = Frame(page3_app_frame, bg = plainWhite)
rail_size_label_frame.grid(row=28, column=0, columnspan=3, padx=50, pady=0, sticky=W+E+S)

def on_get_pdf_button_press(event):
    get_PDF_button.config(image=get_pdf_image_dark)

def on_get_pdf_button_release(event):
    get_PDF_button.config(image=get_pdf_image)

# Reset Workspace button for Workspace
get_PDF_button = Button(rail_size_label_frame, image=get_pdf_image, command= lambda: createPDF("CABINETS"), font=fontSegoeSmall, bd=0, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
get_PDF_button.pack(anchor=W, side="left", padx=(67,0))

get_PDF_button.bind("<Button-1>", on_get_pdf_button_press)
get_PDF_button.bind("<ButtonRelease-1>", on_get_pdf_button_release)


def on_get_second_pdf_button_press(event):
    get_second_PDF_button.config(image=get_pdf_green_image_dark)

def on_get_second_pdf_button_release(event):
    get_second_PDF_button.config(image=get_pdf_green_image)

get_second_PDF_button = Button(rail_size_label_frame, image=get_pdf_green_image, command= lambda: createPDF("ADD_CATEGORY_PARTS"), font=fontSegoeSmall, bd=0, relief="solid", activebackground=plainWhite, bg=plainWhite, fg=textGray)
get_second_PDF_button.pack(anchor=E, side="right", padx=(0,67))

get_second_PDF_button.bind("<Button-1>", on_get_second_pdf_button_press)
get_second_PDF_button.bind("<ButtonRelease-1>", on_get_second_pdf_button_release)


#-------------------------------------------------- main event loop --------------------------------------------------//
# Start the main event loop
root.mainloop()
