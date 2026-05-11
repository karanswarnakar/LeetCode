import math

def separateDigits(inputArr, outputArr):
    for i in inputArr:
        a = i/10
        if math.floor(a) == 0:
            a = i*1
        b = str(a)
        c = b.split(".")
        for j in c:
            outputArr.append(int(j))

        
    print("Output:",outputArr)
nums = [13,25,83,77]
arr = []    
separateDigits(nums,arr)