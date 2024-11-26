    root = tkinter.Tk()
    root.withdraw()
    filename = tkinter.filedialog.askopenfilename()

    def check_filetype():
        for index, character in enumerate(filename):
            if character == ".":
                if filename[index+1:] == "obj":
                    return True
                else:
                    return False