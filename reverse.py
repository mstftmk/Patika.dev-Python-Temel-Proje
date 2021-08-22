liste1 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(x):
  newList=[]
  for i in x:
    newList.append(i[::-1])
  return newList[::-1]

print(reverse(liste1))
