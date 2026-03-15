alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def caesar_encrypt(plaintext,key):
    unciphertext=''
    for i in plaintext.lower():
        if i.isspace():
            unciphertext=unciphertext+i
        else:
            index=alphabet.find(i)
            starting_index=index-key
            starting_letter=alphabet[starting_index]
            unciphertext=unciphertext+starting_letter
    return unciphertext
def atbash_encrypt(plaintext):
    new_alphabet=alphabet[::-1]
    unciphertext=''
    for i in plaintext.lower():
        if i.isspace():
            unciphertext=unciphertext+i
        else:
            index=new_alphabet.find(i)
            starting_letter=alphabet[index]
            unciphertext=unciphertext+starting_letter
    return unciphertext
#print(atbash_encrypt('яхмцьъсцр'))
# for key in range(1,34):
#    print(caesar_encrypt('ч жбъщиуоюя ёхэ цищъз нюйё хзцхн',key))
