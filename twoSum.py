


def twoSum(arr, S):

  sums =[]

  for i in range(0, len(arr)):

    for j in range(i+1, len(arr)):
      
      if arr[i] + arr[j] == S:
        sums.append([arr[i], arr[j]])


  return sums

print(twoSum([1,2,3,4], 5))