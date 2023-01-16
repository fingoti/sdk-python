from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class TimerStatus(Command):
    def __init__(self):
        self._data_store = {
            "property": "timerStatus"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addTimerStatus(self, enabled:bool = None, repeat:bool = None):
    """
    [Read & Write]

    Adds a timerStatus command to the builder

    Arguments
    ----------
    enabled - bool, optional
    
    repeat - bool, optional 
    """
    if(enabled is not None or repeat is not None):
        self.add(TimerStatus().write({
            "enabled": enabled,
            "repeat": repeat
        }))
    else:
        self.add(TimerStatus().read())