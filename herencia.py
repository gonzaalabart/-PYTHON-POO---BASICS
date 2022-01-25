'''La herencia es la capacidad de reutilizar una clase extendiendo su funcionalidad. Una clase que hereda de otra puede añadir nuevos atributos, ocultarlos, añadir nuevos métodos o redefinirlos.
 El nombre de la clase padre se indica entre paréntesis a continuación del nombre de la clase hija.
'''
from clases_y_objetos import Coche


class CocheVolador(Coche):

  ruedas = 8

  def __init__(self, color, aceleracion, esta_volando = False):
    super().__init__(color, aceleracion)
    self.esta_volando = esta_volando

# Funcion super() devuelve un objeto temporal de la superclase que permite invocar a los metodos en la misma. 
  def vuela(self):
    self.esta_volando = True
  
  def aterriza(self):
    self.esta_volando = False

c = Coche('azul', 10)
cv1  = CocheVolador('rojo', 60)
print(cv1.color)
print(cv1.esta_volando)
cv1.acelera()
print(cv1.velocidad)
print(cv1.ruedas)
# print(c.esta_volando) da error porque el atributo esta volando es solo para objetos de la clase CocheVolador no para instancias de la clase Coche


'''FUNCIONES ISINSTANCE() E  ISSUBCLASS()'''
print(type(c))
'''isinstance(objeto, clase) True = 'objeto' es de la 'clase' o de una de sus clases hijas.
isubclass(clase, claseinfo) comprueba la herencia de clases. True = if 'clase' sea una subclase de 'claseinfo' '''

print(isinstance(c, Coche))
print(isinstance(c, CocheVolador))
print(issubclass(Coche, CocheVolador))
print(issubclass(CocheVolador, Coche))


# HERENCIA MULTIPLE

class A:
  def print_a(self):
    print('a')

class B:
  def print_b(self):
    print('b')

class C(A, B):
  def print_c(self):
    print('c')

c = C()

c.print_a()
c.print_b()
c.print_c()