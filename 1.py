def common_prefix():
    x=[]
    for i in zip(*b):
        if (i.count(i[0])==len(i)): 
            x.append(i[0])
        else:
            break
    print(''.join(x))
a=int(input())
b=[]
for i in range(0,a):  
    u=input()
    b.append(u)
common_prefix()
