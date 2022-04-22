list1= [34,78,65,43]

n = int(input("Enter element to search "))


if(n in list1):
    
    print("Element found at Index ",list1.index(n))
    print("Element found at Position ",list1.index(n)+1)
else:
        print("Element not found")
    
