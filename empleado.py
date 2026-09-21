from datetime import date

class Empleado:

    def __init__(self, id_empleado, nombre_completo, fono_contacto,email_corporativo, renta_base):
        self.id_empleado = id_empleado
        self.nombre_completo = nombre_completo
        self.__fono_contacto =fono_contacto
        self.__email_corporativo = email_corporativo
        self.__fecha_contrato = date.today().isoformat()
        self.__renta_base = renta_base
        self.__esta_activo = True

    def obtener_renta_base(self)-> float:
        return self.__renta_base

    def obtener_fono(self)-> str:
        return self.__fono_contacto

    def obtener_email(self) -> str:
        return self.__email_corporativo

    def obtener_fecha_contrato(self) -> str:
        return self.__fecha_contrato
    
    def esta_activo(self)-> bool:
        return self.__esta_activo

    def actualizar_fono(self, nuevo_fono: str):
        if len(nuevo_fono) >=8:
            self.__fono_contacto = nuevo_fono
            print(f" Telefono de {self.nombre_completo} actualizado a : {self.__fono_contacto}")
        else:
            print("Numero de telefono no valido.")

    def calcular_sueldo_liquido(self)-> float:
        return self.__renta_base

class EmpleadoPlanta(Empleado):
    def __init__(self, id_empleado, nombre_completo, fono_contacto,email_corporativo, renta_base, bono_mensual=0.0):
        super().__init__(id_empleado, nombre_completo, fono_contacto, email_corporativo, renta_base)
        self.__bono_mensual = bono_mensual

    def calcular_sueldo_liquido(self) -> float:
        return self.obtener_renta_base() + self.__bono_mensual

class EmpleadoContratista(Empleado):
   
    def __init__(self, id_empleado, nombre_completo, fono_contacto, email_corporativo, valor_hora= 0.0, renta_base=0.0, horas_mensuales=0.0):
        super().__init__(id_empleado, nombre_completo, fono_contacto, email_corporativo, renta_base)
        self.__valor_hora = valor_hora
        self.__horas_mensuales = horas_mensuales
 
    def registrar_horas(self, cant_horas: float):
        if cant_horas > 0:
            self.__horas_mensuales += cant_horas
            print(f" Se registraron {cant_horas} horas a {self.nombre_completo}")

    def calcular_sueldo_liquido(self) -> float:
        return self.__valor_hora * self.__horas_mensuales
if __name__ == "__main__":
    emp_planta = EmpleadoPlanta(101, "Maria Paz Rojas", "+56911112222", "m.paz@ecotech.cl", 850000.0, 150000.0)
    emp_contratista = EmpleadoContratista(202, "Carlos Mendoza", "+56933334444", "c.mendoza@ecotech.cl", 5000.0)
    emp_contratista.registrar_horas(160)

    nomina = [emp_planta, emp_contratista]

    print("===LIQUIDACION DE SUELDOS ECOTECH ===")
    for e in nomina:
        print(f" {e.nombre_completo} | Sueldo Liquido: ${e.calcular_sueldo_liquido():,.0f}")