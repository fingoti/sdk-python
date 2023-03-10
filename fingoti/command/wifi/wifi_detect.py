from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class WifiDetect(Command):
    def __init__(self):
        self._data_store = {
            "property": "wifiDetect"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addWifiDetect(self):
    """
    [Read]

    Adds a wifiDetect command to the builder
    """
    self.add(WifiDetect().read())