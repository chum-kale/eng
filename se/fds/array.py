#/usr/bin/env python

# input array
a = [87, -1, 76, 76, 34]

# sum of all numbers in array
sum = 0
for i in a:
    if i == -1:
        continue
    sum = sum + i
print("sum: " + str(sum))

# length of an array
len = 0
for i in a:
    len += 1
print("len: " + str(len))

# average marks
avg = sum/len
print("average: " + str(avg))

# minimum and maximum marks
min = 100
max = 0
for i in a:
    if (i == -1):
        continue
    if (i > max):
        max = i
    if (i < min):
        min = i
print("min: " + str(min))
print("max: " + str(max))

# number of absent students
absent = 0
for i in a:
    if (i == -1):
        absent += 1
print("absent: " + str(absent))

# number of students with same marks
i = 0
while i < len:
    if (a[i] == -1):
        i += 1
        continue
    count = 0
    j = i + 1
    while j < len:
        if a[i] == a[j]:
            count += 1
        j += 1
    print("frequency of " +  str(a[i]) + " is " + str(count))
    i += 1
