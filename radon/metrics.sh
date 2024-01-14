#!/bin/bash

# Ruta al directorio del proyecto (si se proporciona como argumento, de lo contrario, usa el directorio actual)
PROYECTO_DIR=${1:-.}

# Complejidad ciclomática
radon cc -s -a "$PROYECTO_DIR" --json > informe_cc.json

# Índice de mantenibilidad
radon mi -s "$PROYECTO_DIR" --json > informe_mantenibilidad.json

python generar_informe_mantenibilidad.py

python generar_informe_cc.py









