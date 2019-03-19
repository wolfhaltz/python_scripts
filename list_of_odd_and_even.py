#EN
    #Single list separating odd and even values
    #and show them in ascending order

#PT
    #Lista única que separa valores de pares e ímpares
    #e mostre-os em ordem crescente


#EN
    #First of all, start the vector with two lists,
    #one for the pairs, and one for the odd ones:

#PT
    #Primeiro, inicie o vetor com duas listas,
    #uma para os pares, e outra para os ímpares:
list_of_numbers = [[], []]

value = 0

for c in range(1,5):
    value = int(input('Type a number:'))
    if value%2 == 0:
        list_of_numbers[0].append(value)
    else:
        list_of_numbers[1].append(value)
        
print('-='*30)
list_of_numbers[0].sort()
list_of_numbers[1].sort()

print('Even numbers are:', list_of_numbers[0])
print('Odd numbers are:', list_of_numbers[1])