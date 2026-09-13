from datetime import date
from empleado import EmpleadoPlanta, EmpleadoContratista
from proyecto import Proyecto

class RegistroTiempo:
    def __init__(self, fecha_registro: str, cantidad_horas: float, detalle_actividad: str, trabajador, proyecto_asociado):
        self.fecha_registro = fecha_registro
        self.__cantidad_horas = cantidad_horas
        self.__detalle_actividad = detalle_actividad
        self.trabajador = trabajador
        self.proyecto_asociado = proyecto_asociado

    def validar_jornada(self)-> bool:
        if 0.5 <= self.__cantidad_horas <= 12.0:
            return True
        else:
            return False

    def mostrar_bitacora(self):
        print(f" Fecha: {self.fecha_registro}")
        print(f" Trabajador: {self.trabajador.nombre_completo}")
        print(f" Proyecto: {self.proyecto_asociado.nombre_proyecto}")
        print(f" Horas: {self.__cantidad_horas} hrs | Tarea: {self.__detalle_actividad}")

        if self.validar_jornada():
            print(" Estado: Jornada valida y registrada.")
        else:
            print("Estado: Alerta - Cantidad de horas fuer del rango permitido.")

emp1 = EmpleadoPlanta(101, "María Paz Rojas", "+56911112222", "m.paz@ecotech.cl", 850000.0, 150000.0)
prj1 = Proyecto("PRJ-01", "Paneles Solares Valparaíso", 15000000)

registro1 = RegistroTiempo(
    fecha_registro="2026-09-10",
    cantidad_horas=8.5,
    detalle_actividad="Instalación e inspección de inversores fotovoltaicos",
    trabajador=emp1,
    proyecto_asociado=prj1
)

print("=== BITACORA DE REGISTRO DE TIEMPO ===")
registro1.mostrar_bitacora()