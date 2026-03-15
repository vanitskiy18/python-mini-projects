alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def caesar_encrypt(plaintext,key):
    ciphertext=''
    for i in plaintext.lower():
        if i.isspace():
            ciphertext=ciphertext+i
        else:
            index=alphabet.find(i)
            new_index=(index+key)%len(alphabet)
            new_letter=alphabet[new_index]
            ciphertext=ciphertext+new_letter
    return ciphertext
def atbash_encrypt(plaintext):
    new_alphabet=alphabet[::-1]
    ciphertext=''
    for i in plaintext.lower():
        if i.isspace():
            ciphertext=ciphertext+i
        else:
            index=alphabet.find(i)
            new_letter=new_alphabet[index]
            ciphertext=ciphertext+new_letter
    return ciphertext
# print(caesar_encrypt('айтигенио',3))
#print(atbash_encrypt('айтигенио'))
