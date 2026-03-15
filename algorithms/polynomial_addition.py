y={3:1.0, 2:5.0, 1:4.0, 0:2.0}
x={2:1.0,1:5.0,0:6.0}
def func(x,y):
    z={}
    for i in x.keys():
        for j in y.keys():
            if i==j:
                z[i]=x[i]+y[i]
    for i in x.keys():
        if not i in y.keys():
            z[i]=x[i]
    for j in y.keys():
        if not j in x.keys():
            z[j]=y[j]
    sort_z={}
    a=[]
    for i in z.keys():
        a.append(i)
    for i in range(len(z)-1):
        for j in range(len(z)-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]
    a=a[::-1]
    for i in a:
        sort_z[i]=z[i]       
    print(sort_z)
func(x,y)
        
        
            
            
                
        
    
