def largestNumber(a):
       
    if len(a)==1:  
        return str(a[0])
    
    for i in range(len(a)):
        a[i]=str(a[i])
  
    for i in range(len(a)):
        for j in range(1+i,len(a)):
            if a[j]+a[i]>a[i]+a[j]:
                a[i],a[j]=a[j],a[i]
    
    result=''.join(a)
    
    if(result=='0'*len(result)):
        return '0'
    else:
        return result
         
         

a = [3,30,34,5,9]
print(largestNumber(a))