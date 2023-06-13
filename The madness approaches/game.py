import time
import os

def limpaTela():
    os.system('cls')

def linha(vezes,tipo):
    print(tipo * vezes)

def tempo(seg):
    time.sleep(seg)

def espaco(tam):
    print(" " * tam)

def novaLinha():
    print("\n")

def personagem():
    print("""
    Nome: Mayws Jonhson
    Idade: 33 anos
    Peso: 65 KG
    Altura: 1,87m
    Nacionalidade: Inglês com descendência austriaca""")
    while True:
        opcaoPer = str(input('Digite "K" para sair: '))
        if opcaoPer == "K":
            break
        else:
            opcaoError()

def controlesJogo():
    print("""CONTROLES DO JOGO:
          Interatividade pura, escolha utilizando teclado.
          #==================================================================================#
          Aperte "C" na interação para ver as configurações.
          Aperte "P" para ver o personagem.
          Aperte "V" para voltar a uma opção anterior.
          Aperte "K" para voltar ao jogo quando estiver nas configurações ou no personagem..
          #==================================================================================#

          _____________________________________________________________________________________
          Para interagir siga essas regras:
              * Digite apenas A ou B e nada mais, exceto caso queria a configuração.
              * Se a interatividade pedir números então digite-os corretamente.
              * Em alguns momentos terão mini-games para passar de fase, então prepare-se.""")
    p("_____________________________________________________________________________________")
    while True:
        opcaoControle = str(input("Digite a opção que deseja de acordo com as configurações: ")).upper().strip()
        if opcaoControle == "P" or opcaoControle == "V" or opcaoControle == "K":
            break
        else:
            opcaoError()
    if opcaoControle == "P":
        personagem()

def repetirHora(zero,n,pontos,num,vezes):
    for var in range(1,vezes + 1):
        print(zero,n,pontos,num)
        tempo(1)
        num = num + 5

def p(text):
    print(f"{text}")

def opcaoGame(a,b):
    largura = len(a) + 7
    largurab = len(b) + 7
    print("#" * largura)
    print("# A-",a,"#")
    print("#" * largura)
    tempo(2)
    novaLinha()
    print("#" * largurab)
    print("# B-",b,"#")
    print("#" * largurab)
    tempo(3)
    novaLinha()

def escolha(text):
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("#",text,"#")
    print("-----------------------------------------------------------------------------------------------------------------------")

def repetirNum(vezes,intervalo):
    print("PENSE...")
    tempo(1)
    for var in range(1,vezes+1):
        print(var,end =" > ")
        tempo(intervalo)
    print("FIM")

def gameOver():
    linha(10,"=+=")
    print("GAME OVER!")
    linha(10,"=+=")


novaLinha()
linha(50,"##")
print("SEJA MUITO BEM VINDO AMANTE DA LOUCURA AO NOSSO JOGO! ESCOLHA,EXPLORE E MORRA! HAHAHHAHAA!")
linha(50,"##")
tempo(2)

tempo(2)
linha(25, "---")
p("PARA VER AS CONFIGURAÇÕES DO JOGO APERTE 'C' ")
linha(25,"---")
tempo(2)
novaLinha()

p("CARREGANDO.................[//////---] 70%")
tempo(1)
p("CARREGANDO.................[///////--] 80%")
tempo(1)
p("CARREGANDO.................[////////-] 90%")
tempo(1)
p("CARREGANDO.................[//////////] 100%")

tempo(3)
limpaTela()
linha(60,"-")
tempo(1)
print("""Em 1914 inicia-se a primeira guerra mundial da história,
contendo 17 páises confrotado pela França X União Soviética,
um desses páises era a Inglaterra... Meu páis...""")
tempo(8)
linha(60,"-")

novaLinha()
print("MANCHESTER, INGLATERRA...")
tempo(1)
novaLinha()

linha(20,"=+=")
tempo(1)
print('17 de abril de 1925 - Sexta-Feira.... Primavera')
tempo(1)
linha(20,"=+=")

