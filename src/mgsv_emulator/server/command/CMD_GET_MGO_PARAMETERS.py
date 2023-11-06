from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_PARAMETERS(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_PARAMETERS, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True
        
    def get_data(self):
        data = {
            'MgoParameter': [
                {'id': 1328199047, 'value': 1},
                {'id': 848079236, 'value': 1000},
                {'id': 3779705668, 'value': 5000},
                {'id': 1163418251, 'value': 5000},
                {'id': 2465414369, 'value': 64},
                {'id': 3329735861, 'value': 160},
                {'id': 1316804683, 'value': 900},
                {'id': 2973312482, 'value': 450},
                {'id': 1840770005, 'value': 1500},
                {'id': 810408023, 'value': 1},
                {'id': 4012801301, 'value': 1200},
                {'id': 1918707871, 'value': 18000},
                {'id': 693879535, 'value': 500},
                {'id': 1297488958, 'value': 10000},
                {'id': 2599574229, 'value': 1},
                {'id': 687947340, 'value': 1000},
                {'id': 2341384761, 'value': 200},
                {'id': 2029346817, 'value': 5000},
                {'id': 3368912490, 'value': 2000},
                {'id': 3376035593, 'value': 8},
                {'id': 3342468677, 'value': 4},
                {'id': 2261465657, 'value': 70},
                {'id': 2008882968, 'value': 120},
                {'id': 693362684, 'value': 6},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0},
                {'id': 0, 'value': 0}
            ],
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_GET_MGO_PARAMETERS',
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_PARAMETERS', 'rqid': 0}, 'original_size': 43, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': True, 'data': {'MgoParameter': [{'id': 1328199047, 'value': 1}, {'id': 848079236, 'value': 1000}, {'id': 3779705668, 'value': 
5000}, {'id': 1163418251, 'value': 5000}, {'id': 2465414369, 'value': 64}, {'id': 3329735861, 'value': 160}, {'id': 1316804683, 'value': 900}, {'id': 2973312482, 'value': 450}, {'id': 1840770005, 'value': 1500}, {'id': 810408023, 'value': 1}, {'id': 4012801301, 'value': 1200}, 
{'id': 1918707871, 'value': 18000}, {'id': 693879535, 'value': 500}, {'id': 1297488958, 'value': 10000}, {'id': 2599574229, 'value': 1}, {'id': 687947340, 'value': 1000}, {'id': 2341384761, 'value': 200}, {'id': 2029346817, 'value': 5000}, {'id': 3368912490, 'value': 2000}, {'id': 3376035593, 'value': 8}, {'id': 3342468677, 'value': 4}, {'id': 2261465657, 'value': 70}, {'id': 2008882968, 'value': 120}, {'id': 693362684, 'value': 6}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 
0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}, {'id': 0, 'value': 0}], 'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_MGO_PARAMETERS', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 1601, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
