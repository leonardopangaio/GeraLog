#!/bin/bash

year=$(date +"%Y")
month=$(date +"%m")
day=$(date +"%d")
time=$(date +"%H%M%S%3N")  # Inclui milissegundos para garantir unicidade no nome
log_dir="./logs/${year}/${month}/${day}"
log_name="LogFileName"
log_file="${log_dir}/${log_name}_${time}.log"

# Função para adicionar cores e negrito
function log {
    local log_type="$1"  # Adiciona o tipo como segundo parâmetro
    local message="$2"
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S %z")

    mkdir -p "${log_dir}"

    # Definindo as cores para cada tipo (todas em negrito)
    case "$log_type" in
        INFO)
            color="\033[1;32m"  # Verde, negrito
            ;;
        WARN)
            color="\033[1;38;5;214m"  # Laranja, negrito (ANSI 256 cor 214)
            ;;
        DEBUG)
            color="\033[1;34m"  # Azul, negrito
            ;;
        ERRO)
            color="\033[1;31m"  # Vermelho, negrito
            ;;
        FATAL)
            color="\033[1;97;41m"  # Fundo vermelho, texto branco negrito
            ;;
        TRACE)
            color="\033[1;37m"  # Branco, negrito
            ;;
        EXCEPT)
            color="\033[1;35m"  # Roxo, negrito
            ;;
        *)
            color="\033[1;37m"  # Default para branco negrito
            ;;
    esac

    # Log com a cor aplicada ao tipo
    echo -e "${timestamp} - ${color}[${log_type}]\033[0m - ${message}" 2>&1 | tee -a "${log_file}"
}

# Exemplo de uso
log "INFO" "Este é um log de exemplo de INFO."
log "WARN" "Este é um log de exemplo de WARN."
log "DEBUG" "Este é um log de exemplo de DEBUG."
log "ERRO" "Este é um log de exemplo de ERRO."
log "FATAL" "Este é um log de exemplo de FATAL."
log "TRACE" "Este é um log de exemplo de TRACE."
log "EXCEPT" "Este é um log de exemplo de EXCEPT."
