#EN - Sine, Cosine and Tangent
#       Given any angle, show the sine, cosine, and tangent

#PT - Seno, Cosseno e Tangente
#       Dado um ângulo qualquer, mostre o seno, cosseno e tangente
from math import tan, radians, sin, cos
angle = float(input('Choose the angle that you deserve:'))

sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print('Angle has sine of {:.2f}, cosine of {:.2f} and tangent of {:.2f}').format(sine, cosine, tangent)
