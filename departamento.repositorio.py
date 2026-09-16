import sqlite3

class DepartamentoRepositorio:
    def __init__(self, db_path="ecotech.db"):
        self.db_path = db_path
        self._crear_tablas()

    def _crear_tablas(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            cursor = conn.cursor()
            # Tabla de departamentos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_depto TEXT NOT NULL,
                    gerente TEXT NOT NULL
                )
            """)
            # Tabla empleado modificada para la relación de Agregación (Sin CASCADE)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado (
                    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    departamento_id INTEGER,
                    FOREIGN KEY (departamento_id) REFERENCES departamento(id_departamento) ON DELETE SET NULL
                )
            """)
            conn.commit()

    def crear(self, nombre_depto: str, gerente: str) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO departamento (nombre_depto, gerente) VALUES (?, ?)",
                (nombre_depto, gerente)
            )
            conn.commit()
            return cursor.lastrowid

    def consultar_por_id(self, id_departamento: int) -> dict:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departamento WHERE id_departamento = ?", (id_departamento,))
            row = cursor.fetchone()
            if row:
                return {"id_departamento": row[0], "nombre_depto": row[1], "gerente": row[2]}
            return None

    def listar_todos(self) -> list:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departamento")
            return [{"id_departamento": r[0], "nombre_depto": r[1], "gerente": r[2]} for r in cursor.fetchall()]

    def actualizar(self, id_departamento: int, nombre_depto: str, gerente: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE departamento SET nombre_depto = ?, gerente = ? WHERE id_departamento = ?",
                (nombre_depto, gerente, id_departamento)
            )
            conn.commit()

    def eliminar(self, id_departamento: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM departamento WHERE id_departamento = ?", (id_departamento,))
            conn.commit()
            
    def asignar_empleado_db(self, id_empleado: int, id_departamento: int):
        """Persiste la vinculación del empleado con el departamento."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE empleado SET departamento_id = ? WHERE id_empleado = ?",
                (id_departamento, id_empleado)
            )
            conn.commit()
