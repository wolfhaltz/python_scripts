#EN - Legs and hypotenuse
#       Read the length of the opposite and adjacent legs
#       of a right triangle, and, calculate the hypotenuse.

#PT - Catetos e hipotenusa
#       Leia o comprimento do cateto oposto e do adjacente
#       de um triângulo retângulo, e, calcule a hipotenusa.
from math import hypot

opposite_leg = float(input('Length of opposite leg:'))
adjacent_leg = float(input('Length of adjacent leg:'))

#Now you can solve it in twos ways || Agora, você pode resolver de dois jeitos

#Using the calcule: || Usando o cálculo:
# hypotenuse = (opposite_leg ** 2 + adjacent_leg **2) ** (1/2)

#Or you can simple use the library: || Ou você simplesmente pode usar a biblioteca:
hypotenuse = hypot(opposite_leg, adjacent_leg)

print('Hypotenuse is', hypotenuse)

