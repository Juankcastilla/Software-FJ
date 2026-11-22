
from modelos.servicio import Servicio
from excepciones.errores import DatosInvalidos
import math


class Asesoria(Servicio):
    """
    Servicio especializado para asesorias profesionales.

    El costo se calcula de acuerdo con las horas contratadas
    y la tarifa establecida por hora.
    """

    def __init__(self, nombre, descripcion, precio_base, especialidad):
        super().__init__(nombre, descripcion, precio_base)

        self.__especialidad = None
        self.especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise DatosInvalidos(
                "La especialidad de la asesoria es obligatoria."
            )

        self.__especialidad = valor.strip()

    def validar_parametros(self, cantidad=1):
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
            raise DatosInvalidos(
                "Las horas de asesoria deben ser un valor numerico."
            )

        if not math.isfinite(cantidad) or cantidad <= 0:
            raise DatosInvalidos(
                "Las horas de asesoria deben ser mayores que cero."
            )

        self.verificar_disponibilidad()

        return True

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        self.validar_parametros(cantidad)

        subtotal = self.precio_base * cantidad

        total = self.aplicar_descuento_impuesto(
            subtotal,
            descuento,
            impuesto
        )

        return total

    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Servicio: Asesoria profesional | "
            f"Nombre: {self.nombre} | "
            f"Descripcion: {self.descripcion} | "
            f"Especialidad: {self.__especialidad} | "
            f"Precio por hora: ${self.precio_base:,.2f} | "
            f"Estado: {estado} | "
            f"ID: {self.id}"
        )
