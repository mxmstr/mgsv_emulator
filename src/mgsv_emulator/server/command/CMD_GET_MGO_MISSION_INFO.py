from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_MISSION_INFO(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_MISSION_INFO, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True
        
    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'gp_boost_mag': 0,
            'msgid': 'CMD_GET_MGO_MISSION_INFO',
            'rank_param': {
                'current_rank_xp': 18,
                'earned_rank_xp': 0,
                'rank_xp_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            },
            'result': 'NOERR',
            'rqid': 0,
            'survival_params': {
                'current_survival_wins': 0,
                'earned_survival_gp': 0,
                'reward_category': 'NotImplement',
                'reward_id_a': 0,
                'reward_id_b': 0,
                'reward_id_c': 0,
                'survival_update_key': 0
            },
            'xp_boost_mag': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'match_type': 1, 'msgid': 'CMD_GET_MGO_MISSION_INFO', 'rqid': 0, 'rule_type': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}}, 'original_size': 248, 'session_crypto': True, 'session_key': '82cac4a7c5704161a49b5cf4b7049f78'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'gp_boost_mag': 0, 'msgid': 'CMD_GET_MGO_MISSION_INFO', 'rank_param': {'current_rank_xp': 18, 'earned_rank_xp': 0, 'rank_xp_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, 'result': 'NOERR', 'rqid': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}, 'xp_boost_mag': 0, 'xuid': None}, 'original_size': 425, 'session_crypto': True, 'session_key': '82cac4a7c5704161a49b5cf4b7049f78'}

{'compress': False, 'data': {'match_type': 1, 'msgid': 'CMD_GET_MGO_MISSION_INFO', 'rqid': 0, 'rule_type': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}}, 'original_size': 248, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'gp_boost_mag': 0, 'msgid': 'CMD_GET_MGO_MISSION_INFO', 'rank_param': {'current_rank_xp': 18, 'earned_rank_xp': 0, 'rank_xp_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, 'result': 'NOERR', 'rqid': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}, 'xp_boost_mag': 0, 'xuid': None}, 'original_size': 425, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n

{'compress': False, 'data': {'match_type': 1, 'msgid': 'CMD_GET_MGO_MISSION_INFO', 'rqid': 0, 'rule_type': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}}, 'original_size': 248, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'gp_boost_mag': 0, 'msgid': 'CMD_GET_MGO_MISSION_INFO', 'rank_param': {'current_rank_xp': 18, 'earned_rank_xp': 0, 'rank_xp_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, 'result': 'NOERR', 'rqid': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}, 'xp_boost_mag': 0, 'xuid': None}, 'original_size': 425, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'}

{'compress': False, 'data': {'match_type': 1, 'msgid': 'CMD_GET_MGO_MISSION_INFO', 'rqid': 0, 'rule_type': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}}, 'original_size': 248, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'gp_boost_mag': 0, 'msgid': 'CMD_GET_MGO_MISSION_INFO', 'rank_param': {'current_rank_xp': 18, 'earned_rank_xp': 0, 'rank_xp_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, 'result': 'NOERR', 'rqid': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}, 'xp_boost_mag': 0, 'xuid': None}, 'original_size': 425, 'session_crypto': True, 'session_key': '72eef15982c24f57b7ac6c9986c399ae'} /n
"""
