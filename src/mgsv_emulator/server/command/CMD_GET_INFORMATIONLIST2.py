from mgsv_emulator.command.Command import Command

class CMD_GET_INFORMATIONLIST2(Command):

    def __init__(self, receiver):
        super(CMD_GET_INFORMATIONLIST2, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False

    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'info_list': [],
            'info_num': 0,
            'msgid': 'CMD_GET_INFORMATIONLIST2',
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'is_mgo': 1, 'lang': 'EN', 'msgid': 'CMD_GET_INFORMATIONLIST2', 'region': 'REGION_NA', 'rqid': 0}, 'original_size': 89, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'info_list': [], 'info_num': 0, 'msgid': 'CMD_GET_INFORMATIONLIST2', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 141, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
