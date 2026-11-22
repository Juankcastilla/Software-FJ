
from modelos.entidad import Entidad
from modelos.cliente import Cliente
from modelos.servicio import Servicio
from servicios.sala import Sala
from servicios.equipo import Equipo
from servicios.asesoria import Asesoria
from excepciones.errores import (
    DatosInvalidos,
    ErrorCliente,
    ErrorReserva,
    OperacionNoPermitida
)
import math


class Reserva(Entidad):
    """
    Representa una reserva realizada por un cliente.

    Relaciona un cliente con un servicio y permite calcular
    el costo, confirmar o cancelar la reserva.
    """

    def __init__(self, cliente, servicio, duracion, cantidad=1, personas=1):
        super().__init__()

        if not isinstance(cliente, Cliente):
            raise DatosInvalidos("La reserva requiere un cliente valido.")

        if not isinstance(servicio, Servicio):
            raise DatosInvalidos("La reserva requiere un servicio valido.")

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise DatosInvalidos("La duracion debe ser numerica.")

        if not math.isfinite(duracion) or duracion <= 0:
            raise DatosInvalidos("La duracion debe ser mayor que cero.")

        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise DatosInvalidos("La cantidad debe ser un entero mayor que cero.")

        if isinstance(personas, bool) or not isinstance(personas, int) or personas <= 0:
            raise DatosInvalidos("La cantidad de personas debe ser un entero mayor que cero.")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__cantidad = cantidad
        self.__personas = personas
        self.__costo_total = 0.0
        self.__estado = "Pendiente"

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def personas(self):
        return self.__personas

    @property
    def costo_total(self):
        return self.__costo_total

    @property
    def estado(self):
        return self.__estado

    def procesar(self, descuento=0, impuesto=0):
        """
        Valida y calcula el costo de la reserva.

        El cálculo se adapta al tipo de servicio contratado.
        """

        if self.__estado == "Cancelada":
            raise OperacionNoPermitida(
                "No se puede procesar una reserva cancelada."
            )

        if self.__estado == "Confirmada":
            raise OperacionNoPermitida(
                "La reserva ya se encuentra confirmada."
            )

        try:
            if not self.__cliente.activo:
                raise ErrorCliente(
                    "No se puede reservar con un cliente inactivo."
                )

            if isinstance(self.__servicio, Sala):
                self.__servicio.validar_parametros(
                    cantidad=self.__duracion,
                    personas=self.__personas
                )

                total = self.__servicio.calcular_costo(
                    cantidad=self.__duracion,
                    descuento=descuento,
                    impuesto=impuesto
                )

            elif isinstance(self.__servicio, Equipo):
                total = self.__servicio.calcular_costo(
                    cantidad=self.__cantidad,
                    dias=self.__duracion,
                    descuento=descuento,
                    impuesto=impuesto
                )

            elif isinstance(self.__servicio, Asesoria):
                total = self.__servicio.calcular_costo(
                    cantidad=self.__duracion,
                    descuento=descuento,
                    impuesto=impuesto
                )

            else:
                raise ErrorReserva(
                    "El tipo de servicio no es compatible con la reserva."
                )

        except Exception as error:
            raise ErrorReserva(
                "No fue posible procesar la reserva."
            ) from error

        else:
            self.__costo_total = total
            self.__estado = "Confirmada"
            return self.__costo_total

    def confirmar(self, descuento=0, impuesto=0):
        """Confirma la reserva y calcula su costo."""
        return self.procesar(descuento, impuesto)

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.__estado == "Cancelada":
            raise OperacionNoPermitida(
                "La reserva ya se encuentra cancelada."
            )

        self.__estado = "Cancelada"
        return True

    def describir(self):
        return (
            f"Reserva: {self.id} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duracion: {self.__duracion} | "
            f"Cantidad: {self.__cantidad} | "
            f"Personas: {self.__personas} | "
            f"Costo: ${self.__costo_total:,.2f} | "
            f"Estado: {self.__estado}"
        )

    def __str__(self):
        return self.describir()
