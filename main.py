# Ponto de entrada do Programa Jogo da Forca (Main)
from jogo import *

def main():
    """Função principal que irá dar vida ao Jogo da Forca."""

    print("\n!!BEM-VINDO AO JOGO DA FORCA!!\n")
    print("*"*54)
    print("NESTE JOGO NÃO IREMOS USAR ACENTOS NEM O CARACTER -> Ç")
    print("MAAAAAAAAAAAS, SE OS USARES VAIS PERDER VIDAS NA MESMA")
    print("POR ISSO, PRESTA MUITA ATENÇÃO!!!!! ;)")
    print("*"*54)

    # Declaração e atribuição de variáveis de estado do jogo
    palavra_secreta = obter_palavra_secreta()
    palavra_atual = palavra_escondida(palavra_secreta)
    vidas = 6
    esta_ativo = True
    tentativas_dadas = []

    while esta_ativo:
        print(f"\nPalavra: {palavra_atual}")
        print(f"Tens {vidas} vidas.\n")
        print(f"Estas foram as tuas tentativas-> {mem_tentativas(tentativas_dadas)}")

        tentativa = obter_tentativa()
        
        #Condição para verificar se o jogador quer sair do jogo
        if tentativa == "sair":
            esta_ativo = False
            print("OBRIGADO!! ATÉ À PRÓXIMA")
            break

        #Condição para verificar se a tentativa é repetida
        if tentativa in tentativas_dadas:
             print(f"\nJÁ TENTASTE A LETRA {tentativa}, ESCOLHE OUTRA.")
             continue
        
        #Regista à "memória" criada a tentativa do utilizador
        tentativas_dadas.append(tentativa)
        
        #Condições para verificar se existe ou não a letra introduzida pelo utilizador e gerir as vidas
        if tentativa in palavra_secreta:
                print(f"\nBOA!!! A LETRA {tentativa} FAZ PARTE DA PALAVRA!!")
                palavra_atual = atualiza_palavra_escondida(palavra_secreta, palavra_atual, tentativa)
        else:
            print(f"\nOOOOOOH :( {tentativa} NÃO FAZ PARTE DA PALAVRA)")
            print("IRÁS PERDER 1 VIDA!!!! MAIS SORTE NA PRÓXIMA :) !!!")
            vidas = vidas - 1

        #Condições para verificar o término do jogo
        if "_" not in palavra_atual:
            print("\nPARABÉNS DESCOBRISTE TODAS AS LETRAS :) !!!!!")
            print(f"A PALAVRA SECRETA ERA {palavra_secreta}")
            esta_ativo = False
        elif vidas == 0:
            print("\nGAME OVER!!! :( ACABARAM AS TUAS VIDAS!!")
            print(f"A PALAVRA SECRETA ERA: {palavra_secreta}")
            esta_ativo = False

main()

