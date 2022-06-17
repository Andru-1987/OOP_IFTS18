from uuid import uuid4

class Persona:
    def __init__(self,nombre,dni,apellido):
        self.__id = uuid4().hex
        self.__dni = dni
        self.__nombre = nombre
        self.apellido =apellido
        print(f"Usuario ID {self.get_id()} ha sido exitosamente creado")

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_id(self):
        return self.__id


class Empleado(Persona):
    __sueldo = None

    def __init__(self,nombre,dni,apellido,puesto = "cadete",area = "unknow"):
        super().__init__(nombre,dni,apellido)
        self.puesto = puesto
        self.area = area


    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self,sueldo):
        self.__sueldo = sueldo

    def get_area(self):
        print(f"Area: {self.area}")
        return self.area

    def __str__(self):
        return f"ID: {super().get_id()}\nNombre: {super().get_nombre()}\nArea: {self.area}\n{self.get_sueldo()} pesos"


    def __dict__(self):
        return {
                "id":super().get_id(),
                "nombre": super().get_nombre(),
                "apellido":self.apellido,
                "dni": super().get_dni(),
                "status":self.get_status(),
                "puesto":self.puesto,
                "area": self.area}

class EmpleadoTemp(Empleado):
    __status = "temporal"
    cant_horas = 0
    valor_hora = 0
    
    def __init__(self,nombre,apellido,dni,puesto = "cadete",area = "unknow"):
        super().__init__(nombre,dni,apellido,puesto,area)

    def set_precio_horas(self, cant_horas = 20, valor_hora = 1_000):
        self.cant_horas = cant_horas
        self.valor_hora = valor_hora
        valor_final = self.valor_hora * self.cant_horas
        super().set_sueldo(valor_final)

    def calcular_sueldo(self):
        return super().get_sueldo()
    
    def get_status(self):
        return self.__status

    def __str__(self):
        return super().__str__() + "\nEmpleado Temp"

    def __dict__(self):
        data = {"sueldo":super().get_sueldo(),
                "sueldo_total": self.calcular_sueldo(),
                "horas":self.cant_horas,
                "valor_hora":self.valor_hora,
                "cantidad_horas_extras":None,
                "valor_hora_extras":None
                }
        
        return {**super().__dict__(),**data}
    

class EmpleadoFijo(Empleado):
    __status = "fijo"
    __extras = 0
    __cant_horas = 0
    __valor_hora = 0
    
    def __init__(self,nombre,apellido,dni,puesto = "cadete",area = "unknow"):
        super().__init__(nombre,dni,apellido,puesto,area)

    def set_sueldo_base(self, sueldo_base = 50_000):
        super().set_sueldo(sueldo_base)

    def set_horas_extras(self,cant_horas = 0,valor_hora = 1_000):
        self.__valor_hora = valor_hora
        self.__cant_horas = cant_horas
        self.__extras = self.get_valor_hora() * self.get_cant_horas()  

    def get_extras(self):
        return self.__extras

    def calcular_sueldo(self):
        return self.get_extras() + super().get_sueldo()

    def get_valor_hora(self):
        return self.__valor_hora

    def get_cant_horas(self):
        return self.__cant_horas
    
    def get_status(self):
        return self.__status

    
    def __str__(self):
        return super().__str__() + "\nEmpleado Fijo"


    def __dict__(self):
        data={"sueldo":super().get_sueldo(),
              "sueldo_total": self.calcular_sueldo(),
              "horas":None,
              "valor_hora": None,
              "cantidad_horas_extras":self.get_cant_horas(),
              "valor_hora_extras":self.get_valor_hora()
             }
        return {**super().__dict__(),**data}
