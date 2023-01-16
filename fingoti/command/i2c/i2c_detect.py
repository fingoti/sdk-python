from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class I2CDetect(Command):
    def __init__(self):
        self._data_store = {
            "property": "i2cDetect"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addI2CDetect(self):
    """
    [Read]

    Adds a i2cDetect command to the builder
    """
    self.add(I2CDetect().read())