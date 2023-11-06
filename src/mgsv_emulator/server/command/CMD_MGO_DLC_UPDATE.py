from mgsv_emulator.command.Command import Command

class CMD_MGO_DLC_UPDATE(Command):
    
    def __init__(self, receiver):
        super(CMD_MGO_DLC_UPDATE, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND', 
            'flowid': None, 
            'msgid': 'CMD_MGO_DLC_UPDATE', 
            'now_dlc_flags': 15, 
            'old_dlc_flags': 15, 
            'result': 'NOERR', 
            'rqid': 0, 
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'dlc_flags': 15, 'msgid': 'CMD_MGO_DLC_UPDATE', 'player_id': 0, 'rqid': 0}, 'original_size': 68, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_MGO_DLC_UPDATE', 'now_dlc_flags': 15, 'old_dlc_flags': 15, 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 145, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
