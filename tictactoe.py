from tkinter import *
import random
from tkinter import messagebox
import sys

root = Tk()



root.configure(bg='gray35')

root.geometry('600x600')

root.title('TicTacToe')
l = Label(root,font='cambria 30',fg='white',bg='gray35')
l.pack()


z = random.randint(0,1)

def check_turn():

    if z == 1:
        l['text'] = 'It is X turn'
        
    if z == 0:

        l['text'] = 'It is O turn'

        
check_turn()


def check_win(b1,b2,b3):

    if b1['text'] == b2['text'] and b2['text'] == b3['text'] and b1['text'] != '' and b2['text']!= '' and b3['text'] != '':
        if messagebox.askyesno('Game',b1['text']+''+'wins do you want to retry') == True:
            
            bt1['text'] = ''
            bt2['text'] = ''
            bt3['text'] = ''
            bt4['text'] = ''
            bt5['text'] = ''
            bt6['text'] = ''
            bt7['text'] = ''
            bt8['text'] = ''
            bt9['text'] = ''
            z = random.randint(0,1)
             
             
        else:
            root.withdraw()
            sys.exit()
    else:
        if bt1['text'] and bt2['text'] and bt3['text'] and bt4['text'] and bt5['text'] and bt6['text'] and bt7['text'] and bt8['text'] and bt9['text'] != 'X' or   bt1['text'] and bt2['text'] and bt3['text'] and bt4['text'] and bt5['text'] and bt6['text'] and bt7['text'] and bt8['text'] and bt9['text'] != 'O':
            if messagebox.askyesno('Tie','It is a tie do you want to retry') == True:
            
                bt1['text'] = ''
                bt2['text'] = ''
                bt3['text'] = ''
                bt4['text'] = ''
                bt5['text'] = ''
                bt6['text'] = ''
                bt7['text'] = ''
                bt8['text'] = ''
                bt9['text'] = ''
                z = random.randint(0,1)

            


    


def button_command(bt,bn1,bn2):
    global z,l


    
    

    if bt['text'] == 'X' or bt['text'] == 'O':
        print('Sorry this position is occupied')

    else:
        if z == 1:
            bt['text'] = 'X'
            l['text'] = 'It is O turn'
            #checking for horizontal wins
            check_win(bt,bn1,bn2)
            #checking for diagonal wins
            check_win(bt1,bt5,bt9)
            check_win(bt3,bt5,bt7)
            check_win(bt3,bt6,bt9)
            #checking for vertical wins
            check_win(bt1,bt4,bt7)
            check_win(bt2,bt5,bt8)
            check_win(bt3,bt6,bt9)
            
            z = 0
        elif z == 0:
            bt['text'] = 'O'
            l['text'] = 'It is X trun'
            check_win(bt,bn1,bn2)
            #checking for diagonal wins
            check_win(bt1,bt5,bt9)
            check_win(bt3,bt5,bt7)
            #checking for vertical wins
            check_win(bt1,bt4,bt7)
            check_win(bt2,bt5,bt8)
            check_win(bt3,bt6,bt9)
            z = 1
bt1 = Button(root,bg='gray40',command=lambda: button_command(bt1,bt2,bt3),font='cambria 30',width=5)
bt1.place(x=100,y=100)



bt2 = Button(root,bg='gray40',command=lambda: button_command(bt2,bt1,bt3),font='cambria 30',width=5)
bt2.place(x=250,y=100)



bt3 = Button(root,bg='gray40',command=lambda: button_command(bt3,bt1,bt2),font='cambria 30',width=5)
bt3.place(x=400,y=100)


bt4 = Button(root,bg='gray40',command=lambda: button_command(bt4,bt5,bt6),font='cambria 30',width=5)
bt4.place(x=100,y=200)


bt5 = Button(root,bg='gray40',command=lambda: button_command(bt5,bt6,bt4),font='cambria 30',width=5)
bt5.place(x=250,y=200)


bt6 = Button(root,bg='gray40',command=lambda: button_command(bt6,bt5,bt4),font='cambria 30',width=5)
bt6.place(x=400,y=200)


bt7 = Button(root,bg='gray40',command=lambda: button_command(bt7,bt8,bt9),font='cambria 30',width=5)
bt7.place(x=100,y=300)


bt8 = Button(root,bg='gray40',command=lambda: button_command(bt8,bt7,bt9),font='cambria 30',width=5)
bt8.place(x=250,y=300)


bt9 = Button(root,bg='gray40',command=lambda: button_command(bt9,bt8,bt7),font='cambria 30',width=5)
bt9.place(x=400,y=300)





        





