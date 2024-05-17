l1 =[2,3,6,1,8,9,5]
leng = len(l1)

for i in range(leng):
  min_index = i
  for j in range(i+1,leng):
    if l1[min_index]> l1[j]:
      min_index= j
  l1[min_index],l1[i] = l1[i],l1[min_index]
print(l1)
      