from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class NetworkIP(Command):
    def __init__(self):
        self._data_store = {
            "property": "networkIp"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addNetworkIP(self, dhcp:bool = None, local:str = None, mask:str = None, gateway:str = None, dns:str = None):
    """
    [Read & Write]

    Adds a networkIp command to the builder

    Arguments
    ----------
    dhcp - bool, optional

    local - str, optional

    mask - str, optional

    gateway - str, optional

    dns - str, optional 
    """
    if(dhcp is not None):
        if(dhcp is True):
            self.add(NetworkIP().write({ "dhcp": dhcp }))
        else:
            self.add(NetworkIP().write({
                "dhcp": dhcp,
                "local": local,
                "mask": mask,
                "gateway": gateway,
                "dns": dns
             }))
    else:
        self.add(NetworkIP().read())