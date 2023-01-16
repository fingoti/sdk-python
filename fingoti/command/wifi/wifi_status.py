from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class WifiStatus(Command):
    def __init__(self):
        self._data_store = {
            "property": "wifiStatus"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addWifiStatus(self, restart:bool = None):
    """
    [Read & Write]

    Adds a wifiStatus command to the builder

    Arguments
    ----------
    restart - bool, optional
    """
    if(restart is not None):
        self.add(WifiStatus().write({
            "restart": restart,
        }))
    else:
        self.add(WifiStatus().read())