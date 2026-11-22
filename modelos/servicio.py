
# Importamos la clase abstracta Entidad
from modelos.entidad import Entidad

# Importamos nuestras excepciones personalizadas
from excepciones.errores import DatosInvalidos, ErrorServicio

# Importamos herramientas para validar valores numericos
import math

from abc import abstractmethod

class Servicio(Entidad):
    """
    Clase abstracta que representa un servicio de Software FJ.

    Todos los servicios especializados heredaran esta estructura
    y deberan implementar sus propios metodos.
    """

    def __init__(self, nombre, descripcion, precio_base):

        # Inicializamos la clase padre
        super().__init__()

        # Atributos privados
        self.__nombre = None
        self.__descripcion = None
        self.__precio_base = None
        self.__disponible = True

        # Validamos los datos mediante las propiedades
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_base = precio_base

    # ==========================================
    # PROPIEDAD: NOMBRE
    # ==========================================

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not isinstance(valor, str) or not valor.strip():
            raise DatosInvalidos("El nombre del servicio es obligatorio.")

        self.__nombre = valor.strip()

    # ==========================================
    # PROPIEDAD: DESCRIPCION
    # ==========================================

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):

        if not isinstance(valor, str) or not valor.strip():
            raise DatosInvalidos("La descripcion del servicio es obligatoria.")

        self.__descripcion = valor.strip()

    # ==========================================
    # PROPIEDAD: PRECIO BASE
    # ==========================================

    @property
    def precio_base(self):
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, valor):

        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise DatosInvalidos("El precio debe ser un valor numerico.")

        if not math.isfinite(valor) or valor <= 0:
            raise DatosInvalidos("El precio debe ser mayor que cero.")

        self.__precio_base = float(valor)

    # ==========================================
    # PROPIEDAD: DISPONIBILIDAD
    # ==========================================

    @property
    def disponible(self):
        return self.__disponible

    def desactivar(self):
        """Desactiva temporalmente el servicio."""

        if not self.__disponible:
            raise ErrorServicio("El servicio ya esta desactivado.")

        self.__disponible = False

    def activar(self):
        """Activa nuevamente el servicio."""

        if self.__disponible:
            raise ErrorServicio("El servicio ya esta disponible.")

        self.__disponible = True

    def verificar_disponibilidad(self):
        """Comprueba si el servicio puede utilizarse."""

        if not self.__disponible:
            raise ErrorServicio("El servicio no se encuentra disponible.")

        return True

    # ==========================================
    # METODO AUXILIAR PARA CALCULAR COSTOS
    # ==========================================

    def aplicar_descuento_impuesto(self, subtotal, descuento=0, impuesto=0):
        """
        Aplica un descuento y posteriormente un impuesto.

        Los porcentajes se reciben como numeros entre 0 y 100.
        """

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
            raise DatosInvalidos("El descuento debe ser numerico.")

        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):
            raise DatosInvalidos("El impuesto debe ser numerico.")

        if not math.isfinite(descuento) or not 0 <= descuento <= 100:
            raise DatosInvalidos("El descuento debe estar entre 0 y 100.")

        if not math.isfinite(impuesto) or not 0 <= impuesto <= 100:
            raise DatosInvalidos("El impuesto debe estar entre 0 y 100.")

        valor_descuento = subtotal * (descuento / 100)
        subtotal_descuento = subtotal - valor_descuento

        valor_impuesto = subtotal_descuento * (impuesto / 100)

        total = subtotal_descuento + valor_impuesto

        return round(total, 2)

    # ==========================================
    # METODOS ABSTRACTOS
    # ==========================================

    @abstractmethod
    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        """
        Cada servicio implementara su propia forma de calcular costos.
        """
        pass

    @abstractmethod
    def validar_parametros(self, cantidad=1):
        """
        Cada servicio validara sus propios parametros.
        """
        pass

    @abstractmethod
    def describir(self):
        """
        Cada servicio tendra su propia descripcion.
        """
        pass
