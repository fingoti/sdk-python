from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class MQTTSession(Command):
    def __init__(self):
        self._data_store = {
            "property": "mqttSession"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addMQTTSession(self, duration:int = None):
    """
    [Read & Write]

    Adds a mqttSession command to the builder

    Arguments
    ----------
    duration - int, optional
    """
    if(duration is not None):
        if(duration < 0 or duration > 1440):
            raise ValueError("duration must be between 0 and 1440")
        self.add(MQTTSession().write({
            "duration": duration
        }))
    else:
        self.add(MQTTSession().read())