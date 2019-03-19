#EN
#What this algorithm does?
#Reverses the order of the value placed in the input. As? Follow me the good ones!

#PT
#O que este algoritmo faz?
#Inverte a ordem do valor colocado no input. Como? Siga-me os bons!

n = int(input())
tmp = n
ni = 0

while tmp > 0:
    d=tmp%10
    ni=(ni*10)+d
    tmp=tmp//10
print(ni)