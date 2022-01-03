from __future__ import print_function

# Removing duplicates
def duplicate(d):
    list =[]
    for i in d:
        if i not in list:
            list.append(i)
    return list

# Union of 2 sets

def union(list1, list2):
    list3= list1
    for v in list2:
        if v not in list3:
            list3.append(v)
    return list3

# Intersection of 2 sets

def intersection(list1, list2):
    list3=[]
    for v in list1:
        if v in list2:
            list3.append(v)
    return list3

# Difference of 2 sets

def difference(list1, list2):
    list3=[]
    for v in list1:
        if v not in list2:
            list3.append(v)
    return list3

# Symmetric difference of 2 sets

def symdiff(list1, list2):
    list3=[]
    d1 = difference(list1, list2)
    d2 = difference(list2, list1)
    list3= union(d1, d2)
    return list3

# Function to find number of students who play neither cricket nor badminton

def ncb(list1 , list2 , list3):
    list4 = difference(list1 , union(list2, list3))
    return len(list4)

#Function to find number of students who play cricket and football but not badminton

def cfnb(list1 , list2 , list3):
    list4 = difference(intersection(list1 , list2) , list3)
    return len(list4)

    

# Main programme
# List of total students
total = []
n = int(input(" \n Enter  number of students:"))
print ('Enter roll number of ', n , 'students:')
for i in range (0, n):
    e = input()
    total.append(e)
print ("List of students in the class :" + str(total))

# List of students playing cricket
cric = []
n = int(input(" \n Enter  number of students who play cricket:"))
print ("Enter roll number of ", n , "students:")
for i in range (0, n):
    e = input()
    cric.append(e)
cric = duplicate(cric)
print ("List of students who play cricket :" + str(cric))

# List of students playing badminton
baddy = []
n = int(input(" \n Enter  number of students who play badminton:"))
print ("Enter roll number of ", n , "students:")
for i in range (0, n):
    e = input()
    baddy.append(e)
baddy = duplicate(baddy)
print ("List of students who play badmiton :" + str(baddy))

# List of students playing football
fb = []
n = int(input(" \n Enter  number of students who play football:"))
print ("Enter roll number of ", n , "students:")
for i in range (0, n):
    e = input()
    fb.append(e)
    fb = duplicate(fb)
print ("List of students who play football :" + str(fb))

# Main required output
print (" \n List of students who play both cricket and badminton", intersection(cric, baddy))
print (" \n List of students who play cricket and badminton but not both:" , symdiff(cric , baddy))
print (" \n List of students who play neither cricket nor badminton:" , ncb(total ,cric , baddy))
print (" \n Number of students who play cricket and football but not badminton:" , cfnb(cric , fb , baddy))
