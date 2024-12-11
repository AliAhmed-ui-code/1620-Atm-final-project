from gui import *
import csv

def main()->None:
    """
    This function creates the gui window!
    :return: Sends the window to gui file
    """
    window = Tk()
    window.title('ATM')
    window.geometry('500x500')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()



if __name__ == '__main__':
    main()