#Sorteio de nomes
import random

partipante_um = str(input('Primeiro aluno:'))
participante_dois = str(input('Segundo aluno:'))
partipante_tres = str(input('Terceiro aluno:'))
partipante_quatro = str(input('Quarto aluno:'))
partipante_quinto = str(input('Quinto aluno:'))

lista = [partipante_um, participante_dois, partipante_tres, partipante_quatro, partipante_quinto]

escolhido = random.choice(lista)

print('O aluno escolhido foi {} .'.format(escolhido))