from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class MQTTStatus(Command):
    def __init__(self):
        self._data_store = {
            "property": "mqttStatus"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addMQTTStatus(self, enabled:bool = None):
    """
    [Read & Write]

    Adds a mqttStatus command to the builder

    Arguments
    ----------
    enabled - bool, optional
    """
    if(enabled is not None):
        self.add(MQTTStatus().write({
            "enabled": enabled
        }))
    else:
        self.add(MQTTStatus().read())