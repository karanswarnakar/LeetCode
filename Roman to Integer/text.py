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
def romanToNum(roman="XIV"):
    
    org = []
    number = []  
    
    b = roman[-2:]
    print(b)
    res = 0
    for i in romanNum:
        for j in roman:
            if i == j:
                print(f"Match: {j} -> {romanNum[i]}")
                res = romanNum[i] + res
    print(res)           
romanToNum()  
  