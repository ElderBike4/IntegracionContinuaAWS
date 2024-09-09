#!/bin/bash

# Buscar el ID del contenedor basado en la imagen
containerId=$(sudo docker ps -a -q --filter "ancestor=operaciones-app")

if [ -n "$containerId" ]; then
    echo "Contenedor encontrado con ID: $containerId"

    # Detener el contenedor
    docker stop "$containerId"

    # Eliminar el contenedor
    docker rm "$containerId"
else
    echo "No se encontró ningún contenedor para la imagen 'operaciones-app'."
fi
