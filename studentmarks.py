name=[]
mark=[]
rn=[]
d1={}
d2={}
n1=int(input("Enter Number of transection : "))
for i in range(n1):
    n=input("Enter Name : ")
   
    r=int(input("Enter Roll no. : "))
    d1[r]=n
    
    name.append(n)
    rn.append(r)
    
    for j in range(3):
        m1=int(input("Enter marks of 3 subject : "))
        d2[r]=m1
        mark.append(m1)
print(name)
print(mark)
print(rn)
print(d1)
print(d2)

for j in rn:
    while(i<3):
        
    
