def work(ar, num):
  #the input is gonna be an array of numbers
  #define a counter, then take the total divide in half and keep adding until total is larger than half
  ar = sorted(ar, reverse=True)
  look = sum(ar)// 2
  ret = 0 
  total = 0

  while ret < num:
    total += ar[ret]
    #checks
    if total > look:
      return ret + 1

    ret += 1

num = int(input())
ar = list(map(int, input().split()))

print(work(ar, num))