x,y=input().split()
ten=abs(len(x)-len(y))
for i in range(len(x)):
    if len(y)==1 and y[i] in x:
        break
    if x[i]!=y[i]:
        ten+=1
print(ten)
