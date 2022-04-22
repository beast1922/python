#los = ('a','b','c','d')
#roll = [1,2,3]
#name=["kartik","",""]
#slist = {1:['a','b','c'],2:,3:}
#mark = {1:[12,33,22],2:,3:}

d = {}
n = input("enter number of records")
n = int(n)
th = input("enter minimum threshhold value")
th = int(th)
temp = []
for i in range(n):
    k = input("enter roll number")
    k = int(k)
    j = input("number of subjects")

    j = int(j)
for r in range(j):
    s1 = input("Enter subject name")
    temp.append(s1)
    d[k] = temp
    temp = []

#print(d)
temp=[]
for i in d.keys():
t = d[i]
for j in t:
if(j not in temp):
temp.append(j)
ct = 0
c = 0
print(temp)
for j in temp:

for i in d.keys():
t = d[i]
c = t.count(j)
ct = ct + c
print(j + " " + str(ct))
ct = 0
