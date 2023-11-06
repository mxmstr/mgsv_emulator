from mgsv_emulator.command.Command import Command

class CMD_GET_PLAYERLIST(Command):

    def __init__(self, receiver):
        super(CMD_GET_PLAYERLIST, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True

    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND', 
            'flowid': None, 
            'msgid': 'CMD_GET_PLAYERLIST', 
            'player_list': [
                {'espionage_lose': 19, 'espionage_win': 1, 'fob_grade': 4, 'fob_point': 34, 'fob_rank': 576203, 'index': 0, 'is_insurance': 0, 'league_grade': 19, 'league_rank': 72968, 'name': '00000000000000000_player01', 'playtime': 0, 'point': 0}
            ], 
            'player_num': 1, 
            'result': 'NOERR', 
            'rqid': 0, 
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_PLAYERLIST', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_PLAYERLIST', 'player_list': [{'espionage_lose': 19, 'espionage_win': 1, 'fob_grade': 4, 'fob_point': 34, 'fob_rank': 576203, 'index': 0, 'is_insurance': 0, 'league_grade': 19, 'league_rank': 72968, 'name': '00000000000000000_player01', 'playtime': 0, 'point': 0}], 'player_num': 1, 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 349, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}

{'compress': False, 'data': {'msgid': 'CMD_GET_PLAYERLIST', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_PLAYERLIST', 'player_list': [{'espionage_lose': 19, 'espionage_win': 1, 'fob_grade': 4, 'fob_point': 34, 'fob_rank': 576203, 'index': 0, 'is_insurance': 0, 'league_grade': 19, 'league_rank': 72968, 'name': '00000000000000000_player01', 'playtime': 0, 'point': 0}], 'player_num': 1, 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 349, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}

{'compress': False, 'data': {'msgid': 'CMD_GET_PLAYERLIST', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}
"""