x,y,z=map(str,input().split())
a=[]
for i in range(int(l),int(r)+1):
	a.append(str(i))
c=0
for i in a:
	if n in i:
		c+=1
print(c)
