
class NominaSector():
  areas_disponibles = ["contabilidad","logistica","administracio","ventas"]

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
