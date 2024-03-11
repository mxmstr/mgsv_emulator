from mgsv_emulator.command.Command import Command
from mgsv_emulator.database.Database import Database
import random, string
from mgsv_emulator import settings
import logging
logger = logging.getLogger(settings.LOGGER_NAME)

class CMD_REQAUTH_HTTPS(Command):

    def __init__(self, receiver):
        super(CMD_REQAUTH_HTTPS, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = False
        self._receiver.compress = False
        
        self._database = Database()
        self._database.connect()

    def get_data(self, data):
        steam_id = data['user_name']
        crypto_key = 'MyCoolCryptoKeyAAAAAAA=='
        session_id = str(random.randint(10**(31), 10**32 - 1)).zfill(32)

        self._database.update_player_crypto_key(steam_id, crypto_key)
        self._database.update_player_session_id(steam_id, session_id)

        data = {
            'aes_key': None,
            'cbc_iv': None,
            'crypto_key': crypto_key,
            'crypto_type': 'COMMON',
            'flowid': None,
            'heartbeat_sec': 60,
            'hmac_key': None,
            'inquiry_id': 123456789,
            'is_use_apr': 0,
            'msgid': 'CMD_REQAUTH_HTTPS',
            'result': 'NOERR',
            'rqid': 0,  
            'session': session_id,
            'smart_device_id': 'sMaRtDeViCeId',
            'timeout_sec': 200,
            'user_id': steam_id,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data(data)
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'ccpa_state_index': 20, 'gdpr_country_index': 65, 'hash': 'gGmlGMNVNrcjEI9mEnSEHA==', 'is_tpp': 0, 'msgid': 'CMD_REQAUTH_HTTPS', 'platform': 'Steam', 'rqid': 0, 'ugc': 1, 'user_name': '00000000000000000', 'ver': '14'}, 'original_size': 199, 'session_crypto': False, 'session_key': ''}
{'compress': False, 'data': {'aes_key': None, 'cbc_iv': None, 'crypto_key': 'RRfjaiuZOGAxUSEID3+L4A==', 'crypto_type': 'COMMON', 'flowid': 
None, 'heartbeat_sec': 60, 'hmac_key': None, 'inquiry_id': 301812496, 'is_use_apr': 0, 'msgid': 'CMD_REQAUTH_HTTPS', 'result': 'NOERR', 'rqid': 0, 'session': '92af43b5373d4c968e70e847771b2d98', 'smart_device_id': 'cVpFczZGdXlxSEd0NUJsclpaSXI4TGpPNWFQejY2bDdoeDhJOEpTNVVNbzY1UEM3TzRWR2JkdWExTEp3Yjh3TXc5N3FRUzZLUUpBODlvbkY=', 'timeout_sec': 200, 'user_id': 596163, 'xuid': None}, 'original_size': 455, 'session_crypto': False, 'session_key': None}
"""
