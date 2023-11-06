from mgsv_emulator.command.Command import Command

class CMD_GET_NEXT_MAINTENANCE(Command):
    
    def __init__(self, receiver):
        super(CMD_GET_NEXT_MAINTENANCE, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'maintenance_type': 0,
            'message_type': 0,
            'msgid': 'CMD_GET_NEXT_MAINTENANCE',
            'next_maintenance': 1110,
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_NEXT_MAINTENANCE', 'rqid': 0}, 'original_size': 45, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'maintenance_type': 0, 'message_type': 0, 'msgid': 'CMD_GET_NEXT_MAINTENANCE', 'next_maintenance': 1110, 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 175, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
"""