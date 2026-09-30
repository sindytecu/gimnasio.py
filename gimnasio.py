import mysql.connector
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "gimnasio"
)


def clientes():
    clientName = input("INGRESE NOMBRE: ")
    age = int(input("INGRESE EDAD: "))
    membershipType = input("INGRESE MEMBRESIA (Basic / Premium / VIP): ")
    months = int(input("INGRESE MESES: "))

    if membershipType == "Basic":
        finalPrice = 100 * months
    if membershipType == "Premium":
        finalPrice = 175 * months
    if membershipType == "VIP":
        finalPrice = 250 * months

    if months >= 6:
        status = "ActivePlus"
    else:
        status = "Active"

    if conexion.is_connected():
       cursor = conexion.cursor()
       query = "INSERT INTO cliente(clientName, age, membershipType, months, finalPrice, status) VALUES (%s,%s,%s,%s,%s,%s)"
       cursor.execute(query, (clientName, age, membershipType, months, finalPrice, status))
       conexion.commit()
       print("DATOS GUARDADOS")



def consultar():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cliente")
    for fila in cursor.fetchall():
        print(fila)

def actualizar():
    id_cliente = int(input("INGRESE EL ID: "))
    clientName = input("NUEVO NOMBRE: ")
    age = int(input("NUEVA EDAD: "))
    membershipType = input("NUEVA MEMBRERSIA: ")
    months = int(input("NUEVOS MESES: "))

    if membershipType == "Basic":
        finalPrice = 100 * months
    if membershipType == "Premium":
        finalPrice = 175 * months
    if membershipType == "VIP":
        finalPrice = 250 * months

    if months >= 6:
        status = "ActivePlus"
    else:
        status = "Active"

    cursor = conexion.cursor()
    query = "UPDATE cliente SET clientName=%s, age=%s, membershipType=%s, months=%s, finalPrice=%s, status=%s WHERE id=%s"
    cursor.execute(query, (clientName, age, membershipType, months, finalPrice, status, id_cliente))
    conexion.commit()
    print("DATOS ACTUALIZADOS")



def eliminar():
    id_cliente = int(input("INGRESE EL ID A ELIMINAR: "))
    cursor = conexion.cursor()
    query = "DELETE FROM cliente WHERE id=%s"
    cursor.execute(query, (id_cliente,))
    conexion.commit()
    print("DATOS ELIMINADOS")

def menu():
    lista = ["1. Crear", "2. consultar",  "3. actualizar",  "4. eliminar",  "5. salir"]
    for item in lista:
        print(item)
    desis = (input("INGRESE LA OPCION"))

    match desis:
       case "1":
            clientes()
       case "2":
            consultar()
       case "3":
            actualizar()
       case "4":
            eliminar()
       case "5":
            print("SALIENDO")


menu()