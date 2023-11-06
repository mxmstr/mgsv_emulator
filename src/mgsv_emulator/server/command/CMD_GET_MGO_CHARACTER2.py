from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_CHARACTER2(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_CHARACTER2, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True

    def get_data(self):
        data = {
            'character': {
                'character_list': [
                    {
                        'avatar': {
                            'accessory_flags': 255,
                            'beard_length': 0,
                            'beard_style': 255,
                            'eyebrow_style': 2,
                            'eyebrow_width': 0,
                            'face_color': 0,
                            'face_race': 0,
                            'face_type': 5,
                            'face_variation': 0,
                            'gash_or_tattoo_variation': 0,
                            'hair_color': 1,
                            'hair_style': 255,
                            'left_eye_brightness': 0,
                            'left_eye_color': 0,
                            'motion_frame_list': [4, 5, 3, 0, 7, 5, 4, 7, 4, 10, 5, 5, 3, 5, 0, 4, 3, 8, 0, 0, 4, 10, 0, 5, 0, 2, 2, 0, 0, 3, 5, 8, 10, 2, 2, 0, 0, 4, 10, 0, 8, 6, 7, 3, 6, 0, 5, 7, 5, 5, 3, 0, 0, 5, 4, 5, 5, 5, 10, 8],
                            'right_eye_brightness': 0,
                            'right_eye_color': 0,
                            'tattoo_color': 0,
                            'voice': 15
                        },
                        'last_loadout': 0,
                        'name': '',
                        'player_class': 18,
                        'player_type': 5
                    },
                    {
                        'avatar': {
                            'accessory_flags': 0,
                            'beard_length': 0,
                            'beard_style': 0,
                            'eyebrow_style': 0,
                            'eyebrow_width': 0,
                            'face_color': 0,
                            'face_race': 0,
                            'face_type': 0,
                            'face_variation': 0,
                            'gash_or_tattoo_variation': 0,
                            'hair_color': 0,
                            'hair_style': 0,
                            'left_eye_brightness': 0,
                            'left_eye_color': 0,
                            'motion_frame_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'right_eye_brightness': 0,
                            'right_eye_color': 0,
                            'tattoo_color': 0,
                            'voice': 0
                        },
                        'last_loadout': 0,
                        'name': '',
                        'player_class': 0,
                        'player_type': 5
                    },
                    {
                        'avatar': {
                            'accessory_flags': 0,
                            'beard_length': 0,
                            'beard_style': 0,
                            'eyebrow_style': 0,
                            'eyebrow_width': 0,
                            'face_color': 0,
                            'face_race': 0,
                            'face_type': 0,
                            'face_variation': 0,
                            'gash_or_tattoo_variation': 0,
                            'hair_color': 0,
                            'hair_style': 0,
                            'left_eye_brightness': 0,
                            'left_eye_color': 0,
                            'motion_frame_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            'right_eye_brightness': 0,
                            'right_eye_color': 0,
                            'tattoo_color': 0,
                            'voice': 0
                        },
                        'last_loadout': 0,
                        'name': '',
                        'player_class': 0,
                        'player_type': 5
                    }
                ],
                'last_active': 0,
                'match': {
                    'auto_leave': 1,
                    'briefing_time': 2,
                    'host_comment': 0,
                    'max_capacity': 12,
                    'mission_slot_count': 3,
                    'mission_slot_list': [
                        {
                            'flags': 35,
                            'map': 1,
                            'night': 0,
                            'rule': 0,
                            'rush': 0,
                            'ticket': 30,
                            'time': 5,
                            'unique_character': 1,
                            'weather': 1
                        },
                        {
                            'flags': 34,
                            'map': 0,
                            'night': 1,
                            'rule': 1,
                            'rush': 1,
                            'ticket': 0,
                            'time': 7,
                            'unique_character': 0,
                            'weather': 1
                        },
                        {
                            'flags': 35,
                            'map': 2,
                            'night': 0,
                            'rule': 2,
                            'rush': 0,
                            'ticket': 0,
                            'time': 6,
                            'unique_character': 1,
                            'weather': 1
                        },
                        {
                            'flags': 34,
                            'map': 0,
                            'night': 0,
                            'rule': 0,
                            'rush': 0,
                            'ticket': 0,
                            'time': 0,
                            'unique_character': 0,
                            'weather': 0
                        },
                        {
                            'flags': 34,
                            'map': 0,
                            'night': 0,
                            'rule': 0,
                            'rush': 0,
                            'ticket': 0,
                            'time': 0,
                            'unique_character': 0,
                            'weather': 0
                        }
                    ],
                    'player_num': 2
                },
                'preset_radio_rule_list': [
                    {'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]},
                    {'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]},
                    {'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]},
                    {'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]},
                    {'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]}
                ],
                'selected_bgm': 0,
                'version': 0
            },
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_GET_MGO_CHARACTER2',
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_CHARACTER2', 'player_id': 0, 'rqid': 0}, 'original_size': 57, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'} 
{'compress': True, 'data': {'character': {'character_list': [{'avatar': {'accessory_flags': 255, 'beard_length': 0, 'beard_style': 255, 'eyebrow_style': 2, 'eyebrow_width': 0, 'face_color': 0, 'face_race': 0, 'face_type': 5, 'face_variation': 0, 'gash_or_tattoo_variation': 0, 'hair_color': 1, 'hair_style': 255, 'left_eye_brightness': 0, 'left_eye_color': 0, 'motion_frame_list': [4, 5, 3, 0, 7, 5, 4, 7, 4, 10, 5, 5, 3, 5, 0, 4, 3, 8, 0, 0, 4, 10, 0, 5, 0, 2, 2, 0, 0, 3, 5, 8, 10, 2, 2, 0, 0, 4, 10, 0, 8, 6, 7, 3, 6, 0, 5, 7, 5, 5, 3, 0, 0, 5, 4, 5, 5, 5, 10, 
8], 'right_eye_brightness': 0, 'right_eye_color': 0, 'tattoo_color': 0, 'voice': 15}, 'last_loadout': 0, 'name': '', 'player_class': 18, 'player_type': 5}, {'avatar': {'accessory_flags': 0, 'beard_length': 0, 'beard_style': 0, 'eyebrow_style': 0, 'eyebrow_width': 0, 'face_color': 0, 'face_race': 0, 'face_type': 0, 'face_variation': 0, 'gash_or_tattoo_variation': 0, 'hair_color': 0, 'hair_style': 0, 'left_eye_brightness': 0, 'left_eye_color': 0, 'motion_frame_list': 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'right_eye_brightness': 0, 'right_eye_color': 0, 'tattoo_color': 0, 'voice': 0}, 'last_loadout': 0, 
'name': '', 'player_class': 0, 'player_type': 5}, {'avatar': {'accessory_flags': 0, 'beard_length': 0, 'beard_style': 0, 'eyebrow_style': 0, 'eyebrow_width': 0, 'face_color': 0, 'face_race': 0, 'face_type': 0, 'face_variation': 0, 'gash_or_tattoo_variation': 0, 'hair_color': 0, 'hair_style': 0, 'left_eye_brightness': 0, 'left_eye_color': 0, 'motion_frame_list': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'right_eye_brightness': 0, 'right_eye_color': 0, 'tattoo_color': 0, 'voice': 0}, 'last_loadout': 0, 'name': '', 
'player_class': 0, 'player_type': 5}], 'last_active': 0, 'match': {'auto_leave': 1, 'briefing_time': 2, 'host_comment': 0, 'max_capacity': 12, 'mission_slot_count': 3, 'mission_slot_list': [{'flags': 35, 'map': 1, 'night': 0, 'rule': 0, 'rush': 0, 'ticket': 30, 'time': 5, 'unique_character': 1, 'weather': 1}, {'flags': 34, 'map': 0, 'night': 1, 'rule': 1, 'rush': 1, 'ticket': 0, 'time': 7, 'unique_character': 0, 'weather': 1}, {'flags': 35, 'map': 2, 'night': 0, 'rule': 2, 'rush': 0, 'ticket': 0, 'time': 6, 'unique_character': 1, 'weather': 1}, {'flags': 34, 'map': 0, 'night': 0, 'rule': 0, 'rush': 0, 'ticket': 0, 'time': 0, 'unique_character': 0, 'weather': 0}, {'flags': 34, 'map': 0, 'night': 0, 'rule': 0, 'rush': 0, 'ticket': 0, 'time': 0, 'unique_character': 0, 'weather': 0}], 'player_num': 2}, 'preset_radio_rule_list': [{'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]}, {'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]}, {'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]}, {'preset_radio_id_list': [0, 0, 0, 0, 0, 
0, 0, 0]}, {'preset_radio_id_list': [0, 0, 0, 0, 0, 0, 0, 0]}], 'selected_bgm': 0, 'version': 
130186347867651}, 'crypto_type': 'COMPOUND', 'flowid': None, 'msgid': 'CMD_GET_MGO_CHARACTER2', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 2727, 'session_crypto': True, 
'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
