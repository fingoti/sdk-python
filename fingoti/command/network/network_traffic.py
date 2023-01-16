from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class NetworkTraffic(Command):
    def __init__(self):
        self._data_store = {
            "property": "networkTraffic"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

def addNetworkTraffic(self):
    """
    [Read]

    Adds a networkTraffic command to the builder
    """
    self.add(NetworkTraffic().read())