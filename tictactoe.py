from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.title('Tic-Tac-Toe')

digits = [1,2,3,4,5,6,7,8,9]
mark = ''
count = 0
panels = ["panel"]*10

#labels

Label(root, text = "Player 1 : X", font="Sans-serif").grid(row = 0, column = 1)
Label(root, text= "Player 2 : O", font="Sans-serif").grid(row = 1, column = 1)

#buttons
Button1 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 2, column = 0)
Button2 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 2, column = 1)
Button3 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 2, column = 2)

Button4 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 3, column = 0)
Button5 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 3, column = 1)
Button6 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 3, column = 2)

Button7 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 4, column = 0)
Button8 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 4, column = 1)
Button9 = Button(root, width=20, height=9, font="Sans-serif").grid(row = 4, column = 2)

def win(panel, sign):
    return ((panels[1] == panels[2] == panels[3] == sign) or (panels[4] == panels[5] == panels[6] == sign) or (panels[7] == panels[8] == panels[9] == sign) or (panels[1] == panels[4] == panels[7] == sign) or (panels[2] == panels[5] == panels[8] == sign) or (panels[3] == panels[6] == panels[9] == sign) or (panels[1] == panels[5] == panels[9] == sign) or (panels[3] == panels[5] == panels[7] == sign))

root.mainloop()
