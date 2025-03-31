#!/bin/bash

LOG_FILE="./LogFileName.log"

log() {
    local message="$1"
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $message" >> "$LOG_FILE" 2>&1
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $message"
}

# Função para capturar e logar a saída de um comando
run_and_log() {
    local cmd_output
    cmd_output=$(eval "$1" 2>&1)
    log "$cmd_output"
}

run_and_log "echo 'Hello World'"