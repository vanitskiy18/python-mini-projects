from tkinter import *
from dictionary import words
import random
cnt=0
root=Tk()
root.geometry('225x230')
root.resizable(False,False)
root.title('Learning English')
menu1=Button(text='Can you translate?\nENG->RUS',width=300,height=7,command=lambda language='eng':startLevel(language))
menu2=Button(text='Can you translate?\nRUS->ENG',width=300,height=7,command=lambda language='rus':startLevel(language))
rus_words=words
eng_words=dict([[v,k] for k,v in words.items()])
def showMenu():
    menu1.pack()
    menu2.pack()
def hideMenu():
    menu1.pack_forget()
    menu2.pack_forget()
def chooseWord(language):
    if language=='rus':
        return random.choice([i for i in rus_words])
    if language=='eng':
        return random.choice([a for a in eng_words])
def startLevel(language):
    hideMenu()
    word=chooseWord(language)
    if language=='rus':
        randomLetters=[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(25-len(word))]
        label1=Label(root,text=rus_words.get(word),font='Arial 20')
    if language=='eng':
        randomLetters=[random.choice('АБВГДЕЁЖЗИЙКЛМНОПРОСТУФХЦЧШЩЪЫЬЭЮЯ') for i in range(33-len(word))]
        label1=Label(root,text=eng_words.get(word),font='Arial 20')
    label2=Label(root,text='',font='Arial 20')
    label1.grid(columnspan=5,sticky='ew')
    label2.grid(columnspan=5,sticky='ewsn')
    letters=[i for i in word]
    for i in range(len(randomLetters)):
        letters.append(randomLetters[i])
    random.shuffle(letters)
    buttons=[]
    column=0
    row=3
    for i in range(0,len(letters)):
        buttons.append(Button(root,text=letters[i],width=5))
        buttons[i].config(command=lambda button=buttons[i]: chooseLetter(button))
        buttons[i].grid(column=column,row=row,sticky='ew')
        column=column+1
        if column>4:
            column=0
            row=row+1
    def chooseLetter(button):
        global cnt
        if button.cget('text')==word[cnt] and button.cget('bg')!='green':
            button.config(bg='green')
            label2.config(text=label2.cget('text') + word[cnt])
            cnt=cnt+1
        elif button.cget('bg')!='green':
            for i in buttons:
                i.config(bg='SystemButtonFace')
            label2.config(text='')
            cnt=0
        if cnt>len(word)-1:
            cnt=0
            delete()
            showMenu()
    def delete():
        del letters[:]
        for i in buttons:
            i.destroy()
        del buttons[:]
        label1.destroy()
        label2.destroy()
showMenu()
root.mainloop()
