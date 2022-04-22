los=("speaking","listening","writing","reading")
result={'ishita':[6,7,8,9],'hinal':[7,6,8,9]}
temp=[]
n = int(input("Enter no. of student : - "))
for i in range(n):
    sn=input("Enter name of the student : ")
   
    for j in range(4):
        p1=int(input("Enter marks for s,l,w,r : "))
        temp.append(p1)
    result[sn]=temp
    temp=[]

print("--------------------------")


print("--------- Result ---------")

for i in result.keys():
    j=sum(result[i])/4
    result[i].append(j)
    if(j > 5.9):
        print(i +' is qualified ' +str(j))
    else:
        print(i +' is not qualified ' +str(j))

print(result)

j=0
for i in result.keys():
    temp.append(result[i][4])
print(temp)
    
m = max(temp)
for i in result.keys():
    if(result[i][4] == m):
        print("maximum avg : "+i+" "+ str(m))

temp=[]

for i in result.keys():
    temp.append(result[i][0])
    m=max(temp)


for i in result.keys():
    if(m == result[i][0]):
        print(i + " got maximun in speaking " +str(m))

temp=[]

for i in result.keys():
    temp.append(result[i][1])
    m=max(temp)


for i in result.keys():
    if(m == result[i][1]):
        print(i + " got maximun in listening " +str(m))

temp=[]

for i in result.keys():
    temp.append(result[i][2])
    m=max(temp)


for i in result.keys():
    if(m == result[i][2]):
        print(i + " got maximun in writing " +str(m))

temp=[]

for i in result.keys():
    temp.append(result[i][3])
    m=max(temp)


for i in result.keys():
    if(m == result[i][3]):
        print(i + " got maximun in reading " +str(m))
    
