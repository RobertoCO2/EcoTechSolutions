import sqlite3
from departamento import Departamento

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

    def guardar(self, departamento: Departamento):

        try:       
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO departamento (nombre_depto, gerente) VALUES (?, ?)",
                    (departamento.nombre_depto, departamento.gerente), )
                
                conn.commit()
                departamento.id_departamento = cursor.lastrowid
                print( f"Departamento '{departamento.nombre_depto}' guardado con ID {departamento.id_departamento}")
                return departamento
        except sqlite3.Error as e:
            print(f"Error al guardar departamento: {e}")
            return None
        
    def consultar_por_id(self, id_departamento: int) -> dict:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departamento WHERE id_departamento = ?", (id_departamento,))
            row = cursor.fetchone()
            if row:
                return {"id_departamento": row[0], "nombre_depto": row[1], "gerente": row[2]}
            return None

    def listar_todos(self) -> list:
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id\_departamento, nombre\_depto, gerente FROM departamento ORDER BY nombre\_depto")
                return [Departamento(nombre_depto=r[1], gerente=r[2], id_departamento=r) for r in cursor.fetchall()]
        except sqlite3.error as e:
            print(f"Error al listar deaprtamentos: {e}")
            return []
        
    def actualizar(self, id_departamento: int, nombre_depto: str, gerente: str):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE departamento SET nombre_depto = ?, gerente = ? WHERE id_departamento = ?",
                    (nombre_depto, gerente, id_departamento)
                )
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            print(f"Error al actualizar departamento: {e}")
            return 0
            
    def eliminar(self, id_departamento: int):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("PRAGMA foreign_keys = ON;")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM departamento WHERE id_departamento = ?", (id_departamento,))
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            print(f"Error al eliminar departamento: {e}")
            return 0
            
    def asignar_empleado_db(self, id_empleado: int, id_departamento: int):
        """Persiste la vinculación del empleado con el departamento."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE empleado SET departamento_id = ? WHERE id_empleado = ?",
                    (id_departamento, id_empleado) )
                
                conn.commit()
                return cursor.rowcount
        except sqlite3.Error as e:
            print(f"Error al asignar empleado al departamento: {e}")
            return 0
