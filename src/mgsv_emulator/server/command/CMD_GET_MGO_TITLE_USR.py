from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_TITLE_USR(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_TITLE_USR, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_GET_MGO_TITLE_USR',
            'result': 'NOERR',
            'rqid': 0,
            'title_list': [
                {'flag': 0, 'gp': 0, 'id': 90900},
                {'flag': 0, 'gp': 0, 'id': 11160},
                {'flag': 0, 'gp': 0, 'id': 11180}
            ],
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_TITLE_USR', 'rqid': 0, 'target': {'np_id': {'handler': {'data': '', 'term': 0}}, 'player_id': 0, 'steam_id': 0, 'xuid': 0}}, 'original_size': 130, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_MGO_TITLE_USR', 'result': 'NOERR', 'rqid': 0, 'title_list': [{'flag': 0, 'gp': 0, 'id': 90900}, {'flag': 0, 'gp': 0, 'id': 11160}, {'flag': 0, 'gp': 0, 'id': 11180}], 'xuid': None}, 'original_size': 212, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
