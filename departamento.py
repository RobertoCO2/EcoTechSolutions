class Departamento:
    def __init__(self, nombre_depto, jefe_area=None):
        self.nombre_depto = nombre_depto
        self.jefe_area = jefe_area
        self.lista_colaboradores = []

    def asignar_colaborador(self, colaborador):
        self.lista_colaboradores.append(colaborador)
        print(f" {colaborador.nombre_completo} asignado a {self.nombre_depto}")

if __name__ == "__main__":
    depto1 = Departamento("Investigacion y Desarrollo")
    depto2 = Departamento("Recursos Humanos")

    lista_deptos = [depto1, depto2]
    for d in lista_deptos:  
        print("Departamento:", d.nombre_depto)