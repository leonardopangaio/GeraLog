@echo off

@REM Necessário informar o caminho do script, pois caso seja executado como administrador, o sistema ainda vai encontrar o caminho para salvar o log.
set ScriptPath=

set carimbo=dt%date%_hr%time%
set carimbo=%carimbo:/=.%
set carimbo=%carimbo::=.%
set carimbo=%carimbo:,=.%
set carimbo=%carimbo: =0%

mkdir "%ScriptPath%\Logs\"

@REM Exemplo de utilização do log.
echo %date% - %time% - Pasta logs criada com sucesso. 1>> "%ScriptPath%\Logs\LogFileName_%carimbo%.log" 2>&1
