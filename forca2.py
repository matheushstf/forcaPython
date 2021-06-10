import os

#Desenvolvedores = Matheus Stefanello & Tomas Biasotto

#FUNÇÕES
def inicio():
    print('***********')
    print('\nJOGO DA FORCA \n')
    print('***********')
    input('<-- enter -->')


#GAME LOOP
while True:
   
    #LISTAS
    letrasCertas = []
    letrasErradas = []
    dicas = []
    numDica = -1

    #INICIO
    os.system('cls')
    inicio()

    #JOGADORES
    jogador = str(input('Apresente-se, JOGADOR --> ')).upper()
    competidor = str(input('Apresente-se, COMPETIDOR --> ')).upper()
    palavra = str(input(f'Escolha uma palavra, {jogador} --> ')).upper()
    os.system('cls')

    #TRANSFORMANDO A PALAVRA
    palavraArray = list(palavra)
    palavraCripto = list((len(palavraArray) * '_'))
    os.system('cls')

    #PEDINDO DICAS
    for i in range(1,4):
        dicas.append(str(input(f'Dê a {i}ª dica -> ')))
        os.system('cls')

    while len(letrasCertas) < len(palavraArray) and len(letrasErradas) < 5:
        print(palavraCripto)
        print(f'\nERROS -----------------> {len(letrasErradas)}/5')
        print(letrasErradas, '\n')
        print('''
        digite:
        [1] - para <-JOGAR->
        [2] - para <-DICAS->
        ''')
        option = input(f'escolha, {competidor} --> ')
        os.system('cls')

        while option == '1':
            print(palavraCripto)
            letra = input(f'chute uma letra, {competidor} --> ').upper()

            for i in range (0, len(palavraArray)):
                if letra == palavraArray[i]:
                    palavraCripto[i] = letra
                    letrasCertas.append(letra)
            if letra not in palavraArray:
                letrasErradas.append(letra)
            
            print(palavraCripto)
            os.system('cls')
            option = '0'

        while option == '2':
            try: 
                numDica = numDica + 1
                print(f'DICA --> {dicas[numDica]} \n')
                option = '0'
            except:
                print('SEM + DICAS')
                option = '0'

    #DECIDINDO VENCEDOR
    if len(letrasErradas) >= 5:
        vencedor = jogador
        perdedor = competidor
        print(f'''
        >{jogador}< 
        VENCEU!!
        ---------
        A PALAVRA
        -- ERA --
        ---------
        > {palavra} <
        ''')
    else:
        vencedor = competidor
        perdedor = jogador
        print(f'''
        >{competidor}< 
        VENCEU!!
        ---------
        A PALAVRA
        -- ERA --
        ---------
        > {palavra} <
        ''')

    #HISTORICO DE JOGOS
    log = open('historico.txt', 'a')
    log.write(f'Vencedor - {vencedor} | Perdedor - {perdedor} | Palavra - {palavra}\n')
    historico = open('historico.txt', 'r')
    dados = historico.read()
    print('\n', dados)

    input('<aperte <ENTER> para seguir>')
    os.system('cls')

    print('''
    --FIM DE JOGO--
    [1] --> jogar novamente
    [2] --> sair
    ''')
    escolha = str(input('escolha --> '))
    if escolha == '2':
        break

