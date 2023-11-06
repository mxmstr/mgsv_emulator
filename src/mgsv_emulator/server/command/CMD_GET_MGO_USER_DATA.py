from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_USER_DATA(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_USER_DATA, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'gp': 999999,
            'gp_boost_mag': 0,
            'gp_expire': 'NotImplement',
            'gp_expire_unix_timestamp': 0,
            'msgid': 'CMD_GET_MGO_USER_DATA',
            'rank_xp': 999999,
            'result': 'NOERR',
            'reward': {
                'reward_category': 'MGO_REWARD_CATEGORY_GEAR',
                'reward_id_a': 2589171374,
                'reward_id_b': 0,
                'reward_id_c': 0
            },
            'rqid': 0,
            'survival_ticket_remain': 10,
            'xp_boost_mag': 0,
            'xp_expire': 'NotImplement',
            'xp_expire_unix_timestamp': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_USER_DATA', 'rqid': 0}, 'original_size': 42, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'gp': 9690, 'gp_boost_mag': 0, 'gp_expire': 'NotImplement', 'gp_expire_unix_timestamp': 0, 'msgid': 'CMD_GET_MGO_USER_DATA', 'rank_xp': 18, 'result': 'NOERR', 'reward': {'reward_category': 'MGO_REWARD_CATEGORY_GEAR', 'reward_id_a': 2589171374, 'reward_id_b': 0, 'reward_id_c': 0}, 'rqid': 0, 'survival_ticket_remain': 10, 'xp_boost_mag': 0, 'xp_expire': 'NotImplement', 'xp_expire_unix_timestamp': 0, 'xuid': None}, 'original_size': 420, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
