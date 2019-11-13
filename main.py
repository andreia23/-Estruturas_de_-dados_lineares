from CPaciente import Paciente
from CPilha import Pilha
from CFila import Fila
from CLista import Lista

while True:
  print('#' * 50)
  print('Estruras de dados lineares:')
  print('#' * 50)
  print('[1] - Lista\n[2] - Pilha\n[3] - Fila\n[4] - Sair')
  print('#' * 50)
  estru = int(input('Qual das estruturas acima você deseja trabalhar? '))
  print('#' * 50)
    
#Trabalhando com Lista#
  if estru == 1:
    l1 = Lista()
    while True:
      print('#' * 50)
      print('Opções da Estrutura Lista:')
      print('#' * 50)
      print('[1] - Adicionar dados na lista')
      print('[2] - Remover dados da lista')
      print('[3] - Verificar se a lista está vazia')
      print('[4] - Saber o tamanho da lista')
      print('[5] - Verificar o valor do dado')
      print('[6] - Voltar')
      print('#' * 50)

      op = int(input('Escolha uma das opções acima: '))
      print('#' * 50)

      if op == 1:
        nome = input('Digite seu Nome:')
        cpf = input('Digite seu CPF:')
        horario = input('Digite Horario para sua Consulta:')
        posi = int(input('Digite a Posição que Deseja Adcionar na Lista:'))
        l1.push_lista(nome, cpf, horario, posi)
        print('\nDado adicionado com sucesso\n')

      elif op == 2:
        if l1.isempty_lista() == True:
          print('A Lista esta Vazia!')
        else:
          posi = int(input('Digite a Posição que Deseja Remover:'))
          l1.pop_lista(posi)
          print('Paciente {} Removido com Êxito\n{}'.format(posi, l1))

      elif op == 3:
        if l1.isempty_lista() == True:
          print('A Lista Esta Vazia')
        else:
          print(l1)

      elif op == 4:
        print('A Lista Possui [{}] Pacientes!'.format(l1.size_lista()))
        print(l1)

      elif op == 5:
        posi = int(input('Digite a Posição na qual Deseja Consultar os Dados do Paciente:'))
        print('[{}]'.format(l1.element_lista(posi)))

      elif op == 6:
        break

      else:
        print('Opção inválida')
                
#Trabalhando com Pilha#
  elif estru == 2:
    p1 = Pilha()
    while True:
      print('#' * 50)
      print('Opções da Estrutura Pilha:')
      print('#' * 50)
      print('[1] - Adicionar dados na Pilha')
      print('[2] - Remover dados da Pilha')
      print('[3] - Verificar se a Pilha está Vazia')
      print('[4] - Saber o Tamanho da Pilha')
      print('[5] - Verificar o Valor do Topo da Pilha')
      print('[6] - Voltar')
      print('#' * 50)

      op = int(input('Escolha uma das opções acima: '))
      print('#' * 50)

      if op == 1:
        nome = input('Digite seu Nome:')
        cpf = input('Digite seu CPF:')
        horario = input('Digite Horario para sua Consulta:')
        p1.push_pilha(nome, cpf, horario)
        print('\nDado adicionado com sucesso\n')

      elif op == 2:
        if p1.isempty_pilha() == True:
          print('A Pilha está Vazia!')
        else:
          p1.pop_pilha()
          print('Paciente 1 Removido com Êxito\n{}'.format(p1))

      elif op == 3:
        if p1.isempty_pilha() == True:
          print('A Pilha Esta Vazia')
        else:
          print(p1)

      elif op == 4:
        print('A Pilha Possui [{}] Pacientes!'.format(p1.size_pilha()))
        print(p1)

      elif op == 5:
        print('[{}]'.format(p1.top_pilha()))

      elif op == 6:
        break
      
      else:
        print('Opção inválida')
                
#Trabalhando com Fila#
  elif estru == 3:
    f1 = Fila()
    while True:
      print('#' * 50)
      print('Opções da Estrutura Fila:')
      print('#' * 50)
      print('[1] - Adicionar dados na Fila')
      print('[2] - Remover dados da Fila')
      print('[3] - Verificar se a Fila está Vazia')
      print('[4] - Saber o Tamanho da Fila')
      print('[5] - Verificar o Valor do Topo da Fila')
      print('[6] - Voltar')
      print('#' * 50)

      op = int(input('Escolha uma das opções acima: '))
      print('#' * 50)

      if op == 1:
        nome = input('Digite seu Nome:')
        cpf = input('Digite seu CPF:')
        horario = input('Digite Horario para sua Consulta:')
        f1.push_fila(nome, cpf, horario)
        print('\nDado adicionado com sucesso\n')

      elif op == 2:
        if f1.isempty_fila() == True:
          print('A Fila está Vazia!')
        else:
          f1.pop_fila()
          print('Paciente 1 Removido com Êxito\n{}'.format(f1))

      elif op == 3:
        if f1.isempty_fila() == True:
          print('A Fila Esta Vazia')
        else:
          print(f1)

      elif op == 4:
        print('A Fila Possui [{}] Pacientes!'.format(f1.size_fila()))
        print(f1)

      elif op == 5:
        print('[{}]'.format(f1.top_fila()))

      elif op == 6:
        break
      
      else:
        print('Opção inválida')
                
#Opção para sair da repetição#
  elif estru == 4:
    print('\t\tProjeto foi feito por:\n\t\tAndréia Berto e Felipe Gomes')
    print('#' * 50)
    print('\n\t\t\t\tDeus seja louvado!!!\n')
    print('#' * 50)
    break
    
#Caso a opção seja inválida#
  else:
    print('Opção inválida')

        

