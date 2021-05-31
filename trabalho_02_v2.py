# Nome: Lucas Alesterio Marques Vieira
# Matricula: 11621ECP016

# Inicialização das variaveis
nEstados = 0
nSimbolos = 0
simbolos = []
nGama = 0
gama = []
nAceitacao = 0
aceitacao = []
nTransicoes = 0
transicoes = []
nCadeias = 0
cadeias = []

# Função para coletar as entradas
def entradas():
    # Declação das variaveis globais
    global nEstados, nSimbolos, simbolos, nAceitacao, aceitacao
    global nTransicoes, transicoes, nCadeias, cadeias, nGama, gama
    # Capturando numero de estados e transformando em inteiro
    nEstados = int(input())
    # Capturando numero de simbolos e lista de simbolos
    auxInput = input()
    auxInput = auxInput.split(" ")
    nSimbolos = int(auxInput[0])
    simbolos = auxInput[1:]
    # Capturando numero de simbolos e lista de simbolos da pilha
    auxInput = input()
    auxInput = auxInput.split(" ")
    nGama = int(auxInput[0])
    gama = auxInput[1:]
    # Capturando numero de estados de aceitação e lista de aceitação
    auxInput = input()
    auxInput = auxInput.split(" ")
    nAceitacao = int(auxInput[0])
    aceitacao = list(map(int, auxInput[1:]))
    # Capturando numero de transições
    nTransicoes = int(input())
    # Capturando lista de transições em loop de
    # acordo com o numero digitado anteriormente
    transicoes = []
    while len(transicoes) < nTransicoes:
        transicoes.append(input().split(" "))
    # Capturando numero de cadeias
    nCadeias = int(input())
    # Capturando lista de cadeias em loop de
    # acordo com o numero digitado anteriormente
    cadeias = []
    while len(cadeias) < nCadeias:
        cadeias.append(list(input()))


# Função para percorrer todas as cadeias digitadas
# e faz a busca em cada uma com o estado inicial 0
# , pilha iniciada com "Z" e cadeia digitada
#  printando o resultado
def varredura():
    for cadeia in cadeias:
        print(busca(0, cadeia, ["Z"]))


# Função de busca que tem como entrada o estado inicial
# , a pilha e a cadeia a ser percorrida
def busca(estadoAtual, cadeia, pilha_inicial):
    # Copiando a pilha para uma variavel interna para
    # que não seja alterada entre os ciclos de execução
    pilha = pilha_inicial.copy()
    topo = pilha[-1]

    # Ciclo de testes para caso a cadeia esteja vazia
    if not (cadeia):
        # Se o estado atual esta na lista de aceitação
        # e retorna o resultado
        if estadoAtual in aceitacao:
            return "aceita"
        else:
            # Loop para testar se existe alguma transição
            # vazia a partir do estado atual
            for transicao in transicoes:
                if (
                    int(transicao[0]) == estadoAtual
                    and transicao[1] == "-"
                    and transicao[2] == topo
                ):
                    # Confirma se o proximo é de aceitação e retornar resultado
                    if transicao[3] in aceitacao:
                        return "aceita"
                    # Continua a busca retirando o topo da pilha
                    if transicao[4] == "-":
                        if busca(int(transicao[3]), cadeia, pilha[:-1]) == "aceita":
                            return "aceita"
                    else:
                        # Continua a busca a partir de um novo estado
                        if busca(int(transicao[3]), cadeia, pilha) == "aceita":
                            return "aceita"
            return "rejeita"

    # Verificando todas as possiveis transições a partir
    # do estado inicial
    for transicao in transicoes:
        auxPilha = list(transicao[4])
        if (
            int(transicao[0]) == estadoAtual
            and transicao[1] == cadeia[0]
            and transicao[2] == topo
        ):
            # Inicia uma nova busca removendo o topo da pilha
            # e removendo o ultimo elemento da cadeia
            if transicao[4] == "-":
                if busca(int(transicao[3]), cadeia[1:], pilha[:-1]) == "aceita":
                    return "aceita"
            # Inicia uma nova busca atualizando o topo da pilha
            # e removendo o ultimo elemento da cadeia
            else:
                if (
                    busca(int(transicao[3]), cadeia[1:], pilha[:-1] + auxPilha[::-1])
                    == "aceita"
                ):
                    return "aceita"
        # Teste para caso seja uma transição vazia
        elif (
            int(transicao[0]) == estadoAtual
            and transicao[1] == "-"
            and transicao[2] == topo
        ):
            # Inicia uma nova busca removendo o topo da pilha
            # mantendo a cadeia
            if transicao[4] == "-":
                if busca(int(transicao[3]), cadeia, pilha[:-1]) == "aceita":
                    return "aceita"
            # Inicia uma nova busca atualizando o topo da pilha
            # mantendo a cadeia
            else:
                if (
                    busca(int(transicao[3]), cadeia, pilha[:-1] + auxPilha[::-1])
                    == "aceita"
                ):
                    return "aceita"
    return "rejeita"


# Chamando as funções de entradas e varredura para iniciar o programa
entradas()
varredura()