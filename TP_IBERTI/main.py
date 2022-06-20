import os 
from uuid import uuid4


def main():
    print("**************************************************************************")
    print("Gestionador de usuarios by Anderson Ocana")
    
    print("Para iniciar el programa, deberá indicar el Area y el jefe de área:")
    
    area,jefe_area = [input("Ingrese nombre del area: ") or "ventas" ,input("Ingrese nombre del jefe de area: ") or "No jefe"]
    
    nomina = NominaSector(area,jefe_area)
    
    print("**************************************************************************")
    print("Seleccione las opciones posibles\nPara salir ingrese \"exit\"")

    
    while True:
        os.system('cls')
        opcion = input("""
        1: Listar Empleados
        2: Crear Empleados
        3: Busqueda Empleados
        4: Calculo de Nomina Empleados
        5: Exportar Nomina en archivo CSV
        6: Cerrar el programa o default vacio
        """)
        
        if opcion == "1":
            nomina.listar_nomina()
        elif opcion == "2":
            empleado = Employees(uuid4().hex)
            nomina.add_empleado(empleado)
        elif opcion == "3":
            gestionador = Gestionador()
            nomina.gestion(gestionador)
        elif opcion == "4":
            nomina.calcular_nomina_general()
        elif opcion == "5":
            nomina.save_nomina(data := input("Nombre del archivo") or None)
        else:
            print("Gracias por usar el programa")
            print("**************************************************************************")
            break
        print("**************************************************************************")
main()
