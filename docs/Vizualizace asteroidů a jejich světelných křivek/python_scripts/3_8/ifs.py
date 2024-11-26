    if filename == '':
        print("NO FILE WAS SELECTED")
        vispy.app.quit()
    elif check_filetype() == False:
        print("NEEDS TO BE AN .OBJ FILE")
        vispy.app.quit()