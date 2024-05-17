def merge_alternatively(str1,str2):
    longstr = str1 if len(str1)>len(str2) else str2
    length = len(longstr)
    str3 = ""
    for i in range(length):
        try:
            str3 += str1[i] + str2[i] 
        except:
            str3 += longstr[i]
            
    return str3
str1 = input()
str2 = input()

print(merge_alternatively(str1,str2))