print("-------------inicio-----------")
print("\n")
# entrada de dados 
nota1 = float (input("Informe a primeira nota: "))
while nota1 > 10 :
    print ("Nota invalida ")
    nota1 = float (input("Informe a primeira nota: "))
nota2 = float (input("Informe a segunda nota: "))
while nota2 > 10 :
    print ("Nota invalida ")
    nota2 = float (input("Informe a segunda nota: "))
nota3 = float (input("Informe a terceira nota: "))
while nota3 > 10 :
    print ("Nota invalida ")
    nota3= float (input("Informe a terceira nota: "))
media = float ((nota1 + nota2 + nota3)/3)
# calcula media 
print ("sua media e ", media )
# saida de dados 
if media >= 6 :
    print("reprovado")
else :
    if media >= 5:
        print ("conselho")
    else :
        print("reprovado")
print("----------Fim------------")
