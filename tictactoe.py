from tabnanny import check
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

def checker(digit):
    global count, mark, digits
    # l = [Button1, Button2, Button3, Button4, Button5, Button6, Button6, Button7, Button8, Button9]
    if digit == 1 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            panels[digit] == 'X'
            mark = 'X'
        else:
            panels[digit] == 'O'
            mark = 'O'

        count+=1
        sign = mark
        button1.config(text = mark)

        if(win(panels, sign)):
            if(sign == 'X'):
                msg.showinfo("Player 1 won")
                root.destroy()
            elif(sign == 'O'):
                msg.showinfo("Player 2 won")
                root.destroy()
    elif count > 8 and win(panels, 'X')==False and win(panels, 'O')==False: 
        msg.showinfo("The match is a tie")
        root.destroy

#buttons
button1 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(1)).grid(row = 2, column = 0)
button2 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(2)).grid(row = 2, column = 1)
button3 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(3)).grid(row = 2, column = 2)

button4 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(4)).grid(row = 3, column = 0)
button5 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(5)).grid(row = 3, column = 1)
button6 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(6)).grid(row = 3, column = 2)

button7 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(7)).grid(row = 4, column = 0)
button8 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(8)).grid(row = 4, column = 1)
button9 = Button(root, width=20, height=9, font="Sans-serif", command=lambda: checker(9)).grid(row = 4, column = 2)

def win(panel, sign):
    return ((panels[1] == panels[2] == panels[3] == sign) or (panels[4] == panels[5] == panels[6] == sign) or (panels[7] == panels[8] == panels[9] == sign) or (panels[1] == panels[4] == panels[7] == sign) or (panels[2] == panels[5] == panels[8] == sign) or (panels[3] == panels[6] == panels[9] == sign) or (panels[1] == panels[5] == panels[9] == sign) or (panels[3] == panels[5] == panels[7] == sign))

root.mainloop()















# def addSign(button):
#     l = [Button1,Button2,Button3,Button4,Button5,Button6,Button7,Button8,Button9]
#     if count%2==0:
#         if l[button]['text'] == '':
#             l[button]['text'] == 'X'
#     else:
#         if l[button]['text'] == '':
#             l[button]['text'] == 'O'
