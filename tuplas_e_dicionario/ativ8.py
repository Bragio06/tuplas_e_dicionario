tupla_numeros = (1,23,45,6,78,9,8,76,)

numero = int(input("qual numero você que verificar: "))

for i in tupla_numeros:
    if i == numero:
        print(f"esse tupla tem  {i}")
        break
          
