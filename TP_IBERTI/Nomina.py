import csv
import json
from datetime import datetime

class NominaSector():
    areas_disponibles = ["contabilidad","logistica","administracion","ventas"]
    
    empleados = []
    
    total_nomina = 0
    
    def __init__(self,area,jefe_area):
   
        while(area not in self.areas_disponibles):
            print(f"Sector : {area} no es valida\nSector: ")
            for sector in self.areas_disponibles:
                print(f"{sector}")

            area = (input("Ingrese el sector correcto\t")).lower()

        else:
            self.area = area
            
            self.jefe_area = None if jefe_area != None else jefe_area
            
            print("Se ha creado exitosamente")
    
    
    def add_empleado(self, employees):
        import json
        
        print("Como desea generar usuarios?\n1: CSV\n2: Manual")
        option =  input() or None
        
        while option != None:
            if option =="1":
                print("******************************************************")
                path = input("Indique la ruta:\t")
                self.empleados += employees.add_by_csv(path)
                
            elif option == "2":
                print("******************************************************")
                print("Carga manual")
                self.empleados += employees.add_manually()
            else:
                break
            print("Desea ingresar nuevos usuarios?\n1: CSV\n2: Manual")
            option =  input() or None
        else:
            print("Opcion no valida, no se genera Carga")
            
        print(self.empleados)

    def gestion(self, gestionador): 
        
        input_dict = {}
        key = input("Ingrese parametro de búsqueda: ")
        input_dict[key] = input("Ingrese valor de búsqueda: ")
        
        self.empleados = gestionador.gestionar_empleados(self.empleados, **input_dict)
    
    
    def carga_nomina(self):
        contador = 0
        verificar = (input("Desea ingresar un empleado? \"Si\" o \"No\"")).lower() or "s"
        while verificar not in ["n","no"]:
            self.add_empleado()
            contador+=1
            verificar = (input("Desea ingresar un empleado? \"Si\" o \"No\"")).lower() or "s"
        else:
            print(f"Termino la carga de {contador} empleados")
            
    def calcular_nomina_general(self):
        if len(self.empleados) != 0:
            print("Mostramos toda la nomina separada por nomina fija y temporal")
            nomina_fija = 0
            nomina_temporal = 0
            for empleado in self.empleados:
                print(f'Nombre del empleado: {empleado.get("nombre")}, sueldo = {empleado.get("sueldo_total",0)}')
                self.total_nomina += empleado.get("sueldo_total",0)
                if empleado.get("status") == "fijo":
                    nomina_fija += empleado.get("sueldo_total", 0)
                else:
                    nomina_temporal += empleado.get("sueldo_total")
            print(f"Total nomina Temporal {nomina_temporal}\tTotal nomina fija {nomina_temporal}")
            print(f"Total Nomina = {self.total_nomina}")
        
        return self.total_nomina

            
    def listar_nomina(self):
        if len(self.empleados) != 0:
            for empleado in self.empleados:
                print(empleado)
        return self.empleados
                
    def save_nomina(self):
        time = datetime.now()
        
        print(self.empleados)
        
        data_keys = None if len(self.empleados) == 0 else self.empleados[0].keys()
        
        
        name_file = time.strftime("%b_%d")+"_data.csv"
        
        if data_keys is not None:
            with open(name_file,"w",newline = "") as output:
                dict_writer = csv.DictWriter(output,data_keys)
                dict_writer.writeheader()
                dict_writer.writerows(self.empleados)
            print("El archivo ha sido creado con exito")
        else:
            print("No hay empleados")
