from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class ScheduleRequest(Command):
    def __init__(self):
        self._data_store = {
            "property": "scheduleRequest"
        }
    
    def read(self, payload):
        self._data_store["operation"] = CommandOperation.READ
        self._data_store["payload"] = payload
        return model_to_dict(self)

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addScheduleRequest(self, slot:int = None, request = None):
    """
    [Read & Write]

    Adds a scheduleRequest command to the builder

    Arguments
    ----------
    slot - int, required
    
    request - object, optional
        The request array for the device to run when the schedule triggers
    """
    validSlot = { 1, 2, 3, 4 }
    if(slot not in validSlot):
        raise ValueError("slot must be one of %r." % validSlot)
    else:
        if(request is None):
            self.add(ScheduleRequest().read({ "slot": slot }))
        else:
            self.add(ScheduleRequest().write({
                "slot": slot,
                "request": request
            }))