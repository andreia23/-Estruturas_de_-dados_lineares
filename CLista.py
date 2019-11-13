from CPaciente import Paciente

###Classe Lista###
class Lista:
  def __init__(self,top = None):
    self._top = top

#Getters e Setters
  def get_top(self):
    return self._top

#Métodos Basicos
  def push_lista(self, nome, cpf, horario, posi):
    z = Paciente(nome, cpf, horario)
    p = q = self._top
    if self._top == None:
      self._top = z
    elif self.size_lista() <= posi:
      while p.get_prox() != None:
        p = p.get_prox()
      p.set_prox(z)
      z.set_prox(None)
    else:
      for i in range(posi):
        q = q.get_prox()
      for j in range(posi - 1):
        p = p.get_prox()
      z.set_prox(q)
      p.set_prox(z)

  def pop_lista(self,posi):
    p = q = self._top
    if self._top == None:
      return 'A Lista já está vazia'
    elif self.size_lista() <= posi:
      if p.get_prox() != None:
        while p.get_prox().get_prox() != None:
          p = p.get_prox()
        p.set_prox(None)
      else:
        self._top = None
    else:
      for i in range(posi):
        q = q.get_prox()
      for j in range(posi - 1):
        p = p.get_prox()
      p.set_prox(q.get_prox())
      q = None
    return 'Remoção feita com sucesso' 

  def isempty_lista(self):
    if self._top == None:
      return True
    else:
      return False

  def size_lista(self):
    if self._top == None:
      return 'A estrutura não possui nemhum elemento'
    else:
      tam = 0
      p = self._top
      while p != None:
        tam += 1
        p = p.get_prox()
      return tam

  def element_lista(self,posi):
    if self._top == None:
      return 'O valor do elemento é',None
    elif self.size_lista() <= posi:
      return 'Essa posição é maior que o tamanho da lista'
    else:
      p = self._top
      for i in range(posi):
        p = p.get_prox()
      return 'Paciente {}: Nome: {}\tCPF: {}\tHorario: {}'.format(posi, p.get_nome(), p.get_cpf(), p.get_horario())

#Print#
  def __str__(self):
    p = self._top
    v = ''
    while p != None:
      v += '[Nome:' + p.get_nome() + '\tCPF:' + p.get_cpf() + '\tHorário Marcado:' + p.get_horario() + ']' + '\n'
      p = p.get_prox()
    return 'Lista:\n{}'.format(v)
   
