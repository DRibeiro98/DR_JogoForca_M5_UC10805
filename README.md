# Projeto: Jogo da Forca

## 📝 Definição do Problema
Criar um programa/jogo em Python onde o utilizador seja capaz de descobrir uma palavra com palpites unicos e sucessivos de letras dentro de um limite de tentativas.

## 🎯 Objetivo do Jogo
Permitir que o utilizador descubra uma palavra secreta, adivinhando letra a letra de forma individual e consecutiva antes de se acabarem as suas vidas/tentativas a que tem direito.

## 📑 Regras Principais
**1.** A Palavra secreta é apresentada escondida sob a forma de traços P/ex. para uma palavra com 5 letras: ( **_ _ _ _ _** )\
**2.** Através do teclado o utilizador irá introduzir uma letra de cada vez\
**3.** Se a letra indicada pelo utilizador existir o programa irá revelar os espaços correspondentes que contenham essa letra.\
**4.** Se a letra indicada pelo utilizador **não** existir na palavra secreta, este irá perder 1 vida/tentativa

## 🎖️ Condições de Vitória e Derrota
- **Vitória->** Todas as letras da palavra secreta são descobertas antes do utilizador esgotar as suas vidas
- **Derrota->** O utilizador perdas as suas vidas antes de descobrir todas as letras da palavra secreta

## 🛠️ Limitações e Restrições Técnicas
- **Número de Vidas:** Máximo de 6 vidas(como tipico jogo da forca: 1x cabeça, 1x tronco, 2x braços e 2x pernas)
- **Tipo de Input:** Apenas caracteres alfabéticos irão ser considerados válidos independentemente de serem maiusculos ou minúsculos.
- **Ambiente:** Código será realizado em Python e executado em modo consola/terminal