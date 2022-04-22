j = []
ip = input("Enter how many values you want to enter in list: ")
ip = int(ip)
for i in range(ip):
    k = input("Enter values:- ")
    k = int(k)
    j.append(k)

print(range(ip))
elem = input("Enter element you want to search in list:- ")
elem = int(elem)
for i in range(ip):
    if elem == j[i]:
        print("\nElement found at Index:", i)
        print("Element found at Position:", i+1)
    else:
        print("Element not found")
        
print(j)
