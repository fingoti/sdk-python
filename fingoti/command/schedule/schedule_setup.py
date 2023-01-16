from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class ScheduleSetup(Command):
    def __init__(self):
        self._data_store = {
            "property": "scheduleSetup"
        }
    
    def read(self, payload):
        self._data_store["operation"] = CommandOperation.READ
        self._data_store["payload"] = payload
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addScheduleSetup(self, slot:int = None, clear:bool = None):
    """
    [Read & Write]

    Adds a scheduleSetup command to the builder

    Arguments
    ----------
    slot - int, required
    
    duration - int, optional 
    """
    validSlot = { 1, 2, 3, 4 }
    if(slot not in validSlot):
        raise ValueError("slot must be one of %r." % validSlot)
    else:
        if(clear is None):
            self.add(ScheduleSetup().read({ "slot": slot }))
        else:
            self.add(ScheduleSetup().write({
                "slot": slot,
                "clear": clear
            }))