from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class TimerInterval(Command):
    def __init__(self):
        self._data_store = {
            "property": "timerInterval"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addTimerInterval(self, interval:int = None):
    """
    [Read & Write]

    Adds a timerInterval command to the builder

    Arguments
    ----------
    interval - int, optional
    """
    if(interval is not None):
        if(interval < 1 or interval > 86400):
            raise ValueError("interval must be between 1 and 86400")
        else:
            self.add(TimerInterval().write({
                "interval": interval
            }))
    else:
        self.add(TimerInterval().read())