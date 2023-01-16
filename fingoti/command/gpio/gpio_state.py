from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class GPIOState(Command):
    def __init__(self):
        self._data_store = {
            "property": "gpioState"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addGPIOState(self, **kwargs):
    """
    [Read & Write]

    Adds a gpioState command to the builder

    Keyword Arguments
    ----------
    gpio - int
    
    value - int

    save - bool
    
    state - array[int]

    """
    if(len(kwargs) is 0):
        self.add(GPIOState().read())
    else:
        kwargKeys = kwargs.keys();
        if("gpio" in kwargKeys):
            self.add(GPIOState().write({
                "gpio": kwargs["gpio"],
                "value": kwargs["value"],
                "save": kwargs["save"]
            }))
        elif("state" in kwargKeys):
            self.add(GPIOState().write({
                "state": kwargs["state"],
                "save": kwargs["save"]
            }))
        else:
            self.add(GPIOState().write({
                "save": kwargs["save"]
            })) 