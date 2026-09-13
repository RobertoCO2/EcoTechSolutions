import sqlite3
def crear_tablas():
    conexion = sqlite3.connect("ecotech.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DEPARTAMENTO (
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre  TEXT NOT NULL UNIQUE)""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleado(
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo     TEXT NOT NULL,
            fono_contacto       TEXT NOT NULL,
            email_corporativo   TEXT NOT NULL UNIQUE,
            renta_base          REAL NOT NULL,
            tipo_empleado       TEXT NOT NULL )""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proyecto (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo         TEXT NOT NULL UNIQUE,
            nombre         TEXT NOT NULL,
            presupuesto    REAL NOT NULL)""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registro_tiempo (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_registro      TEXT NOT NULL,
            cantidad_horas      REAL NOT NULL,
            detalle_actividad   TEXT NOT NULL,
            empleado_id         INTEGER NOT NULL,
            proyecto_id         INTEGER NOT NULL,
            FOREIGN KEY (empleado_id) REFERENCES empleado(id) ON DELETE CASCADE,
            FOREIGN KEY (proyecto_id) REFERENCES proyecto(id) ON DELETE CASCADE)""")

    conexion.commit()
    conexion.close()
    print(" Base de datos 'ecotech.db' y tablas creada exitosamente.")

if __name__ =="__main__":
    crear_tablas()

