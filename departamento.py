class Departamento:
    def __init__(self, id_departamento: int, nombre_depto: str, gerente: str):
        self.id_departamento = id_departamento
        self.nombre_depto = nombre_depto
        self.gerente = gerente
        self.colaboradores = []  # Lista local en memoria para gestión de agregación

    def asignar_colaborador(self, empleado):
        """Asigna un colaborador al departamento si no está ya incluido."""
        if empleado not in self.colaboradores:
            self.colaboradores.append(empleado)
            # Asumiendo que el objeto empleado tiene un atributo departamento_id
            empleado.departamento_id = self.id_departamento

    def reasignar_colaborador(self, empleado, nuevo_departamento):
        """Remueve al colaborador y delega la asignación al nuevo departamento."""
        if empleado in self.colaboradores:
            self.colaboradores.remove(empleado)
        nuevo_departamento.asignar_colaborador(empleado)
