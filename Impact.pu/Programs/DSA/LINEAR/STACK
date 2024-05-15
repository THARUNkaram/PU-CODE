s=[]
cap=5
top=0
bottom=0

def pushstk(num):
  global top
  global s
  if top == cap:
    print("stack is full")
    return
  s.append(num)
  top +=1 
def popstk():
  global top
  if top == bottom:
    print("stack is empty")
    return
  print(f"{s[top-1]} is popped out")
  top-=1
def printlist():
  if top == bottom:
    print("stack is empty")
    return
  for i in range(top-1,-1,-1):
    print(s[i])
if __name__ == "__main__":
  pushstk(10)
  pushstk(11)
  pushstk(12)
  pushstk(13)
  pushstk(14)
  print(printlist())
  popstk()
  popstk()
  popstk()

print(s)