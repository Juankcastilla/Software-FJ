
from modelos.cliente import Cliente
from modelos.servicio import Servicio
from modelos.reserva import Reserva

from excepciones.errores import (
    DatosInvalidos,
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    RegistroDuplicado
)

import logging
from pathlib import Path


class SistemaGestion:
    """
    Clase principal para administrar el sistema Software FJ.

    Permite registrar y consultar clientes, servicios y reservas.
    La informacion se almacena en listas durante la ejecucion.
    """

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        self.__configurar_logs()

        self.logger.info("Sistema Software FJ iniciado correctamente.")

    def __configurar_logs(self):
        """Configura el archivo donde se guardan los registros."""

        carpeta_logs = Path(__file__).resolve().parent.parent / "logs"
        carpeta_logs.mkdir(exist_ok=True)

        archivo_log = carpeta_logs / "sistema.log"

        self.logger = logging.getLogger("SoftwareFJ")
        self.logger.setLevel(logging.INFO)

        # Evita crear varios registros iguales.
        if not self.logger.handlers:
            manejador = logging.FileHandler(
                archivo_log,
                encoding="utf-8"
            )

            formato = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            manejador.setFormatter(formato)
            self.logger.addHandler(manejador)

    # --------------------------------------------------
    # REGISTRO DE CLIENTES
    # --------------------------------------------------

    def registrar_cliente(self, cliente):
        """Registra un cliente si no existe previamente."""

        try:
            if not isinstance(cliente, Cliente):
                raise DatosInvalidos(
                    "El registro requiere un objeto Cliente."
                )

            for registrado in self.__clientes:
                if registrado.correo == cliente.correo:
                    raise RegistroDuplicado(
                        "Ya existe un cliente con ese correo."
                    )

            self.__clientes.append(cliente)

        except Exception:
            self.logger.exception("Error al registrar un cliente.")
            raise

        else:
            self.logger.info(
                f"Cliente registrado: {cliente.nombre}"
            )
            return True

        finally:
            self.logger.debug("Finalizo el proceso de registro de cliente.")

    # --------------------------------------------------
    # REGISTRO DE SERVICIOS
    # --------------------------------------------------

    def registrar_servicio(self, servicio):
        """Registra un servicio si no existe previamente."""

        try:
            if not isinstance(servicio, Servicio):
                raise DatosInvalidos(
                    "El registro requiere un objeto Servicio."
                )

            for registrado in self.__servicios:
                if registrado.nombre.lower() == servicio.nombre.lower():
                    raise RegistroDuplicado(
                        "Ya existe un servicio con ese nombre."
                    )

            self.__servicios.append(servicio)

        except Exception:
            self.logger.exception("Error al registrar un servicio.")
            raise

        else:
            self.logger.info(
                f"Servicio registrado: {servicio.nombre}"
            )
            return True

        finally:
            self.logger.debug("Finalizo el proceso de registro de servicio.")

    # --------------------------------------------------
    # REGISTRO DE RESERVAS
    # --------------------------------------------------

    def registrar_reserva(self, reserva):
        """Registra una reserva de un cliente y servicio existentes."""

        try:
            if not isinstance(reserva, Reserva):
                raise DatosInvalidos(
                    "El registro requiere un objeto Reserva."
                )

            if reserva.cliente not in self.__clientes:
                raise ErrorReserva(
                    "El cliente no se encuentra registrado en el sistema."
                )

            if reserva.servicio not in self.__servicios:
                raise ErrorReserva(
                    "El servicio no se encuentra registrado en el sistema."
                )

            for registrada in self.__reservas:
                if registrada.id == reserva.id:
                    raise RegistroDuplicado(
                        "La reserva ya se encuentra registrada."
                    )

            self.__reservas.append(reserva)

        except Exception:
            self.logger.exception("Error al registrar una reserva.")
            raise

        else:
            self.logger.info(
                f"Reserva registrada: {reserva.id}"
            )
            return True

        finally:
            self.logger.debug("Finalizo el proceso de registro de reserva.")

    # --------------------------------------------------
    # BUSQUEDA DE CLIENTES
    # --------------------------------------------------

    def buscar_cliente(self, identificador):
        """Busca un cliente por su ID o correo electrónico."""

        for cliente in self.__clientes:
            if (
                cliente.id == identificador
                or cliente.correo == identificador.lower()
            ):
                return cliente

        raise ErrorCliente("No se encontro el cliente solicitado.")

    # --------------------------------------------------
    # BUSQUEDA DE SERVICIOS
    # --------------------------------------------------

    def buscar_servicio(self, identificador):
        """Busca un servicio por su ID o nombre."""

        for servicio in self.__servicios:
            if (
                servicio.id == identificador
                or servicio.nombre.lower() == identificador.lower()
            ):
                return servicio

        raise ErrorServicio("No se encontro el servicio solicitado.")

    # --------------------------------------------------
    # BUSQUEDA DE RESERVAS
    # --------------------------------------------------

    def buscar_reserva(self, identificador):
        """Busca una reserva mediante su ID."""

        for reserva in self.__reservas:
            if reserva.id == identificador:
                return reserva

        raise ErrorReserva("No se encontro la reserva solicitada.")

    # --------------------------------------------------
    # CONSULTA DE REGISTROS
    # --------------------------------------------------

    def listar_clientes(self):
        """Retorna todos los clientes registrados."""
        return list(self.__clientes)

    def listar_servicios(self):
        """Retorna todos los servicios registrados."""
        return list(self.__servicios)

    def listar_reservas(self):
        """Retorna todas las reservas registradas."""
        return list(self.__reservas)

    def mostrar_resumen(self):
        """Retorna un resumen de los registros del sistema."""

        return (
            f"Clientes registrados: {len(self.__clientes)}\n"
            f"Servicios registrados: {len(self.__servicios)}\n"
            f"Reservas registradas: {len(self.__reservas)}"
        )
