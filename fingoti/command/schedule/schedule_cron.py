from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class ScheduleCron(Command):
    def __init__(self):
        self._data_store = {
            "property": "scheduleCron"
        }
    
    def read(self, payload):
        self._data_store["operation"] = CommandOperation.READ
        self._data_store["payload"] = payload
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addScheduleCron(self, slot:int = None, cron:str = None):
    """
    [Read & Write]

    Adds a scheduleCron command to the builder

    Arguments
    ----------
    slot - int, required
    
    cron - str, optional
    """
    validSlot = { 1, 2, 3, 4 }
    if(slot not in validSlot):
        raise ValueError("slot must be one of %r." % validSlot)
    else:
        if(cron is None):
            self.add(ScheduleCron().read({ "slot": slot }))
        else:
            self.add(ScheduleCron().write({
                "slot": slot,
                "cron":cron
            }))