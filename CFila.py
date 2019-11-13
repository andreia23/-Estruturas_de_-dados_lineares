from CPaciente import Paciente

###Classe Fila###
class Fila:
  def __init__(self, top=None):
    self._top = top

#Getters e Setters
  def get_top(self):
    return self._top

#Métodos Basicos
  def push_fila(self, nome, cpf, horario):
    q = Paciente(nome, cpf, horario)
    p = self._top
    if self._top == None:
      self._top = q
    else:
      while p.get_prox() != None:
        p = p.get_prox()
      p.set_prox(q)
      q.set_prox(None)

  def pop_fila(self):
    if self._top == None:
      return 'A Fila já está vazia'
    self._top = self._top.get_prox()

  def isempty_fila(self):
    if self._top == None:
      return True
    else:
      return False

  def size_fila(self):
    if self._top == None:
      return 'A estrutura não possui nemhum elemento'
    else:
      tam = 0
      p = self._top
      while p != None:
        tam += 1
        p = p.get_prox()
      return tam
      
  def top_fila(self):
    if self._top == None:
      return 'O valor do elemento é',None
    else:
      return 'Paciente 1: Nome: {}\tCPF: {}\tHorario: {}'.format(self._top.get_nome(), self._top.get_cpf(), self._top.get_horario())

#Print#
  def __str__(self):
    p = self._top
    v = ''
    while p != None:
      v += '[Nome:' + p.get_nome() + '\tCPF:' + p.get_cpf() + '\tHorário Marcado:' + p.get_horario() + ']' + '\n'
      p = p.get_prox()
    return 'Fila:\n{}'.format(v)
           
