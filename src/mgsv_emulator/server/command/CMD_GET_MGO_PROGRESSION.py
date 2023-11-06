from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_PROGRESSION(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_PROGRESSION, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_GET_MGO_PROGRESSION',
            'progression': {
                'character_list': [
                    {'legendary': 1, 'prestige': 1, 'xp': 999999},
                    {'legendary': 1, 'prestige': 1, 'xp': 999999},
                    {'legendary': 1, 'prestige': 1, 'xp': 999999}
                ],
                'permanent_unlock_list': [1146596596, 1689202044],
                'version': 143737279559449
            },
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_PROGRESSION', 'player_id': 0, 'rqid': 0}, 'original_size': 58, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_MGO_PROGRESSION', 'progression': {'character_list': [{'legendary': 0, 'prestige': 0, 'xp': 49493}, {'legendary': 0, 'prestige': 0, 'xp': 0}, {'legendary': 0, 'prestige': 0, 'xp': 0}], 'permanent_unlock_list': [1146596596, 1689202044], 'version': 143737279559449}, 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 333, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
