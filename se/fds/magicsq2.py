from __future__ import print_function
row = int(input("Enter the number of rows:")) 
col = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrixa = [] 

print("Enter the entries rowwise:") 
  
# User input 
for i in range(row):          # A for loop for row entries 
    a =[] 
    for j in range(col):      # A for loop for column entries 
         a.append(int(input())) 
    matrixa.append(a)     

 
# For printing first  matrix 
for i in range(row): 
    for j in range(col): 
        print(matrixa[i][j], end = " ")

    print() 


sum1=0 
flag=0 
for j in range(col): 
    sum1+=matrixa[0][j]
    print(matrixa[0][j])
sum2=sum1   
sum1=0 
for i in range(1,row): 
    sum1=0 
    for j in range(col): 
        sum1+=matrixa[i][j]
        print(matrixa[i][j])

    if sum1!=sum2: 
        flag=1

    break 
sum2=0 

if flag==0:    
    for j in range(col): 
        sum2=0 
        for i in range(row): 
            sum2+=matrixa[i][j] 
        if sum1!=sum2: 
            flag=1 
        break 
sum2=0       
if flag==0: 
    for i in range(row): 
        for j in range(col): 
            if i==j: 
                sum2+=matrixa[i][j]


    if sum1!=sum2: 
        flag=1 

j=col-1   
sum2=0 

if flag==0: 
    for i in range(row): 
        sum2+=matrixa[i][j] 
        j=j-1 
   
    if sum1!=sum2 : 
        flag=1 

if flag==0: 
    print("Given Matrix is a Magic Square") 
else:
    print("Given Matrix is not a Magic Square")