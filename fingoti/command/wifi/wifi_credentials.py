from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class WifiCredentials(Command):
    def __init__(self):
        self._data_store = {
            "property": "wifiCredentials"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addWifiCredentials(self, slot:int = None, ssid:str = None, password:str = None):
    """
    [Read & Write]

    Adds a wifiCredentials command to the builder

    Arguments
    ----------
    slot - int, required
    
    ssid - str, optional 

    password - str, optional
    """
    if(slot is not None and ssid is not None and password is not None):
        validSlots = { 0, 1 }
        if(slot not in validSlots):
            raise ValueError("slot must be one of %r." % validSlots)
        else:
            self.add(WifiCredentials().write({
                "slot": slot,
                "ssid": ssid,
                "password": password
            }))
    else:
        self.add(WifiCredentials().read())