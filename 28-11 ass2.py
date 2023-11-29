x=int(input())
y=int(input())
z=int(input())
n=int(input())
res=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k!=n:
                l=[]
                l.append(i)
                l.append(j)
                l.append(k)
                res.append(l)
               
print(res)
