# Projeto: Jogo da Forca

## 📝 Definição do Problema 
Criar um programa/jogo em Python onde o utilizador seja capaz de descobrir uma palavra com palpites únicos e sucessivos de letras dentro de um limite de tentativas.

## 🎯 Objetivo do Jogo
Permitir que o utilizador descubra uma palavra secreta, adivinhando letra a letra de forma individual e consecutiva antes de se acabarem as suas vidas/tentativas a que tem direito.

## 📑 Regras Principais
**1.** A Palavra secreta é apresentada escondida sob a forma de traços, por exemplo, para uma palavra com 5 letras: ( **_ _ _ _ _** )\
**2.** Através do teclado o utilizador irá introduzir uma letra de cada vez\
**3.** Se a letra indicada pelo utilizador existir o programa irá revelar os espaços correspondentes que contenham essa letra.\
**4.** Se a letra indicada pelo utilizador **não** existir na palavra secreta, este irá perder 1 vida/tentativa\
**5.** Letras com acento ou o "ç"/"Ç"  são inputs válidos para o sistema, mas **NÃO PARA O JOGO**, ou seja, utilizador irá perder uma vida.\
**6.** Caracteres especiais genéricos como "@" ou números irão ser considerados inputs inválidos e irá ser dada uma nova oportunidade ao utilizador sem perder vidas.\
**7.** O utilizador poderá a qualquer momento terminar o jogo, bastando-lhe escrever "sair", sendo aceite o input em qualquer formato, por exemplo, "SAIR", "SaIR"...

## 🎖️ Condições de Vitória e Derrota
- **Vitória->** Todas as letras da palavra secreta são descobertas antes do utilizador esgotar as suas vidas
- **Derrota->** O utilizador perde as suas 6 vidas antes de descobrir todas as letras da palavra secreta

## 🛠️ Limitações e Restrições Técnicas
- **Número de Vidas:** Máximo de 6 vidas(como o típico jogo da forca: 1x cabeça, 1x tronco, 2x braços e 2x pernas)
- **Tipo de Input:** Apenas caracteres alfabéticos irão ser considerados válidos independentemente de serem maiúsculos ou minúsculos.
- **Tratamento de Exceções:** Foi implementado o bloco *try...except* para capturar interrupções forçadas através do "KeyboardInterrupt" e "EOFError", terminando o jogo com uma mensagem de aviso ao utilizador
- **Ambiente:** Código será realizado em Python e executado em modo consola/terminal

## 🖥️ Instruções de Execução
- **Python** deverá estar instalado no computador.
- Deverá ser executado o ficheiro main.py, através do terminal/PowerShell na pasta raiz do projeto
 ### Exemplo(Windows):
 **1.** Abrir terminal/PowerShell\
 **2.** Executar-> cd + (caminho da pasta raiz do projeto)\
 **3.** Executar-> python main.py

---
---

## 📝 Requisitos para o Jogo da Forca

### **Requisitos Funcionais:**
**1.** O sistema deve permitir selecionar uma palavra secreta de forma aleatória a partir de uma lista definida previamente.\
**2.** O sistema deve apresentar a palavra secreta no ecrã sob a forma de traços(Underscore), sendo que cada traço corresponde à letra que falta adivinhar.\
**3.** O sistema deve solicitar ao utilizador a introdução de **um** caractere alfabético de cada vez através do teclado\
**4.** O sistema deverá validar o input introduzido pelo utilizador garantindo que apenas são aceites caracteres alfabéticos válidos, sejam as letras maiúsculas ou minúsculas\
**5.** Em cada tentativa o sistema deverá atualizar o estado da palavra desvendando as letras descobertas/acertadas\
**6.** O sistema deverá gerir o contador de vidas, decrementando uma vida em caso de falha.

### **Requisitos Não Funcionais:**
**1.** O jogo deverá ser executado inteiramente na consola/terminal, com mensagens intuitivas e será totalmente em português.\
**2.** O código-fonte deverá ser escrito seguindo as boas práticas da **PEP 8**.\
**3.** O Programa deverá ter implementado blocos de exceção para evitar que vá abaixo caso o utilizador introduza algum dado inválido ou caso ocorra um erro inesperado.

---
---
## 📈 Fluxograma do Jogo da Forca

![Fluxograma do Jogo da Forca](./diagramas/FluxogramaJogoDaForca.png)
---
---
## 🛖 Estrutura do Projeto e Funções Principais
- **main.py:** Ponto de entrada do Programa -> Gere o fluxo principal de execução do jogo
- **jogo.py:** Lógica principal e a mecânica do jogo -> Inclui as funções responsáveis por validar inputs do utilizador, por verificar as tentativas, gerir o contador de vidas e atualização do ecrã
- **palavras.py:** Módulo de dados com a lista de palavras secretas. -> Dedicado exclusivamente a guardar a lista de palavras para a seleção da palavra secreta