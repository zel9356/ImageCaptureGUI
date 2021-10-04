"""
Capture GUI, this is the code that runs the main GUI, which then allows the
UVMSIS to automated
"""
import tkinter as t
from tkinter import ttk, scrolledtext, messagebox
import cv2 as cv
"""
an edit 
"""
"""
Varibales that need to be global
such as the window
And set up for window
"""
# setting up the capture GUI Frame or Window, captureWindow
captureWindow = t.Tk()

# set up our window, size, title, icon
captureWindow.geometry("1300x800")
captureWindow.title("Capture GUI")  # Better name?
captureWindow.iconbitmap("imagesForGUI\cover.ico")  # make our own image

# parchment name variable
name = t.Entry(captureWindow)

# list of filters, 8 elements long, default is None, no filter in that position
filterList = ["None"] * 8

# numbers passes need to image entire doc
# number of images being stitched together
numOfRounds = 1  # default is 1, whole doc covered in one image

# List of filter value drop downs
filterValues = []

# amount drop down
amount = ttk.Combobox(captureWindow)

# widget width and other astetic constnts
width = 20
borderwidth = 2
font = "Helvetica"
fontSize = 12
titleBg = "dim gray"
titleRelief = "groove"
fg = "snow"
bg = "gray"
buttonRelief = "raised"
labelRelief = "flat"
padx = 5
pady = 5
# blank label
blankLabel = t.Label(captureWindow, text="")
blankLabel.configure(font=(font, fontSize), width=width, borderwidth=borderwidth)


def makeListOfAvailableFilters(fileName):
    """
    makes a list of filters form the text file, 1 line 1 filter name
    :param: name of file containing filter names
    :return: list of strings that represent filters
    """
    filters = []
    f = open(fileName)
    for line in f:
        filters.append(line.strip())
    return filters


def makeFilterColumn(filterNames, column):
    """
    makes the column of filter drop down boxes to chose a filter per slot in wheel
    also makes text box at top describing the column
    :param filterNames: list of the names of the available filters
    :param column: int column to place into, for easy changing of gui
    :return: int updated column, two over
    """
    filterLabel = t.Label(captureWindow, text="Choose Filters", fg=fg, bg=titleBg)
    filterLabel.configure(font=(font, fontSize), width=width, borderwidth=borderwidth, relief=titleRelief)
    filterLabel.grid(column=column, row=0, padx=padx, pady=pady)
    blankLabel.grid(column=column + 1, row=0)
    for i in range(0, 4):
        filterValues.append(ttk.Combobox(captureWindow))
        filterValues[i].configure(font=(font, fontSize), width=width)
        filterValues[i]['values'] = filterNames
        # row 0 is taken so we have to place a row down, row =i + 1
        filterCountLabel = t.Label(captureWindow, text="Filter " + str(i + 1), fg=fg, bg=bg)
        filterCountLabel.configure(font=(font, fontSize), width=width, borderwidth=borderwidth, relief=labelRelief)
        filterCountLabel.grid(column=column, row=i + 1, padx=padx, pady=pady)
        filterValues[i].grid(column=column + 1, row=i + 1)
        filterValues[i].current(0)
    return column + 2


def cameraAndLightsButton(column):
    """
    Mkaes the button that turns on and off the lights and opens the camera view for focusing
    :param column: int column to place into, for easy changing of gui
    :return: int updated column
    """

    # these two may be able to be combined, not sure yet
    def lightsON():
        """
        event for the pressing of Lights ON button
        turns the lights on
        :return:
        """
        # TODO call a function that turns the lights on

    def lightsOFF():
        """
        event for the pressing of Lights OFF button
        turns the lights off
        :return:
        """
        # TODO call a function that turns the lights off

    def cameraPushed():
        """
        event for when the camera live view button is pushed
        Opens live camera view for focusing
        :return:
        """
        # TODO call a function that opens a camera live view

    # Lights on button creation and placement
    lightsOnButton = t.Button(captureWindow, text="Lights ON", fg=fg, bg=bg)
    lightsOnButton.configure(font=(font, fontSize), width=width, borderwidth=borderwidth, relief=buttonRelief,
                             command=lightsON)
    lightsOnButton.grid(column=column, row=0, padx=padx, pady=pady)

    # Lights off button creation and placement
    lightsOffButton = t.Button(captureWindow, text="Lights OFF", fg=fg, bg=bg)
    lightsOffButton.configure(font=(font, fontSize), width=width, borderwidth=borderwidth, relief=buttonRelief,
                              command=lightsOFF)
    lightsOffButton.grid(column=column, row=1, padx=padx, pady=pady)

    # camera live view button creation and placement
    cameraLiveViewButton = t.Button(captureWindow, text="Camera Live View", fg=fg, bg=bg)
    cameraLiveViewButton.configure(font=(font, fontSize), width=width, borderwidth=borderwidth, relief=buttonRelief,
                                   command=cameraPushed)
    cameraLiveViewButton.grid(column=column, row=2, padx=padx, pady=pady)

    return column + 1


def makeNameEntry(column):
    """
    makes a label that prompts for the name of the document being imaged and an entry box
    to put the info into
    :param column: int column to place into, for easy changing of gui
    :return: int updated column
    """
    enterNameLabel = t.Label(captureWindow, text="Enter File Name", fg=fg, bg=titleBg)
    enterNameLabel.configure(font=(font, fontSize), width=width, borderwidth=borderwidth, relief=titleRelief)
    enterNameLabel.grid(column=column, row=0, padx=padx, pady=pady)
    name.configure(font=(font, fontSize), width=width, borderwidth=borderwidth)
    name.grid(column=column, row=1)
    return column + 1


def makeAmountColumn(column):
    """
    makes the column that has a label prompting of the amount of images need for stitching and the combo box to choose
    the amount
    :param column: int column to place into, for easy changing of gui
    :return: int updated column
    """
    amountLabel = t.Label(captureWindow, text="Choose stitch amount", fg=fg, bg=titleBg)
    amountLabel.configure(font=(font, fontSize), width=width, borderwidth=borderwidth, relief=titleRelief)
    amountLabel.grid(column=column, row=0, padx=padx, pady=pady)
    amount.configure(font=(font, fontSize), width=width)
    amount['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    amount.grid(column=column, row=1, padx=padx, pady=pady)
    amount.current(0)
    return column + 1


def makeGoButton(column):
    """
    makes the go button, starts the imaging process
    :param column: int column to place into, for easy changing of gui
    :return: int updated column
    """


    def GOEvent():
        """

        :return:
        """
        # lets error catch first
        
        # TODO

    goButton = t.Button(captureWindow, text="GO", fg=fg, bg=bg)
    goButton.configure(font=(font, fontSize), width=width, borderwidth=borderwidth, relief=buttonRelief,
                       command=GOEvent)
    goButton.grid(column=column, row=0, padx=padx, pady=pady)
    return column


def makeWidgets():
    """
    calls functions that make widgets for the GUI
    :return:
    """
    column = 0
    filterNames = makeListOfAvailableFilters("filterList")
    column = makeFilterColumn(filterNames, column)
    column = makeNameEntry(column)
    column = makeAmountColumn(column)
    column = cameraAndLightsButton(column)
    column = makeGoButton(column)


def main():
    """
    Main function
    :return: NONE
    """
    makeWidgets()

    # Displays the captureWindow GUI
    captureWindow.mainloop()
    print("main")


if __name__ == '__main__':
    main()
