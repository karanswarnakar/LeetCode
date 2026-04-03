def TwoSum(arr, target):
    for i in range(len(arr)-1):
        if arr[i] + arr[i+1] == target:
            print([i ,i+1])
            
TwoSum([1,2,3,9], 12)


    