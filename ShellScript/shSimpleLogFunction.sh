#!/bin/bash

carimbo_full="$(date +"%Y%m%dT%H%M%S")"

# Função para log
function log {
    local message="$1"

    # Caminho da pasta que você deseja verificar
    pasta="./logs"

    # Verifica se a pasta existe
    if [ ! -d "$pasta" ]; then
        # Se a pasta não existir, cria a pasta
        mkdir -p "$pasta"
        log "Pasta '$pasta' criada."
    fi

    echo "$(date +"%Y-%m-%d %H:%M:%S") - $message" >> ${pasta}/executaLote_${carimbo_full}.log 2>&1
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $message"
}

