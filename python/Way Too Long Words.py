#look at the input
def work(word):
  #find some way to check the len of the word
  le = len(word)

  #if the len of the word is longer than 10 
  if le > 10:
    #we just return
    return word[0] + str(le - 2) + word[-1]
  return word


n = int(input())

for _ in range(n):
  word = input()
  print(work(word))