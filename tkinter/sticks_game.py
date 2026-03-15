from tkinter import *
import random
window=Tk()
window.geometry('400x300')
window.title('Палочки')
sticks=20
def player():
    global sticks
    delete_sticks=int(entry_sticks.get())
    list1=[1,2,3]
    if delete_sticks in list1 and delete_sticks<sticks:
        sticks=sticks-delete_sticks
        label_sticks.config(text=(sticks*'|'))
        status.config(text=str(sticks))
    if sticks==1:
        status.config(text='Вы победили',fg='green')
        button.config(state=DISABLED)
    else:
        label_move.config(text='Ход компьютера, ожидайте')
        button.config(state=DISABLED)
        window.after(2000,computer)
def computer():
    global sticks
    if sticks==4:
        delete_sticks=3
    elif sticks==3:
        delete_sticks=2
    elif sticks==2:
        delete_sticks=1
    else:
        delete_sticks=random.randint(1,3)
    sticks=sticks-delete_sticks
    label_sticks.config(text=(sticks*'|'))
    status.config(text=str(sticks))
    if sticks==1:
        status.config(text='Компьютер победил',fg='red')
        button.config(state=DISABLED)
    else:
        label_move.config(text='Введите число от 1 до 3')
        button.config(state=NORMAL)
label_move=Label(font=('Arial',15,'bold'),text='Введите число от 1 до 3')
entry_sticks=Entry(font=('Arial',15,'bold'))
label_sticks=Label(font=('Arial',30,'bold'),text=sticks*'|')
status=Label(font=('Arial',30,'bold'))
button=Button(font=('Arial',15,'bold'),text='Взять палочку',command=player)
label_move.pack(pady=10)
entry_sticks.pack(pady=10)
label_sticks.pack(pady=10)
status.pack(pady=10)
button.pack(pady=10)
