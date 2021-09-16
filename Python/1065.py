def hansu(num):
  h = 0
  for i in range(1, num+1):
    if i < 100:
      h += 1
    else:
      nums = list(map(int, str(i)))
      if nums[0] - nums[1] == nums[1] - nums[2]:
        h += 1
  return h

print(hansu(int(input())))