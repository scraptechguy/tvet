from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

def check_filetype():
    for index, character in enumerate(filename):
        if character == ".":
            if filename[index+1:] == "obj":
                return True
            else:
                return False

right_filetype = check_filetype()
print(right_filetype)