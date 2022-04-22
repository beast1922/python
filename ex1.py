sub = ("Maths","Science","English")
n = input("Number of students you want to enter :") #number of students data 
n = int(n) #string to int
roll = [] #first empty index
name=[]
result={}
for i in range (n): #loop will run for the range of n(total students)
    r=input("Enter Id of the student : ")
    r=int(r)
    n1=input("Enter name of the student : ")
    roll.append(r) #id will be entered in roll variable
    name.append(n1) #student name will be append in name variable
    m1=input("Enter marks of Maths : ")  #enter marks of 3 subjects
    m1=int(m1)
    m2=input("Enter marks of Science : ")
    m2=int(m2)
    m3=input("Enter marks of English : ")
    m3=int(m3)
    temp=(m1,m2,m3) #all 3 subject marks will be entered through tuple in temp ex = (45,67,89)
    result[r] = temp #marks will be assign to students id wise. ex id[1] = (45,67,89)
print(result)
mt=[] #first empty index for maths subject 
sc=[]
en=[]
for j in result.keys(): #keys() method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion.
    t=result[j] #all result will assign to t
    mt.append(t[0]) #maths subject marks will enter in index 0 of t
    sc.append(t[1]) #science subject marks will enter in index 1 of t
    en.append(t[2]) #english subject marks will enter in index 2 of t
mh=max(mt) #maximun marks of maths subject of all result will assign to mh variable
sh=max(sc)
eh=max(en)
for j in result.keys():
    t = result[j]
    if(t[0] == mh): #if in result first index of maths marks is maximum then it will print that out of all result
        print("Maths")
        print(mh)
        te = roll.index(j) #roll number index of that student will assign to te
        print(name[te]) #name of te will print
        final=("maths",mh,name[te])
        print(final)
    if(t[1] == sh):
        print("Science")
        print(sh)
        te = roll.index(j)
        print(name[te])
        final=("Science",sh,name[te])
        print(final)
    if(t[2] == eh):
        print("english")
        print(eh)
        te = roll.index(j)
        print(name[te])
        final=("english",eh,name[te])
        print(final)
        
    
