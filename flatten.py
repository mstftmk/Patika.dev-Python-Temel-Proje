def flatten(x):
  flat_list=[]
  for i in x:
    #looking each item in list
    if type(i) is list:
      #if there is a list inside list, we are going to look inside that sublist too
      for sub_i in i:
        #then append that item in the new flatten list
        flat_list.append(sub_i)
    else:
      flat_list.append(i)
  for i in flat_list:
    #here, we are checking new flatten list if there is a sublist left inside.
    if type(i) is list:
      #if still there is a sublist in flatten list, then do the process again.
      return flatten(flat_list)
  return flat_list

newList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(newList))

