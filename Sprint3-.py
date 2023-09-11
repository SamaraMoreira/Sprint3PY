import datetime

def opcoes():
    print("""
    [ 1 ] Cadastro
    [ 2 ] Mais sobre a Porto Seguro
    [ 3 ] Área exclusiva
    [ 4 ] Ouvidoria
    [ 5 ] Sair
    """)
def inicio():
    print("----------------------------------------------")
    print("Bem Vindo a Porto Seguro, selecione uma opção")
    print("----------------------------------------------")
    menu()


def dados_pessoais():
        print("Insira seus dados para fazer o seu cadastro: ")
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        if idade < 18:
            print("Não podemos fazer o seguro para menor de idade, o seguro precisa ser feito no nome do seu responsavel")
            exit()
        cpf = str(input("Digite o seu cpf: "))
        rg = str(input("Digite o seu Rg: "))
        telefone = int(input("Digite o seu telefone: "))
        valida = True
        print(f"Verifique os seus dados:\nNome = {nome}\nIdade = {idade}\nCpf = {cpf}\nRg = {rg}\nTelefone = {telefone}")
        while valida == True:         
            try:
                verifica = int(input(f"Digite (1) se os seus dados pessoais estão corretos, caso contrario digite (2): "))
                if verifica == 2:
                    return dados_pessoais()
                elif verifica == 1:
                    dados_gerais = {"Nome":nome,"Idade":idade,"CPF":cpf, "RG": rg,"Telefone":telefone} 
                    return dados_gerais
                else:
                    print("Digite apenas os numeros apresentados")                 
            except ValueError:
                print("Entrada inválida, digite apenas 1 ou 2")

def cadastro_endereco():
    estado = str(input("Digite seu estado: "))
    cidade = str(input("Digite sua cidade: "))
    bairro = str(input("Digite seu bairro: "))
    while True:
        try:
            numero_bairro = int(input("Digite o numero de sua casa: "))
            break
        except ValueError:
            print("Digite ano valida")

        

    complemento = str(input("Digite o complemento: "))
    valida = True
    print(f"Verifique os seus dados:\n Estado = {estado}\nCidade = {cidade}\nBairro = {bairro}\nNúmero = {numero_bairro}\nComplemento = {complemento}")
    while valida == True:     
        try:
            verifica = int(input(f"Digite (1) se os seus dados pessoais estão corretos, caso contrario digite (2): "))
            if verifica == 2:
                return cadastro_endereco()
            elif verifica == 1:
                dados_endereco = {"Estado":estado,"Cidade":cidade,"Bairro":bairro,"Número":numero_bairro,"Complemento":complemento} 
                break
            else:
                print("Digite apenas os numeros apresentados")
        except ValueError:
            print("Entrada inválida, digite apenas 1 ou 2")
    return dados_endereco

def cadastro_bike():
    data = datetime.date.today()
    ano = data.year
    Nome_bike = str(input("Digite a marca da bike: "))
    while True:
        try:
            Ano_bike = int(input("Em que ano a bike foi adquirida? "))
            if Ano_bike > ano:
                print("Ano inválido")
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um ano válido.")
          

    utilidade_bike = (input("Para qual utilidade a bike será usada? Lazer? Meio de transporte? Trilhas? Velocidade e manobras?"),)
    tipo_bike = str(input("Digite qual foi o tipo da bike: "))
    Valor_bike = float(input("Digite o valor da bike: "))
    acessorios= []
    while True:
        acessorio = input("Insira um acessório (ou digite 'fim' para encerrar): ").lower()
        if acessorio == "fim":
            break 
        acessorios.append(acessorio)
    valida = True
    print(f"Verifique os seus dados:\n Marca = {Nome_bike}\nAno = {Ano_bike}\nUtilidade = {utilidade_bike}\nTipo = {tipo_bike}\nValor = {Valor_bike}\n Acessórios = {acessorios}")
    while valida == True:      
        verifica = int(input(f"Digite (1) se os seus dados pessoais estão corretos, caso contrario digite (2):  "))
        if verifica == 2:
            return cadastro_bike()
        elif verifica == 1:
            bike = {"Marca":Nome_bike,"Ano":Ano_bike,"Utilidade":utilidade_bike,"Tipo":tipo_bike,"Valor":Valor_bike,"Acessórios":acessorios} 
            break
    return bike

def opcaoAreaExclsuiva():
    print("""
            Área Exclusiva
          1 - Meus dados
          2 - Bike
          3 - Vistoria 
          4 - Sair
          """)
    
def criarCadastro():
    user = input("Digite o seu usuario para cadastro em nosso sistema: ")
    senha = input("Digite a senha para cadastro em nosso sistema: ")
    login = user,senha
    return login

def validarLogin(usuario, senha_cadastrada, user_login, senha_login):
    if usuario == user_login and senha_cadastrada == senha_login:
        return True
    return False

def login():
    user_cadastrado, senha_cadastrada = criarCadastro()
    return user_cadastrado,senha_cadastrada

def meusDados():
    pessoal = dados_pessoais()
    endereco = cadastro_endereco()
    dados = (pessoal, endereco)
    
    print("Dados pessoais:")
    for chave, valor in pessoal.items():
        print(f"{chave}: {valor}")
    
    print("\nEndereço:")
    for chave, valor in endereco.items():
        print(f"{chave}: {valor}")
    
    return dados
