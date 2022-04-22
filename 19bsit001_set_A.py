#Set-A
name = []
r = []
count = 0

n = input("Enter total number of students whose name you want to enter:- ")
n = int(n)

for i in range(n):
    nm = input("Enter student name:- ")
    name.append(nm)


ch = input("Enter one character you want to search in list:- ")

for i in name:
    for j in i:
        if(ch == j):
            count = 1
    r.append(count)
    count = 0
            
print("\nList of student name:- ")
print(name)
print("\nList of occurrence of character in string:- ")
print(r)
