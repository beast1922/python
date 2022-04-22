 los = ("Chemistry","Biology","Maths","English")
n = input("Enter number of students to enter : -")
n = int(n)
rl = [1,2,3]
nm = ["Heer","Pinal","Radhika"]
slist = {1:["Chemistry","Biology","Maths"],2:["Maths","English"],3:["Biology","English"]}
smark = {1:[70,80,80],2:[33,55],3:[60,70]}
t1 = []
t2 = []
count =[]
for i in range(n):
    r = input("Enter roll  : -")
    r = int(r)
    n1 = input("Enter name : -")
    rl.append(r)
    nm.append(n1)
    print("Enter for student " + n1)
    k = input("Enter number of subjects : -")
    k = int(k)
    for d in range(k):
        sn = input("name of the subject : -")
        sm = input("marks of the subject : -")
        sm = int(sm)
        t1.append(sn)
        t2.append(sm)
        slist[r] = t1
        smark[r] = t2
        t1 = []
        t2 = []
l = 0
print("---------Student Wise Report---------")
for i in rl:
    t1 = slist[i]
    t2 = smark[i]
    t = sum(t2)
    for j in los:
        if(j not in t1):
            k = los.index(j)
            t2.insert(k,"Ab")
            t1.insert(k,"Ab")
    
    print(str(i)+ " " +nm[l] +" " +str(t2) + " " +str(t))
    t1 = []
    t2 = []
    l = l + 1

print(slist)
print(smark)
 

ct=[]
c=0
for i in los:
    for j in slist.keys():
        t=slist[j]
        if(i in t):
            c=c+1
    print("---------------------------------------------")
    print("Subject:- "+i+ " "+ " Taken by total student:- " +str(c))
    ct.append(c)
    c=0


mx=0
k=0
h=0
print("---------Subject Wise Report---------")
for i in los:
    for j in rl:
        d=slist[j]
        d1=smark[j]
        if(i in d):
            #print(i)
            if(mx<d1[k]):
                mx=d1[k]
                s=nm[rl.index(j)]
    k=k+1
    
    print(str(i)+ " "+ str(mx) +" "+s)
    mx=0
