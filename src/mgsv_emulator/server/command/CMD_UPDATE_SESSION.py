from mgsv_emulator.command.Command import Command

class CMD_UPDATE_SESSION(Command):
    
    def __init__(self, receiver):
        super(CMD_UPDATE_SESSION, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND', 
            'flowid': None, 
            'fob_index': -1, 
            'msgid': 'CMD_UPDATE_SESSION', 
            'result': 'NOERR', 
            'rqid': 0, 
            'sneak_mode': -1, 
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '82cac4a7c5704161a49b5cf4b7049f78'}

{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 
'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '82cac4a7c5704161a49b5cf4b7049f78'}

{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '82cac4a7c5704161a49b5cf4b7049f78'}

{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 
'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '82cac4a7c5704161a49b5cf4b7049f78'}

{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '82cac4a7c5704161a49b5cf4b7049f78'}

{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 
'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '82cac4a7c5704161a49b5cf4b7049f78'}


{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n

{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n

{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}


{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}
{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}

{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}

{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n

{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n

{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'msgid': 'CMD_UPDATE_SESSION', 'rqid': 0}, 'original_size': 39, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'fob_index': -1, 'msgid': 'CMD_UPDATE_SESSION', 'result': 'NOERR', 'rqid': 0, 'sneak_mode': -1, 'xuid': None}, 'original_size': 138, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
"""