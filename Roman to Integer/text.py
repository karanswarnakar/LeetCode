romanNum = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}
# XXIV
# 10+10+1+5 = 26
# 10+10+4
# 4 and 9 NEED TO FIX 

def arraySum(arr):
    result = 0
    for i in arr:
        result+=i
    print(result) 

def romanToNum(roman="LVXIV"):
    
    org = []
    number = []  
    formation = False
    
    
    b = roman[-2:]
    m = roman[:-2]
    
    print("Fprmation: ",b)
    
    res = []
    if b == "IV":
        formation = True
        res.append(4)
        print("4 is Added to array")
    elif b == "IX":
        formation = True
        res.append(9)
        print("9 is Added to array")
    
    print(m)
    for i in romanNum:
       
        if formation:
             for j in m:
                if i == j:
                    print(f"Match: {j} -> {romanNum[i]}")
                    res.append(romanNum[i])
        else:
            for j in roman:
                if i == j:
                    print(f"Match: {j} -> {romanNum[i]}")
                    res.append(romanNum[i])
                
    arraySum(res)           
romanToNum()  
  