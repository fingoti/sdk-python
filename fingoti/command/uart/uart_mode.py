from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class UARTMode(Command):
    def __init__(self):
        self._data_store = {
            "property": "uartMode"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addUARTMode(self, mode:int = None):
    """
    [Read & Write]

    Adds a uartMode command to the builder

    Arguments
    ----------
    mode - int, optional
    """
    validModes = { 0, 1 }
    if(mode is not None):
        if(mode not in validModes):
            raise ValueError("mode must be one of %r." % validModes)
        else:
            self.add(UARTMode().write({
                "mode": mode
            }))
    else:
        self.add(UARTMode().read())