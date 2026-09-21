class Departamento:
    def __init__(self, id_departamento, nombre_depto, gerente):
        self.id_departamento = id_departamento
        self.nombre_depto = nombre_depto
        self.gerente = gerente
        self.__colaboradores = []  # Lista local en memoria para gestión de agregación

    def asignar_colaborador(self, empleado):
        """Asigna un colaborador al departamento si no está ya incluido."""
        if empleado not in self.__colaboradores:
            self.__colaboradores.append(empleado)
           
            empleado.departamento_id = self.id_departamento

    def reasignar_colaborador(self, empleado, nuevo_departamento):
        """Remueve al colaborador y delega la asignación al nuevo departamento."""
        if empleado in self.__colaboradores:
            self.__colaboradores.remove(empleado)
        nuevo_departamento.asignar_colaborador(empleado)

    def obtener_colaboradores(self):
        return self.__colaboradores