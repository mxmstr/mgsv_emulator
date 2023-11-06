from mgsv_emulator.command.Command import Command
from mgsv_emulator.database.Database import Database



class CMD_AUTH_STEAMTICKET(Command):

    def __init__(self, receiver):
        super(CMD_AUTH_STEAMTICKET, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = False

    def get_account(self, data):
        data = {
            'account_id': '00000000000000000', 
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
        # we need to proxy client request to konami server
        # or implement our own auth service based on client ip
        return data

    def execute(self, data):
        # p = Proxy()

        data = self.get_account(data)
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress':False, 'data': {'country': 'ww', 'lang': 'en', 'msgid': 'CMD_AUTH_S+TEAMTICKET', 'region': 4, 'rqid': 0, 'steam_ticket': 'aaaaaaaa', 'steam_ticket_size': 234}, 'original_size': 1557, 'session_crypto': False, 'session_key': ''}
{'compress': False, 'data': {'account_id': '00000000000000000', 'crypto_type': 'COMMON', 'currency': 'USD', 'flowid': None, 'loginid_password': 'aaaaaaaa', 'msgid': 'CMD_AUTH_STEAMTICKET', 'result': 'NOERR', 'rqid': 0, 'smart_device_id': 'cVpFczZGdXlxSEd0NUJsclpaSXI4TGpPNWFQejY2bDdoeDhJOEpTNVVNbzY1UEM3TzRWR2JkdWExTEp3Yjh3TXc5N3FRUzZLUUpBODlvbkY=', 'xuid': None}, 'original_size': 340, 'session_crypto': False, 'session_key': None}

{'compress': False, 'data': {'country': 'ww', 'lang': 'en', 'msgid': 'CMD_AUTH_STEAMTICKET', 'region': 4, 'rqid': 0, 'steam_ticket': 'aaaaaaaa', 'steam_ticket_size': 234}, 'original_size': 1557, 'session_crypto': False, 'session_key': ''}
{'compress': False, 'data': {'account_id': '00000000000000000', 'crypto_type': 'COMMON', 'currency': 'USD', 'flowid': None, 'loginid_password': 'aaaaaaaa', 'msgid': 'CMD_AUTH_STEAMTICKET', 'result': 'NOERR', 'rqid': 0, 'smart_device_id': 'cVpFczZGdXlxSEd0NUJsclpaSXI4TGpPNWFQejY2bDdoeDhJOEpTNVVNbzY1UEM3TzRWR2JkdWExTEp3Yjh3TXc5N3FRUzZLUUpBODlvbkY=', 'xuid': None}, 'original_size': 340, 'session_crypto': False, 'session_key': None}
"""
