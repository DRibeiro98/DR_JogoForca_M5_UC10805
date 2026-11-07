# Módulo responsável pela Lógica e mecânica do Jogo da Forca
import random

from palavras import palavrasSecretas

def obter_palavra_secreta():
    """Função para Escolher um palavra aleatória da lista de palavras"""
    return random.choice(palavrasSecretas)

def palavra_escondida(palavraSecreta):
    """Função que troca a palavra secreta por traços -> _"""
    palavra = "_ " * len(palavraSecreta)
    return palavra

def obter_tentativa():
    """Função que irá pedir e validar o input inserido pelo utilizador"""
    valido = False

    while not valido:
        tentativa = input("Introduz apenas uma letra ou escreve sair para terminar: ").strip().lower()

        if tentativa == "sair":
            return tentativa
        elif len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, Introduz apenas uma letra válida.")
        else:
            valido = True

    return tentativa

    

