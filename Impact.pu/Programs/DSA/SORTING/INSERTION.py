### insertion sort
'''def insertionsort(l1):
  for i in range(1,len(l1)):
    key = l1[i]
    j = i-1
    while j>=0 and key <l1[j]:
      l1[j+1] = l1[j]
      j -=1
    l1[j+1]=key
  print(l1)
  
l1=[7,37,5,6,9,2,4,1,6,7]
insertionsort(l1)
'''
### using slow and fast insted of i and j
def insertionsort(l1):
  fast = 1 
  slow=0
  for fast in range(fast,len(l1)):
    key = l1[fast]
    slow = fast -1
    while (slow >=0 and key <l1[slow]):
      l1[slow+1] = l1[slow]
      slow -=1
    l1[slow+1]=key
  print(l1)
  
l1=[7,37,5,6,9,2,4,1,6,7]
insertionsort(l1)