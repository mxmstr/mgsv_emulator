from mgsv_emulator.command.Command import Command

class CMD_MGO_MISSION_RESULT(Command):
    
    def __init__(self, receiver):
        super(CMD_MGO_MISSION_RESULT, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True
        
    def get_data(self):
        data = {
            'character_index': 0, 
            'code': 0, 
            'crypto_type': 'COMPOUND', 
            'current_gp': 999999, 
            'current_xp': 999999, 
            'earned_gp': 0, 
            'earned_xp': 0, 
            'flowid': None, 
            'msgid': 'CMD_MGO_MISSION_RESULT', 
            'rank_param': {
                'current_rank_xp': 999999, 
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
            'ucd': '595034-0',
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'action_list': {'key': 0, 'value': 0}, 'actions_list': [{'key': 1009056792, 'value': 0}, {'key': 3074809037, 'value': 0}, {'key': 1172841627, 'value': 0}, {'key': 3011730052, 'value': 0}, {'key': 1117213263, 'value': 0}, {'key': 2279509158, 'value': 0}, {'key': 2638259174, 'value': 0}, {'key': 1264902684, 'value': 0}, {'key': 2360290610, 'value': 0}, {'key': 759608047, 'value': 0}, {'key': 3509205066, 'value': 0}, {'key': 1898812427, 'value': 0}, {'key': 914658497, 'value': 0}, {'key': 3220552451, 'value': 0}, {'key': 3391131435, 'value': 0}, {'key': 3278021499, 'value': 0}, {'key': 3685558784, 'value': 0}, {'key': 2597492381, 'value': 0}, {'key': 956134950, 'value': 0}, {'key': 3743820509, 'value': 0}, {'key': 4247973858, 'value': 0}, {'key': 4198921810, 'value': 0}, {'key': 3531791035, 'value': 0}, {'key': 1125549357, 'value': 0}, {'key': 4011328285, 'value': 0}, {'key': 433024927, 'value': 0}, {'key': 3323394328, 'value': 0}, {'key': 3896997883, 'value': 0}, {'key': 1086661461, 'value': 0}, {'key': 309943336, 'value': 0}, {'key': 3317856281, 'value': 0}, {'key': 255959188, 'value': 0}, {'key': 29930463, 'value': 0}, {'key': 1077628973, 'value': 0}, {'key': 1871304466, 'value': 0}, {'key': 3001637186, 'value': 0}, {'key': 2973130442, 'value': 0}, {'key': 2228647481, 'value': 0}, {'key': 1957865976, 'value': 0}, {'key': 3622646006, 'value': 0}, {'key': 3800451315, 'value': 0}, {'key': 1369013445, 'value': 0}, {'key': 1953425872, 'value': 0}, {'key': 3875254222, 'value': 0}, {'key': 259229151, 'value': 0}, {'key': 1810991501, 'value': 0}, {'key': 1170814218, 'value': 0}, {'key': 1274279971, 'value': 0}, {'key': 1939875265, 'value': 0}, {'key': 1360877150, 'value': 0}, {'key': 136521089, 'value': 0}, {'key': 3608168627, 'value': 0}, {'key': 1578514372, 'value': 0}, {'key': 2208556267, 'value': 0}], 'char_index': 0, 'earned_gp': 0, 'earned_xp': 0, 'gp_boost_mag': 100, 'match_type': 1, 'msgid': 'CMD_MGO_MISSION_RESULT', 'no_contest': 0, 'rank_param': {'current_rank_xp': 0, 'earned_rank_xp': 0}, 'room_id': '0x0', 'rqid': 0, 'rule_type': 1, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}, 'win_type': 1, 'xp_boost_mag': 100}, 'original_size': 2032, 'session_crypto': True, 'session_key': 'd0c2778d0f334249b4960523d8563723'}
{'compress': True, 'data': {'character_index': 0, 'code': 0, 'crypto_type': 'COMPOUND', 'current_gp': 9690, 'current_xp': 54265, 'earned_gp': 0, 'earned_xp': 0, 'flowid': None, 'msgid': 'CMD_MGO_MISSION_RESULT', 'rank_param': {'current_rank_xp': 18, 'earned_rank_xp': 0, 'rank_xp_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, 'result': 'NOERR', 'rqid': 0, 'survival_params': {'current_survival_wins': 0, 'earned_survival_gp': 0, 'reward_category': 'NotImplement', 'reward_id_a': 0, 'reward_id_b': 0, 'reward_id_c': 0, 'survival_update_key': 0}, 'ucd': '595034-0', 'xuid': None}, 'original_size': 500, 'session_crypto': True, 'session_key': 'd0c2778d0f334249b4960523d8563723'}
"""
