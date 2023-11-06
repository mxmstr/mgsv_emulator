from mgsv_emulator.command.Command import Command
import random, string

class CMD_REQAUTH_HTTPS(Command):

    def __init__(self, receiver):
        super(CMD_REQAUTH_HTTPS, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = False

    def get_data(self):
        data = {
            'aes_key': None,
            'cbc_iv': None,
            'crypto_key': 'MyCoolCryptoKeyAAAAAAA==',
            'crypto_type': 'COMMON',
            'flowid': None,
            'heartbeat_sec': 60,
            'hmac_key': None,
            'inquiry_id': 123456789,
            'is_use_apr': 0,
            'msgid': 'CMD_REQAUTH_HTTPS',
            'result': 'NOERR',
            'rqid': 0,  
            'session': '11111111111111111111111111111111',
            'smart_device_id': 'sMaRtDeViCeId',
            'timeout_sec': 200,
            'user_id': 000000,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'ccpa_state_index': 20, 'gdpr_country_index': 65, 'hash': 'gGmlGMNVNrcjEI9mEnSEHA==', 'is_tpp': 0, 'msgid': 'CMD_REQAUTH_HTTPS', 'platform': 'Steam', 'rqid': 0, 'ugc': 1, 'user_name': '00000000000000000', 'ver': '14'}, 'original_size': 199, 'session_crypto': False, 'session_key': ''}
{'compress': False, 'data': {'aes_key': None, 'cbc_iv': None, 'crypto_key': 'RRfjaiuZOGAxUSEID3+L4A==', 'crypto_type': 'COMMON', 'flowid': 
None, 'heartbeat_sec': 60, 'hmac_key': None, 'inquiry_id': 301812496, 'is_use_apr': 0, 'msgid': 'CMD_REQAUTH_HTTPS', 'result': 'NOERR', 'rqid': 0, 'session': '92af43b5373d4c968e70e847771b2d98', 'smart_device_id': 'cVpFczZGdXlxSEd0NUJsclpaSXI4TGpPNWFQejY2bDdoeDhJOEpTNVVNbzY1UEM3TzRWR2JkdWExTEp3Yjh3TXc5N3FRUzZLUUpBODlvbkY=', 'timeout_sec': 200, 'user_id': 596163, 'xuid': None}, 'original_size': 455, 'session_crypto': False, 'session_key': None}
"""
