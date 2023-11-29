n=int(input())
l=[6,5,10]
for i in range(1,n+1):
    op=input().split()
    if op[0]=='print':
        print(l)
    elif op[0]=='remove':
        x=int(op[1])
        l.remove(x)
    elif op[0]=='append':
        x=int(op[1])
        l.append(x)
    elif op[0]=='sort':
        l.sort()
    elif op[0]=='pop':
        l.pop()
    elif op[0]=='reverse':
        l.reverse()
    elif op[0]=='insert':
        i=int(op[1])
        x=int(op[2])
l.insert(i,x)
