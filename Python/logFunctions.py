from datetime import datetime
import os

ano: str = datetime.now().strftime("%y")
mes: str = datetime.now().strftime("%m")
dia: str = datetime.now().strftime("%d")
momento: str = datetime.now().strftime("%H%M%S")

def GeraLogColor(LogMensage: str) -> None:
    LogPathNow: str = str(os.getcwd()) + "/logs/" + str(ano) + "/" + str(mes) + "/" + str(dia)
    if not os.path.exists(LogPathNow):
        os.makedirs(LogPathNow)
    LogFileName: str = f"{LogPathNow}/LogFileName_{momento}.log"
    with open (LogFileName,"a",encoding='utf-8') as log:
        log.writelines(str(LogMensage) + '\n')
    if 'INFO' in LogMensage:
        color: str = "green"
        LogMensage = LogMensage.replace("INFO",f"[bold {color}]INFO[/bold {color}]")
    elif 'WARN' in LogMensage:
        color: str = "yellow"
        LogMensage = LogMensage.replace("WARN",f"[bold {color}]WARN[/bold {color}]")
    elif 'ERROR' in LogMensage:
        color: str = "red"
        LogMensage = LogMensage.replace("ERROR",f"[bold {color}]ERROR[/bold {color}]")
    elif 'EXCPT' in LogMensage:
        color: str = "purple"
        LogMensage = LogMensage.replace("EXCPT",f"[bold {color}]EXCPT[/bold {color}]")
    elif 'DEBUG' in LogMensage:
        color: str = "blue"
        LogMensage = LogMensage.replace("DEBUG",f"[bold {color}]DEBUG[/bold {color}]")
    else:
        LogMensage = LogMensage
    print(LogMensage)

def GeraLog(LogMensage: str) -> None:
    LogPathNow: str = str(os.getcwd()) + "/logs/" + str(ano) + "/" + str(mes) + "/" + str(dia)
    if not os.path.exists(LogPathNow):
        os.makedirs(LogPathNow)
    LogFileName: str = f"{LogPathNow}/LogFileName_{momento}.log"
    with open (LogFileName,"a",encoding='utf-8') as log:
        log.writelines(LogMensage + '\n')
    print(LogMensage)