from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class UARTTrigger(Command):
    def __init__(self):
        self._data_store = {
            "property": "uartTrigger"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addUARTTrigger(self, length:int = None, terminator = None):
    """
    [Read & Write]

    Adds a uartTrigger command to the builder

    Arguments
    ----------
    length - int, optional
    
    terminator, optional 
    """
    if(length is not None or terminator is not None):
        if(length < 0 or length > 256):
            raise ValueError("length must be between 0 and 256")
        else:
            self.add(UARTTrigger().write({
                "length": length,
                "terminator": terminator
            }))
    else:
        self.add(UARTTrigger().read())