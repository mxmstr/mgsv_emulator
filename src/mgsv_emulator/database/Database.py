#!/usr/bin/python3.11
from mgsv_emulator.logger import Logger
import pymysql, json, os

logger = Logger.create_logger('mgsv')

class Database(object):
    """docstring for Database"""
    def __init__(self):
        pass

    def connect(self):

        self._db = pymysql.connect(host="localhost",
                    user="root",
                    passwd="123",
                    db="mgsv_server")
                    #cursorclass=pymysql.cursors.DictCursor)

    def disconnect(self):
        self._db.close()

    def execute_query(self, query, values):

        cur = self._db.cursor()
        result = cur.execute(query, values)
        self._db.commit()

        return result

    def fetch_query(self, query, values, get_dict=False):

        if get_dict:
            cur = self._db.cursor(pymysql.cursors.DictCursor)
        else:
            cur = self._db.cursor()
        cur.execute(query, values)

        return cur.fetchall()
    
    def fetch_one_query(self, query, values, get_dict=False):

        if get_dict:
            cur = self._db.cursor(pymysql.cursors.DictCursor)
        else:
            cur = self._db.cursor()
        cur.execute(query, values)

        return cur.fetchone()

    def get_player_by_steam_id(self, steam_id):

        return self.fetch_one_query(
            "SELECT * FROM server_user WHERE steam_id = %s", 
            (steam_id,)
            )

    def add_player(self, steam_id):
        
        character_json = '{}'
        loadout_json = '{}'

        with open('/var/www/mgsv_server/wsgi-scripts/mgsv_emulator/server/command/default_character.json', 'r') as file:
            character_json = file.read()

        with open('/var/www/mgsv_server/wsgi-scripts/mgsv_emulator/server/command/default_loadout.json', 'r') as file:
            loadout_json = file.read()
        
        self.execute_query(
            "INSERT INTO server_user (steam_id, character_json, loadout_json) VALUES (%s, %s, %s)", 
            (steam_id,character_json,loadout_json)
            )
        
        return self.get_player_by_steam_id(steam_id)

    def get_player_by_session_id(self, session_id):

        return self.fetch_one_query(
            "SELECT * FROM server_user WHERE session_id = %s", 
            (session_id,),
            True
            )

    def update_player_session_id(self, player_id, new_session_id):

        return self.execute_query(
            "UPDATE server_user SET session_id = %s WHERE steam_id = %s",
            (new_session_id, player_id)
            )

    def update_player_crypto_key(self, player_id, new_crypto_key):

        return self.execute_query(
            "UPDATE server_user SET crypto_key = %s WHERE steam_id = %s",
            (new_crypto_key, player_id)
            )
    
    def get_player_character_json(self, player_id):

        return self.fetch_one_query(
            "SELECT character_json FROM server_user WHERE id = %s",
            (player_id),
            True
            )
    
    def update_player_character_json(self, player_id, json_data):

        json_string = json.dumps(json_data)
        return self.execute_query(
            "UPDATE server_user SET character_json = %s WHERE id = %s",
            (json_string, player_id)
            )
    
    def delete_player_character(self, player_id, character_index):
        
        character = json.loads(self.get_player_character_json(player_id)['character_json'])
        del character['character_list'][character_index]

        return self.update_player_character_json(player_id, character)
    
    def get_player_loadout_json(self, player_id):

        return self.fetch_one_query(
            "SELECT loadout_json FROM server_user WHERE id = %s",
            (player_id),
            True
            )
    
    def update_player_loadout_json(self, player_id, json_data):
        
        json_string = json.dumps(json_data)

        result = self.execute_query(
            "UPDATE server_user SET loadout_json = %s WHERE id = %s",
            (json_string, player_id)
            )

        #logger.debug('update_player_loadout_json: {} {}'.format(player_id, result))

        return result

    def get_player_match_info(self, player_id):

        return self.fetch_query(
            "SELECT * FROM match_info WHERE player_id = %s", 
            (player_id,),
            True
            )
    
    def get_player_preset_radio_rule_list(self, player_id):

        return self.fetch_query(
            "SELECT * FROM preset_radio_rule_list WHERE player_id = %s", 
            (player_id,),
            True
            )
    
    def get_player_characters(self, player_id):

        return self.fetch_query(
            "SELECT * FROM character_attributes WHERE player_id = %s", 
            (player_id,),
            True
            )
    
    def create_avatar_upsert_sql(self, avatar_data, avatar_index, character_id):

        insert_fields = []
        insert_values = []
        update_fields = []

        for key, value in avatar_data.items():
            insert_fields.append(key)
            insert_values.append(value)
            update_fields.append(f"{key} = VALUES({key})")

        upsert_sql = """
        INSERT INTO avatar ({}, avatar_index, character_id) 
        VALUES ({}, %s, %s)
        ON DUPLICATE KEY UPDATE {}
        """.format(
            ', '.join(insert_fields),
            ', '.join(['%s'] * len(insert_values)),
            ', '.join(update_fields)
        )

        insert_values.extend([avatar_index, character_id])

        return upsert_sql, insert_values

    def update_player_character(self, player_id, character, character_index):
        
        self.execute_query(
            """
                INSERT INTO character (user_id, custom_name, player_class, player_type, last_loadout) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE custom_name=%s, player_class=%s, player_type=%s, last_loadout=%s
            """,
            (
                player_id, character['name'], character['player_class'], character['player_type'], character['last_loadout'],
                character['name'], character['player_class'], character['player_type'], character['last_loadout']
            )
        )
        
        character_id = self._db.cursor().lastrowid
        avatar = character['avatar']

        avatar_upsert_sql, avatar_values = self.create_avatar_upsert_sql(avatar, character_index, character_id)
        self.execute_query(avatar_upsert_sql, avatar_values)
    
    def get_player_character_loadouts(self, character_id):

        results = self.fetch_query(
            "SELECT * FROM loadout WHERE character_id = %s ORDER BY loadout_id", 
            (character_id,)
            )
        
        loadouts = []

        for result in results:

            loadout = {
                'loadout_id': result['loadout_id'],
                'name': result['custom_name'],
                'character_id': result['character_id'],
                'gears': [],
                'items': [],
                'skills': [],
                'weapons': [],
                'support_weapons': []
            }

            loadout['gear_list'] = self.fetch_query("SELECT * FROM gear WHERE loadout_id = %s", (result[0],), True)
            loadout['item_list'] = self.fetch_query("SELECT * FROM item WHERE loadout_id = %s", (result[0],), True)
            loadout['skill_list'] = self.fetch_query("SELECT * FROM skill WHERE loadout_id = %s", (result[0],), True)
            loadout['weapon_list'] = self.fetch_query("SELECT * FROM weapon WHERE loadout_id = %s", (result[0],), True)
            loadout['support_weapon_list'] = self.fetch_query("SELECT * FROM support_weapon WHERE loadout_id = %s", (result[0],), True)

            loadouts.append(loadout)
        
        return loadouts
    
    def update_player_character_loadout(self, character_id, character_index, loadout, loadout_index):
        
        # Insert or update loadout
        self.execute_query(
            """
                INSERT INTO loadout (character_id, custom_name, version) 
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE custom_name=%s, version=%s
            """,
            (character_id, loadout['name'], loadout['version'], loadout['name'], loadout['version'])
            )
        
        loadout_id = self._db.cursor().lastrowid

        # Handle gear_list
        for gear in loadout['gear_list']:
            self.execute_query(
                """
                    INSERT INTO gear (loadout_id, id, model, color_list) 
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE model=%s, color_list=%s
                """,
                (loadout_id, gear['id'], gear['model'], str(gear['color_list']), gear['model'], str(gear['color_list']))
                )
        
        # Similarly, handle item_list, skill_list, support_weapon_list, weapon_list, etc.
        # ...

