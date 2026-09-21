import sqlite3
from proyecto import Proyecto

class ProyectoRepositorio:
    def __init__(self, ruta="ecotech.db"):
        self.ruta = ruta

    def guardar(self, proyecto: Proyecto):
        try:
            with sqlite3.connect(self.ruta) as con:
                cur = con.execute(
                    """ INSERT INTO proyecto (codigo_proyecto, nombre_proyecto, presupuesto)
                    VALUES (?, ?, ?) """,
                (proyecto.codigo_proyecto,
                 proyecto.nombre_proyecto,
                 proyecto.presupuesto), )

                print(f"Proyecto '{proyecto.codigo_proyecto}' guardado exitosamente.")
                return cur.lastrowid

        except sqlite3.IntegrityError:
            print(f"Error: El codigo de proyecto '{proyecto.codigo_proyecto}' ya existe en la base de datos.")
            return None

    def obtener_todos(self) -> list:
        try:
            with sqlite3.connect(self.ruta) as con:
                filas = con.execute("""
                    SELECT codigo_proyecto, nombre_proyecto, presupuesto
                    FROM proyecto ORDER BY nombre_proyecto """). fetchall()

                return [Proyecto(r, r[1], r[2]) for r in filas]
        except sqlite3.Error as e:
            print(f"Error al consultar proyectos: {e}")
            return []

    def obtener_por_codigo(self, codigo: str):
        try:
            with sqlite3.connect(self.ruta) as con:
                row = con.execute("""
                    SELECT codigo_proyecto, nombre_proyecto, presupuesto
                    FROM proyecto WHERE codigo_proyecto = ? """, (codigo,), ).fetchone()       

                if row:
                    return Proyecto(row,row[1], row[2])
                return None
        except sqlite3.Error as e:
            print(f"Error al buscar proyecto por codigo: {e}")
            return None

    def actualizar(self, proyecto: Proyecto) -> int:
        try:
            with sqlite3.connect(self.ruta) as con:
                cur =con.execute("""
                    UPDATE proyecto
                    SET nombre_proyecto = ?, presupesto = ?
                    WHERE codigo_proyecto = ? """, 
                    (proyecto.nombre_proyecto, proyecto.presupuesto, proyecto.codigo_proyecto),)
                return cur.rowcount

        except sqlite3.Error as e:
            print(f"Error al actulaizar proyecto: {e}")
            return 0

    def eliminar(self, codigo: str) -> int:
        try:
            with sqlite3.connect(self.ruta) as con:
                cur = con.execute(
                    "DELETE FROM proyecto WHERE codigo_proyecto = ?", (codigo,),)
                
                return cur.rowcount
        except sqlite3.Error as e:
            print(f"Error al eliminar proyecto: {e}")
            return 0

if __name__ == "__main__":

    repo = ProyectoRepositorio()
    p_test = Proyecto("PRJ-100", "Planta fotovoltaica Norte", 25000000.0)
    repo.guardar(p_test)

    print("\n---Lista de proyectos en la base de datos---")
    for p in repo.obtener_todos():
        p.mostrar_resumen()    