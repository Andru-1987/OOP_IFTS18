from users import EmpleadoTemp
from users import EmpleadoFijo

class NominaSector():
  areas_disponibles = ["contabilidad","logistica","administracio","ventas"]
  empleados = []

  def add_empleado():
  	"""Creacion de usuario base y carga a la nomina
  	"""
  	data = (input("Que empleado desea cargar?\nTemporal\tFijo")).lower()
	nombre = (input("ingrese nombre\t")).lower()
	apellido = (input("ingrese apellido\t")).lower()
	dni = int(input("ingrese dni: \t"))
	area = self.area 
	puesto = (input("ingrese puesto\t")).lower() or None

  	if(data == "fijo"):
  		salario_base = float(input("Salario Base : ")) or None
  		selector = (input("Cuenta con horas extras? SI or No")) or "n"
  		
  		empleado = EmpleadoFijo(nombre,dni,apellido,puesto,area)

  		if (selector == "s" or selector =="si")
	  		cant_horas = float(input("ingrese cantidad de horas \t")) or None
	  		valor_hora = float(input("ingrese valor por hora \t")) or None
	  		empleado.set_horas_extras(cant_horas,valor_hora)
	  	

  	else:
  		empleado = EmpleadoTemp()

  	empleados.append(empleado)
  	return 1

  def __init__(self,area,jefe_area):
   
    while(area not in self.areas_disponibles):
      print(f"Sector : {area} no es valida\nSector: ")
      for sector in self.areas_disponibles:
       print(f"{sector}")
       
      area = (input("Ingrese el sector correcto\t")).lower()
    
    else:
      
      self.area = area
      self.jefe_area = jefe_area
      print("Se ha cargado exitosamente")


    



sector = NominaSector("area", "Miguel")

