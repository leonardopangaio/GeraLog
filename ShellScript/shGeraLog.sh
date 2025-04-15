#!/bin/bash

year=$(date +"%Y")
month=$(date +"%m")
day=$(date +"%d")
time=$(date +"%H%M%S%3N")  # Inclui milissegundos para garantir unicidade no nome
log_dir="./logs/${year}/${month}/${day}"
log_name="logFileName"
log_file="${log_dir}/${log_name}_${time}.log"

function colorize {
    local color_code="$1"
    local text="$2"
    printf "${color_code}%s\033[0m" "${text}"
}

# Função para adicionar cores e negrito
function log {
    local type
    local message

    if [[ $# -eq 1 ]]; then
        type="INFO"               # Default
        message="$1"              # Só veio uma mensagem, então é a mensagem
    elif [[ $# -ge 2 ]]; then
        type="${1:-INFO}"
        message="$2"
    else
        return 1
    fi

    local timestamp=$(date +"%Y-%m-%d %H:%M:%S %z")

    mkdir -p "${log_dir}"

    # Definindo cores
    declare -A cores
    cores["INFO"]="\033[1;32m"  # Verde, negrito
    cores["WARN"]="\033[1;38;5;214m"  # Laranja, negrito (ANSI 256 cor 214)
    cores["ERRO"]="\033[1;31m"  # Vermelho, negrito
    cores["DEBUG"]="\033[1;34m"  # Azul, negrito
    cores["EXCEPT"]="\033[1;35m"  # Roxo, negrito
    cores["FATAL"]="\033[1;97;41m"  # Fundo vermelho, texto branco negrito
    cores["TRACE"]="\033[1;37m"  # Branco, negrito
    
    # Substitui [TIPO] por sua versão colorida
    message_colored="${message}"
    for chave in "${!cores[@]}"; do
        esc_inicial="${cores[${chave}]}"
        esc_reset="\033[0m"
        message_colored=$(echo "${message_colored}" | sed "s/\[${chave}\]/$(colorize "${cores[${chave}]}" "[${chave}]")/g")
    done

    # Verifica se o tipo é válido antes de acessar o array
    if [[ -z "${cores[${type}]}" ]]; then
        type="INFO"  # Se o tipo não for válido, usa 'INFO' como padrão
    fi

    # Colore o tipo do log
    if [[ -n "${cores[${type}]}" ]]; then
        type_colored=$(colorize "${cores[${type}]}" "${type}")
    else
        type_colored="${type}"
    fi

    echo -e "${timestamp} - [$(basename $0)] - ${type} - ${message}" >> "${log_file}" 2>&1
    echo -e "${timestamp} - [$(basename $0)] - ${type_colored} - ${message_colored}" 


}