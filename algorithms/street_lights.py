import random
n=random.randint(1,1000)
l=random.randint(1,10**9)
lights_cor=[random.randint(0,l) for i in range(n)]
for i in range(len(lights_cor)-1):
    for j in range(len(lights_cor)-i-1):
        if lights_cor[j]>lights_cor[j+1]:
            lights_cor[j],lights_cor[j+1] = lights_cor[j+1],lights_cor[j]
x=lights_cor[0]
for i in range(len(lights_cor)-1):
    if x<(lights_cor[i+1]-lights_cor[i])/2:
        x=(lights_cor[i+1]-lights_cor[i])/2
y=l-lights_cor[-1]
if x>y:
    print(x)
else:
    print(y)
