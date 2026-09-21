class Proyecto:
    def __init__(self, codigo_proyecto, nombre_proyecto, presupuesto):
        self.codigo_proyecto = codigo_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.presupuesto = presupuesto
        self.__equipo_asignado = []

    def mostrar_resumen(self):
        print(f"[Codigo: {self.codigo_proyecto}] - {self.nombre_proyecto} | Presupuesto: ${self.presupuesto:,.0f}")

    def asociar_miembro(self, emp):
        self.__equipo_asignado.append(emp)
        print(f" {emp.nombre_completo} asociado al proyecto {self.nombre_proyecto}")

    def remover_miembro(self, emp):
        if emp in self.__equipo_asignado:
            self.__equipo_asignado.remove(emp)
            print(f" {emp.nombre_completo} removido de {self.nombre_proyecto}")

    def obtener_equipo(self):
        return self.__equipo_asignado
    
if __name__ == "__main__":
    p1 = Proyecto("PRJ-01", "Paneles Solares Valparaíso", 15000000.0)
    print(f"Proyecto: {p1.nombre_proyecto} | Presupuesto: ${p1.presupuesto:,.0f}")