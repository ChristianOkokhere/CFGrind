#given a number partition the kilos into two even numbers if possible return true if not return false
 
 
def divide(weight):
  #this one is easy its a good primer, just check if the thing is even or odd if there is an even number than we can gauntee that we can split it into two even numbers odd numbers this is not the caes
  if weight % 2 == 0 and weight !=2:
    return True
  return False
  
 
weight = int(input())
result = divide(weight)
print("YES" if result else "NO")