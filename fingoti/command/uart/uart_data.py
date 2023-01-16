from socket import SO_RCVLOWAT
from fingoti.command.models import Command, CommandOperation
from fingoti.model_utils import model_to_dict

class UARTData(Command):
    def __init__(self):
        self._data_store = {
            "property": "uartData"
        }

    def write(self, payload):
        self._data_store["operation"] = CommandOperation.WRITE
        self._data_store["payload"] = payload
        return model_to_dict(self)

def addUARTData(self, data):
    """
    [Read & Write]

    Adds a uartData command to the builder

    Arguments
    ----------
    data - array[int], required
        data to send out on UART 
    """
    self.add(UARTData().write({
        "data": data
    }))