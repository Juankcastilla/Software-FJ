
# Importamos las herramientas necesarias para crear clases abstractas
from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Entidad(ABC):
    """
    Clase abstracta principal del sistema Software FJ.

    Representa una entidad general que puede tener un identificador
    y una fecha de creación.
    """

    def __init__(self):
        # Atributos privados para aplicar encapsulamiento
        self.__id = str(uuid.uuid4())[:8].upper()
        self.__fecha_creacion = datetime.now()

    # Propiedad para consultar el identificador
    @property
    def id(self):
        return self.__id

    # Propiedad para consultar la fecha de creación
    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    # Método abstracto que deben implementar las clases hijas
    @abstractmethod
    def describir(self):
        pass
