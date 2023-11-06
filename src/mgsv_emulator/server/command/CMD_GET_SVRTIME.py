from mgsv_emulator.command.Command import Command
import time

class CMD_GET_SVRTIME(Command):

    def __init__(self, receiver):
        super(CMD_GET_SVRTIME, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = False

    def get_time(self):
        data = {
            'crypto_type': 'COMMON', 
            'date': 1420088400, 
            'flowid': None, 
            'msgid': 'CMD_GET_SVRTIME', 
            'result': 'NOERR', 
            'rqid': 0, 
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_time()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_SVRTIME', 'rqid': 0}, 'original_size': 36, 'session_crypto': False, 'session_key': ''}
{'compress': False, 'data': {'crypto_type': 'COMMON', 'date': 1698730856, 'flowid': None, 'msgid': 'CMD_GET_SVRTIME', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 120, 'session_crypto': False, 'session_key': None}
{'compress': False, 'data': {'crypto_type': 'COMMON', 'date': 1420088400, 'flowid': None, 'msgid': 'CMD_GET_SVRTIME', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 120, 'session_crypto': False, 'session_key': None}
"""
