
"""
Excepciones personalizadas del sistema Software FJ.

Estas clases permiten identificar y controlar los diferentes
errores que pueden presentarse durante la ejecución.
"""


# Excepción general del sistema
class ErrorSistema(Exception):
    """Clase base para los errores personalizados del sistema."""
    pass


# Errores relacionados con los clientes
class ErrorCliente(ErrorSistema):
    """Se utiliza cuando existe un problema con un cliente."""
    pass


# Errores relacionados con los servicios
class ErrorServicio(ErrorSistema):
    """Se utiliza cuando existe un problema con un servicio."""
    pass


# Error cuando un servicio no está disponible
class ServicioNoDisponible(ErrorServicio):
    """Se genera cuando se intenta utilizar un servicio no disponible."""
    pass


# Errores relacionados con las reservas
class ErrorReserva(ErrorSistema):
    """Se utiliza cuando existe un problema con una reserva."""
    pass


# Error cuando una operación no está permitida
class OperacionNoPermitida(ErrorSistema):
    """Se genera cuando se intenta realizar una operación incorrecta."""
    pass


# Error cuando los datos ingresados no son válidos
class DatosInvalidos(ErrorSistema):
    """Se genera cuando los datos no cumplen las validaciones."""
    pass


# Error cuando se intenta registrar información duplicada
class RegistroDuplicado(ErrorSistema):
    """Se genera cuando un registro ya existe en el sistema."""
    pass
