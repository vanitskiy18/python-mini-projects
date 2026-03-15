import random
n=random.randint(1,100)
coin_nom=[random.randint(1,100) for i in range(n)]
x=0
for i in coin_nom:
    x=x+i
y=x/2
for i in range(len(coin_nom)-1):
    for j in range(len(coin_nom)-i-1):
        if coin_nom[j]<coin_nom[j+1]:
            coin_nom[j],coin_nom[j+1] = coin_nom[j+1],coin_nom[j]
a=0
b=0
for i in coin_nom:
    a=a+i
    b=b+1
    if a>y:
        break
print(b)
    
