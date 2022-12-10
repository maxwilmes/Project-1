from gui import*
from tkinter import*


def main():
    window = Tk()
    window.title('MULTI-USE CALCULATOR')
    window.geometry('500x530')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()



if __name__ == '__main__':
    main()