tempo(3)
limpaTela()
repetirHora("0",5,":",10,5)
novaLinha()

p("BIPPPPP!!!!")
tempo(2)
limpaTela()
escolha("""Mayws.. Um homen simples acorda 05:30 e levanta de sua cama piscando lentamente, pega seus ocúlos
e se dirige a cozinha,bebe um copo d'água e pensa no que fazer pela manhã VAMOS VER...""")
tempo(7)
novaLinha()

opcaoGame("FAZER CAFÉ", "BEBER WISKY")

repetirNum(10,1)
novaLinha()
op1 = 0
while True:
    opcao = str(input("QUAL OPÇÃO DESEJA? [A/B]: ")).upper()
    if opcao == "A":
        op1 +=1
        limpaTela()
        escolha("MAYWS FAZ O CAFÉ MAS FICA EM DÚVIDA DO QUE COMER...")
        tempo(1)
        novaLinha()
        opcaoGame("UM PEDAÇO DE PÃO", "UM RESTO DE BOLO FOFO")
        repetirNum(10,1)
        break
    elif opcao == "B":
        op1 +=2
        limpaTela()
        escolha("MAYWS QUER SEU WISKY PARA ACORDAR... COMO BEBER?")
        tempo(1)
        novaLinha()
        opcaoGame("UM COPINHO...", "VIRAR A GARRAFA TODA!")
        repetirNum(10,1)
        break
    else:
        linha("=-=",20)
        print("OPÇÃO ERRADA! TENTE NOVAMENTE!")
        linha("=-=", 20)
def ruaAvenida(opcaoavenida):
        if opcaoavenida == "A":
            escolha("VOCÊ CHEGA NO CEMITÉRIO DE MANCHESTER ÁS 07:15 E BATE SEU PONTO , A MANHÃ PARECE FRIA HOJE...")
            tempo(2)
            novaLinha()
            print("O JOGO ACABOU, OBRIGADO POR TESTAR A BETA! :D")
            return opcaoavenida
        else:
            escolha("MAYWS ESTÁ ANDANDO E VÊ UMA LOJA COM UMA BANCADA DE JORNAIS NO POSTO DE GASOLINA...OPS! VOCÊ TEM £0,25 O QUE ACHA DE UM JORNAL?")
            tempo(3)
            novaLinha()
            opcaoGame("COMPRAR JORNAL", "NÃO COMPRAR E IR LOGO...")
            repetirNum(10,1)

def jornalCarona(opcaojc):
     if opcaojc == "A":
                escolha("O JORNAL VINHA COM ALGUMAS INFORMAÇÕES INRRELEVANTES, MAS A PRINCIPAL ERA SOBRE...")
                tempo(2)
                novaLinha()
                print("""
                    [AQUI ENTRA UM JORNAL]
                """)
                tempo(3)
                novaLinha()
                escolha("MAYWS SE ENTRISTECE AO LER... PESADELOS AINDA-OS ASSOMBRA.. MAYWS SE DIRIGE AO TRABALHO...")
                tempo(2)
                novaLinha()
                print("""
                 [ flashback... alguma coisa tenebrosa]
                """)
                tempo(2)
     else:
        escolha("SEU CHEFE PASSA PARA REABASTECER O TANQUE E O VÊ, ENTÃO LHE OFERECE UMA CARONA ATÉ O TRABALHO...")
        tempo(3)
        novaLinha()
        print("""
        [ AQUI ENTRA UM CARRO]
        """)
        tempo(2)
        opcaoGame("ACEITAR A CARONA","REJEITAR EDUCADAMENTE E IR A PÉ")
        repetirNum(10,1)
        
