from CPaciente import Paciente
from CPilha import Pilha
from CFila import Fila
from CLista import Lista


while True:
    #Menu de estruturas#
    
    print('Sistema de Agendamento de Consultas da Drª Andréia Berto:')
    print('\n1- Agendamento\n2- Consulta\n3- Fila\n4- Sair')
    estru = int(input('Escolha uma das opções: '))
    
    #Agendamento#
    if estru == 1:
        #Menu das opções de lista#
        print('\nOpções da estrura lista:')
        print('1 - Agendar Consulta:')
        print('2 - Cancelar Consulta:')
        print('3 - Oganizar Cronograma:')
        print('4 - Voltar')
        
        p1 = Pilha()
        l1 = Lista()
        while True:
            op = int(input('Escolha uma das opções acima: '))
            if op == 1:
              nome = input('Digite seu Nome:')
              cpf = input('Digite seu CPF:')
              horario = input('Digite Horario para sua Consulta:')
              p1.push_pilha(nome, cpf, horario)
              print('Consulta Agendada Com Êxito!')
            elif op == 2:
                posis = int(input('Digite a posição que deseja remover: '))
                print(lista.pop_lista(posis))
            elif op == 3:
                print('A lista está vazia?',lista.isempty_lista())
            elif op == 4:
                print(lista.size_lista())
            elif op == 5:
                po = int(input('Digite a posição que você deseja ver o valor: '))
                print(lista.top_lista(po))
            elif op == 6:
                break
            else:
                print('Opção inválida')
                

    #Caso a opção seja inválida#
    else:
        print('Opção inválida')

        

