import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                  (id INTEGER PRIMARY KEY, nombre TEXT, salario REAL)''')

# Insertar múltiples registros
empleados = [
    ('Juan Ignacio Font', 2500.50),
    ('Geronimo Font', 2700.00),
    ('Ayrton Cornaglia', 3000.00)
]

cursor.executemany("INSERT INTO empleados (nombre, salario) VALUES (?, ?)", empleados)

# Guardar cambios
conexion.commit()

# Consultar todos los registros
cursor.execute("SELECT * FROM empleados")
resultados = cursor.fetchall()

for empleado in resultados:
    print(empleado)

# Cerrar la conexión
conexion.close()