l1 = [1,2,3,2,4]
leng = len(l1)
for i in range(leng):
  for j in range(i+1,leng):
    if l1[i]==l1[j]:
      l1.pop(j)
      leng -=1
      break
      #j +=1
print(l1)