n=int(input("Enter the total number of students: "))
arr=[]
for i in range(n):
    ele=float(input("Enter the percentage: "))
    arr.append(ele)
print("The entered list is: ",arr)

def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j-=1
        l[j+1]=key
        print("The list at iteration",i,"is: ",l) 

    return l

def shell_sort(l):
    n=len(l)
    gap=n//2
    print("gap is: ",gap)
    while gap>0:
        for i in range(gap,n):
            temp=l[i]
            j=i
            while j>=gap and l[j-gap]>temp:
                l[j]=l[j-gap]
                j-=gap
            l[j]=temp
        gap//=2
    print("The list at iteration",i,"is: ",l)
    return l
    
choice=input("Enter your choice: Insertion for insertion sort and shell for shell sort: ")
if choice.lower()=="insertion":
    print("The sorted list is: ",insertion_sort(arr))
elif choice.lower()=="shell":
    print("The sorted list is: ",shell_sort(arr))
else:
    print("Choice not found")