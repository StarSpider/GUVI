v1 = int(input(""))
v2 = int(input(""))
v3 = int(input(""))
 
if (v1 > v2) and (v1 > v3):
   largest = v1
elif (v2 > v1) and (v2 > v3):
   largest = v2
else:
   largest = v3
 
print(largest)
