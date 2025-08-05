import random

print("[]=====================================[]")
print("[]        jogo de adivinhação          []")
print("[]            O_MARQUEZINI             []")
print("[]=====================================[]")
print(" ")
print(" ")


numeroSecreto = random.randrange(0, 100)

totalTentativas = 0
pontos = 999

print("qual o nivel de dificuldade? ")
print(" ")
print("(1) - fácil(o_o) (2) - medio(0_0) (3) - difícil(X_X)")
print(" ")

level = int(input("escolha um nivel: "))

if level <= 1:
    print("20 tentativas (fácil, igual a sua vida, provavelmente).")
    totalTentativas = 20

elif level == 2:
    print("10 tentativas (essa dificuldade combina com você).")
    totalTentativas = 10

elif level ==3:
    print("3 tentativas (pra quem ta querendo se provar?) .")
    totalTentativas = 3

else:
    print("### BUG ENCONTRADO!!! ### 1 tentativas ### ")
    totalTentativas = 1

for rodada in range(1, totalTentativas + 1):
    print("Tentativa {} de {}".format(rodada, totalTentativas))
    chute_str = input("Digite um número entre 1 a 100: ")
    chute = int(chute_str)

  
    if chute < 1 or chute > 100:
        print("Número inválido. O número deve ser entre 1 e 100.")
        continue  

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if acertou:
        print(f"Você acertou e fez {pontos}!")
        break  
    else:
        if maior:
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou! Seu chute foi menor que o número secreto.")
    
    pontosPerdidos = abs(numeroSecreto - chute)
    pontos -= pontosPerdidos  
    
print("Fim de jogo! O número era", numeroSecreto)