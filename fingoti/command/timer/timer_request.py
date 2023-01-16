from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class TimerRequest(Command):
    def __init__(self):
        self._data_store = {
            "property": "timerRequest"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addTimerRequest(self, request = None):
    """
    [Read & Write]

    Adds a timerRequest command to the builder

    Arguments
    ----------
    request - object, optional
        The request array for the device to run whne the timer triggers 
    """
    if(request is not None):
            self.add(TimerRequest().write({
                "request": request
            }))
    else:
        self.add(TimerRequest().read())