def caronaAceita(opcaocarona):
    if opcaocarona == "A":
        escolha("MAYWS ENTRA NO CARRO DE SEU CHEFE...")
        tempo(4)
        p("- Bom dia Mayws")
        tempo(3)
        p("> Bom dia")
        tempo(3)
        p("- Que belo sexta, hoje a maxíma é de 10°C")
        tempo(5)
        p("> Sim.. Parece bom.")
        tempo(3)
        p("- Então...")
        tempo(3)
        p("- Como está a vida? Parece cansado...")
        tempo(4)
        p("> Vai normal.. hoje o turno é o mesmo?")
        tempo(3)
        p("- Sim, inclusive... teremos menos mortos hoje, afinal é uma sexta não?")
        tempo(3)
        p("> ...")
        tempo(2)
        p("- Brincadeiras a parte,mas Mayws....")
        tempo(3)
        p("- Você ainda sente falta dele?")
        tempo(3)
        p("- Sabe que somos amigos há muito tempo... Você precisa melhorar.. ver o valor da vida mesmo tendo acontecido aquilo.")
        tempo(6.5)
        p("> É, estou tentando que posso...")
        tempo(3)

        print(" * CARRO PARANDO * ")
        tempo(2.5)
        
        p("- Chegamos.. Poucos enterros hoje,o dia promete em, pronto?")
        tempo(3)
        p("> Sim, vamos...")
        tempo(1.5)
        novaLinha()
        
    else:
        escolha("MAYWS RECUSA A CARONA DE SEU CHEFE EDUCADAMENTE E DIZ QUE VAI A PÉ PARA OBSERVAR O MUNDO...")
        tempo(3)
        escolha("CHEGANDO CEMITÉRIO ÁS 07:15MAYWS VÊ UM NEVOEIRO DENSO, COM SEU SOBRETUDO ELE ENTRA E VAI PARA A CABANA DE FERRAMENTAS")
        tempo(3)
        gameOver()
        print("OBRIGADO POR TESTAR A BETA! :D")
        return opcaocarona
def opcaoError():
        linha("=-=",20)
        print("OPÇÃO ERRADA! TENTE NOVAMENTE!")
        linha("=-=", 20)   
cont = 0
distancia = 1000 

