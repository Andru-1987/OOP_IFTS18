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
    
    def add_empleado(self, employees):
        import json
        
        print("Como desea generar usuarios?\n1: CSV\n2: Manual")
        option =  input() or None
        
        while option != None:
            if option =="1":
                print("**************************************************************************")
                path = input("Indique la ruta:\t")
                if path != None:
                    self.empleados += employees.add_by_csv(path)
                
            elif option == "2":
                print("**************************************************************************")
                print("Carga manual")
                self.empleados += employees.add_manually()
            else:
                break
            print("Desea ingresar nuevos usuarios?\n1: CSV\n2: Manual\nPor default se cancela")
            option =  input() or None
        else:
            print("Generacion de Carga Exitosa")


    def gestion(self, gestionador): 
        
        input_dict = {}
        key = input("Ingrese parametro de búsqueda: ")
        input_dict[key] = input("Ingrese valor de búsqueda: ")
        
        self.empleados = gestionador.gestionar_empleados(self.empleados, **input_dict)
        
           
    def calcular_nomina_general(self):
        
        if len(self.empleados) != 0:
            print("Mostramos toda la nomina separada por nomina fija y temporal")
        
            nomina_fija = 0
            count_fija = 0
            
            nomina_temporal = 0
            count_temporal = 0
            
            count = 0
            
            for empleado in self.empleados:
                self.total_nomina += empleado.get("sueldo_total",0)
                
                if empleado.get("status") == "fijo":
                    count_fija += 1
                    nomina_fija += empleado.get("sueldo_total", 0)
                elif empleado.get("status") == "temporal":
                    count_temporal += 1
                    nomina_temporal += empleado.get("sueldo_total",0)
                else:
                    count += 1
            print("\nLista empleados Temporal")
            print("**************************************************************************")
            for empleado in self.empleados:
                if empleado.get("status") == "temporal":
                    print(f'Nombre: {empleado.get("nombre")} Sueldo: $ {round(empleado.get("sueldo_total",0),2)}')
            
            print("\nLista empleados Fijo")
            print("**************************************************************************")
            for empleado in self.empleados:
                if empleado.get("status") == "fijo":
                    print(f'Nombre: {empleado.get("nombre")} Sueldo: $ {round(empleado.get("sueldo_total",0),2)}')
                
            print(f"\nCantidad total de usuarios temporales: {count_temporal} empleados")
            print(f"Cantidad total de usuarios fijos: {count_fija} empleados")
            print(f"Cantidad total de usuarios no definidos: {count} empleados")
            
            print(f"\nTotal nomina Temporal $ {round(nomina_temporal,2)}\nTotal nomina Fija $ {round(nomina_temporal,2)}")
            print(f"Total Nomina $ {round(self.total_nomina,2)}")
        else:
            print("No hay nomina")
                                    
        return self.total_nomina

            
    def listar_nomina(self):
        
        if len(self.empleados) != 0:
            for empleado in self.empleados:
                print(json.dumps(empleado, indent = 2))
        else:
            print("No existen empleados")
        
                
    def save_nomina(self, nombre_archivo):
        time = datetime.now()
        
        data_keys = None if len(self.empleados) == 0 else self.empleados[0].keys()
        
        if data_keys is not None:
                    
            if nombre_archivo != "" or nombre_archivo is not None:
                name_file = nombre_archivo +".csv"
            else:
                name_file = time.strftime("%b_%d")+"_data.csv"

            with open(name_file,"w",newline = "") as output:
                dict_writer = csv.DictWriter(output,data_keys)
                dict_writer.writeheader()
                dict_writer.writerows(self.empleados)
            print("El archivo ha sido creado con exito")
        else:
            print("No hay empleados")
