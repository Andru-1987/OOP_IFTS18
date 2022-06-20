class Gestionador:
    
    def gestionar_empleados(empleados,**kwargs):
        import json
        init_len = len(empleados)
        key= None
        value = None

        for a,b in kwargs.items():
            key = a
            value = b

        print(f"Imprime una lista con el siguiente criterio de busqueda {key} = '{value}'")

        key_list = empleados[0].keys() if len(empleados)!=0 else [] 

        if len(empleados) != 0 and (key in key_list):
            new_list =[empleado for empleado in empleados if empleado.get(key)==value]
            if len(new_list)!=0:
                for empleado in new_list:
                    print( json.dumps(empleado ,indent = 1))
            else:
                print("No existe ningún empleado con ese criterio de busqueda")
        else:
            print("No hay elementos con esa criteria")


        print("Desea eliminar todos los elementos con esa criteria?\n\tOpcion 1\nDesea eliminar un registro en particular?\n\tOpcion 2\n\tPara ello hay que eliminar usando el ID Opcion 2")
        
        opcion_in= input("Opcion por default \"CANCELA\"")

        if opcion_in == "1":
            temp_list =[empleado for empleado in empleados if not empleado.get(key)==value]
            empleados = temp_list
            return empleados
        elif opcion_in == "2":
            id = input("inserte el id")
            temp_list =[empleado for empleado in empleados if not empleado.get("id")==id]
            empleados = temp_list
            return empleados
        else:
            print("Se cancela la operacion.")
        
        return empleados
