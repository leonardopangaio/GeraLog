from rich.console import Console
from datetime import datetime
import inspect
import os

class console:
    """
    Classe criada para gerenciar de forma simples os logs vindos dos scripts python.

    Ela vai ter métodos para tratar os seguintes níveis:
    - trace;
    - debug;
    - info;
    - warning;
    - erro;
    - fatal;

    Cada um dos níveis é chamado através de seu método e tem uma coloração diferente na saída para o console.

    Cada nível serve para o desenvolvedor passar uma informação e para decidir quando ela deve ser exibida/salva no arquivo de log, ele pode alterar a verbosidade ao instanciar a classe.
    
    Segue relação de níveis e código:
    - 60 - exibe apenas Fatal;
    - 50 - exibe Fatal e Erro;
    - 40 - exibe Fatal, Erro e Warning;
    - 30 - exibe Fatal, Erro, Warning e Info;
    - 20 - exibe Fatal, Erro, Warning, Info e Debug;
    - 10 - exibe Fatal, Erro, Warning, Info, Debug e Trace;
    
    Para instanciar ela podemos usar o seguinte exemplo:

    from logClass import console

    logger = console(10, filename='LogFile')

    logger.info('Olá Mundo.')
    """
    
    def __init__(self, loglevel: int, filename: str = None) -> None:
        """__init__ _summary_

        _extended_summary_

        Método de inicialização da classe.

        Este método trata o loglevel e o nome do arquivo, assim como as variáveis que serão utilizadas por ele.

        :param loglevel: Valor recebido na instanciação do objeto para definir quais serão os métodos que darão saída em console/arquivo de log.
        :type loglevel: int
        :param filename: Nome para o arquivo de log que será gerado, caso seja definido, defaults to None
        :type filename: str, optional
        :raises Exception: Se loglevel informado for inválido, ele retorna um erro de 'Inválid Log-Level'
        """
        self.list_loglevel: list[int] = [60,50,40,30,20,10]
        if loglevel not in self.list_loglevel:
            raise Exception('Invalid Log-Level.')
        else:
            self.loglevel: int = loglevel
        
        # Definição dos carimbos de data e hora para criação dos arquivos
        self.ano: str = datetime.now().astimezone().strftime("%y")
        self.mes: str = datetime.now().astimezone().strftime("%m")
        self.dia: str = datetime.now().astimezone().strftime("%d")
        self.momento: str = datetime.now().astimezone().strftime("%H%M%S")
        
        self.filename: str = filename
        
        # Definição do caminho e arquivo de log
        if filename:
            self.LogPathNow: str = str(os.getcwd()) + "/logs/" + str(self.ano) + "/" + str(self.mes) + "/" + str(self.dia)
            if not os.path.exists(self.LogPathNow):
                os.makedirs(self.LogPathNow)
            self.LogFileName: str = f"{self.LogPathNow}/{self.filename}_{self.momento}.log"
        else:
            self.LogFileName: str = None
    
    def trace(self, message: str) -> None:
        """trace _summary_

        _extended_summary_

        :param message: Mensagem recebida pelo método.
        :type message: str
        """
        if self.loglevel <= 10:
            console = Console()
            caller_name:str  = f'({inspect.stack()[1].function})'
            
            color: str = "white"
            tag: str = f'TRACE'
            color_tag: str = f'[bold {color}]TRACE[/bold {color}]'
            
            current_time: datetime = datetime.now().astimezone()
            formatted_time: str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f %z')
            
            full_message: str = f'{formatted_time} - {caller_name} - {tag} - {message}'
            color_full_message: str = f'{formatted_time} - {caller_name} - {color_tag} - {message}'
            if self.LogFileName:
                with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                    log.writelines(full_message + "\n")
            console.print(color_full_message, soft_wrap=True)

    def debug(self, message: str) -> None:
        """debug _summary_

        _extended_summary_

        :param message: Mensagem recebida pelo método.
        :type message: str
        """
        if self.loglevel <= 20:
            console = Console()
            caller_name:str  = f'({inspect.stack()[1].function})'
            
            color: str = "blue"
            tag: str = f'DEBUG'
            color_tag: str = f'[bold {color}]DEBUG[/bold {color}]'
            
            current_time: datetime = datetime.now().astimezone()
            formatted_time: str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f %z')
            
            full_message: str = f'{formatted_time} - {caller_name} - {tag} - {message}'
            color_full_message: str = f'{formatted_time} - {caller_name} - {color_tag} - {message}'
            if self.LogFileName:
                with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                    log.writelines(full_message + "\n")
            console.print(color_full_message, soft_wrap=True)

    def info(self, message: str) -> None:
        """Docstring for info
        
        :param self: Description
        :type self: 
        :param message: Mensagem recebida pelo método.
        :type message: str"""
        if self.loglevel <= 30:
            console = Console()
            caller_name:str  = f'({inspect.stack()[1].function})'
            
            color: str = "green"
            tag:str =  f'INFO'
            color_tag: str = f'[bold {color}]INFO[/bold {color}]'
            
            current_time: datetime = datetime.now().astimezone()
            formatted_time: str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f %z')
            
            full_message: str = f'{formatted_time} - {caller_name} - {tag} - {message}'
            color_full_message: str = f'{formatted_time} - {caller_name} - {color_tag} - {message}'
            if self.LogFileName:
                with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                    log.writelines(full_message + "\n")
            console.print(color_full_message, soft_wrap=True)
    
    def warn(self, message: str) -> None:
        """warn _summary_

        _extended_summary_

        :param message: Mensagem recebida pelo método.
        :type message: str
        """
        if self.loglevel <= 40:
            console = Console()
            caller_name:str  = f'({inspect.stack()[1].function})'
            
            color: str = "yellow"
            tag: str = f'WARN'
            color_tag: str = f'[bold {color}]WARN[/bold {color}]'
            
            current_time: datetime = datetime.now().astimezone()
            formatted_time: str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f %z')
            
            full_message: str = f'{formatted_time} - {caller_name} - {tag} - {message}'
            color_full_message: str = f'{formatted_time} - {caller_name} - {color_tag} - {message}'
            if self.LogFileName:
                with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                    log.writelines(full_message + "\n")
            console.print(color_full_message, soft_wrap=True)
    
    def erro(self, message: str) -> None:
        """

        :param message: 

        """
        if self.loglevel <= 50:
            console = Console()
            caller_name:str  = f'({inspect.stack()[1].function})'
            
            color: str = "red"
            tag: str = f'ERROR'
            color_tag: str = f'[bold {color}]ERROR[/bold {color}]'
            
            current_time: datetime = datetime.now().astimezone()
            formatted_time: str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f %z')
            
            full_message: str = f'{formatted_time} - {caller_name} - {tag} - {message}'
            color_full_message: str = f'{formatted_time} - {caller_name} - {color_tag} - {message}'
            if self.LogFileName:
                with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                    log.writelines(full_message + "\n")
            console.print(color_full_message, soft_wrap=True)

    def fatal(self, message: str) -> None:
        """

        :param message: 

        """
        if self.loglevel <= 60:
            console = Console()
            caller_name:str  = f'({inspect.stack()[1].function})'
            
            color: str = "purple"
            tag: str = f'FATAL'
            color_tag: str = f'[bold {color}]FATAL[/bold {color}]'
            
            current_time: datetime = datetime.now().astimezone()
            formatted_time: str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f %z')
            
            full_message: str = f'{formatted_time} - {caller_name} - {tag} - {message}'
            color_full_message: str = f'{formatted_time} - {caller_name} - {color_tag} - {message}'
            if self.LogFileName:
                with open (str(self.LogFileName),"a",encoding='utf-8') as log:
                    log.writelines(full_message + "\n")
            console.print(color_full_message, soft_wrap=True)

    
