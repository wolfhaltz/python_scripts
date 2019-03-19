#O que este algoritmo faz?
#Inverte a ordem do valor colocado no input. Como? Siga-me os bons!

#Deixe o usuário digitar algo:
n = int(input())
#Estabeleça que tmp será n:
tmp = n

ni = 0
#Enquanto maior que 0, faça:
while tmp > 0:
    #Dígito é igual ao valor colocado pelo usuário dividido por 10:
    d=tmp%10 #Supondo que o usuário digite 12, neste ponto, 12%10=1,2
    #ni vezes 10 mais o dígito:
    ni=(ni*10)+d #No exemplo utilizado acima, usando o número 12, nesta etapa seria: ni=(0*10)+1,2
    #Divida o valor obtido numa divisão inteira por 10:
    tmp=tmp//10
print(ni)