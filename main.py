# Universidade Federal Fronteira Sul
# Trabalho de algoritmos e programação
# Professoras Andressa Sebben e Marina Girolimetto
# Alunos: Marco Antonio Duz e Pedro Augusto Sciesleski
from time import sleep

# -------------------------Classes---------------------


class Aluno:
    nome = None
    cpf = None
    peso = 0
    altura = 0
    imc = 0
    Status = False


class Exercicio:
    nomeExercicio = None
    numSeries = 0
    numRepeticoes = 0
    pesoExercicio = 0


# -------------------------Variáveis globais---------------------
alunos = []
treinos = []

# -------------------------Funçoes de Validações/Verificações---------------------


def validaAltura(a):
    while True:
        try:
            a = float(a)
            if a > 0 and a <= 2.5:
                return a
            else:
                print("Altura inválida altura deve ser entre 0 e 2.50 metros")
                a = input("favor inserir novamente: ")
        except ValueError:
            a = input("Altura inválida, digite-a novamente: ")


def validaOp(op):
    while True:
        try:
            op = int(op)
            return op
        except ValueError:
            return 0


def validaPeso(p):
    while True:
        try:
            a = float(p)
            if a > 0:
                return a
            else:
                print("Peso inválido o peso deve ser maior que 0")
                a = input("favor inserir novamente: ")
        except ValueError:
            a = input("Peso inválida, digite-o novamente: ")

# validação de CPF do site vivaolinux dispoínel em:
# https://www.vivaolinux.com.br/script/Validador-e-gerador-de-CPF-em-Python


