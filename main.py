
from gestion.sistema import SistemaGestion
from modelos.cliente import Cliente
from modelos.reserva import Reserva

from servicios.sala import Sala
from servicios.equipo import Equipo
from servicios.asesoria import Asesoria

from excepciones.errores import ErrorSistema


def mostrar_menu():
    """Muestra las opciones principales del programa."""

    print("\n" + "=" * 45)
    print("       SISTEMA INTEGRAL SOFTWARE FJ")
    print("=" * 45)
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear una reserva")
    print("4. Consultar clientes")
    print("5. Consultar servicios")
    print("6. Consultar reservas")
    print("7. Cancelar una reserva")
    print("8. Consultar resumen del sistema")
    print("9. Salir")
    print("=" * 45)


def registrar_cliente(sistema):
    """Solicita los datos y registra un nuevo cliente."""

    print("\n--- REGISTRO DE CLIENTE ---")

    nombre = input("Nombre completo: ")
    correo = input("Correo electronico: ")
    telefono = input("Telefono: ")

    cliente = Cliente(nombre, correo, telefono)

    sistema.registrar_cliente(cliente)

    print("\nCliente registrado correctamente.")
    print(cliente.describir())


def registrar_servicio(sistema):
    """Permite seleccionar y registrar un servicio."""

    print("\n--- REGISTRO DE SERVICIO ---")
    print("1. Reserva de sala")
    print("2. Alquiler de equipos")
    print("3. Asesoria profesional")

    opcion = input("Seleccione el tipo de servicio: ")

    nombre = input("Nombre del servicio: ")
    descripcion = input("Descripcion: ")
    precio = float(input("Precio base: "))

    if opcion == "1":
        capacidad = int(input("Capacidad maxima de personas: "))

        servicio = Sala(
            nombre,
            descripcion,
            precio,
            capacidad
        )

    elif opcion == "2":
        inventario = int(input("Cantidad de equipos disponibles: "))

        servicio = Equipo(
            nombre,
            descripcion,
            precio,
            inventario
        )

    elif opcion == "3":
        especialidad = input("Especialidad de la asesoria: ")

        servicio = Asesoria(
            nombre,
            descripcion,
            precio,
            especialidad
        )

    else:
        print("Opcion de servicio no valida.")
        return

    sistema.registrar_servicio(servicio)

    print("\nServicio registrado correctamente.")
    print(servicio.describir())


def crear_reserva(sistema):
    """Permite crear y confirmar una reserva."""

    print("\n--- CREACION DE RESERVA ---")

    clientes = sistema.listar_clientes()
    servicios = sistema.listar_servicios()

    if not clientes:
        print("No existen clientes registrados.")
        return

    if not servicios:
        print("No existen servicios registrados.")
        return

    print("\nCLIENTES DISPONIBLES")

    for indice, cliente in enumerate(clientes, start=1):
        print(f"{indice}. {cliente.nombre} - {cliente.correo}")

    opcion_cliente = int(input("Seleccione un cliente: "))

    if not 1 <= opcion_cliente <= len(clientes):
        print("Seleccion de cliente no valida.")
        return

    cliente = clientes[opcion_cliente - 1]

    if not cliente.activo:
        print("El cliente seleccionado esta inactivo.")
        return

    print("\nSERVICIOS DISPONIBLES")

    for indice, servicio in enumerate(servicios, start=1):
        print(f"{indice}. {servicio.nombre} - ${servicio.precio_base:,.2f}")

    opcion_servicio = int(input("Seleccione un servicio: "))

    if not 1 <= opcion_servicio <= len(servicios):
        print("Seleccion de servicio no valida.")
        return

    servicio = servicios[opcion_servicio - 1]

    if not servicio.disponible:
        print("El servicio seleccionado no esta disponible.")
        return

    print("\nDATOS DE LA RESERVA")

    if isinstance(servicio, Equipo):
        cantidad = int(input("Cantidad de equipos: "))
        duracion = int(input("Dias de alquiler: "))
        personas = 1

    elif isinstance(servicio, Sala):
        cantidad = 1
        duracion = float(input("Cantidad de horas: "))
        personas = int(input("Cantidad de personas: "))

    elif isinstance(servicio, Asesoria):
        cantidad = 1
        duracion = float(input("Cantidad de horas: "))
        personas = 1

    else:
        print("Tipo de servicio no reconocido.")
        return

    descuento = float(input("Descuento en porcentaje (0 si no aplica): "))
    impuesto = float(input("Impuesto en porcentaje (0 si no aplica): "))

    reserva = Reserva(
        cliente,
        servicio,
        duracion,
        cantidad,
        personas
    )

    total = reserva.confirmar(
        descuento=descuento,
        impuesto=impuesto
    )

    sistema.registrar_reserva(reserva)

    print("\nReserva creada y confirmada correctamente.")
    print(reserva.describir())
    print(f"Total a pagar: ${total:,.2f}")


def consultar_clientes(sistema):
    """Muestra todos los clientes registrados."""

    print("\n--- LISTADO DE CLIENTES ---")

    clientes = sistema.listar_clientes()

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(cliente.describir())


def consultar_servicios(sistema):
    """Muestra todos los servicios registrados."""

    print("\n--- LISTADO DE SERVICIOS ---")

    servicios = sistema.listar_servicios()

    if not servicios:
        print("No hay servicios registrados.")
        return

    for servicio in servicios:
        print(servicio.describir())


def consultar_reservas(sistema):
    """Muestra todas las reservas registradas."""

    print("\n--- LISTADO DE RESERVAS ---")

    reservas = sistema.listar_reservas()

    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print(reserva.describir())


def cancelar_reserva(sistema):
    """Busca y cancela una reserva."""

    print("\n--- CANCELAR RESERVA ---")

    reservas = sistema.listar_reservas()

    if not reservas:
        print("No existen reservas registradas.")
        return

    for reserva in reservas:
        print(
            f"ID: {reserva.id} | "
            f"Cliente: {reserva.cliente.nombre} | "
            f"Estado: {reserva.estado}"
        )

    identificador = input("\nIngrese el ID de la reserva: ").strip()

    reserva = sistema.buscar_reserva(identificador)
    reserva.cancelar()

    print("Reserva cancelada correctamente.")


def ejecutar_sistema():
    """Controla el funcionamiento general del programa."""

    sistema = SistemaGestion()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                registrar_cliente(sistema)

            elif opcion == "2":
                registrar_servicio(sistema)

            elif opcion == "3":
                crear_reserva(sistema)

            elif opcion == "4":
                consultar_clientes(sistema)

            elif opcion == "5":
                consultar_servicios(sistema)

            elif opcion == "6":
                consultar_reservas(sistema)

            elif opcion == "7":
                cancelar_reserva(sistema)

            elif opcion == "8":
                print("\n--- RESUMEN DEL SISTEMA ---")
                print(sistema.mostrar_resumen())

            elif opcion == "9":
                print("\nGracias por utilizar Software FJ.")
                print("Programa finalizado.")
                break

            else:
                print("Opcion no valida. Intente nuevamente.")

        except ErrorSistema as error:
            print(f"\nError del sistema: {error}")

        except ValueError:
            print("\nError: debe ingresar un valor numerico valido.")

        except Exception as error:
            print(f"\nSe presento un error inesperado: {error}")


if __name__ == "__main__":
    ejecutar_sistema()
