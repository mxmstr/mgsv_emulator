from mgsv_emulator.command.Command import Command

class CMD_GET_MGO_LOADOUT(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_LOADOUT, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True

    def get_data(self):
        data = {
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'loadout': {
            'character_list': [
                {
                'loadout_list': [
                    {
                    'gear_list': [
                        {
                        'color_list': [0, 0],
                        'id': 0,
                        'model': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 1,
                        'model': 0
                        },
                        {
                        'color_list': [2358646918, 1376435972],
                        'id': 2,
                        'model': 2111805397
                        },
                        {
                        'color_list': [0, 0],
                        'id': 3,
                        'model': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 4,
                        'model': 0
                        }
                    ],
                    'item_list': [
                        {
                        'id': 3042025770,
                        'slot': 0
                        },
                        {
                        'id': 215757141,
                        'slot': 1
                        },
                        {
                        'id': 3042025770,
                        'slot': 2
                        },
                        {
                        'id': 3042025770,
                        'slot': 3
                        }
                    ],
                    'name': 'Loadout 1',
                    'skill_list': [
                        {
                        'id': 3633305101,
                        'slot': 0
                        },
                        {
                        'id': 519513254,
                        'slot': 1
                        },
                        {
                        'id': 464081694,
                        'slot': 2
                        },
                        {
                        'id': 4228227366,
                        'slot': 3
                        }
                    ],
                    'support_weapon_list': [
                        {
                        'id': 3234702229,
                        'slot': 0
                        },
                        {
                        'id': 3042025770,
                        'slot': 1
                        },
                        {
                        'id': 3042025770,
                        'slot': 2
                        },
                        {
                        'id': 3042025770,
                        'slot': 3
                        }
                    ],
                    'weapon_list': [
                        {
                        'color_list': [0, 0],
                        'id': 3298413411,
                        'part_list': [1233100119, 3779714243, 3779714243, 2627764214, 451724223, 414743123],
                        'slot': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 3042025770,
                        'part_list': [0, 0, 0, 0, 0, 0],
                        'slot': 1
                        },
                        {
                        'color_list': [0, 0],
                        'id': 640897114,
                        'part_list': [1233100119, 3779714243, 3779714243, 451724223, 451724223, 414743123],
                        'slot': 2
                        }
                    ]
                    }
                ]
                },
                {
                'loadout_list': [
                    {
                    'gear_list': [
                        {
                        'color_list': [0, 0],
                        'id': 0,
                        'model': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 1,
                        'model': 0
                        },
                        {
                        'color_list': [76167981, 2445034557],
                        'id': 2,
                        'model': 1998788085
                        },
                        {
                        'color_list': [0, 0],
                        'id': 3,
                        'model': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 4,
                        'model': 0
                        }
                    ],
                    'item_list': [
                        {
                        'id': 3042025770,
                        'slot': 0
                        },
                        {
                        'id': 3042025770,
                        'slot': 1
                        },
                        {
                        'id': 3042025770,
                        'slot': 2
                        },
                        {
                        'id': 3042025770,
                        'slot': 3
                        }
                    ],
                    'name': '',
                    'skill_list': [
                        {
                        'id': 0,
                        'slot': 0
                        },
                        {
                        'id': 0,
                        'slot': 1
                        },
                        {
                        'id': 0,
                        'slot': 2
                        },
                        {
                        'id': 0,
                        'slot': 3
                        }
                    ],
                    'support_weapon_list': [
                        {
                        'id': 3042025770,
                        'slot': 0
                        },
                        {
                        'id': 3042025770,
                        'slot': 1
                        },
                        {
                        'id': 3042025770,
                        'slot': 2
                        },
                        {
                        'id': 3042025770,
                        'slot': 3
                        }
                    ],
                    'weapon_list': [
                        {
                        'color_list': [0, 0],
                        'id': 3042025770,
                        'part_list': [0, 0, 0, 0, 0, 0],
                        'slot': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 3042025770,
                        'part_list': [0, 0, 0, 0, 0, 0],
                        'slot': 1
                        },
                        {
                        'color_list': [0, 0],
                        'id': 3042025770,
                        'part_list': [0, 0, 0, 0, 0, 0],
                        'slot': 2
                        }
                    ]
                    }
                ]
                },
                {
                'loadout_list': [
                    {
                    'gear_list': [
                        {
                        'color_list': [0, 0],
                        'id': 0,
                        'model': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 1,
                        'model': 0
                        },
                        {
                        'color_list': [76167981, 2445034557],
                        'id': 2,
                        'model': 1998788085
                        },
                        {
                        'color_list': [0, 0],
                        'id': 3,
                        'model': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 4,
                        'model': 0
                        }
                    ],
                    'item_list': [
                        {
                        'id': 3042025770,
                        'slot': 0
                        },
                        {
                        'id': 3042025770,
                        'slot': 1
                        },
                        {
                        'id': 3042025770,
                        'slot': 2
                        },
                        {
                        'id': 3042025770,
                        'slot': 3
                        }
                    ],
                    'name': '',
                    'skill_list': [
                        {
                        'id': 0,
                        'slot': 0
                        },
                        {
                        'id': 0,
                        'slot': 1
                        },
                        {
                        'id': 0,
                        'slot': 2
                        },
                        {
                        'id': 0,
                        'slot': 3
                        }
                    ],
                    'support_weapon_list': [
                        {
                        'id': 3042025770,
                        'slot': 0
                        },
                        {
                        'id': 3042025770,
                        'slot': 1
                        },
                        {
                        'id': 3042025770,
                        'slot': 2
                        },
                        {
                        'id': 3042025770,
                        'slot': 3
                        }
                    ],
                    'weapon_list': [
                        {
                        'color_list': [0, 0],
                        'id': 3042025770,
                        'part_list': [0, 0, 0, 0, 0, 0],
                        'slot': 0
                        },
                        {
                        'color_list': [0, 0],
                        'id': 3042025770,
                        'part_list': [0, 0, 0, 0, 0, 0],
                        'slot': 1
                        },
                        {
                        'color_list': [0, 0],
                        'id': 3042025770,
                        'part_list': [0, 0, 0, 0, 0, 0],
                        'slot': 2
                        }
                    ]
                    }
                ]
                }
            ]
            },
            'version': 192687032374006
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_LOADOUT', 'player_id': 0, 'rqid': 0}, 'original_size': 54, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'loadout': {'character_list': [{'loadout_list': [{'gear_list': [{'color_list': [0, 0], 'id': 0, 'model': 0}, {'color_list': [0, 0], 'id': 1, 'model': 0}, {'color_list': [2358646918, 1376435972], 'id': 2, 'model': 2111805397}, {'color_list': [0, 0], 'id': 3, 'model': 0}, {'color_list': [0, 0], 'id': 4, 'model': 0}], 'item_list': [{'id': 3042025770, 'slot': 0}, {'id': 215757141, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'name': 'Loadout 1', 'skill_list': [{'id': 3633305101, 'slot': 0}, {'id': 519513254, 'slot': 1}, {'id': 464081694, 'slot': 2}, {'id': 4228227366, 'slot': 3}], 'support_weapon_list': [{'id': 3234702229, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 
'weapon_list': [{'color_list': [0, 0], 'id': 3298413411, 'part_list': [1233100119, 3779714243, 3779714243, 2627764214, 451724223, 414743123], 'slot': 0}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 1}, {'color_list': [0, 0], 'id': 640897114, 'part_list': [1233100119, 3779714243, 3779714243, 451724223, 451724223, 414743123], 'slot': 2}]}]}, {'loadout_list': [{'gear_list': [{'color_list': [0, 0], 'id': 0, 'model': 0}, {'color_list': [0, 0], 'id': 1, 'model': 0}, {'color_list': [76167981, 2445034557], 'id': 2, 'model': 1998788085}, {'color_list': [0, 0], 'id': 3, 'model': 0}, {'color_list': [0, 0], 'id': 4, 'model': 0}], 'item_list': [{'id': 3042025770, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'name': '', 'skill_list': [{'id': 0, 'slot': 0}, {'id': 0, 'slot': 1}, {'id': 0, 'slot': 2}, {'id': 0, 'slot': 3}], 'support_weapon_list': [{'id': 3042025770, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'weapon_list': [{'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 0}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 1}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 2}]}]}, {'loadout_list': [{'gear_list': [{'color_list': [0, 0], 'id': 0, 'model': 0}, {'color_list': [0, 0], 'id': 1, 'model': 0}, {'color_list': [76167981, 2445034557], 'id': 2, 'model': 1998788085}, {'color_list': [0, 0], 'id': 3, 'model': 0}, {'color_list': [0, 0], 'id': 4, 'model': 0}], 'item_list': [{'id': 3042025770, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'name': '', 'skill_list': [{'id': 0, 'slot': 0}, {'id': 0, 'slot': 1}, {'id': 0, 'slot': 2}, {'id': 0, 'slot': 3}], 'support_weapon_list': [{'id': 3042025770, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'weapon_list': [{'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 0}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 1}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 2}]}]}], 'version': 192687032374006}, 'msgid': 'CMD_GET_MGO_LOADOUT', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 2810, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
