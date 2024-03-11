from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_PURCHASABLE_ITEM_LIST(Command):
    
    def __init__(self, receiver):
        super(CMD_GET_MGO_PURCHASABLE_ITEM_LIST, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND', 
            'flowid': None, 
            'msgid': 'CMD_GET_MGO_PURCHASABLE_ITEM_LIST', 
            'purchasable_item_list': {
                'purchasable_item_list': [
                    {
                        'category': 0, 
                        'price': 800, 
                        'purchase_id': 3001001, 
                        'purchase_type': 0
                    }, 
                    {
                        'category': 1, 
                        'price': 100, 
                        'purchase_id': 4115003, 
                        'purchase_type': 0
                    }
                ]
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
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_PURCHASABLE_ITEM_LIST', 'purchase_id': 0, 'rqid': 0}, 'original_size': 70, 'session_crypto': True, 'session_key': 'd0c2778d0f334249b4960523d8563723'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_MGO_PURCHASABLE_ITEM_LIST', 'purchasable_item_list': {'purchasable_item_list': [{'category': 0, 'price': 800, 'purchase_id': 3001001, 'purchase_type': 0}, {'category': 1, 'price': 100, 'purchase_id': 4115003, 'purchase_type': 0}]}, 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 308, 'session_crypto': True, 'session_key': 'd0c2778d0f334249b4960523d8563723'}
"""
