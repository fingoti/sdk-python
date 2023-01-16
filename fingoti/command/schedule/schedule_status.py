from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class ScheduleStatus(Command):
    def __init__(self):
        self._data_store = {
            "property": "scheduleStatus"
        }
    
    def read(self, payload):
        self._data_store["operation"] = CommandOperation.READ
        self._data_store["payload"] = payload
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addScheduleStatus(self, slot:int = None, enabled:bool = None):
    """
    [Read & Write]

    Adds a scheduleStatus command to the builder

    Arguments
    ----------
    slot - int, required
    
    enabled - bool, optional 
    """
    validSlot = { 1, 2, 3, 4 }
    if(slot not in validSlot):
        raise ValueError("slot must be one of %r." % validSlot)
    else:
        if(enabled is None):
            self.add(ScheduleStatus().read({ "slot": slot }))
        else:
            self.add(ScheduleStatus().write({
                "slot": slot,
                "enabled": enabled
            }))