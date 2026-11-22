# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## 1. Descripción del proyecto

Software FJ es un sistema desarrollado en Python que permite administrar clientes, servicios y reservas mediante programación orientada a objetos (POO).

El sistema funciona desde una interfaz de consola y almacena la información en listas durante la ejecución del programa. No utiliza bases de datos.

## 2. Objetivo general

Desarrollar un sistema de gestión que permita registrar y administrar clientes, servicios y reservas, aplicando los principios de programación orientada a objetos, validaciones de datos y manejo de excepciones en Python.

## 3. Objetivos específicos

- Implementar clases que representen clientes, servicios y reservas.
- Aplicar abstracción, herencia, encapsulamiento y polimorfismo.
- Desarrollar validaciones para controlar los datos ingresados.
- Implementar excepciones personalizadas para manejar errores.
- Administrar los registros mediante listas.
- Generar registros de actividad y errores mediante el módulo logging.
- Simular operaciones de gestión desde un menú interactivo.

## 4. Funcionalidades del sistema

El sistema permite:

1. Registrar clientes y validar sus datos.
2. Evitar registros duplicados mediante el correo electrónico.
3. Registrar salas, equipos y asesorías.
4. Calcular costos de los servicios.
5. Crear y confirmar reservas.
6. Validar la disponibilidad de los servicios.
7. Controlar la capacidad de las salas y el inventario de equipos.
8. Consultar clientes, servicios y reservas.
9. Cancelar reservas.
10. Consultar un resumen de los registros.
11. Registrar eventos y errores en un archivo de logs.

## 5. Tecnologías utilizadas dentro del sistema

- Python 3.
- Visual Studio Code.
- Git.
- GitHub.
- Biblioteca estándar de Python: abc, datetime, uuid, math, re, logging y pathlib.

## 6. Estructura del proyecto

```text
Software-FJ/
│
├── main.py
│
├── modelos/
│   ├── __init__.py
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   └── reserva.py
│
├── servicios/
│   ├── __init__.py
│   ├── sala.py
│   ├── equipo.py
│   └── asesoria.py
│
├── excepciones/
│   ├── __init__.py
│   └── errores.py
│
├── gestion/
│   ├── __init__.py
│   └── sistema.py
│
├── logs/
│   └── .gitkeep
│
├── README.md
└── .gitignore
```

## 7. Principios de programación orientada a objetos

### Abstracción
Se implementan las clases abstractas Entidad y Servicio mediante el módulo abc.

### Herencia
Cliente, Servicio y Reserva reutilizan la estructura de Entidad. Las clases Sala, Equipo y Asesoria heredan de Servicio.

### Encapsulamiento
Se utilizan atributos privados y propiedades para controlar el acceso y la modificación de los datos.

### Polimorfismo
Las clases especializadas implementan sus propios métodos calcular_costo(), validar_parametros() y describir().

## 8. Manejo de excepciones

El sistema cuenta con excepciones personalizadas para controlar errores relacionados con clientes, servicios, reservas, datos inválidos y registros duplicados.

También implementa estructuras try, except, else y finally, además de encadenamiento de excepciones.

## 9. Registro de actividad

Se utiliza el módulo logging para almacenar eventos y errores en el archivo:

`logs/sistema.log`

Este archivo permite consultar información sobre la ejecución del programa y los errores presentados.

## 10. Instalación y ejecución

### Requisitos
- Tener Python 3 instalado.
- Tener el proyecto descargado o clonado.

### Ejecución

Desde la carpeta principal del proyecto, ejecutar:

```bash
python main.py
```

El programa mostrará un menú interactivo con las opciones disponibles para administrar clientes, servicios y reservas.

## 11. Pruebas realizadas

Se realizaron pruebas individuales de las clases y pruebas integrales del sistema.

Entre las operaciones verificadas se encuentran:

- Registro correcto de clientes.
- Detección de clientes duplicados.
- Registro de los tres tipos de servicios.
- Cálculo de costos de salas, equipos y asesorías.
- Creación y confirmación de reservas.
- Rechazo de reservas con inventario insuficiente.
- Consulta de registros.
- Cancelación de reservas.
- Generación de registros de actividad y errores.

Se completó una simulación de 13 operaciones del sistema, con resultados satisfactorios.

## 12. Consideraciones

La información de clientes, servicios y reservas se almacena temporalmente en listas durante la ejecución del programa. Por esta razón, los datos se reinician al cerrar la aplicación.

El archivo de logs conserva registros de actividad y errores, pero no almacena los datos de los clientes ni las reservas.

## 13. Conclusión

El desarrollo de Software FJ permitió aplicar los conceptos fundamentales de programación orientada a objetos en una solución práctica. Se implementaron clases, herencia, abstracción, encapsulamiento, polimorfismo, validaciones y excepciones personalizadas, integrando los componentes en un sistema funcional que permite administrar clientes, servicios y reservas.
