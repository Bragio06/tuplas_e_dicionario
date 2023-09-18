tupla_numeros = (1,23,45,6,78,9,8,76,)
tupla_vazia = ()
for x in tupla_numeros:

    if x % 2 == 0:
        tupla_vazia += (x,)
        
print(tupla_vazia)