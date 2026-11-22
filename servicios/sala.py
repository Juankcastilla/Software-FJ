
# Importamos la clase abstracta Servicio
from modelos.servicio import Servicio

# Importamos las excepciones personalizadas
from excepciones.errores import DatosInvalidos, ErrorServicio

# Importamos herramientas para validar numeros
import math


class Sala(Servicio):
    """
    Servicio especializado para la reserva de salas.

    El costo se calcula de acuerdo con las horas contratadas
    y la tarifa establecida por hora.
    """

    def __init__(self, nombre, descripcion, precio_base, capacidad_maxima):

        # Inicializamos los atributos heredados de Servicio
        super().__init__(nombre, descripcion, precio_base)

        # Atributo privado de capacidad
        self.__capacidad_maxima = None

        # Validamos la capacidad de la sala
        self.capacidad_maxima = capacidad_maxima

    # ==========================================
    # PROPIEDAD: CAPACIDAD MAXIMA
    # ==========================================

    @property
    def capacidad_maxima(self):
        return self.__capacidad_maxima

    @capacidad_maxima.setter
    def capacidad_maxima(self, valor):

        if isinstance(valor, bool) or not isinstance(valor, int):
            raise DatosInvalidos("La capacidad debe ser un numero entero.")

        if valor <= 0:
            raise DatosInvalidos("La capacidad debe ser mayor que cero.")

        self.__capacidad_maxima = valor

    # ==========================================
    # VALIDAR PARAMETROS
    # ==========================================

    def validar_parametros(self, cantidad=1, personas=1):
        """
        Valida las horas de reserva y la cantidad de personas.
        """

        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
            raise DatosInvalidos("Las horas deben ser un valor numerico.")

        if not math.isfinite(cantidad) or cantidad <= 0:
            raise DatosInvalidos("Las horas deben ser mayores que cero.")

        if isinstance(personas, bool) or not isinstance(personas, int):
            raise DatosInvalidos("La cantidad de personas debe ser un entero.")

        if personas <= 0:
            raise DatosInvalidos("Debe existir al menos una persona.")

        if personas > self.__capacidad_maxima:
            raise ErrorServicio(
                f"La sala permite maximo {self.__capacidad_maxima} personas."
            )

        self.verificar_disponibilidad()

        return True

    # ==========================================
    # CALCULAR COSTO
    # ==========================================

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        """
        Calcula el costo de la reserva por horas.

        cantidad: numero de horas contratadas.
        descuento: porcentaje de descuento.
        impuesto: porcentaje de impuesto.
        """

        self.validar_parametros(cantidad)

        subtotal = self.precio_base * cantidad

        total = self.aplicar_descuento_impuesto(
            subtotal,
            descuento,
            impuesto
        )

        return total

    # ==========================================
    # DESCRIBIR SERVICIO
    # ==========================================

    def describir(self):
        """Devuelve la informacion del servicio de salas."""

        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Servicio: Reserva de salas | "
            f"Nombre: {self.nombre} | "
            f"Descripcion: {self.descripcion} | "
            f"Precio por hora: ${self.precio_base:,.2f} | "
            f"Capacidad: {self.__capacidad_maxima} personas | "
            f"Estado: {estado} | "
            f"ID: {self.id}"
        )
