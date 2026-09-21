import sqlite3


class RegistroTiempo:
    def __init__(self, fecha_registro: str, cantidad_horas: float, detalle_actividad: str, trabajador, proyecto_asociado):

        if cantidad_horas <= 0 or cantidad_horas > 24:
            raise ValueError("La cantidad de horas debe estar entre 0.1 y 24.")
        
        self.fecha_registro = fecha_registro
        self.cantidad_horas = cantidad_horas
        self.detalle_actividad = detalle_actividad
        self.trabajador = trabajador
        self.proyecto_asociado = proyecto_asociado

    def mostrar_bitacora(self):
        nombre = getattr(
            self.trabajador, "nombre_completo", str(self.trabajador)
        )
        print(
            f"{self.fecha_registro} | {nombre} | {self.cantidad_horas} horas |"
            f" {self.detalle_actividad}")

class RegistroTiempoRepositorio:
    def __init__(self, db_path="ecotech.db"):
        self.db_path = db_path

    def guardar_registro(self, registro: RegistroTiempo):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("PRAGMA foreign_keys = ON;")
                cursor = conn.cursor()
                emp_id = getattr(
                    registro.trabajador, "id_empleado", registro.trabajador)
                prj_id = getattr(
                    registro.proyecto_asociado,
                    "id_proyecto",
                    registro.proyecto_asociado,)
                cursor.execute(
                    """ INSERT INTO registro_tiempo (fecha_registro, cantidad_horas, detalle_actividad,
                    empleado_id, proyecto_id)
                    VALUES (?, ?, ?, ?, ?) """,
                    ( str(registro.fecha_registro),
                     registro.cantidad_horas,
                     registro.detalle_actividad, emp_id, prj_id),)
                
                conn.commit()
                print("Registro de tiempo guardado exitosamente en SQLITE.")
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error al giardar registro de tiempo: {e}")
            return None

    def filtrar_por_empleado(self, empleado_id: int) -> list:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT id_registro, fecha_registro, cantidad_horas,"
                     "detalle_actividad, empleado_id, proyecto_id FROM "
                     "registro_tiempo WHERE empleado_id =?",
                     (empleado_id,),)
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al filtrar po empleado: {e}")
            return []

    def filtrar_por_proyecto(self, proyecto_id: int)-> list:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                SELECT id_registro, fecha_registro, cantidad_horas,
                detalle_actividad, empleado_id, proyecto_id FROM registro_tiempo
                WHERE proyecto_id = ?""", (proyecto_id,),)

                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al filtrar por proyecto: {e}")
            return []
           