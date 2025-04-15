#!/bin/bash

source ./shGeraLog.sh

# Exemplo de uso
log "INFO" "Este é um log de exemplo de INFO."
log "WARN" "Este é um log de exemplo de WARN."
log "DEBUG" "Este é um log de exemplo de DEBUG."
log "ERRO" "Este é um log de exemplo de ERRO."
log "FATAL" "Este é um log de exemplo de FATAL."
log "TRACE" "Este é um log de exemplo de TRACE."
log "EXCEPT" "Este é um log de exemplo de EXCEPT."

# Exemplo de uso
log "INFO" "[INFO] - Este é um log de exemplo de INFO."
log "WARN" "[WARN] - Este é um log de exemplo de WARN."
log "DEBUG" "[DEBUG] - Este é um log de exemplo de DEBUG."
log "ERRO" "[ERRO] - Este é um log de exemplo de ERRO."
log "FATAL" "[FATAL] - Este é um log de exemplo de FATAL."
log "TRACE" "[TRACE] - Este é um log de exemplo de TRACE."
log "EXCEPT" "[EXCEPT] - Este é um log de exemplo de EXCEPT."

log "" "Teste sem tipo..."
log "teste só com 1 parâmetro"