def dadosBike():
    bike = cadastro_bike()
    print("Minha Bike:")
    for chave, valor in bike.items():
        print(f"{chave}: {valor}")
    return bike

def areaexclusiva():
    while True:
        try: 
            opcaoAreaExclsuiva()
            menu = int(input("Selecione a opção: "))
            if menu == 1:
                meusDados()
            elif menu == 2:
                dadosBike()
            elif menu == 3:
                instrucoes()
            elif menu == 4:
                exit()
            else:
                print("Opção inválida. Digite um valor entre 1 e 4.")
        except ValueError:
            print("Entrada inválida.")

def cadastradocomarea():
    pessoal = dados_pessoais()
    endereco = cadastro_endereco()
    bike = cadastro_bike()
    while True:
        try:
            escolha_inicial = int(input("""Gostaria de acessar sua área exclusiva?:  
1 - SIM
2 - Não
Caso digite 2, você será redirecionado para o menu, e por não ter integração com o banco de dados, os dados serão perdidos: """))
            break
        except ValueError:
            print("\nDigite apenas 1 ou 2")

    if escolha_inicial == 2:
        menu()
    elif escolha_inicial == 1:
        while True:
                opcaoAreaExclsuiva()
                menua = int(input("Selecione a opção: "))
                if menua == 1:
                    print("Dados pessoais:")
                    for chave, valor in pessoal.items():
                        print(f"{chave}: {valor}")
                    print("\nEndereço:")
                    for chave, valor in endereco.items():
                        print(f"{chave}: {valor}")  
                elif menua == 2:
                    print("Minha Bike:")
                    for chave, valor in bike.items():
                        print(f"{chave}: {valor}")
                elif menua == 3:
                    instrucoes()
                elif menua == 4:
                    menu()
                else:
                    print("Opção inválida. Digite um valor entre 1 e 4.") 

def instrucoes():
    print("Para realizar a vistoria, é preciso que você reserve um tempo para encaminhar as fotos. As fotos precisam ser tiradas no momento, seguindo as instruções.")
    print("Você não precisa realizar a vistoria nesse momento, a opção ficará disponvel para que realize diante as sua disponibilidade.")
    print("É importante frisar que caso inicie e não conclue a etapa da vistoria, todo o andamento será perdido, você precisa realizar todo o processo novamente\n")
    while True:
        try:
            verifica = int(input("Gostaria de realizar a vistoria? digite (1) para sim e (2) para não: " ))
            if verifica == 2:
                    try:
                        vmenu = int(input("Se deseja voltar ao menu digite (1) caso contrario digite (2):"))
                        if vmenu == 1:
                            menu()
                        elif vmenu == 2:
                            exit()
                    except ValueError:
                        print("Entrada inválida.")
            elif verifica == 1:
                vistoria()
            else:
                print("Digite apenas 1 ou 2")
        except ValueError:
            print("Entrada inválida, digite apenas os numeros apresentados")

def vistoria():
    print ("No momento, essa etapa está em construção")
    
def mais_sobre(): 
    print("Somos a companhia que está com você em todos os momentos da vida A Porto é mais do que uma seguradora:"" é um ecossistema com todas as soluções para transformar sonhos em realidades diárias. ",
          " Com mais de 75 anos de mercado, possui hoje três verticais de negócios: Porto Seguros,"
           "Porto Saúde e Porto Seguro Bank, formando, assim, um conjunto de soluções de proteção para os seus momentos que vão desde o dia a dia até o grande dia.")
    while True:
        try:
            voltar = int(input("Se deseja voltar ao menu digite (1) caso contrario digite (2): "))
            if voltar == 1: 
                menu() 
                break    
            elif voltar == 2:
                exit()
            else:
                print("\nNumero invalido")
        except ValueError:
            print("\nEntrada inválida, digite apenas numeros")


def ouvidoria():
    print ("Você pode ligar para a Central de Atendimento (333-PORTO OU 3337-6786) ou acessar a seção Fale Conosco do site.")
    while True:
        try:
            voltar = int(input("Se deseja voltar ao menu digite (1) caso contrario digite (2): "))
            if voltar == 1: 
                menu() 
                break    
            elif voltar == 2:
                exit()
            else:
                print("\nNumero invalido")
        except ValueError:
            print("\nEntrada inválida, digite apenas numeros")


def menu():
    while True:
        opcoes()
        try:
            menu = int(input("Selecione a opção: "))
            if menu == 1:
                cadastradocomarea()
            elif menu == 2:
                mais_sobre()
            elif menu == 3:
                user_login = input("Digite seu usuário para fazer login: ")
                senha_login = input("Digite sua senha: ")
                if validarLogin(cadastrado[0], cadastrado[1], user_login, senha_login):
                    print("Login bem-sucedido!")
                    areaexclusiva()
                else:
                    print("Usuário ou senha incorretos.")
                    exit()
            elif menu == 4:
                ouvidoria()
            elif menu == 5:
                exit()
            else:
                print("Opção inválida. Digite um valor entre 1 e 5.")
        except ValueError:
            print("Entrada inválida, digite apenas")

cadastrado = criarCadastro()
menu()

