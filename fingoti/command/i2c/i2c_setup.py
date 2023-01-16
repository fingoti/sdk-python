from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class I2CSetup(Command):
    def __init__(self):
        self._data_store = {
            "property": "i2cSetup"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addI2CSetup(self, scan:bool = None, speed:int = None):
    """
    [Read & Write]

    Adds a i2cSetup command to the builder

    Arguments
    ----------
    scan - bool, optional
    speed - int, optional
    """
    if(speed is not None and scan is None):
        if(speed < 25000 or speed > 1000000):
            raise ValueError("speed must be between 25000 and 1000000")
        self.add(I2CSetup().write({
            "speed": speed
        }))
    elif (scan is not None and speed is None): 
        self.add(I2CSetup().write({
            "scan": scan
        }))
    elif(scan is not None and speed is not None):
        self.add(I2CSetup().write({
            "speed": speed,
            "scan": scan
        }))
    else:
        self.add(I2CSetup().read())