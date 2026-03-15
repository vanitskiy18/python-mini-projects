from tkinter import *
from tkinter import messagebox
import math
window=Tk()
window.title('Решатель уравнений')
window.geometry('250x300')
def equate(event):
    try:
        a=float(entry_a.get())
        b=float(entry_b.get())
        c=float(entry_c.get())
        x=messagebox.askyesno('Проверка',f'Вы уверены, что хотите решить это уравнение со значеними {int(a)},{int(b)},{int(c)}?')
        if x==True:
            D=b**2-4*a*c
            if D>=0:
                x_1=(-b+math.sqrt(D))/(2*a)
                x_2=(-b-math.sqrt(D))/(2*a)
                text=f'Дискриминант равен {D}\nx1={x_1}\nx2={x_2}'
                output.delete(0.0,END)
                output.insert(END,text)
            else:
                text=f'Дикриминант равен {D}\nУравнение не имеет решений'
                output.delete(0.0,END)
                output.insert(END,text)
    except ValueError:
        text='Убедитесь что ввели 3 числа'
        output.delete(0.0,END)
        output.insert(END,text)
def clearence(event):
    event.widget.delete(0,END)
frame_1=LabelFrame(text='Введите исходные данные',height=50,width=200)
entry_a=Entry(frame_1,width=5)
label_1=Label(frame_1,width=5,text='x**2 +')
entry_b=Entry(frame_1,width=5)
label_2=Label(frame_1,width=5,text='x +')
entry_c=Entry(frame_1,width=5)
label_3=Label(frame_1,width=5,text='= 0')
frame_2=LabelFrame(text='Решение',height=150,width=200)
output=Text(frame_2,height=5)
frame_1.pack(padx=5,pady=5)
entry_a.place(x=5,y=5)
label_1.place(x=30,y=5)
entry_b.place(x=75,y=5)
label_2.place(x=100,y=5)
entry_c.place(x=140,y=5)
label_3.place(x=165,y=5)
frame_2.pack(padx=5,pady=5)
output.pack(padx=5,pady=5)
entry_a.bind('<F1>',lambda event: messagebox.showinfo('Информация','Введите число a'))
entry_b.bind('<F1>',lambda event: messagebox.showinfo('Информация','Введите число b'))
entry_c.bind('<F1>',lambda event: messagebox.showinfo('Информация','Введите число c'))
window.bind('<Return>',equate)
window.bind('<Control-Key-1>',lambda event: entry_a.focus())
window.bind('<Control-Key-2>',lambda event: entry_b.focus())
window.bind('<Control-Key-3>',lambda event: entry_c.focus())
entry_a.bind('<FocusIn>',clearence)
entry_b.bind('<FocusIn>',clearence)
entry_c.bind('<FocusIn>',clearence)


