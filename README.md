# Siatema de Gestion Ecotech Solutions

Proyecto de desarrollado en Python para la asignatura de Programacion Orientada a Objetos. El sistema gestiona departamentos, empleados y registros de tiempo con persistencia en SQL y consumo de API externa.

# Caracteristicas Principales

- Modelo POO: Aplicacion de Herencia, Encapsulamiento y Poliformismo en la liquidacion de sueldos.
- Persitencia de Datos: Base de datos SQLite (`ecotech.db`) con restricciones de integridad y operaciones CRUD.
- Servicio Externo:Consumo de la API de indicadores económicos (`mindicador.cl`) mediante la librería `requests` con manejo de timeouts y estrategia de degradación grácil.

# Requisitos Previos

- Python 3.10 o superior.
- Librerías listadas en `requirements.txt`.

# Instalacion de Dependencias necesaria:
1. Instalar dependencias necesarias:
    ```bash
    pip intall -r requeriments.txt

2. Ejecutar el sistema Cprincipal:
  
  python main.py
