from uuid import uuid4

class Persona:
  def __init__(self,nombre,dni,apellido):
      self.__id = uuid4().hex
      self.__nombre = nombre
      self.apellido =apellido
      print(f"Usuario ID {self.get_id()} ha sido exitosamente creado")

  def get_nombre(self):
      return self.__nombre

  def get_id(self):
      return self.__id

  def __str__(self):
      pass


class Empleado(Persona):
  __sueldo = None

  def __init__(self,nombre,dni,apellido,puesto = "cadete",area = "unknow"):
    super().__init__(nombre,dni,apellido)
    self.puesto = puesto
    self.area = area
    

  def get_sueldo(self):
    if(self.__sueldo != None):
      print(f"Sueldo base {self.__sueldo}")

    return self.__sueldo

  def set_sueldo(self,sueldo):
    self.__sueldo = sueldo

  def get_area(self):
    print(f"Area: {self.area}")
    return self.area

  def __str__(self):
    return f"ID: {super().get_id()}\nNombre: {super().get_nombre()}\nArea: {self.area}\n{self.get_sueldo()} pesos"




class EmpleadoTemp(Empleado):
  
  def __init__(self,nombre,dni,apellido,puesto = "cadete",area = "unknow"):
    super().__init__(nombre,dni,apellido,puesto,area)

  def set_precio_horas(self,precio_hora = 1_000,cant_horas = 20):
    self.cant_horas = cant_horas
    self.precio_hora = precio_hora
    valor_final = self.precio_hora * self.cant_horas
    super().set_sueldo(valor_final)

  def get_sueldo(self):
    return super().get_sueldo()

  def __str__(self):
    return super().__str__() + "\nEmpleado Temp"


class EmpleadoFijo(Empleado):
  def __init__(self,nombre,dni,apellido,puesto = "cadete",area = "unknow"):
    super().__init__(nombre,dni,apellido,puesto,area)

  def set_sueldo_base(self, sueldo_base = 50_000):
    super().set_sueldo(sueldo_base)

  def set_horas_extras(self,cant_horas = 0,valor_hora = 1_000):
    self.__valor_hora = valor_hora
    self.__cant_horas = cant_horas
    self.__extras = self.get_valor_hora() * self.get_cant_horas()  
  
  def get_extras(self):
    return self.__extras

  def calcular_salario(self):
    return self.__extras + super().get_sueldo()

  def get_valor_hora(self):
    return self.__valor_hora

  def get_cant_horas(self):
    return self.__cant_horas
    
  def __str__(self):
    return super().__str__() + "\nEmpleado Fijo"



empleado = EmpleadoFijo("Anderson",93940198,"Ocaña")

print(empleado.get_sueldo())

empleado.set_sueldo_base(80_000)

print(empleado.get_sueldo())

empleado.set_horas_extras(10)

print(empleado.calcular_salario())
