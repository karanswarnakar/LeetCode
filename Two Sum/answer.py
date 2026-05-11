def TwoSum(arr, target):
    arr.sort()
    for i in arr:
        for j in arr:
            y = i + j
            if y == target: 
                print([arr.index(i),arr.index(j)])
                return
          
a = int(input("Enter Range: "))                
c = []
target = int(input("Enter Target Value: ")) 
for i in range(0,a):     
    b = int(input(f"Enter Position {i}: "))     
    c.append(b)
    
TwoSum(c, target)