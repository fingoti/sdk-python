from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class GPIOToggle(Command):
    def __init__(self):
        self._data_store = {
            "property": "gpioToggle"
        }
    
    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addGPIOToggle(self, gpio:int):
    """
    [Write]

    Adds a gpioToggle command to the builder

    Arguments
    ----------
    gpio - int
    """
    validGPIO = {1,2,3,4}
    if(gpio not in validGPIO):
        raise ValueError("gpio must be one of %r." % validGPIO)

    self.add(GPIOToggle().write({
        "gpio": gpio,
    }))