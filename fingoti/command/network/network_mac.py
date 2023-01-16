from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class NetworkMAC(Command):
    def __init__(self):
        self._data_store = {
            "property": "networkMac"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addNetworkMAC(self):
    """
    [Read]

    Adds a networkMac command to the builder
    """
    self.add(NetworkMAC().read())