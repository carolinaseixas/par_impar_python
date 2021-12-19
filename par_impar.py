# Jogo do par ou ímpar
# Jogo contra a máquina no qual a máquina sorteia um número, o usuário escolhe par ou ímpar e descobre se acertou

import re
import random

maquina = random.randint(1,11)

print("A maquina escolheu um numero inteiro entre 1 e 10. Voce acha que eh par ou impar?")
escolha = input('Digite [P] para par ou [I] para impar\n')


#Verificando se o input é 'P', 'p', 'I' ou 'i' e, caso não for, pedindo para tentar novamente
while len(escolha) > 1 or re.match("[^pPiI]",escolha) :
    escolha = input('Por favor, digite a letra [P] para par ou a letra [I] para impar\n')

#Se o usuario acertou, ou seja, escolheu 'P' ou 'p' para um número par ou 'I' ou 'i' para um número ímpar...
if (maquina % 2 == 0 and re.match("[pP]",escolha)) or (maquina % 2 != 0 and re.match("[iI]",escolha)) :
    print("Parabens, voce acertou! O numero escolhido pela maquina foi " + str(maquina) + ".")
#Se o usuario errou, ou seja, escolheu 'P' ou 'p' para um número ímpar ou 'I' ou 'i' para um número par...
else :
    print("Voce errou... O numero escolhido pela maquina foi " + str(maquina) + ".")

print("Jogo encerrado")
