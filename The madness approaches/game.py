import time
import os

WHITE = '\033[1;97m'RESET = '\033[0m'
RED = '\033[1;91m'
GREEN = '\033[1;92m'
YELLOW = '\033[1;93m'
BLUE = '\033[1;94m'
MAGENTA = '\033[1;95m'
CYAN = '\033[1;96m'

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

def opcaoError():
        linha(RED + "=-=",20)
        print("OPÇÃO ERRADA! TENTE NOVAMENTE!")
        linha("=-=", 20)  
        print(RESET)

def personagem():
    print(CYAN)
    print("Nome: Mayws Jonhson")
    tempo(0.5)
    print("Idade: 33 anos")
    tempo(0.5)
    print("Peso: 65 KG")
    tempo(0.5)
    print("Altura: 1,87m")
    tempo(0.5)
    print("Nacionalidade: Inglês com descendência austriaca")
    print(RESET)
    novaLinha()

    while True:
        opcaoPer = str(input(GREEN +'DIGITE "S" PARA IR AO MENU PRINCIPAL / "M" PARA VOLTAR AO MENU: '+ RESET)).upper().strip()
        if opcaoPer == "S":
            limpaTela()
            menuStart()
            break
        elif opcaoPer == "M":
            limpaTela()
            opcaoMenu()
            break
        else:
            opcaoError()

def controlesJogo():
    novaLinha()
    print(CYAN + "CONTROLES DO JOGO:")
    tempo(0.5)
    print(' Interatividade pura, escolha utilizando teclado.')
    print(' #==================================================================================#')
    print(' Aperte "C" na interação para ver as configurações.')
    print(' Aperte "P" na interação para ver o personagem.')
    print(' Aperte "M" na interação para voltar a tela principal do jogo.')
    print(' Aperte "K" para voltar ao jogo quando estiver nas configurações ou no personagem...')
    print(' #==================================================================================#\n  ')
    tempo(0.5)
    print('_____________________________________________________________________________________')
    print('Para interagir siga essas regras:')
    print(' * Digite apenas A ou B e nada mais, exceto caso queria a configuração.')
    print(' * Se a interatividade pedir números então digite-os corretamente.')
    print(' * Em alguns momentos terão mini-games para passar de fase, então prepare-se.')
    p("_____________________________________________________________________________________"+ RESET)
    tempo(0.5)
    novaLinha()

    while True:
        opcaoControle = str(input(GREEN+'DIGITE "S" PARA IR A TELA INICIAL / "M" PARA VOLTAR AO MENU:'+RESET)).upper().strip()
        if opcaoControle == 'S':
            limpaTela()
            menuStart()
            break
        elif opcaoControle == 'M':
            limpaTela()
            opcaoMenu()
            break
        else:
            opcaoError()

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

def opcaoSobre():
    print(GREEN)
    linha(30,"=+=")
    print('Olá, bem-vindo e veja um pouco mais sobre nosso jogo!')
    print('JOGO FEITOR POR PEDRO HENRIQUE(PROGRAMADOR) & THIAGO DE ARAÚJO (DESING GRÁFICO)')
    print('Versão: BETA 5.0.2')
    linha(30,"=+=")
    tempo(0.5)
    novaLinha()
    linha(52,"---")
    print('Sobre: A história do jogo conta sobre Mayws... um homen que perdeu sua familía em um bombardeio na primeira guerra mundial e 7 após esse evento traumatizante, Mayws trabalha em um cemitério enterrando corpos, mas a loucura do passado lhe assombra de uma maneira infernal...')
    linha(52,"---")
    novaLinha()
    print('Digite "S" para voltar a tela inicial ou "M" para voltar ao menu.')

    while True:
        presskm = str(input(":")).upper().strip()
        if presskm == "S":
            limpaTela()
            menuStart()
            break
        elif presskm == "M":
            limpaTela()
            opcaoMenu()
            break
        else:
            opcaoError()

    print(RESET)

def opcaoMenu():
    print(CYAN +'     ______________')
    print('     | PERSONAGEM |')
    print('     --------------\n')
    tempo(0.5)
    print('     _____________')
    print('     | CONTROLES |')
    print('     -------------\n' + RESET)
    tempo(0.5)

    while True:
        opcaomenu = str(input(GREEN + 'DIGITE "P" PARA VER O PERSONAGEM / "C" PARA VER OS CONTROLES OU "S" PARA VOLTAR A TELA INICIAL:' + RESET)).upper().strip()
        if opcaomenu == 'P':
            limpaTela()
            personagem()
            break
        elif opcaomenu == 'C':
            limpaTela()
            controlesJogo()
            break
        elif opcaomenu == "S":
            limpaTela()
            menuStart()
            break
        else:
            opcaoError()

