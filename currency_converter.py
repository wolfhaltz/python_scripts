#Currency converter
#PT - Conversor de moedas

#Btw, the values are hypothetical.
#Consider US$1,00 = R$3,27

#PT - A propósito, os valores são hipotéticos
#     Considere US$1,00 = R$3,27

cotation = 3.27

real = float(input('How many reais do you have in your pocket?'))
dolar = real/3.27

print('With R${:.2f} you can buy US${:.2f}').format(real,dolar)