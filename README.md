# Servicio de Notificación de Tarifa Limitada

¡Hola! Soy Juan José, y esta es mi prueba técnica para el puesto de Senior Backend Engineer en Modak.

En este proyecto, encontrarán dos versiones del mismo servicio, desarrolladas independientemente en Python y Go. Aunque no soy un experto en Go y lo estoy aprendiendo mediante este mini proyecto, daré lo mejor de mí para demostrar mi flujo de trabajo y experiencia en desarrollo.

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

Para la ejecución del proyecto es necesario instalar `pre-commit` [https://pre-commit.com/], y `golangci-lint` [https://github.com/golangci/golangci-lint]. Para ahorrar costos, el CI se ejecuta en instancias pre-commit, intentando evitar la pérdida de tiempo de ejecución dentro de GitHub Actions.

Ejecute el proyecto con python 3.10

```bash
brew install python@3.10
```

Una vez instalado Python y clonado el presente repositorio, ejecute:

```bash
pipx install --editable .
```

Luego, ya en el folder del proyecto, (Y CADA VEZ QUE EL PROYECTO SE CLONE) ejecute:
```bash
pre-commit install
pre-commit
```

## CLI:
El proyecto tiene su propio CLI, diseñado para ejecutar varias de las tareas normales del desarrollo, incluyendo los tests para Python y Go. Para conocer todos los comandos puede utilizar el comando "help" o "-h

```bash
modak -h
```
