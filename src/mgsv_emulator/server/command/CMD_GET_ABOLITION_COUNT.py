from mgsv_emulator.command.Command import Command

class CMD_GET_ABOLITION_COUNT(Command):

    def __init__(self, receiver):
        super(CMD_GET_ABOLITION_COUNT, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False

    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND', 
            'flowid': None, 
            'info': {
                'count': 3, 
                'date': 1624118103, 
                'max': 2147483647, 
                'num': 21614, 
                'status': 0
                }, 
            'msgid': 'CMD_GET_ABOLITION_COUNT', 
            'result': 'NOERR', 
            'rqid': 0, 
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_ABOLITION_COUNT', 'rqid': 0}, 'original_size': 44, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'info': {'count': 3, 'date': 1624118103, 'max': 2147483647, 'num': 21614, 'status': 0}, 'msgid': 'CMD_GET_ABOLITION_COUNT', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 189, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
