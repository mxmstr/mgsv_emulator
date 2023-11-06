from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_MATCH_STAT(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_MATCH_STAT, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False
        
    def get_data(self):
        data = {
            'abandon': 0,
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_GET_MGO_MATCH_STAT',
            'played': 0,
            'result': 'NOERR',
            'rqid': 0,
            'started': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_MATCH_STAT', 'rqid': 0, 'target': {'np_id': {'handler': {'data': '', 'term': 0}}, 'player_id': 0, 'steam_id': 0, 'xuid': 0}}, 'original_size': 131, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'} 
{'compress': False, 'data': {'abandon': 4, 'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_MGO_MATCH_STAT', 'played': 0, 'result': 'NOERR', 'rqid': 0, 'started': 4, 'xuid': None}, 'original_size': 146, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
