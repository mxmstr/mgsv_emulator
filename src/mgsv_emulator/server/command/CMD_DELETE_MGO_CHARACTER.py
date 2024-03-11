from mgsv_emulator.command.Command import Command
from mgsv_emulator.database.Database import Database

class CMD_DELETE_MGO_CHARACTER(Command):

    def __init__(self, receiver):
        super(CMD_DELETE_MGO_CHARACTER, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False
        
        self._database = Database()
        self._database.connect()

    def get_data(self, data):

        session_key = self._receiver.session_key
        player_id = self._database.get_player_by_session_id(session_key)['id']
        character_index = data['characterIndex']

        self._database.delete_player_character(player_id, character_index)

        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_DELETE_MGO_CHARACTER',
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data(data)
        return self._receiver.action(data, self.__class__.__name__)

"""

{'compress': False, 'data': {'characterIndex': 2, 'msgid': 'CMD_DELETE_MGO_CHARACTER', 'rqid': 0}, 'original_size': 64, 'session_crypto': True, 'session_key': '70063169125304320129575126463724'}

"""
