from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_PURCHASED_ITEM(Command):
    
    def __init__(self, receiver):
        super(CMD_GET_MGO_PURCHASED_ITEM, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = False
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_GET_MGO_PURCHASED_ITEM',
            'purchasable_item_list': {
                'purchasable_item_list': []
            },
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'category': 0, 'msgid': 'CMD_GET_MGO_PURCHASED_ITEM', 'purchase_id': 0, 'rqid': 0}, 'original_size': 76, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': False, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_MGO_PURCHASED_ITEM', 'purchasable_item_list': {'purchasable_item_list': []}, 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 168, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
