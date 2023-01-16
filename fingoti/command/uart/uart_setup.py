from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class UARTSetup(Command):
    def __init__(self):
        self._data_store = {
            "property": "uartSetup"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addUARTSetup(self, baudrate:int = None, databits:int = None, parity:int = None, stopbits:int = None):
    """
    [Read & Write]

    Adds a uartSetup command to the builder

    Arguments
    ----------
    baudrate - int, optional
    
    duration - int, optional 

    parity - int, optional

    stopbits - int, optional
    """
    if(baudrate is not None or databits is not None or parity is not None or stopbits is not None):
        validBaudrates = { 300, 600, 1200, 2400, 4800, 9600, 19200, 31250, 38400, 57600, 74800, 115200, 230400, 256000, 460800, 921600, 1843200, 3686400 } 
        validDatabits = { 5, 6, 7, 8 }
        validParityStop = { 0, 1, 2 }

        if(baudrate is not None and baudrate not in validBaudrates):
            raise ValueError("baudrate must be one of %r." % validBaudrates)
        
        if(databits is not None and databits not in validDatabits):
            raise ValueError("databits must be one of %r." % validDatabits)

        if(parity is not None and parity not in validParityStop):
            raise ValueError("parity must be one of %r." % validParityStop)

        if(stopbits is not None and stopbits not in validParityStop):
            raise ValueError("stopbits must be one of %r." % validParityStop)

        self.add(UARTSetup().write({
            "baudrate": baudrate,
            "databits": databits,
            "parity": parity,
            "stopbits": stopbits
        }))
    else:
        self.add(UARTSetup().read())