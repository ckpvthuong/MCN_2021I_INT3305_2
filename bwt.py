
# input: - str: string
# output: - [L,index], L: string, index: int
def transform(str):
  
  n = len(str)
  listShift = [str]

  for i in range(n-1):
    prerow = listShift[-1]
    nextrow = prerow[1:] + prerow[0]
    listShift.append(nextrow)

  sortedList = sorted(listShift)

  L=""
  index=None
  for i in range(n):
    row = sortedList[i]
    L+= row[-1]
    if row == str: index = i  
  
  print(L,index)
  return [L,index]

# input: - [L,index], L: string, index: int
# output: - str: string
def recover(input):
  L=input[0]
  index=input[1]
  
  n = len(L)
  F = sorted(L)

  output=""+F[index]
  output = recurse(F,L,index,output)
  print(output)
  return output 
  
def recurse(F,L,index, output):
  n = len(F)
  if len(output) == n: return output
  c=F[index]

  count1 = 0
  for i in range(index+1):
    if F[i] == c: count1+=1

  count2 = 0
  for i in range(n):
    if c==L[i]:
      count2 += 1
      if count2 == count1:
        index = i
        output += F[i]
        break

  return recurse(F,L,index,output)

output = transform("burrow-wheeler transform")
recover(output)