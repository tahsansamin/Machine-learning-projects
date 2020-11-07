from tkinter import *



import time


import sys


from tkinter import messagebox


import threading



root = Tk()



root.geometry('600x500')



root.title('Click the Cat')

instruct_label = Label(root,text='JUST CLICK!',font='cambria 50').pack()

cat_img = PhotoImage(file='D:/DOCUMENTS/Desktop/Python Projects/cat.png')

current_var = StringVar()


current_var.set(0)


current_time = StringVar()



Time = 15



score = 0


def countdown():

    global Time


    while True:
        current_time.set(Time)
        time.sleep(1)

        Time -= 1

        

        if Time == 0:


            


            info = 'Time up your score: '+str(score)


            messagebox.showinfo('Done',info)

            sys.exit()




time_label = Label(root,textvariable=current_time,font='cambria 15').pack()



thread1 = threading.Thread(target=countdown)

thread1.start()
def click_func():


    global score

    score+=500

    current_var.set(score)


cat_button = Button(root,image=cat_img,font='arialblack 40',command=click_func).place(x=35,y=150)

current_score = Label(root,textvariable=current_var,font='cambria 15').place(x=10,y=100)


root.mainloop()
 




    
