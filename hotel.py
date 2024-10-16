#objetos principales:
#Habitacion: tipo(individual o doble), numero habitacion, disponibilidad,noches_reservadas,reservante.
#Huesped: nombre,identificacion.
#Hotel: gestiona la reservacion de habitaciones.

#relaciones
#El huesped puede reservar una o mas habitaciones.
#Una habitacion solo puede ser reservada por una persona.
#El hotel gestiona que habitaciones estan disponibles o reservadas y quien las reserva.
import random
class Habitacion:
    def __init__(self,
                 numero_habitacion,
                 reservante = None,
                 disponibilidad = True, 
                 tipo = "individual",
                 noches_reservadas=0,):
        
        self.numero_habitacion = numero_habitacion
        self.reservante = reservante
        self.disponibilidad = disponibilidad
        self.tipo = tipo
        self.noches_reservadas = noches_reservadas
    
    def reservar(self,reservante,noches_reservadas):
        self.reservante = reservante
        self.noches_reservadas = noches_reservadas
        self.disponibilidad = False


    def __str__(self):
        return (
        f"habitacion numero '{self.numero_habitacion}' ({self.tipo})" 
        f" se encuentra '{'disponible' if self.disponibilidad else 'no disponible'}'"
        f" esta reservada por {self.noches_reservadas} noches"
        f" y fue reservada por '{'nadie' if self.reservante is None else self.reservante}'")
    
    def __repr__(self):
        return self.__str__()  # Llama a __str__ para la representación
    
class Huesped:
    def __init__(self,nombre,identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
    


class Hotel:
    def __init__(self,nombre,N_habitaciones):
        self.nombre= nombre
        self.N_habitaciones = N_habitaciones
        self.huespedes = []
        self.habitaciones = []
        self.tipo = ["individual","doble"]
        for i in range(N_habitaciones):
            self.habitacion = Habitacion(i,tipo=random.choice(self.tipo))
            self.habitaciones.append(self.habitacion)

    def ver_habitaciones(self):
        return self.habitaciones

    def reservar_habitacion(self,tipo,reservante,noches_reservadas):
        habitacion_reservada = False
        for habitacion in self.habitaciones:
            if habitacion.tipo == tipo and habitacion.disponibilidad == True:
                habitacion.reservar(reservante,noches_reservadas)
                print(f"la habitacion # {habitacion.numero_habitacion} ha sido reservada")
                habitacion_reservada = True
                break
        if not habitacion_reservada:
                print("No hay habitaciones disponibles")


    def registrar_huesped(self,huesped):
        
        if isinstance(huesped,Huesped):
            self.huespedes.append(huesped)
            print(f"el huesped {huesped.nombre} con id '{huesped.identificacion}' ha sido reistrado exitosamente!!!")
        else:
            print(f"No se pudo registrar el huesped.")    

huesped1 = Huesped("jorgen","3438SF83'LBC")
hotel1 = Hotel("pasaje Aristi",10)
hotel1.registrar_huesped(huesped1)
hotel1.reservar_habitacion("individual","jorge",3)
Habitaciones_reservadas = [hr for hr in hotel1.habitaciones if not hr.disponibilidad]
print(Habitaciones_reservadas)
