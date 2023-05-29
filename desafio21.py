num1 = int(input("entre com o primeiro numero"))
num2 = int(input("entre com o segundo numero"))
num3 = int(input("entre com o terceiro numero"))

def maior (num1,num2, num3) :
    if num1 > num2 and num3:
        print("numero maior ", num1)
        return num1
    if num2 > num2 and num3 :
        print("numero maior ", num2)
        return num2
    if num3 > num1 and num2 :
        print("numero maior ", num3)
        return num3
    

print(maior(num1, num2, num3))

