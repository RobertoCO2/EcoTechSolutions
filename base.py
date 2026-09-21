import sqlite3
def crear_tablas():
    with sqlite3.connect("ecotech.db") as conexion:
        conexion.execute("PRAGMA foreign_keys = ON;")
        cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departamento (
            id_departamento      INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_departamento  TEXT NOT NULL UNIQUE,
            gerente              TEXT NOT NULL )""")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleado(
            id_empleado         INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo     TEXT NOT NULL,
            fono_contacto       TEXT NOT NULL,
            email_corporativo   TEXT NOT NULL UNIQUE,
            renta_base          REAL NOT NULL,
            tipo_empleado       TEXT NOT NULL,
            departamento_id     INTEGER,
            FOREIGN KEY (departamento_id) REFERENCES departamento(id_departamento) ON DELETE SET NULL )""")
    

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proyecto (
            id_proyecto      INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_proyecto  TEXT NOT NULL UNIQUE,
            nombre_proyecto  TEXT NOT NULL,
            presupuesto      REAL NOT NULL)""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registro_tiempo (
            id_registro         INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_registro      TEXT NOT NULL,
            cantidad_horas      REAL NOT NULL,
            detalle_actividad   TEXT NOT NULL,
            empleado_id         INTEGER NOT NULL,
            proyecto_id         INTEGER NOT NULL,
            FOREIGN KEY (empleado_id) REFERENCES empleado(id_empleado) ON DELETE CASCADE,
            FOREIGN KEY (proyecto_id) REFERENCES proyecto(id_proyecto) ON DELETE CASCADE)""")

   
    print(" Base de datos 'ecotech.db' y tablas creada exitosamente.")

if __name__ =="__main__":
    crear_tablas()

