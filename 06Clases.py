class Persona:
   #ATRIBUTO DE CLASE
   especie = "humano"

   #METODO DE INSTANCIA
   def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    #METODO DE INSTANCIA
   def saludar(self):
      print(f'Hola, mi nombre es {self.nombre}')


   def cumplir_anios(self, estado_humor):
      print(f'Cumplir {self.edad + 1} años me pone {estado_humor}')

juan = Persona("Juan", 37)

juan.saludar()
juan.cumplir_anios("feliz")


#IMPPRIMIR SOLO EL NOMBRE


#IMPRIMIR SOLO LA EDAD