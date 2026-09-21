from departamento import Departamento
from proyecto import Proyecto
from empleado import EmpleadoPlanta, EmpleadoContratista
from registro_tiempo import RegistroTiempo
from empleado_repositorio import EmpleadoRepositorio
from base import crear_tablas

def ejecutar_sistema():
    print("============================================")
    print("=== SISTEMA DE GESTIÓN ECOTECH SOLUTIONS ===")
    print("============================================\n")

    crear_tablas()
    depto = Departamento(1, "Desarrollo Sostenible", "María Paz Rojas")
    proyecto = Proyecto("PRJ-01", "Paneles Solares Valparaíso", 15000000.0)

    emp_planta = EmpleadoPlanta(101, "María Paz Rojas", "+56911112222", "maria.rojas@ecotech.cl", 850000.0, 150000.0)
    emp_contratista = EmpleadoContratista(202, "Carlos Mendoza", "+56933334444", "carlos.mendoza@ecotech.cl", 5000.0)
    emp_contratista.registrar_horas(160)
                                            
    depto.asignar_colaborador(emp_planta)
    depto.asignar_colaborador(emp_contratista)
    proyecto.asociar_miembro(emp_planta)
    proyecto.asociar_miembro(emp_contratista)

    registro = RegistroTiempo(
        fecha_registro="2026-09-10",
        cantidad_horas=8.5,
        detalle_actividad="Instalación e inspección de inversores fotovoltaicos",
        trabajador=emp_planta,
        proyecto_asociado=proyecto)

    print("\n--- LIQUIDACION DE NOMINA ---")
    for emp in [emp_planta, emp_contratista]:
        print(f" {emp.nombre_completo} | Sueldo Líquido: ${emp.calcular_sueldo_liquido():,.0f}")

    print("\n--- REGISTRO TIEMPO ---")
    registro.mostrar_bitacora()

    repo = EmpleadoRepositorio()
    

    print("\n--- 1. Guardando Empleados en la Base de Datos ---")
    repo.guardar(emp_planta)
    repo.guardar(emp_contratista)
   
    print("\n--- 2. Actualizando telefono de Empleado ---")
    filas_upd = repo.actualizar_fono(emp_planta.id_empleado, "+56999998888")
    if filas_upd > 0:
        print("Telefono actualizado correctamente en SQLite.")

    print("\n--- 3. Probando metodo Eliminar ---")
    filas_afectadas = repo.eliminar(emp_planta.id_empleado)
    if filas_afectadas > 0:
        print(f"Empleado eliminado con exito.")
    else:
        print("No se encontro ningun empleado con ese ID.")

    print("\n--- 4. Consultando lista de empleados actualizada ---")
    lista = repo.obtener_todos()
    for e in lista:
        print(f"ID: {e.id_empleado} | Nombre: {e.nombre_completo}")

if __name__ == "__main__":
    ejecutar_sistema()
