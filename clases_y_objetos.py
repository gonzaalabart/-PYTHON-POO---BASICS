class Coche:
  
  '''Esta clase define el estado y el comportamiento de un coche'''
  ruedas = 4

  def __init__(self, color, aceleracion):
    self.color = color
    self.aceleracion = aceleracion
    self.velocidad = 0
  
  def acelera(self):
    self.velocidad = self.velocidad + self.aceleracion

  def frena(self):
    v = self.velocidad - self.aceleracion
    if v < 0:
      v = 0
    self.velocidad = v

# Creando Objetos
c1 = Coche('rojo', 20)
print(c1.color)
print(c1.ruedas)
c2 = Coche('azul', 30)
print(c2.color)
print(c2.aceleracion)
print(c1.velocidad)
c1.acelera()
print(c1.velocidad)
print(c1.velocidad)
c1.marchas = 6
print(c1.marchas)
# print(c2.marchas)    ... AttributeError, object has no attribute 'marchas'

#Dos formas de llamar al metodo acelera():

c1.acelera()
Coche.acelera(c2)
print(c1.velocidad)
print(c2.velocidad)

# Atributo de clase != atributo de instancia, modificar el atributo de clase modifica a todas las instancias, no al reves
print(c2.ruedas)
Coche.ruedas = 6
print(c2.ruedas)