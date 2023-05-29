num1 = int(input("entre com o primeiro numero: "))
num2 = int(input("entre com o segundo  numero: "))
pergunta = (input ("entre com com a operacao desejada  1 soma 2 mutiplicar 3 maior 4 menor  "))
def soma (num1 , num2):
    total = num1 + num2
    return total
def mult (num1 , num2):
    total = num1 * num2
    return total
def maior (num1, num2):
    total = max(num1,num2)
    return total
def menor (num1, num2):
    total = min(num1 , num2)
    return total
if pergunta == 1:
   print(soma()) 
if pergunta == 2:
   print(mult(num1,num2)) 
if pergunta == 3:
   print(maior(num1,num2)) 
if pergunta == 4:
   print(menor(num1,num2)) 






