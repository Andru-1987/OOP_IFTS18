from users import EmpleadoTemp
from users import EmpleadoFijo

class NominaSector():
    areas_disponibles = ["contabilidad","logistica","administracio","ventas"]
    empleados = []

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
    
    
    def add_empleado(self):
    
    # Creacion de usuario base y carga a la nomina
    
        data = (input("Que empleado desea cargar?\nTemporal o Fijo")).lower() or "fijo"
        print(f"El empleado será {data}")
        nombre = (input("Ingrese nombre\t")).lower()
        apellido = (input("Ingrese apellido\t")).lower()
        dni = int(input("Ingrese dni: \t") or 0)
        area = self.area 
        puesto = (input("Ingrese puesto\t")).lower() or None

        if(data != "temporal"):
            salario_base = float(input("Salario Base : ") or 0)
            selector = (input("Cuenta con horas extras? SI or No")).lower() or "no"
            
            empleado = EmpleadoFijo(nombre,dni,apellido,puesto,self.area)

            if (selector == "s" or selector =="si"):
                cant_horas = float(input("Ingrese cantidad de horas \t")) or None
                valor_hora = float(input("Ingrese valor por hora \t")) or None
                empleado.set_horas_extras(cant_horas,valor_hora)

        else:
            horas = float(input("Horas realizadas: ") or 0)
            valor = float(input("Valor por hora : ") or 0)
            empleado = EmpleadoTemp(nombre,dni,apellido,puesto,self.area)
            empleado.set_precio_horas(horas,valor)
            
        self.empleados.append(empleado)
        return 1



    

    

sector = NominaSector("area", "Miguel")

sector.add_empleado()
sector.add_empleado()


print(sector.empleados)

