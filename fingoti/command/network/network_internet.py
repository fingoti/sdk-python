from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class NetworkInternet(Command):
    def __init__(self):
        self._data_store = {
            "property": "networkInternet"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addNetworkInternet(self):
    """
    [Read]

    Adds a networkInternet command to the builder
    """
    self.add(NetworkInternet().read())