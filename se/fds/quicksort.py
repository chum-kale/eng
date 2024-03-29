def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
  
# Function to do Quick sort
  
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
def top_five_percentage(arr):
    print("TOP five percentage is")
    for i in range(len(arr)-1, len(arr)-6, -1):
            print(arr[i])
  
                  
percentage = []
n = int(input("Enter number of students whose percentage are to be displayed : "))
print("Enter percentage for",n,"students (Press ENTER after every students percentage): ")
for i in range(0, n):
    ele = int(input())
    percentage.append(ele)  # adding the element

print("The percentage of",n,"students are : ")
print(percentage)
quickSort(percentage, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % percentage[i]),
top_five_percentage(percentage)