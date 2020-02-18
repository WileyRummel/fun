l = ['a',2,4,'C',66,'D',43]

def filter_list(l):
  'return a new list with the strings filtered out'
  nums = []
  for x in l:
      if isinstance(x, int):
          nums.append(x)
          print(nums)
      else:
          print("not num   - " + x )
          pass
  return nums

filter_list(l)
