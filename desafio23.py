num1 = int(input("entre com o primeiro numero: "))
num2 = int(input("entre com o segundo  numero: "))
pergunta = (input ("entre com com a operacao desejada  a soma b mutiplicar c maior d menor  "))
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
   print(soma(num1,num2)) 
if pergunta == 2:
   print(mult(num1,num2)) 
if pergunta == 3:
   print(maior(num1,num2)) 
if pergunta == 4:
   print(menor(num1,num2)) 






