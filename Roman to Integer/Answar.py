romanNum = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}
genarate = {}


for i in range(1, 11):
    for j in romanNum:
        if i == 1:
            print(romanNum[0])
        elif i == 2:
            print(romanNum[0],romanNum[0])
        elif i == 3:
            print(romanNum[0],romanNum[0],romanNum[0])
        elif i == 4:
            print(romanNum[0],romanNum[1])
        elif i == 5:
            print(romanNum[1])
        elif i == 6:
            print(romanNum[1],romanNum[0])  
        elif i == 7:
            print(romanNum[0],romanNum[0],romanNum[0])
        elif i == 8:
            print(romanNum[1],romanNum[0],romanNum[0],romanNum[0])
        elif i == 9:
            print(romanNum[0],romanNum[3])
        
        