def validaCpf(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def verificaAluno(a):
    e = False
    for i in range(len(alunos)):
        if a == alunos[i].nome:
            e = True
            break
    if not e:
        print("Aluno não encontrado voltando para o menu principal")
        sleep(1)
        return None, None
    else:
        return e, i


def verificaExercicio(t, iA):
    e = False
    for i in range(len(treinos[iA])):
        if t == treinos[iA][i].nomeExercicio:
            e = True
            return e, i
    if not e:
        return e, 0


def validaNome(a):
    e = False
    for i in range(len(alunos)):
        if a == alunos[i].nome:
            e = True
            break
    return e

# -------------------------Funções relacionadas ao aluno---------------------


def calculaImc(p, a):
    imc = p/a**2
    return imc


def CadAluno():
    a = Aluno()
    while True:
        nome = input("\nNome: ")
        if validaNome(nome):
            print("usuário já existente, tente outro nome")
        else:
            a.nome = nome
            break
    while True:
        cpf = input("CPF: ")
        if validaCpf(cpf):
            a.cpf = cpf
            break
        else:
            print("Cpf inválido digite-o novamente: \n")
    a.peso = validaPeso(input("Peso (Kg): "))
    a.altura = validaAltura(input("Altura (m): "))
    a.imc = calculaImc(a.peso, a.altura)
    return a


def ConsultAluno():
    a = input("Insira o nome do aluno: ")
    e, i = verificaAluno(a)
    if e:
        print("Aluno(a):", alunos[i].nome)
        print("Cpf:", alunos[i].cpf)
        print(f"Peso: {alunos[i].peso}Kg")
        print(f"Altura: {alunos[i].altura:.2f}m")
        print(f"IMC: {alunos[i].imc:.2f}")
        if alunos[i].Status == False:
            print("Aluno inativo não existe treino\n")
        else:
            print("\n------Treinos-----\n")
            for iE in range(len(treinos[i])):
                print(treinos[i][iE].nomeExercicio)
                print("Quantidade de séries:", treinos[i][iE].numSeries)
                print("Quantidade de repetições:",
                      treinos[i][iE].numRepeticoes)
                print("Carga do exercício:", treinos[i][iE].pesoExercicio)
                print()
        while True:
            if input("digite 0 para voltar ao menu: ") == '0':
                break


def AtualizaAluno():
    a = input("Insira o nome do aluno que deseja atualizar: ")
    e, i = verificaAluno(a)
    if e:
        while True:
            op = input("Qual dado deseja alterar - nome, cpf, peso ou altura: ")
            if op == 'nome':
                alunos[i].nome = input(
                    f"digite o novo nome (atual: {alunos[i].nome}): ")
            elif op == 'cpf':
                alunos[i].cpf = input(
                    f"digite o novo cpf (atual: {alunos[i].cpf}): ")
            elif op == 'peso':
                alunos[i].peso = validaPeso(
                    input(f"digite o novo peso (atual: {alunos[i].peso:.2f}): "))
                alunos[i].imc = calculaImc(alunos[i].peso, alunos[i].altura)
            elif op == 'altura':
                alunos[i].altura = validaAltura(
                    input(f"digite a nova altura (atual: {alunos[i].altura:.2f}m): "))
                alunos[i].imc = calculaImc(alunos[i].peso, alunos[i].altura)
            else:
                print("opção invalida tente novamente")
                continue
            a = input(
                "deseja alterar mais alguma informação digite S para sim e N para não: ")
            if a == 'S':
                continue
            elif a == 'N':
                break
            else:
                print("opção inválida voltando para o menu principal")
                sleep(1)
                break


def ExcluirAluno():
    a = input("Insira o nome do aluno que deseja excluir ")
    e, i = verificaAluno(a)
    if e == False:
        print("Aluno não encontrado voltando para o menu principal")
        sleep(1)
    else:
        alunos.pop(i)
        print("aluno excluido com sucesso")
        sleep(1)


def RelatorioAluno():
    print("\n1-Relatório de alunos ativos")
    print("2-Relatório de alunos inativos")
    print("3-Relatório de todos os alunos")
    op = int(input("Digite o número da opção desejada: "))
    print()
    if op == 1:
        mostrarAlunos(True, True)
    elif op == 2:
        mostrarAlunos(False, False)
    elif op == 3:
        mostrarAlunos(True, False)
    else:
        print("opção inválida, voltando para o menu principal")
        sleep(1)
        return None


def mostrarAlunos(op1, op2):
    qtd0 = True
    for i in range(len(alunos)):
        if alunos[i].Status == op1 or alunos[i].Status == op2:
            qtd0 = False
            print(f"-----Aluno {i+1}-----")
            print("Nome:", alunos[i].nome)
            print("Cpf:", alunos[i].cpf)
            print(f"Peso: {alunos[i].peso} Kg")
            print(f"Altura: {alunos[i].altura} cm")
            print(f"IMC: {alunos[i].imc:.2f}")
            if op1 == True and op2 == False:
                if alunos[i].Status == True:
                    print("Aluno ativo")
                elif alunos[i].Status == False:
                    print("Aluno inativo")
            print()
    if qtd0 and (op1 == True and op2 == True):
        print("nenhum aluno ativo foi encontrado\n")
    elif qtd0 and (op1 == False and op2 == False):
        print("nenhum aluno inativo foi encontrado\n")
    elif qtd0:
        print("Não há alunos cadastrados\n")
    while True:
        if input("digite 0 para voltar ao menu: ") == '0':
            break

# -------------------------Funções relacionadas ao treino---------------------


def GerenciarTreino():
    a = input("Insira o nome do aluno: ")
    e, iA = verificaAluno(a)
    if e:
        while True:
            print("\n1-incluir um novo exercício ao treino do aluno")
            print("2-alterar exercício do aluno")
            print("3-Excluir exercício do aluno")
            print("4-excluir todos os exercícios do treino do aluno")
            print("5-sair\n")
            op = validaOp(input("Digite o número da opção desejada: "))
            print()
            if op == 1:
                t = input("insira o nome do exercício: ")
                eE, iE = verificaExercicio(t, iA)
                if eE:
                    print("\nEste exercício já existe, gotaria de altera-lo?")
                    op = input("Disite S para sim ou N para não: ")
                    if op == 'S':
                        print()
                        alteraExercicio(iA, iE)
                        break
                    elif op == 'N':
                        break
                    else:
                        print("opção inválida")
                        sleep(1)
                else:
                    treinos[iA].append(incluirExercicio(t, iA))
                break
            elif op == 2:
                t = input("insira o nome do exercício a ser alterado: ")
                print()
                eE, iE = verificaExercicio(t, iA)
                if eE:
                    alteraExercicio(iA, iE)
                    break
                else:
                    print("Este exercício não existe, gotaria de cria-lo?")
                    op = input("Disite S para sim ou N para não: ")
                    if op == 'S':
                        treinos[iA].append(incluirExercicio(t, iA))
                        break
                    elif op == 'N':
                        break
                    else:
                        print("\nopção inválida")
                        sleep(1)
            elif op == 3:
                t = input("insira o nome do exercício a ser excluido: ")
                eE, iE = verificaExercicio(t, iA)
                if eE:
                    excluirExercicio(iA, iE)
                    break
                else:
                    print("Exercício não encontrado")
                    sleep(1)
            elif op == 4:
                excluirTreino(iA)
                alunos[iA].Status = False
                break
            elif op == 5:
                break
            else:
                print("opção inválida tente novamente")
                sleep(1)


def alteraExercicio(iA, iE):
    while True:
        op = input(
            "Qual dado deseja alterar - nome, numero de repetições(numRep), numero de Series(numSerie) ou peso do exercicio(pesoExer): ")
        if op == 'nome':
            treinos[iA][iE].nomeExercicio = input(
                f"digite o novo nome (atual: {treinos[iA][iE].nome}): ")
        elif op == 'numSerie':
            treinos[iA][iE].numSeries = input(
                f"digite o novo cpf (atual: {treinos[iA][iE].numSeries}): ")
        elif op == 'numRep':
            treinos[iA][iE].numRepeticoes = input(
                f"digite o novo cpf (atual: {treinos[iA][iE].numRepeticoes}): ")
        elif op == 'pesoExer':
            treinos[iA][iE].pesoExercicio = input(
                f"digite o novo peso (atual: {treinos[iA][iE].pesoExercicio}): ")
        else:
            print("opção invalida tente novamente")
            continue
        a = input(
            "deseja alterar mais alguma informação digite S para sim e N para não: ")
        if a == 'S':
            continue
        elif a == 'N':
            break
        else:
            print("opção inválida voltando para o menu principal")
            sleep(1)
            break


def incluirExercicio(nome, iA):
    alunos[iA].Status = True
    e = Exercicio()
    e.nomeExercicio = nome
    e.numSeries = input("Digite o numero de series do exercicio: ")
    e.numRepeticoes = input("Digite o numero de repetições do exercicio: ")
    e.pesoExercicio = input("Digite a carga (Kg) do exercicio: ")
    return e


def excluirExercicio(iA, iE):
    treinos[iA].pop(iE)
    print("exercicio excluido com sucesso\n")
    sleep(1)


def excluirTreino(iA):
    treinos[iA].clear()
    print("treino excluido com sucesso")
    sleep(1)

# ---------------------função MAIN - Menu Principal-----------------------


print("Bem vindo ao sistema")
while True:
    print("\n-------------------------------------\n")
    print("Escolha uma das opções: ")
    print("1-Cadastrar aluno")
    print("2-Gerenciar treino")
    print("3-Consultar aluno")
    print("4-Atualizar cadastro do aluno")
    print("5-Excluir aluno")
    print("6-Relatório de alunos")
    print("Digite -1 para encerrar a sessão")
    print("\n-------------------------------------\n")
    op = validaOp(input("Digite o número da opção desejada: "))
    if op == -1:
        print("Programa encerrado")
        break
    elif op == 1:
        vazio = []
        alunos.append(CadAluno())
        treinos.append(vazio)
    elif op == 2:
        GerenciarTreino()
    elif op == 3:
        ConsultAluno()
    elif op == 4:
        AtualizaAluno()
    elif op == 5:
        ExcluirAluno()
    elif op == 6:
        RelatorioAluno()
    else:
        print('Opção inválida tente novamente')
        sleep(1)
