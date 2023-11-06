from mgsv_emulator.command.Command import Command

class CMD_SEND_IPANDPORT(Command):
    
    def __init__(self, receiver):
        super(CMD_SEND_IPANDPORT, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND', 
            'flowid': None, 
            'msgid': 'CMD_SEND_IPANDPORT', 
            'result': 'NOERR', 
            'rqid': 0, 
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'ex_ip': '192.168.0.10', 'ex_port': 5733, 'in_ip': '192.168.0.10', 'in_port': 5733, 'msgid': 'CMD_SEND_IPANDPORT', 'nat': 'OPEN_INTERNET', 'rqid': 0, 'secure_device_address': 'NotImplement', 'xnaddr': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'}, 'original_size': 236, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_SEND_IPANDPORT', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 107, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
