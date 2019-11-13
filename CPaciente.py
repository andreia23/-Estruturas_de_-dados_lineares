###Classe Paciente###
class Paciente:
  def __init__(self, nome, cpf, horario, prox = None):
    self._nome = nome
    self._cpf = cpf
    self._horario = horario
    self._prox = prox

#Getters e Setters#
  def get_nome(self):
    return self._nome
    
  def get_cpf(self):
    return self._cpf
    
  def get_horario(self):
    return self._horario

  def get_prox(self):
    return self._prox

  def set_nome(self, novo_nome):
    self._nome = novo_nome
    
  def set_cpf(self, novo_cpf):
    self._cpf = novo_cpf
    
  def set_horario(self, novo_horario):
    self._horario = novo_horario

  def set_prox(self,novo_prox):
    self._prox = novo_prox

#Print#
  def __str__(self):
    return 'NOME:{}\nCPF:{}\nHORÁRIO DE CHEGADA:{}'.format(self._nome, self._cpf, self._horario)
