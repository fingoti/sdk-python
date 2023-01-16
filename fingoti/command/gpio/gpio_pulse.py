from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class GPIOPulse(Command):
    def __init__(self):
        self._data_store = {
            "property": "gpioPulse"
        }
    
    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addGPIOPulse(self, gpio:int, duration:int):
    """
    [Write]

    Adds a gpioPulse command to the builder

    Arguments
    ----------
    gpio - int
    
    duration - int
    """
    validGPIO = {1,2,3,4}
    if(gpio not in validGPIO):
        raise ValueError("gpio must be one of %r." % validGPIO)
    
    if(duration < 1 or duration > 30):
        raise ValueError("duration must be between 1 and 30")

    self.add(GPIOPulse().write({
        "gpio": gpio,
        "duration": duration
    }))