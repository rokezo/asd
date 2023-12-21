def suma (massiv):
    total = 0
    for i in range(len(massiv)):
        total += massiv[i]
    return total 


def seredne(massiv, suma):
    return suma/len(massiv)





start = int(input('enter number one: '))
final = int(input('enter number two: '))
parni = []
neparni = []
kratne = []
for i in range(start, final):
    if i %2 == 0:
        parni.append(i)
    else:
        neparni.append(i)
    if i %9 == 0:
        kratne.append(i)


sumaparni = suma(parni)
sumaneparni = suma(neparni)
sumakratne = suma(kratne)

seredparne = seredne(parni,sumaparni)
seredneparne = seredne(neparni, sumaneparni)
serednekratne = seredne(kratne, sumakratne)

print(parni, sumaparni, seredneparne)

print(neparni, sumaneparni, seredneparne)

print(kratne, sumakratne, serednekratne)

        
        