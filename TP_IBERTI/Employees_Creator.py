class Employees:
    status = ""
    
    def __init__(self,tag):
        self.status = tag
        
    def add_manually(self):
        data = (input("Que empleado desea cargar?\nTemporal o Fijo")).lower() or "fijo"
        print(f"El empleado será {data}")
        nombre = (input("Ingrese nombre\t")).lower()
        apellido = (input("Ingrese apellido\t")).lower()
        dni = input("Ingrese dni: \t")
        dni = int(dni) if dni.isdigit() else 0
        area = input("Ingrese el area del empleado\n") or "Not related"
        puesto = (input("Ingrese puesto\t")).lower() or None

        if(data != "temporal"):
            salario_base = float(input("Salario Base : ") or 0) 
            selector = (input("Cuenta con horas extras? SI or No")).lower() or "no"
            
            empleado = EmpleadoFijo(nombre,apellido,dni,puesto,area)
            empleado.set_sueldo(salario_base)

            if (selector == "s" or selector =="si"):
                cant_horas = float(input("Ingrese cantidad de horas \t")) or None
                valor_hora = float(input("Ingrese valor por hora \t")) or None
                empleado.set_horas_extras(cant_horas,valor_hora)

        else:
            horas = float(input("Horas realizadas: ") or 0)
            valor = float(input("Valor por hora : ") or 0)
            empleado = EmpleadoTemp(nombre,apellido,dni,puesto,area)
            empleado.set_precio_horas(horas,valor)
            
        return [empleado.__dict__()]
    
    def add_by_csv(self,path:str)->list:
        import pandas as pd
        
        if path != None:
            employees = pd.read_csv(path).to_dict('records')
            return employees
        else: 
            print("No data")