while True:

    opcao = str(input("QUAL OPÇÃO DESEJA? [A/B]: ")).upper()
    tempo(1)
    novaLinha()

    if opcao == "A" or opcao == "B" and op1 == 1:
        limpaTela()
        escolha("MAYWS TOMA SEU BANHO E SE DIRIGE AO SEU TRABALHO... QUAL CAMINHO IR?")
        tempo(1)
        novaLinha()
        opcaoGame("IR PELA QUADRA PRINCIPAL DE CARRO,E,RAPIDAMENTE CHEGAR AO TRABALHO", "IR PELA AVENIDA PRINCIPAL A PÉ, ANDAR UM POUCO E OBSERVAR O MUNDO...")
        repetirNum(10,1)

        while True:
            opcaoavenida = str(input("QUAL OPÇÃO DESEJA? [A/B]: ")).upper().strip()
            if opcaoavenida == "A" or opcaoavenida == "B":
                break
            else:
                opcaoError()
                
        ruaAvenida(opcaoavenida)
        if ruaAvenida == "A":
            break

        while True:
            opcaojc = str(input("QUAL OPÇAO DESEJA? [A/B]: ")).upper().strip()
            if opcaojc == "A" or opcaojc == "B":
                break
            else:
                opcaoError()

        jornalCarona(opcaojc)
        if jornalCarona == "A":
            break
        while True:
            opcaocarona = str(input("QUAL OPÇÃO DESEJA? [A/B]: ")).upper().strip()
            if opcaocarona == "A" or opcaocarona == "B":
                break
            else:
                opcaoError()

        caronaAceita(opcaocarona)
        if caronaAceita == "B":
            break

    elif opcao == "A" and op1 == 2:
        limpaTela()
        escolha("MAYWS TOMA SUE COPINHO DE WISKY PARA ACORDAR, E SE DIRIGE AO BANHEIRO PARA LAVAR SEU ROSTO.. QUAL CAMINHO IREMOS AO TRABALHO?")
        tempo(2)
        novaLinha()
        opcaoGame("IR PELA QUADRA PRINCIPAL DE CARRO,E,RAPIDAMENTE CHEGAR AO TRABALHO", "IR PELA AVENIDA PRINCIPAL A PÉ, ANDAR UM POUCO E OBSERVAR O MUNDO...")
        repetirNum(10,1) 

        while True:
            opcaoavenida = str(input("QUAL OPÇÃO DESEJA? [A/B]: ")).upper().strip()
            if opcaoavenida == "A" or opcaoavenida == "B":
                break
            else:
                opcaoError()

        ruaAvenida(opcaoavenida)
        if ruaAvenida == "A":
            break

        while True:
            opcaojc = str(input("QUAL OPÇAO DESEJA? [A/B]: ")).upper().strip()
            if opcaojc == "A" or opcaojc == "B":
                break
            else:
                opcaoError()

        jornalCarona(opcaojc)
        if jornalCarona == "A":
            break
        while True:
            opcaocarona = str(input("QUAL OPÇÃO DESEJA? [A/B]: ")).upper().strip()
            if opcaocarona == "A" or opcaocarona == "B":
                break
            else:
                opcaoError()

        caronaAceita(opcaocarona)
        if caronaAceita == "B":
            break
         
    elif opcao == "B" and op1 == 2:
        limpaTela()
        escolha("MAYWS FICA BEBADO E VAI PARA O TRABALHO,LAVANDO SEU ROSTO E INDO PARA SUA GARAGEM... LIGA SEU CARRO E VAI AO TRABALHO...")
        tempo(2)
        for carro in range(1,100):
            if carro == 1:
                print("  QUADRA PRINCIPAL")
                time.sleep(8)
            print("    #    |    #")
            time.sleep(0.1)
            cont += 1
            if cont == 10:
                time.sleep(1)
                print(f"       .[+].    {distancia} metros")
                distancia -= 100
                cont = 0
        tempo(1)
        print("""
                #############
            ######################   MAYWS DE TÃO BEBADO NÃO PERCEBEU QUE DESVIOU DA PISTA E QUE HÁ UMA AVORE
        ###########################  APENAS A 30M DE DISTÂNCIA E SUA LAMBORGHINI ESTÁ EM 60KM/H... 
        ###############################  PENSE RAPIDAMENTE!
        ############################
        #########################
            ######################
                    |    |
                    |      |
                    |     |
                    |      |
                    |    |
                ====#     #====     30 metros!!!!!
        """)
        tempo(5)
        opcaoGame("DEIXAR BATER...","TENTAR DESVIAR!")
        repetirNum(5,1)
        opcaox = str(input("Digite a opção que deseja [A/B]: ")).upper()

        if opcaox == "A":
            limpaTela()
            escolha("MAYWS BATE O CARRO EM UMA VELOCIDADE ABISMAL CONTRA ARVORE,FAZENDO O MOTOR EXPLODIR E JA INCONCIENTE MORRE...")
            tempo(2)
            novaLinha()
            gameOver()
            tempo(2)
            print("""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████""")
            break

        elif opcaox == "B":
            limpaTela()
            escolha("MAYWS DESVIA DA ARVORE A TEMPO E CONSEGUE CHEGAR AO CEMITÉRIO NO HORÁRIO,AS 07:15")
            novaLinha()
            gameOver()
            novaLinha()
            print("OBRIGADO POR TESTAR A BETA :D!")
            break

        else:
            opcaoError()
    else:
        opcaoError()
    break
novaLinha()
print("OBRIGADO POR ACOMPANHAR E TESTAR A FASE BETA DO NOSSO JOGO MARAVILHOSO, A LOUCURA SE APROXIMA!")
tempo(8)
novaLinha()
print("CRÉDITOS: ")
tempo(2)
novaLinha()
print("Programador por:   Pedro Henrique")
tempo(3)
novaLinha()
print("Design por:     Thiago de Araújo")
tempo(3)
novaLinha()
print("Roterizado por:    Thiago & Pedro")
tempo(3)
novaLinha()
print("Agradecimentos:  Positivo, Pycharm, VsCode, Python.")
tempo(3)
novaLinha()
print("""
================================================
# Copyright 2023 | ThiagoDesing | HenriqueDev  #
================================================
""")