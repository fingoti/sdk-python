from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class UARTSession(Command):
    def __init__(self):
        self._data_store = {
            "property": "uartSession"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addUARTSession(self, duration:int = None):
    """
    [Read & Write]

    Adds a uartSession command to the builder

    Arguments
    ----------
    duration - int, optional 
    """
    if(duration is not None):
        if(duration < 0 or duration > 1440):
            raise ValueError("duration must be between 0 and 1440")
        else:
            self.add(UARTSession().write({
                "duration": duration
            }))
    else:
        self.add(UARTSession().read())