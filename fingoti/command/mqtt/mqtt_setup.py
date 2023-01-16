from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class MQTTSetup(Command):
    def __init__(self):
        self._data_store = {
            "property": "mqttSetup"
        }
    
    def read(self):
        self._data_store["operation"] = CommandOperation.READ
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addMQTTSetup(self, host:str = None, port:int = None, qos:int = None, secure:bool = False, retain:bool = False, username:str = None, clear: bool = False):
    """
    [Read & Write]

    Adds a mqttSetup command to the builder

    Arguments
    ----------
    host - str, optional
    
    port - int, optional

    qos - int, optional

    secure - bool, optional

    retain - bool, optional

    username - str, optional

    clear - bool, optional
    """
    if(port is not None and port is not None and qos is not None and username is not None):
        validQos = { 0, 1, 2 }
        if(qos not in validQos):
            raise ValueError("qos must be one of %r." % validQos)
        self.add(MQTTSetup().write({
            "host": host,
            "port": port,
            "qos": qos,
            "secure": secure,
            "retain": retain,
            "username": username
        }))
    elif(clear is not False):
        self.add(MQTTSetup().write({
            "clear": clear
        }))
    else:
        self.add(MQTTSetup().read())