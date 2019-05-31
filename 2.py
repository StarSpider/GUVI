x,y,z=map(int,input().split())
c=0
z=str(z)
for i in range(l,r+1):
	a=str(i)
	if n in a:
		c+=1
print(c)
