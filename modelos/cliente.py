
# Importamos la clase abstracta Entidad
from modelos.entidad import Entidad

# Importamos nuestras excepciones personalizadas
from excepciones.errores import DatosInvalidos, ErrorCliente

# Importamos herramientas para validar el correo
import re


class Cliente(Entidad):
    """
    Representa un cliente de Software FJ.

    Hereda de Entidad y permite almacenar información personal
    mediante atributos privados y validaciones.
    """

    def __init__(self, nombre, correo, telefono):

        # Inicializamos los atributos de la clase padre
        super().__init__()

        # Atributos privados del cliente
        self.__nombre = None
        self.__correo = None
        self.__telefono = None
        self.__activo = True

        # Validamos los datos utilizando sus propiedades
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # ==========================================
    # PROPIEDAD: NOMBRE
    # ==========================================

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not isinstance(valor, str):
            raise DatosInvalidos("El nombre debe ser texto.")

        valor = valor.strip()

        if len(valor) < 3:
            raise DatosInvalidos("El nombre debe tener al menos 3 caracteres.")

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]+", valor):
            raise DatosInvalidos("El nombre contiene caracteres no permitidos.")

        self.__nombre = valor

    # ==========================================
    # PROPIEDAD: CORREO
    # ==========================================

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if not isinstance(valor, str):
            raise DatosInvalidos("El correo debe ser texto.")

        valor = valor.strip().lower()

        patron = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(patron, valor):
            raise DatosInvalidos("El correo electrónico no es válido.")

        self.__correo = valor

    # ==========================================
    # PROPIEDAD: TELEFONO
    # ==========================================

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        if not isinstance(valor, str):
            raise DatosInvalidos("El teléfono debe ingresarse como texto.")

        # Permitimos espacios y el signo + en el teléfono
        telefono_limpio = valor.replace(" ", "").replace("-", "")

        if telefono_limpio.startswith("+"):
            telefono_limpio = telefono_limpio[1:]

        if not telefono_limpio.isdigit():
            raise DatosInvalidos("El teléfono solo debe contener números.")

        if not 7 <= len(telefono_limpio) <= 15:
            raise DatosInvalidos("El teléfono debe tener entre 7 y 15 dígitos.")

        self.__telefono = valor.strip()

    # ==========================================
    # PROPIEDAD: ESTADO DEL CLIENTE
    # ==========================================

    @property
    def activo(self):
        return self.__activo

    # ==========================================
    # METODOS DE GESTION
    # ==========================================

    def desactivar(self):
        """Desactiva un cliente."""

        if not self.__activo:
            raise ErrorCliente("El cliente ya se encuentra desactivado.")

        self.__activo = False

    def activar(self):
        """Activa nuevamente un cliente."""

        if self.__activo:
            raise ErrorCliente("El cliente ya se encuentra activo.")

        self.__activo = True

    def describir(self):
        """Implementación del método abstracto de Entidad."""

        estado = "Activo" if self.__activo else "Inactivo"

        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono} | "
            f"Estado: {estado} | "
            f"ID: {self.id}"
        )

    def __str__(self):
        """Representación del cliente como texto."""

        return self.describir()
