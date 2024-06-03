# Servicio de Notificación de Tarifa Limitada

Hola! Soy Juan Jose, y esta es mi prueba técnica para Senior Backend Engineer en Modak.

En el presente proyecto, encontrarán dos versiones del mismo servicio, desarrolladas independientemente en Python y Go. 
Aunque no soy un experto en Go y lo estoy aprendiendo mediante este mini proyecto, daré lo mejor de mí para demostrar mi 
flujo de trabajo y experiencia en desarrollo.

## Metodología

Estoy desarrollando este proyecto usando la metodología BDD (Behavior Driven Development) y especificación mediante ejemplos:
- [Specification By Example](https://martinfowler.com/bliki/SpecificationByExample.html)

También estoy utilizando GitFlow mediante GitKraken:
- [GitFlow](https://www.gitkraken.com/learn/git/git-flow)

Además, he implementado SonarQube como profiler y analizador estático de código.

## Estructura del Proyecto

El proyecto se encuentra dividido en dos carpetas principales:
- `python/`: Contiene la implementación en Python.
- `go/`: Contiene la implementación en Go.

Cada una de estas carpetas contiene el código fuente correspondiente, así como los tests y la configuración necesaria para ejecutar el servicio.

## Ejecución del Proyecto

Para la ejecucion del proyecto es necesario instalar `pre-commit` por lo que es necesario, para cualquiera de los dos entornos, tener Python 3.x instalado.

una vez instalado python, y clonado el presente repo, ejecute:

- `pip install pre-commit`

En caso de usar MacOS y tener Homebrew, puede instalarlo mediante 
- `brew install pre-commit`

### Python

# -- Paso 1: Crea y activa el virtual python environment.
$ virtualenv --python python3 .venv
$ source .venv/bin/activate

# -- En WINDOWS:
# call .venv/Scripts/activate

# -- Paso 2: Instala los paquetes requeridos con pip.
$ pip install -r py.requirements/all.txt

