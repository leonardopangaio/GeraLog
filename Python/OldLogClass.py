from datetime import datetime
import os
import pymsteams
import sys
import json
import time
import traceback


class GeraLog:
    """
    Para instanciar a classe GeraLog será necessário passar os seguintes atributos:
    - loglevel:         Este atributo definirá a verbosidade do salvamento do log.
                        Podendo ser:
                            - default: exibindo apenas os logs de ERRO e WARNING;
                            - verbose: exibindo os logs de ERRO, WARNING e INFO;
                            - debug: exibindo todos os tipos de log;
    - filename:         Este atributo definirá qual será o título do arquivo que será salvo;
                        Por padrão o log será criado na pasta do programa, seguindo a estrutura ./logs/ANO/MES/DIA/{filename}_{momento da criação do arquivo}.log
    - console:          Este atributo define se a saída também deverá ser exibida no console ou não;
                        São aceitos os valores 0 e 1 ou True e False;
                        Caso seja utilizado a biblioteca TQDM para geração de barras de progresso, sugere-se que seja utilizado este atributo atrelado ao tqdm(disable=console),
                        Caso não tenha saída para o console ele irá exibir a barra de progresso, caso haja, ele ficará desabilitado;
    - relheader:        Este atributo recebe o cabeçalho de criação do CSV, que será preenchido pelo método geraCSV.
                        Caso não seja desejado a utilização do método geraCsv, este atributo deverá receber o valor None;
    - token:            Este atributo é a URL de conexão com o Teams webhook, necessário para realizar o envio da mensagem para o time no Microsoft Teams;

    Os métodos desta classe são:
    - __init__:             Método de inicialização da classe, onde o objeto será instanciado;
    - geraInfo:             Método de escrever as informações no log em modo INFO;
                            O parâmetro que deve ser passado é o LogMessage;
    - geraDebug:            Método de escrever as informações no log em modo DEBUG;
    - geraErro:             Método de escrever as informações no log em modo de ERRO;
    - geraWarning:          Método de escrever as informações no log em modo de WARN;
    - geraException:        Método de escrever as informações no log em modo de EXCPT.
    - msTeamsMessage:       Método de envio de mensagem para um determinado time no Microsoft Teams;
    - geraCsv:              Método de criação de arquivo CSV para conseguir controlar as saídas desejadas;
    - geraJson:             Método de criação de arquivo JSON para salvar dados de retorno de API;
                            Os parâmetros são:
                            jsonFileName para definir o nome do arquivo;
                            jsonMessage para inserir a mensagem que vai ser salva no formato JSON;
    - getFunctionName       Método para que seja possível retornar o nome da função que chamou o geraException;
                            Este método deverá ser utilizado pela classe importada, e não por seu objeto instanciado;
    """
    
    def __init__(self, loglevel, filename, console, relheader=None, token=None):
        self.filename = filename
        self.list_loglevel = ["default","verbose","debug"]
        if loglevel not in self.list_loglevel:
            raise Exception('Invalid Log-Level.')
        else:
            self.loglevel = loglevel
        self.list_console=[0, 1]
        if console not in self.list_console:
            raise Exception('Invalid console argument.')
        else:
            self.console = console
        
        self.relheader = relheader

        self.TeamsWebHook = pymsteams.connectorcard(token)

        # Definição dos carimbos de data e hora para criação dos arquivos
        self.ano: str = datetime.now().strftime("%y")
        self.mes: str = datetime.now().strftime("%m")
        self.dia: str = datetime.now().strftime("%d")
        self.momento: str = datetime.now().strftime("%H%M%S")

        # Definição do caminho e arquivo de log
        self.LogPathNow = str(os.getcwd()) + "/logs/" + str(self.ano) + "/" + str(self.mes) + "/" + str(self.dia)
        if not os.path.exists(self.LogPathNow):
            os.makedirs(self.LogPathNow)
        self.LogFileName = f"{self.LogPathNow}/{self.filename}_{self.momento}.log"

        # Definição do caminho e arquivo de relatório e criação do rel com o header instanciado
        self.RelPathNow = str(os.getcwd()) + "/rel/" + str(self.ano) + "/" + str(self.mes) + "/" + str(self.dia)
        if not os.path.exists(self.RelPathNow):
            os.makedirs(self.RelPathNow)
        self.RelFileName = f"{self.RelPathNow}/{self.filename}_{self.momento}.csv"
        if self.relheader != None:
            with open (str(self.RelFileName),"a",encoding='utf-8') as rel:
                rel.writelines(str(self.relheader) + "\n")
        else:
            pass

        # Definição do caminho e arquivo dos jsons
        self.JsonPathNow = str(os.getcwd()) + "/json/" + str(self.ano) + "/" + str(self.mes) + "/" + str(self.dia)
        if not os.path.exists(self.JsonPathNow):
            os.makedirs(self.JsonPathNow)

    def geraInfo(self, LogMessage):
        if self.loglevel == "debug" or self.loglevel == "verbose":
            try:
                with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                    log.writelines(str(datetime.now()) + " - INFO - " + str(LogMessage) + "\n")
            except Exception as eError:
                self.geraException(f'Exception Message: {eError}')
                self.geraException(f'Exception Type: {type(eError)}')
                self.geraException(f'Exception Doc: {eError.__doc__}')
                self.geraException(f'sys.exc_info Details: {sys.exc_info}')
            if self.console == 1:
                print(str(datetime.now()) + " - INFO - " + str(LogMessage))
            else:
                pass
        else:
            pass

    def geraDebug(self, LogMessage):
        if self.loglevel == "debug":
            try:
                with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                    log.writelines(str(datetime.now()) + " - DEBUG - " + str(LogMessage) + "\n")
            except Exception as eError:
                self.geraException(f'Exception Message: {eError}')
                self.geraException(f'Exception Type: {type(eError)}')
                self.geraException(f'Exception Doc: {eError.__doc__}')
                self.geraException(f'sys.exc_info Details: {sys.exc_info}')
            if self.console == 1:
                print(str(datetime.now()) + " - DEBUG - " + str(LogMessage))
            else:
                pass
        else:
            pass

    def geraError(self, LogMessage):
        try:
            with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                log.writelines(str(datetime.now()) + " - ERROR - " + str(LogMessage) + "\n")
        except Exception as eError:
            self.geraException(f'Exception Message: {eError}')
            self.geraException(f'Exception Type: {type(eError)}')
            self.geraException(f'Exception Doc: {eError.__doc__}')
            self.geraException(f'sys.exc_info Details: {sys.exc_info}')
        if self.console == 1:
            print(str(datetime.now()) + " - ERROR - " + str(LogMessage))
        else:
            pass

    def geraWarning(self, LogMessage):
        try:
            with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                log.writelines(str(datetime.now()) + " - WARN - " + str(LogMessage) + "\n")
        except Exception as eError:
            self.geraException(f'Exception Message: {eError}')
            self.geraException(f'Exception Type: {type(eError)}')
            self.geraException(f'Exception Doc: {eError.__doc__}')
            self.geraException(f'sys.exc_info Details: {sys.exc_info}')
        if self.console == 1:
            print(str(datetime.now()) + " - WARN - " + str(LogMessage))
        else:
            pass
    
    # TODO: Incluir o nome da função
    #def geraException(self, FunctionName, LogMessage):
    def geraException(self, LogMessage):
        try:
            with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                #log.writelines(str(datetime.now()) + " - " + FunctionName + " - EXCPT - " + str(LogMessage) + "\n")
                log.writelines(str(datetime.now()) + " - " + " - EXCPT - " + str(LogMessage) + "\n")
        except Exception as eError:
            ExceptionDict = {}
            ExceptionDict['Exception_Message'] = str(eError)
            ExceptionDict['Exception_Type'] = str(type(eError))
            ExceptionDict['Exception_Doc'] = str(eError.__doc__)
            ExceptionDict['sys.exc_info_Details'] = str(sys.exc_info)
            return ExceptionDict
        if self.console == 1:
            print(str(datetime.now()) + " - EXCPT - " + str(LogMessage))
        else:
            pass

    def msTeamsMessage(self,payload):
        self.TeamsWebHook.text(f"{datetime.now()} - MSG - {payload}.")
        try:
            self.TeamsWebHook.send()
        except Exception as eError:
            self.geraException(f'Exception Message: {eError}')
            self.geraException(f'Exception Type: {type(eError)}')
            self.geraException(f'Exception Doc: {eError.__doc__}')
            self.geraException(f'sys.exc_info Details: {sys.exc_info}')
        else:
            self.geraInfo("Mensagem enviada para o Microsoft Teams com sucesso!")

    def geraCsv(self,RelMessage):
        if self.relheader == None:
            self.geraError("Não foi definido um cabeçalho para o CSV.")
        else:
            try:
                with open (str(self.RelFileName),"a",encoding='utf-8') as rel:
                    rel.writelines(str(RelMessage) + "\n")
            except Exception as eError:
                self.geraException(f'Exception Message: {eError}')
                self.geraException(f'Exception Type: {type(eError)}')
                self.geraException(f'Exception Doc: {eError.__doc__}')
                self.geraException(f'sys.exc_info Details: {sys.exc_info}')

    def geraJson(self, jsonFileName, jsonMessage):
        if jsonFileName != None:
            self.JsonFileName = f"{self.JsonPathNow}/{jsonFileName}_{self.momento}.json"
        elif jsonFileName == None:
            self.JsonFileName = f"{self.JsonPathNow}/{self.filename}_{self.momento}.json"
        try:
            with open(str(self.JsonFileName),"a") as jsonFile:
                jsonFile.writelines(json.dumps(jsonMessage))
        except Exception as eError:
            self.geraException(f'Exception Message: {eError}')
            self.geraException(f'Exception Type: {type(eError)}')
            self.geraException(f'Exception Doc: {eError.__doc__}')
            self.geraException(f'sys.exc_info Details: {sys.exc_info}')

    def getFunctionName():
        Names = {"Module Name":str(traceback.extract_stack(None, 2)[0][0]), "Function Name": str(traceback.extract_stack(None, 2)[0][2])}
        return Names

def timer(function):
    """
    Esta função timer foi criada para ser um decorador para calculo do tempo de execução da função que utilizar ele.
    Os retornos possíveis deste timer são dois dicionários:
        1 - Caso a função utilizadora tenha um retorno, o dicionário será gerado com os seguintes dados: FunctionReturn, FunctionName e TimeSpent;
        2 - Caso a função utilizadora não tenha um retorno, o dicionário será gerado com os seguintes dados: FunctionName e TimeSpent.
    """
    def wrapper(*args, **kwargs):
        init_time = time.time()
        funcReturn = function(*args, **kwargs)
        end_time = time.time()
        result_time = end_time - init_time
        if funcReturn == None:
            response={"FunctionName":function.__name__, "TimeSpent":"{:.5f}".format(result_time)}
            return response
        else:
            response={"FunctionReturn":funcReturn, "FunctionName":function.__name__, "TimeSpent":"{:.5f}".format(result_time)}
            return response
    return wrapper
