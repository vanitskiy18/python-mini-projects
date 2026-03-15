import random
x=[2,5,1,3,4]
def qsort(y):
    if len(y)>=2:
        d=[]
        b=[]
        c=[]
        a=random.choice(y)
        for i in y:
            if i<a:
                 d.append(i)
            if i==a:
                 b.append(i)
            if i>a:
                 c.append(i)
        return qsort(d)+b+qsort(c)
    else:
        return y
print(qsort(x))

    