def menuStart():
    print(CYAN + '     _________')
    print('     | START |')
    print('     ---------\n')
    tempo(0.5)
    print('     _________')
    print('     |  MENU |')
    print('     ---------\n')
    tempo(0.5)
    print('     _________')
    print('     | SOBRE |')
    print('     ---------\n' + RESET)
    print(GREEN + 'DIGITE "S" PARA INICIAR')
    print('DIGITE "M" PARA VER O MENU')
    print('DIGITE "A" PARA VER MAIS'+ RESET )

    while True:
        opcaostart = str(input(': ')).upper().strip()
        if opcaostart == 'M':
            limpaTela()
            opcaoMenu()
            break
        elif opcaostart == 'A':
            limpaTela()
            opcaoSobre()
            break
        elif opcaostart == 'S':
            break
        else:
            opcaoError()
    limpaTela()
    tempo(1)


def pressEnter():
    while True:
        enter = str(input('Pressione ENTER para continuar...'))
        if enter != "":
            limpaTela()
        else:
            break
        limpaTela()

limpaTela()
menuStart()
novaLinha()
linha(50,"##")
print("SEJA MUITO BEM VINDO AMANTE DA LOUCURA AO NOSSO JOGO! ESCOLHA,EXPLORE E MORRA! HAHAHHAHAA!")
linha(50,"##")
tempo(2)

tempo(2)
linha(25, "---")
p("PARA VER AS CONFIGURAÇÕES DO JOGO APERTE 'M' ")
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
tempo(0.5)
print("""Em 1914 inicia-se a primeira guerra mundial da história,
contendo 17 páises confrotado pela França X União Soviética,
um desses páises era a Inglaterra... Meu páis...""")
tempo(0.5)
linha(60,"-")
pressEnter()

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
pressEnter()
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
        pressEnter()
        novaLinha()
        opcaoGame("UM PEDAÇO DE PÃO", "UM RESTO DE BOLO FOFO")
        repetirNum(10,1)
        break
    elif opcao == "B":
        op1 +=2
        limpaTela()
        escolha("MAYWS QUER SEU WISKY PARA ACORDAR... COMO BEBER?")
        presEnter()
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
            pressEnter()
            novaLinha()
            print("O JOGO ACABOU, OBRIGADO POR TESTAR A BETA! :D")
            return opcaoavenida
        else:
            escolha("MAYWS ESTÁ ANDANDO E VÊ UMA LOJA COM UMA BANCADA DE JORNAIS NO POSTO DE GASOLINA...OPS! VOCÊ TEM £0,25 O QUE ACHA DE UM JORNAL?")
            pressEnter()
            novaLinha()
            opcaoGame("COMPRAR JORNAL", "NÃO COMPRAR E IR LOGO...")
            repetirNum(10,1)

def jornalCarona(opcaojc):
     if opcaojc == "A":
                escolha("O JORNAL VINHA COM ALGUMAS INFORMAÇÕES INRRELEVANTES, MAS A PRINCIPAL ERA SOBRE...")
                pressEnter()
                novaLinha()
                print("""
                    [AQUI ENTRA UM JORNAL]
                """)
                tempo(3)
                novaLinha()
                escolha("MAYWS SE ENTRISTECE AO LER... PESADELOS AINDA-OS ASSOMBRA.. MAYWS SE DIRIGE AO TRABALHO...")
                pressEnter()
                novaLinha()
                print("""
                 [ flashback... alguma coisa tenebrosa]
                """)
                tempo(2)
     else:
        escolha("SEU CHEFE PASSA PARA REABASTECER O TANQUE E O VÊ, ENTÃO LHE OFERECE UMA CARONA ATÉ O TRABALHO...")
        pressEnter()
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
        pressEnter()
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
        pressEnter()
        escolha("CHEGANDO CEMITÉRIO ÁS 07:15MAYWS VÊ UM NEVOEIRO DENSO, COM SEU SOBRETUDO ELE ENTRA E VAI PARA A CABANA DE FERRAMENTAS")
        pressEnter()
        gameOver()
        print("OBRIGADO POR TESTAR A BETA! :D")
        return opcaocarona
 
cont = 0
distancia = 1000 

while True:

    opcao = str(input("QUAL OPÇÃO DESEJA? [A/B]: ")).upper()
    tempo(1)
    novaLinha()

    if opcao == "A" or opcao == "B" and op1 == 1:
        limpaTela()
        escolha("MAYWS TOMA SEU BANHO E SE DIRIGE AO SEU TRABALHO... QUAL CAMINHO IR?")
        pressEnter()
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
        pressEnter()
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
        pressEnter()
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
            pressEnter()
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
            pressEnter()
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
pressEnter()
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