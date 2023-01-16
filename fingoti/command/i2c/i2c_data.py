from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class I2CData(Command):
    def __init__(self):
        self._data_store = {
            "property": "i2cData"
        }
    
    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addI2CData(self, address:int, profile):
    """
    [Write]

    Adds a i2CData command to the builder

    Arguments
    ----------
    address - int
    
    profile - array[string]
    """
    if(address < 0 or address > 255):
        raise ValueError("address must be between 0 and 255")
    
    if(len(profile) < 1):
        raise ValueError("profile must be an array of strings")

    self.add(I2CData().write({
        "address": address,
        "profile": profile
    }))