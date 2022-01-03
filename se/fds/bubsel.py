# Selection sort function
def selectionsort (arr):
    for s in range (len(arr)):
        min = s
        for i in range (s + 1 , len(arr)):
            if arr[i] < arr[min]:
                min = i
        (arr[s], arr[min]) = (arr[min], arr[s])
    return arr

# Bubble sort function
def bubblesort (arr):
    for i in range (len(arr)):
        for j in range (0 , len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t
    return arr


def printarray(arr):
    print ("Marks of students in ascending order:")
    for i in range (len(arr)):
        print (arr[i])
    print("\n")

# Function to display top 5 marks
def top(arr):
    print ("Top 5 marks are:")
    print (arr[-1:-6:-1] , sep="\n")


# Main function
arr = []
n = int(input("Enter number of students: "))
for i in range(n):
    e = float(input("Percentage:"))
    arr.append(e)
print ('\n')
sortedarr = selectionsort(arr)
printarray(sortedarr)
top(sortedarr)
printarray(sortedarr)





