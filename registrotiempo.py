import sqlite3


class RegistroTiempo:
    def __init__(self, fecha_registro, cantidad_horas, detalle_actividad, trabajador, proyecto_asociado):
        self.fecha_registro = fecha_registro
        self.cantidad_horas = cantidad_horas
        self.detalle_actividad = detalle_actividad
        self.trabajador = trabajador
        self.proyecto_asociado = proyecto_asociado

    def mostrar_bitacora(self):
        print(
            f"{self.fecha_registro} | {self.trabajador.nombre_completo} | "
            f"{self.cantidad_horas} horas | {self.detalle_actividad}"
        )

class RegistroTiempoRepositorio:
    def __init__(self, db_path="ecotech.db"):
        self.db_path = db_path
        self._crear_tablas()

    def _crear_tablas(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            cursor = conn.cursor()
            # Tabla del proyecto (entidad requerida para la clave foránea)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_proyecto TEXT NOT NULL
                )
            """)
            # Tabla registro_tiempo estructurada como relación de Composición (ON DELETE CASCADE)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registro_tiempo (
                    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    cantidad_horas REAL NOT NULL,
                    descripcion TEXT,
                    empleado_id INTEGER NOT NULL,
                    proyecto_id INTEGER NOT NULL,
                    FOREIGN KEY (empleado_id) REFERENCES empleado(id_empleado) ON DELETE CASCADE,
                    FOREIGN KEY (proyecto_id) REFERENCES proyecto(id_proyecto)
                )
            """)
            conn.commit()

    def guardar_registro(self, registro: RegistroTiempo):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO registro_tiempo (fecha, cantidad_horas, descripcion, empleado_id, proyecto_id)
                VALUES (?, ?, ?, ?, ?)
            """, (str(registro.fecha), registro.cantidad_hours, registro.descripcion, registro.empleado_id, registro.proyecto_id))
            conn.commit()

    def filtrar_por_empleado(self, empleado_id: int) -> list:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM registro_tiempo WHERE empleado_id = ?", (empleado_id,))
            return cursor.fetchall()

    def filtrar_por_proyecto(self, proyecto_id: int) -> list:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM registro_tiempo WHERE proyecto_id = ?", (proyecto_id,))
            return cursor.fetchall()
