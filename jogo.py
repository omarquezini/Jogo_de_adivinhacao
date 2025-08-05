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