from mgsv_emulator.command.Command import Command
from mgsv_emulator.database.Database import Database
from mgsv_emulator import settings
import hashlib
import logging
logger = logging.getLogger(settings.LOGGER_NAME)


class CMD_AUTH_STEAMTICKET(Command):

    def __init__(self, receiver):
        super(CMD_AUTH_STEAMTICKET, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = False
        
        self._database = Database()
        self._database.connect()

    def get_account(self, data):
        logger.info(data['steam_ticket'])
        steam_ticket = data['steam_ticket']

        # Terribly hacky way to get a unique user id from the steam ticket
        hash_object = hashlib.sha256(steam_ticket[16:28].encode())
        hash_value = int(hash_object.hexdigest(), 16)

        # Ensure a 17-digit hash value
        steam_id = hash_value % (10**17)

        player_data = self._database.get_player_by_steam_id(steam_id)

        if not player_data:
            player_data = self._database.add_player(steam_id)

        data = {
            'account_id': player_data[1], 
            'crypto_type': 'COMMON', 
            'currency': 'USD', 
            'flowid': None, 
            'loginid_password': 'password', 
            'msgid': 'CMD_AUTH_STEAMTICKET', 
            'result': 'NOERR', 
            'rqid': 0, 
            'smart_device_id': 'sMaRtDeViCeId', 
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_account(data)
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress':False, 'data': {'country': 'ww', 'lang': 'en', 'msgid': 'CMD_AUTH_STEAMTICKET', 'region': 4, 'rqid': 0, 'steam_ticket': 'aaaaaaaa', 'steam_ticket_size': 234}, 'original_size': 1557, 'session_crypto': False, 'session_key': ''}
{'compress': False, 'data': {'account_id': '00000000000000000', 'crypto_type': 'COMMON', 'currency': 'USD', 'flowid': None, 'loginid_password': 'aaaaaaaa', 'msgid': 'CMD_AUTH_STEAMTICKET', 'result': 'NOERR', 'rqid': 0, 'smart_device_id': 'cVpFczZGdXlxSEd0NUJsclpaSXI4TGpPNWFQejY2bDdoeDhJOEpTNVVNbzY1UEM3TzRWR2JkdWExTEp3Yjh3TXc5N3FRUzZLUUpBODlvbkY=', 'xuid': None}, 'original_size': 340, 'session_crypto': False, 'session_key': None}

{'compress': False, 'data': {'country': 'ww', 'lang': 'en', 'msgid': 'CMD_AUTH_STEAMTICKET', 'region': 4, 'rqid': 0, 'steam_ticket': 'aaaaaaaa', 'steam_ticket_size': 234}, 'original_size': 1557, 'session_crypto': False, 'session_key': ''}
{'compress': False, 'data': {'account_id': '00000000000000000', 'crypto_type': 'COMMON', 'currency': 'USD', 'flowid': None, 'loginid_password': 'aaaaaaaa', 'msgid': 'CMD_AUTH_STEAMTICKET', 'result': 'NOERR', 'rqid': 0, 'smart_device_id': 'cVpFczZGdXlxSEd0NUJsclpaSXI4TGpPNWFQejY2bDdoeDhJOEpTNVVNbzY1UEM3TzRWR2JkdWExTEp3Yjh3TXc5N3FRUzZLUUpBODlvbkY=', 'xuid': None}, 'original_size': 340, 'session_crypto': False, 'session_key': None}

FAAAAHt7e3sFAAAAvvNZPwEAEAF7e3t7e3t7e
3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7
e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==', 'steam_ticket_size': 234}, 'original_size': 1557, 'session_crypto': False, 'session_key': ''}


FAAAAHt7e3sCAAAAYHtpqvOGMwF7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7
e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t
7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7e3t7AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAA==
"""
