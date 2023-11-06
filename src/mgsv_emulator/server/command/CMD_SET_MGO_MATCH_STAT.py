from mgsv_emulator.command.Command import Command

class CMD_SET_MGO_MATCH_STAT(Command):

    def __init__(self, receiver):
        super(CMD_SET_MGO_MATCH_STAT, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND', 
            'flowid': None, 
            'msgid': 'CMD_SET_MGO_MATCH_STAT', 
            'result': 'NOERR', 
            'rqid': 0, 
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'abandon': 6, 'msgid': 'CMD_SET_MGO_MATCH_STAT', 'played': 1, 'rqid': 0, 'started': 10, 'target': {'np_id': {'handler': {'data': '', 'term': 0}}, 'player_id': 0, 'steam_id': 0, 'xuid': 0}}, 'original_size': 167, 'session_crypto': True, 'session_key': 'd0c2778d0f334249b4960523d8563723'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_SET_MGO_MATCH_STAT', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 111, 'session_crypto': True, 'session_key': 'd0c2778d0f334249b4960523d8563723'}
"""
