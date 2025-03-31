#!/bin/bash

function GeraLog {
    local message="$1"
    echo "$(date +"%Y-%m-%d %H:%M:%S") - ${HOSTNAME} - $message" >> ~/LogFileName.log 2>&1
    echo "$(date +"%Y-%m-%d %H:%M:%S") - ${HOSTNAME} - $message"
}