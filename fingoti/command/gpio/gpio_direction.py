from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class GPIODirection(Command):
    def __init__(self):
        self._data_store = {
            "property": "gpioDirection"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addGPIODirection(self, **kwargs):
    """
    [Read & Write]

    Adds a gpioDirection command to the builder

    Keyword Arguments
    ----------
    gpio - int, optional

    value - int, optional

    save - bool, optional
    
    direction - array[int], optional

    """
    if(len(kwargs) is 0):
        self.add(GPIODirection().read())
    else:
        kwargKeys = kwargs.keys();
        if("gpio" in kwargKeys):
            self.add(GPIODirection().write({
                "gpio": kwargs["gpio"],
                "value": kwargs["value"],
                "save": kwargs["save"]
            }))
        elif("direction" in kwargKeys):
            self.add(GPIODirection().write({
                "direction": kwargs["direction"],
                "save": kwargs["save"]
            }))
        else:
            self.add(GPIODirection().write({
                "save": kwargs["save"]
            })) 