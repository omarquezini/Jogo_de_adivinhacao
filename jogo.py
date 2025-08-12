import random

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'

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
print(F" {GREEN}(1) - fácil(o_o)")
print("")
print(f" {YELLOW}(2) - medio(0_0)")
print("")
print(f" {RED}(3) - difícil(X_X)")
print(f" ")

level = int(input("escolha um nivel: "))

if level <= 1:
    print("")
    print("20 tentativas (fácil, igual a sua vida, provavelmente).")
    totalTentativas = 20

elif level == 2:
    print("")
    print("10 tentativas (essa dificuldade combina com você).")
    totalTentativas = 10

elif level ==3:
    print("")
    print("5 tentativas (pra quem ta querendo se-provar?) .")
    totalTentativas = 5

else:
    print("")
    print("### BUG ENCONTRADO!!! ### 1 tentativas ### ")
    totalTentativas = 1

for rodada in range(1, totalTentativas + 1):
    print("")
    print("Tentativa {} de {}".format(rodada, totalTentativas))
    chute_str = input("Digite um número entre 1 a 100: ")
    chute = int(chute_str)

  
    if chute < 1 or chute > 100:
        print("")
        print(F"{RED}Número inválido. O número deve ser entre 1 e 100 idiota.")
        continue  

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if acertou:
        print(f"{GREEN}Você acertou e fez {pontos}!")
        break  
    else:
        if maior:
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif menor:
            print("Você errou! Seu chute foi menor que o número secreto.")
    
    pontosPerdidos = abs(numeroSecreto - chute)
    pontos -= pontosPerdidos  

print("")
print("Fim de jogo! O número era", numeroSecreto)