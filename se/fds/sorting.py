def sort(arr):
  for i in range(1,len(arr)):
      k=arr[i]
      j= i-1
      while (j>=0 and arr[j]>k):
          arr[j+1] = arr[j]
          j=j-1
      arr[j + 1] = k
      print ("pass" , i ,":-" , arr[:])

arr=[]
n = int(input("Enter number of students:"))
for i in range(n):
    e= float(input("Percentage:"))
    arr.append(e)
print ('\n')
sort(arr)
print (" \n Sorted elements of array: \n " , arr) 