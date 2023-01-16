from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class MQTTCertificate(Command):
    def __init__(self):
        self._data_store = {
            "property": "mqttCertificate"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addMQTTCertificate(self, pem:str = None, clear:bool = False):
    """
    [Read & Write]

    Adds a mqttCertificate command to the builder

    Arguments
    ----------
    pem - str, optional
    
    clear - bool, optional
    """
    if(pem is not None):
        self.add(MQTTCertificate().write({
            "pem": pem
        }))
    elif(clear is not False):
        self.add(MQTTCertificate().write({
            "clear": clear
        }))
    else:
        self.add(MQTTCertificate().read())