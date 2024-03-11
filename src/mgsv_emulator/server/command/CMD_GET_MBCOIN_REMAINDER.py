from mgsv_emulator.command.Command import Command

class CMD_GET_MBCOIN_REMAINDER(Command):

    def __init__(self, receiver):
        super(CMD_GET_MBCOIN_REMAINDER, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False

    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_GET_MBCOIN_REMAINDER',
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

