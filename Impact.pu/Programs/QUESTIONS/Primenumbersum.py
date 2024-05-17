count = 0
list=[]
n = int(input())
for num in range(1 ,n+1):
   if num > 2:
       for i in range(2, num):
           if (num % i) == 0:
               break
           else:
               list.append(num)
print(list)
for i in list:
    for j in list:
        count = i +j
        if i==j:
            break
        elif count == 34:
           print(i,j)