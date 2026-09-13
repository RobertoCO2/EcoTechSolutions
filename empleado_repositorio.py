import sqlite3
from empleado import EmpleadoPlanta, EmpleadoContratista

class EmpleadoRepositorio:
    def __init__(self, ruta="ecotech.db"):
        self.ruta = ruta

    def guardar(self, empleado):
        """C (CREATE): Inserta un empleado en la base de datos."""
        try:
            with sqlite3.connect(self.ruta) as con:
                tipo = "Planta" if isinstance(empleado, EmpleadoPlanta) else "Contratista"
                cur = con.execute("""
                    INSERT INTO empleado(nombre_completo, fono_contacto, email_corporativo, renta_base,tipo_empleado)
                    VALUES (?, ?, ?, ?, ?)
                """, (empleado.nombre_completo, empleado.obtener_fono(), empleado.obtener_email(), empleado.obtener_renta_base(), tipo))

                empleado.id_empleado =cur.lastrowid
                print(f" Empleado '{empleado.nombre_completo}' guardado con ID {empleado.id_empleado}")
                return empleado

        except sqlite3.IntegrityError:
            print(f" Error: El correo '{empleado.obtener_email()}' ya esta registrado.")
        except sqlite3.Error as e:
            print(f" Error de base de datos: {e}")

    def obtener_todos(self):
        """R (Read): Obtiene todos los empleados y los devuelve como objeto de Python."""
        try:
            with sqlite3.connect(self.ruta) as con:
                filas = con.execute("""
                    SELECT id, nombre_completo, fono_contacto, email_corporativo, renta_base, tipo_empleado
                    FROM empleado ORDER BY nombre_completo
                    """).fetchall()

                empleados = []
                for f in filas:
                    # f[0]:id, f[1]:nombre, f[2]fono, f[3]:email, f[4]:renta, f[5]:tipo
                    if f[5] == "Planta":
                        emp = EmpleadoPlanta(f[0], f[1], f[2], f[3], f[4])
                    else:
                        emp = EmpleadoContratista(f[0], f[1], f[2], f[3], f[4])
                    empleados.append(emp)
                return empleados
        except sqlite3.Error as e:
            print(f" Error al consultar empleados: {e}")
            return []

if __name__ =="__main__":
    repo = EmpleadoRepositorio()

    print("\n--- 1. Guardado Empleado en SQLite ---")
    emp1 = EmpleadoPlanta(1, "Maria Paz Rojas", "+56911112222", "m.pazs@ecotech.cl", 850000.0, 150000.0)
    repo.guardar(emp1)

    print("\n--- 2. Consultando Empleados desde SQLite ---")
    lista = repo.obtener_todos()
    for e in lista:
        print(f" ID: {e.id_empleado} | Nombre: {e.nombre_completo} | Correo: {e.obtener_email()}")


    