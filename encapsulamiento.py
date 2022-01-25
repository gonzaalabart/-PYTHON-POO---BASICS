'''Hace referencia a la capacidad que tiene un objeto de ocultar su estado, de manera que sus datos solo se puedan modificar por medio de las operaciones (métodos) que ofrece.
Por defecto, en Python, todos los atributos de una clase (atributos de datos y métodos) son públicos.
No obstante, hay una forma de indicar en Python que un atributo, ya sea un dato o un método, es interno a una clase y no se debería utilizar fuera de ella.  Esto es usando el carácter guión bajo _atributo antes del nombre del atributo que queramos ocultar.'''

class A:
  def __init__(self):
    self._contador = 0 #Atributo Privado
  
  def incrementa(self):
    self._contador += 1
  
  def cuenta(self):
    return self._contador

class B(object):
  def __init__(self):
    self.__contador = 0 #Atributo privado utilizando __, hace que el identificador sea literalmente reemplazado por el texto _Clase__atributo, donde Clase es el nombre de la clase actual.
  
  def incrementa(self):
    self.__contador += 1
  
  def cuenta(self):
    return self.__contador

a = A()
a.incrementa()
a.incrementa()
a.incrementa()
print(a.cuenta())

b = B()
b.incrementa()
b.incrementa()
print(b.cuenta())
print(b.__contador)