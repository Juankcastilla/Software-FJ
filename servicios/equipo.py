
from modelos.servicio import Servicio
from excepciones.errores import DatosInvalidos, ErrorServicio


class Equipo(Servicio):
    """
    Servicio especializado para el alquiler de equipos tecnologicos.

    El costo depende de la cantidad de equipos alquilados
    y del numero de dias de alquiler.
    """

    def __init__(self, nombre, descripcion, precio_base, stock_disponible):
        super().__init__(nombre, descripcion, precio_base)

        self.__stock_disponible = None
        self.stock_disponible = stock_disponible

    @property
    def stock_disponible(self):
        return self.__stock_disponible

    @stock_disponible.setter
    def stock_disponible(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise DatosInvalidos("El inventario debe ser un numero entero.")

        if valor < 0:
            raise DatosInvalidos("El inventario no puede ser negativo.")

        self.__stock_disponible = valor

    def validar_parametros(self, cantidad=1, dias=1):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise DatosInvalidos("La cantidad de equipos debe ser un entero.")

        if cantidad <= 0:
            raise DatosInvalidos("Debe alquilar al menos un equipo.")

        if isinstance(dias, bool) or not isinstance(dias, int):
            raise DatosInvalidos("Los dias de alquiler deben ser un entero.")

        if dias <= 0:
            raise DatosInvalidos("Los dias de alquiler deben ser mayores que cero.")

        if cantidad > self.__stock_disponible:
            raise ErrorServicio(
                f"Solo hay {self.__stock_disponible} equipos disponibles."
            )

        self.verificar_disponibilidad()
        return True

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0, dias=1):
        self.validar_parametros(cantidad, dias)

        subtotal = self.precio_base * cantidad * dias

        total = self.aplicar_descuento_impuesto(
            subtotal, descuento, impuesto
        )

        return total

    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Servicio: Alquiler de equipos | "
            f"Nombre: {self.nombre} | "
            f"Descripcion: {self.descripcion} | "
            f"Precio por equipo/dia: ${self.precio_base:,.2f} | "
            f"Inventario: {self.__stock_disponible} equipos | "
            f"Estado: {estado} | "
            f"ID: {self.id}"
        )
