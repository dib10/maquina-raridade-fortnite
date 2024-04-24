import random
import os
from art import logo

máquina = {
    "Grudante":["incomum"],
    "Combustível":["comum"],
    "Atadura":["comum"],
    "Kit Médico":["incomum"],
    "Poção de escudo pequena":["incomum"],
    "maçã":["incomum"],
    "Granada de Onda de Choque":["épica"],
    "Cogumelo":["incomum"],
    "Alface":["comum"],
    "Vara de pesca":["comum"],
    "Cura-Cura":["rara"],
    "Espingarda guardião do portão": ["comum","incomum","rara","épica","lendária"],
    "SMG Arauto": ["comum","incomum","rara","épica","lendária"],
    "Rifle A.E caçada lunar": ["comum","incomum","rara","épica","lendária"], 
    "Rifle de Assalto Belicoforjado": ["comum","incomum","rara","épica","lendária"], 
    "Escopeta Martelo": ["comum","incomum","rara","épica","lendária"],
    "Espingarda Automática Frenética": ["comum","incomum","rara","épica","lendária"], 
    "RA Nêmesis": ["comum","incomum","rara","épica","lendária"],
    "SMG Rajada de Trovão": ["comum","incomum","rara","épica","lendária"],
    "Rifle de Precisão do Ceifador": ["comum","incomum","rara","épica","lendária"],
    "Pistola Sentinela": ["comum","incomum","rara","épica","lendária"],
    "Canhão de Mão": ["comum","incomum","rara","épica","lendária"]
}

def maquina_sortida():
    item = random.choice(list(máquina.keys()))
    raridade = random.choice(máquina[item])
    raridade_colorida = tratar_cores_raridade(raridade)

    print(f"Você recebeu o item {item} de raridade {raridade_colorida}")

def tratar_cores_raridade(raridade):
    if raridade == "comum":
        return f"\033[90m{raridade}\033[0m"  # Cinza
    elif raridade == "incomum":
        return f"\033[32m{raridade}\033[0m"  # Verde
    elif raridade == "rara":
        return f"\033[34m{raridade}\033[0m"  # Azul
    elif raridade == "épica":
        return f"\033[35m{raridade}\033[0m"  # Roxo
    elif raridade == "lendária":
        return f"\033[33m{raridade}\033[0m"  # Amarelo
    

print(logo)
print("Olá, eu sou uma máquina com defeito, você pode comprar um item aleatório por 100 de ouro!🦑")
ouro = random.randint(1000,5000)
while True:
    print(f"Você possui \033[33m{ouro}\033[0m de ouro")
    print("Deseja comprar um item aleatório? (s/n): ")
    resposta = input().lower()
    if resposta == "s":
        if ouro >= 100:
            ouro -= 100
            os.system('cls')  # limpar o terminal
            maquina_sortida()
        else:
            print("\033[31mVocê não tem ouro suficiente!\033[0m")
            break
    else:
        break
print("Obrigado por usar a máquina aleatória")