sal = float(input("Informe o salario: "))
if sal > 8250:
    salarioporcento = (sal*10)/100
    novosal = sal + salarioporcento
    print( "O seu novo salario e de: ", novosal)
else:
    salarioporcento = (sal*15)/100
    novosal = sal + salarioporcento
    print( "O seu novo salario e de: ", novosal)