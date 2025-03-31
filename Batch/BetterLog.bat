@echo off

@REM Necessário informar o caminho do script, pois caso seja executado como administrador, o sistema ainda vai encontrar o caminho para salvar o log.
set ScriptPath=

@REM Seting year, month and date variables
FOR /F "skip=1 tokens=1-6" %%A IN ('WMIC Path Win32_LocalTime Get Day^,Hour^,Minute^,Month^,Second^,Year /Format:table') DO (
    if "%%B" NEQ "" (
        SET /A FDATE=%%F*10000+%%D*100+%%A
    )
)

set year=%FDATE:~0,4%
set month=%FDATE:~4,2%
set day=%FDATE:~6,2%

@REM Seting timestamp
set timestamp=%time%
set timestamp=%timestamp:/=%
set timestamp=%timestamp::=%
set timestamp=%timestamp:,=%
set timestamp=%timestamp: =0%

set log_path=%ScriptPath%\logs\%year%\%month%\%day%

@REM Creatig log folder
if not exist %log_path% (
    mkdir %log_path%
)

@REM Example of utilization
echo %date% - %time% - Hello World 1>> "%log_path%\HelloWorld_%timestamp%.log" 2>&1