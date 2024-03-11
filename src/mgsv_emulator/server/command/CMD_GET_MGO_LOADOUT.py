from mgsv_emulator.command.Command import Command
from mgsv_emulator.database.Database import Database
import json

class CMD_GET_MGO_LOADOUT(Command):

    def __init__(self, receiver):
        super(CMD_GET_MGO_LOADOUT, self).__init__(receiver)
        self._receiver.encrypt = True
        self._receiver.compress = True
        self._database = Database()
        self._database.connect()

    def get_data(self):

        session_key = self._receiver.session_key
        player_id = self._database.get_player_by_session_id(session_key)['id']
        loadout_json = self._database.get_player_loadout_json(player_id)['loadout_json']

        data = {
            "loadout": json.loads(loadout_json),
            'crypto_type': 'COMPOUND',
            'flowid': None,
            'msgid': 'CMD_GET_MGO_LOADOUT', 
            'result': 'NOERR', 
            'rqid': 0, 
            'xuid': None
        }
        return data

        # character_list = self._database.get_player_characters(player_id)
        # loadout = {
        #     "character_list": [],
        #     "version": 192687032374006,
        # }

        # for index, character in enumerate(character_list):
        #     loadout["character_list"].append(self._database.get_player_character_loadouts(character['id']))

        # data = {
        #     'crypto_type': 'COMPOUND',
        #     'flowid': None,
        #     "loadout": {
        #         "character_list": [
        #             {
        #                 "loadout_list": [
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [1563954279, 0],
        #                                 "id": 0,
        #                                 "model": 878119308,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 1160916322],
        #                                 "id": 1,
        #                                 "model": 3265718520,
        #                             },
        #                             {"color_list": [76167981, 0], "id": 2, "model": 3491263666},
        #                             {"color_list": [0, 0], "id": 3, "model": 3286648596},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 1",
        #                         "skill_list": [
        #                             {"id": 579839945, "slot": 0},
        #                             {"id": 3633305101, "slot": 1},
        #                             {"id": 0, "slot": 2},
        #                             {"id": 0, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 269631637, "slot": 1},
        #                             {"id": 4081261017, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3712829282,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     2072995294,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1428948095,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [1563954279, 0],
        #                                 "id": 0,
        #                                 "model": 878119308,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 1160916322],
        #                                 "id": 1,
        #                                 "model": 3265718520,
        #                             },
        #                             {"color_list": [76167981, 0], "id": 2, "model": 3491263666},
        #                             {"color_list": [0, 0], "id": 3, "model": 3286648596},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 2",
        #                         "skill_list": [
        #                             {"id": 3633305101, "slot": 0},
        #                             {"id": 519513254, "slot": 1},
        #                             {"id": 464081694, "slot": 2},
        #                             {"id": 4228227366, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [1563954279, 0],
        #                                 "id": 0,
        #                                 "model": 878119308,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 1160916322],
        #                                 "id": 1,
        #                                 "model": 3265718520,
        #                             },
        #                             {"color_list": [76167981, 0], "id": 2, "model": 3491263666},
        #                             {"color_list": [0, 0], "id": 3, "model": 3286648596},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 3",
        #                         "skill_list": [
        #                             {"id": 3633305101, "slot": 0},
        #                             {"id": 519513254, "slot": 1},
        #                             {"id": 464081694, "slot": 2},
        #                             {"id": 4228227366, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [1563954279, 0],
        #                                 "id": 0,
        #                                 "model": 878119308,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 1160916322],
        #                                 "id": 1,
        #                                 "model": 3265718520,
        #                             },
        #                             {"color_list": [76167981, 0], "id": 2, "model": 3491263666},
        #                             {"color_list": [0, 0], "id": 3, "model": 3286648596},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 4",
        #                         "skill_list": [
        #                             {"id": 3633305101, "slot": 0},
        #                             {"id": 519513254, "slot": 1},
        #                             {"id": 464081694, "slot": 2},
        #                             {"id": 4228227366, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [1563954279, 0],
        #                                 "id": 0,
        #                                 "model": 878119308,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 1160916322],
        #                                 "id": 1,
        #                                 "model": 3265718520,
        #                             },
        #                             {"color_list": [76167981, 0], "id": 2, "model": 3491263666},
        #                             {"color_list": [0, 0], "id": 3, "model": 3286648596},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 5",
        #                         "skill_list": [
        #                             {"id": 3633305101, "slot": 0},
        #                             {"id": 519513254, "slot": 1},
        #                             {"id": 464081694, "slot": 2},
        #                             {"id": 4228227366, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                 ]
        #             },
        #             {
        #                 "loadout_list": [
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [441935374, 0],
        #                                 "id": 0,
        #                                 "model": 4065425141,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2421028971, 1358930537],
        #                                 "id": 2,
        #                                 "model": 1204402912,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 3,
        #                                 "model": 2086923139,
        #                             },
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 1117833305, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "",
        #                         "skill_list": [
        #                             {"id": 579839945, "slot": 0},
        #                             {"id": 2747167640, "slot": 1},
        #                             {"id": 0, "slot": 2},
        #                             {"id": 0, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 4081261017, "slot": 0},
        #                             {"id": 1767259635, "slot": 1},
        #                             {"id": 2364332929, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 607421681,
        #                                 "part_list": [
        #                                     2663252349,
        #                                     3712829282,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1992229818,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [441935374, 0],
        #                                 "id": 0,
        #                                 "model": 4065425141,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2421028971, 1358930537],
        #                                 "id": 2,
        #                                 "model": 1204402912,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 3,
        #                                 "model": 2086923139,
        #                             },
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 2",
        #                         "skill_list": [
        #                             {"id": 4225071198, "slot": 0},
        #                             {"id": 943980862, "slot": 1},
        #                             {"id": 1904833689, "slot": 2},
        #                             {"id": 3872009463, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3601061635, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [441935374, 0],
        #                                 "id": 0,
        #                                 "model": 4065425141,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2421028971, 1358930537],
        #                                 "id": 2,
        #                                 "model": 1204402912,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 3,
        #                                 "model": 2086923139,
        #                             },
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 3",
        #                         "skill_list": [
        #                             {"id": 4225071198, "slot": 0},
        #                             {"id": 943980862, "slot": 1},
        #                             {"id": 1904833689, "slot": 2},
        #                             {"id": 3872009463, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3601061635, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [441935374, 0],
        #                                 "id": 0,
        #                                 "model": 4065425141,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2421028971, 1358930537],
        #                                 "id": 2,
        #                                 "model": 1204402912,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 3,
        #                                 "model": 2086923139,
        #                             },
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 4",
        #                         "skill_list": [
        #                             {"id": 4225071198, "slot": 0},
        #                             {"id": 943980862, "slot": 1},
        #                             {"id": 1904833689, "slot": 2},
        #                             {"id": 3872009463, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3601061635, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [441935374, 0],
        #                                 "id": 0,
        #                                 "model": 4065425141,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2421028971, 1358930537],
        #                                 "id": 2,
        #                                 "model": 1204402912,
        #                             },
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 3,
        #                                 "model": 2086923139,
        #                             },
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 5",
        #                         "skill_list": [
        #                             {"id": 4225071198, "slot": 0},
        #                             {"id": 943980862, "slot": 1},
        #                             {"id": 1904833689, "slot": 2},
        #                             {"id": 3872009463, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3601061635, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                 ]
        #             },
        #             {
        #                 "loadout_list": [
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 0,
        #                                 "model": 2579147060,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2358646918, 2450835308],
        #                                 "id": 2,
        #                                 "model": 2281828283,
        #                             },
        #                             {"color_list": [0, 0], "id": 3, "model": 0},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "",
        #                         "skill_list": [
        #                             {"id": 579839945, "slot": 0},
        #                             {"id": 464081694, "slot": 1},
        #                             {"id": 0, "slot": 2},
        #                             {"id": 0, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 2248417544, "slot": 1},
        #                             {"id": 269631637, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 423384800,
        #                                 "part_list": [
        #                                     3863544238,
        #                                     4053784175,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 1,
        #                             },
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 1147843460,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3712829282,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 0,
        #                                 "model": 2579147060,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2358646918, 2450835308],
        #                                 "id": 2,
        #                                 "model": 2281828283,
        #                             },
        #                             {"color_list": [0, 0], "id": 3, "model": 0},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 2",
        #                         "skill_list": [
        #                             {"id": 3633305101, "slot": 0},
        #                             {"id": 519513254, "slot": 1},
        #                             {"id": 464081694, "slot": 2},
        #                             {"id": 4228227366, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 0,
        #                                 "model": 2579147060,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2358646918, 2450835308],
        #                                 "id": 2,
        #                                 "model": 2281828283,
        #                             },
        #                             {"color_list": [0, 0], "id": 3, "model": 0},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 3",
        #                         "skill_list": [
        #                             {"id": 3633305101, "slot": 0},
        #                             {"id": 519513254, "slot": 1},
        #                             {"id": 464081694, "slot": 2},
        #                             {"id": 4228227366, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 0,
        #                                 "model": 2579147060,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2358646918, 2450835308],
        #                                 "id": 2,
        #                                 "model": 2281828283,
        #                             },
        #                             {"color_list": [0, 0], "id": 3, "model": 0},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 4",
        #                         "skill_list": [
        #                             {"id": 3633305101, "slot": 0},
        #                             {"id": 519513254, "slot": 1},
        #                             {"id": 464081694, "slot": 2},
        #                             {"id": 4228227366, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                     {
        #                         "gear_list": [
        #                             {
        #                                 "color_list": [2421028971, 0],
        #                                 "id": 0,
        #                                 "model": 2579147060,
        #                             },
        #                             {"color_list": [0, 0], "id": 1, "model": 0},
        #                             {
        #                                 "color_list": [2358646918, 2450835308],
        #                                 "id": 2,
        #                                 "model": 2281828283,
        #                             },
        #                             {"color_list": [0, 0], "id": 3, "model": 0},
        #                             {"color_list": [0, 0], "id": 4, "model": 0},
        #                         ],
        #                         "item_list": [
        #                             {"id": 3042025770, "slot": 0},
        #                             {"id": 215757141, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "name": "Loadout 5",
        #                         "skill_list": [
        #                             {"id": 3633305101, "slot": 0},
        #                             {"id": 519513254, "slot": 1},
        #                             {"id": 464081694, "slot": 2},
        #                             {"id": 4228227366, "slot": 3},
        #                         ],
        #                         "support_weapon_list": [
        #                             {"id": 3234702229, "slot": 0},
        #                             {"id": 3042025770, "slot": 1},
        #                             {"id": 3042025770, "slot": 2},
        #                             {"id": 3042025770, "slot": 3},
        #                         ],
        #                         "weapon_list": [
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 3298413411,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     2627764214,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 0,
        #                             },
        #                             {"id": 3042025770, "slot": 1},
        #                             {
        #                                 "color_list": [0, 0],
        #                                 "id": 640897114,
        #                                 "part_list": [
        #                                     1233100119,
        #                                     3779714243,
        #                                     3779714243,
        #                                     451724223,
        #                                     451724223,
        #                                     414743123,
        #                                 ],
        #                                 "slot": 2,
        #                             },
        #                         ],
        #                     },
        #                 ]
        #             },
        #         ],
        #         "version": 192687032374006,
        #     },
        #     'msgid': 'CMD_GET_MGO_LOADOUT', 'result': 'NOERR', 'rqid': 0, 'xuid': None
        # }

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{'compress': False, 'data': {'msgid': 'CMD_GET_MGO_LOADOUT', 'player_id': 0, 'rqid': 0}, 'original_size': 54, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
{'compress': True, 'data': {'crypto_type': 'COMPOUND', 'flowid': None, 'loadout': {'character_list': [{'loadout_list': [{'gear_list': [{'color_list': [0, 0], 'id': 0, 'model': 0}, {'color_list': [0, 0], 'id': 1, 'model': 0}, {'color_list': [2358646918, 1376435972], 'id': 2, 'model': 2111805397}, {'color_list': [0, 0], 'id': 3, 'model': 0}, {'color_list': [0, 0], 'id': 4, 'model': 0}], 'item_list': [{'id': 3042025770, 'slot': 0}, {'id': 215757141, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'name': 'Loadout 1', 'skill_list': [{'id': 3633305101, 'slot': 0}, {'id': 519513254, 'slot': 1}, {'id': 464081694, 'slot': 2}, {'id': 4228227366, 'slot': 3}], 'support_weapon_list': [{'id': 3234702229, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 
'weapon_list': [{'color_list': [0, 0], 'id': 3298413411, 'part_list': [1233100119, 3779714243, 3779714243, 2627764214, 451724223, 414743123], 'slot': 0}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 1}, {'color_list': [0, 0], 'id': 640897114, 'part_list': [1233100119, 3779714243, 3779714243, 451724223, 451724223, 414743123], 'slot': 2}]}]}, {'loadout_list': [{'gear_list': [{'color_list': [0, 0], 'id': 0, 'model': 0}, {'color_list': [0, 0], 'id': 1, 'model': 0}, {'color_list': [76167981, 2445034557], 'id': 2, 'model': 1998788085}, {'color_list': [0, 0], 'id': 3, 'model': 0}, {'color_list': [0, 0], 'id': 4, 'model': 0}], 'item_list': [{'id': 3042025770, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'name': '', 'skill_list': [{'id': 0, 'slot': 0}, {'id': 0, 'slot': 1}, {'id': 0, 'slot': 2}, {'id': 0, 'slot': 3}], 'support_weapon_list': [{'id': 3042025770, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'weapon_list': [{'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 0}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 1}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 2}]}]}, {'loadout_list': [{'gear_list': [{'color_list': [0, 0], 'id': 0, 'model': 0}, {'color_list': [0, 0], 'id': 1, 'model': 0}, {'color_list': [76167981, 2445034557], 'id': 2, 'model': 1998788085}, {'color_list': [0, 0], 'id': 3, 'model': 0}, {'color_list': [0, 0], 'id': 4, 'model': 0}], 'item_list': [{'id': 3042025770, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'name': '', 'skill_list': [{'id': 0, 'slot': 0}, {'id': 0, 'slot': 1}, {'id': 0, 'slot': 2}, {'id': 0, 'slot': 3}], 'support_weapon_list': [{'id': 3042025770, 'slot': 0}, {'id': 3042025770, 'slot': 1}, {'id': 3042025770, 'slot': 2}, {'id': 3042025770, 'slot': 3}], 'weapon_list': [{'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 0}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 1}, {'color_list': [0, 0], 'id': 3042025770, 'part_list': [0, 0, 0, 0, 0, 0], 'slot': 2}]}]}], 'version': 192687032374006}, 'msgid': 'CMD_GET_MGO_LOADOUT', 'result': 'NOERR', 'rqid': 0, 'xuid': None}, 'original_size': 2810, 'session_crypto': True, 'session_key': '92af43b5373d4c968e70e847771b2d98'}
"""
