import interface as i
from ciphers import caesar_encrypt
from ciphers import atbash_encrypt
def encrypt():
    currentcipher=i.choice.get()
    if currentcipher=='Цезарь':
        plaintext=i.plaintextbox.get()
        key=int(i.keybox.get())
        i.ciphermessage.config(text=caesar_encrypt(plaintext,key))
    elif currentcipher=='Атбаш':
        plaintext=i.plaintextbox.get()
        i.ciphermessage.config(text=atbash_encrypt(plaintext))
def change_cipher():
    currentcipher=i.choice.get()
    if currentcipher=='Цезарь':
        i.ciphername.config(text='Зашифровано шифром Цезаря')
        i.keybox.config(state='normal')
    elif currentcipher=='Атбаш':
        i.ciphername.config(text='Зашифровано шифром Атбаш')
        i.keybox.config(state='disabled')
i.radiocaesar.config(command=change_cipher)
i.radioatbash.config(command=change_cipher)
i.button.config(command=encrypt)
i.choice.set('Атбаш')
change_cipher()
i.window.mainloop()
