# arr = [1,2,3,4]

# for i in range(0,4):
#     print(arr[i])
    
# for i in arr:
#     print(i)

# def TwoSum(arr, target):
#     i=0
#     while(arr):
#        if i == len(arr):
#            break
#        print(arr[i])
#        i = i + 1
            
            
# TwoSum([1,2,3,9], 12)

def TwoSum(arr, target):
    arr.sort()
    for i in arr:
        for j in arr:
            if i == j:
                continue
            y = i + j
            if y == target: 
                print(i,j)
                return
            
                
            
TwoSum([1,2,3,9], 6)


# def TwoSum(arr, target):
#     arr.sort()
#     for i in arr:
#         for j in arr:
#             y = i + j
#             if y == target: 
#                 if i > j or i < j:
#                     print(i,j)
#                     return
            

# TwoSum([1,2,3], 6)   