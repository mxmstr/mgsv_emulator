#!/usr/bin/python3.11
import sys
import os
sys.path.append(os.path.dirname(__file__))
# how is this import possible, database is 2 levels higher
from database import Database
from datetime import datetime
import time
import copy
from .client_proxy import ClientProxy
from .server_commands import server_commands
from .logger import Logger



class ServerHandler(object):
	"""class that processes requests and composes answers
	however, last changes to command are made by encoder:
	original size is calculated after session encoding"""
	def __init__(self, player=None):
		self._handlers = {
			"CMD_GENERIC_ERROR": self.cmd_generic_error,
			"CMD_AUTH_STEAMTICKET": self.cmd_auth_ticket,
			"CMD_REQAUTH_HTTPS": self.cmd_reqauth,
			"CMD_GET_URLLIST": self.cmd_get_urllist,
			"CMD_GET_SVRLIST": self.cmd_get_srvlist,
			"CMD_GET_SVRTIME": self.cmd_get_srvtime,
			"CMD_SEND_IPANDPORT": self.cmd_send_ipandport,
			"CMD_GET_PLAYERLIST": self.cmd_get_playerlist,
			"CMD_SET_CURRENTPLAYER": self.cmd_set_currentplayer,
			"CMD_GET_ABOLITION_COUNT": self.cmd_get_abolition_count,
			"CMD_GET_CHALLENGE_TASK_REWARDS": self.cmd_get_challenge_task_rewards,
			"CMD_GET_LOGIN_PARAM": self.cmd_get_login_param,
			"CMD_GET_COMBAT_DEPLOY_RESULT": self.cmd_get_combat_deploy_result,
			"CMD_GET_SERVER_ITEM_LIST": self.cmd_get_server_item_list,
			"CMD_SYNC_RESOURCE": self.cmd_sync_resource,
			"CMD_SYNC_SOLDIER_BIN": self.cmd_sync_soldier_bin,
			"CMD_SEND_BOOT": self.cmd_send_boot,
			"CMD_GET_INFORMATIONLIST": self.cmd_get_informationlist,
			"CMD_SYNC_MOTHER_BASE": self.cmd_sync_mother_base,
			"CMD_GET_FOB_STATUS": self.cmd_get_fob_status,
			"CMD_GET_ONLINE_PRISON_LIST": self.cmd_get_online_prison_list,
			"CMD_GET_OWN_FOB_LIST": self.cmd_get_own_fob_list,
			"CMD_MINING_RESOURCE": self.cmd_mining_resource,
			"CMD_UPDATE_SESSION": self.cmd_update_session,
			"CMD_GET_CHALLENGE_TASK_TARGET_VALUES": self.cmd_get_challenge_task_target_values,
			"CMD_GET_FOB_NOTICE": self.cmd_get_fob_notice,
			"CMD_SEND_MISSION_RESULT": self.cmd_send_mission_result,
			"CMD_GET_DAILY_REWARD": self.cmd_get_daily_reward,
			"CMD_GET_FOB_REWARD_LIST": self.cmd_get_fob_reward_list,
			"CMD_GET_PLAYER_PLATFORM_LIST": self.cmd_get_player_platform_list,
			"CMD_SYNC_LOADOUT": self.cmd_sync_loadout,
			"CMD_ABORT_MOTHER_BASE": self.cmd_abort_mother_base,
			"CMD_GET_RESOURCE_PARAM": self.cmd_get_resource_param,
			"CMD_GET_SERVER_ITEM": self.cmd_get_server_item,
			"CMD_SALE_RESOURCE": self.cmd_sale_resource,
			"CMD_GET_WORMHOLE_LIST": self.cmd_get_wormhole_list,
			"CMD_GET_FOB_TARGET_LIST": self.cmd_get_fob_target_list,
			"CMD_GET_FOB_TARGET_DETAIL": self.cmd_get_fob_target_detail,
			"CMD_SNEAK_MOTHER_BASE": self.cmd_sneak_mother_base
		}
		self._db = Database()
		self._db.connect()
		self._logger = Logger()
		self._player = player

	def _command_get(self, name):
		return server_commands[name]

	def process_message(self, client_request, client_ip, httpMsg=None):
		# TODO: move deepcopy part here and send it to the handler function
		msgid = client_request['data']['msgid']
		self._logger.log_event(_text=msgid)
		command = None
		if msgid == 'CMD_AUTH_STEAMTICKET':
			# authenticating user, need to save ip
			# httpMsg is encoded version of CMD_AUTH_STEAMTICKET
			command = self._handlers[msgid](httpMsg, client_ip)
		else:
			# every other command, process as usual
			if client_request['session_key']:
				player = self._db.player_find_by_session_id(client_request['session_key'], get_dict=True)
				if isinstance(player, dict):
					try:
						command = self._handlers[msgid](client_request)
					except KeyError:
						self._logger.log_event('--msgid not found: {}'.format(msgid))
						self._logger.log_error("missing MSGID {}:\n{}".format(msgid, client_request))
						command = self._handlers['CMD_GENERIC_ERROR']()
						command['data']['msgid'] = msgid
					except:
						raise
					else:
						pass
						#command(client_request)
				else:
					# not a dict, list of dicts or None
					command = self.get_error()
			else:
				command = self._handlers[msgid](client_request)

		if isinstance(command, dict):
			if 'session_key' in command:
				if command['session_key'] == -1 and client_request['session_key']:
					command['session_key'] = client_request['session_key']
		return command

	def _session_exists(self, session_id):
		if session_id:
			self._db.user_find_by_session_id(session_id)
		else:
			pass

	def _populate_player_default_values(self, player_id, steam_id):
		sql = 'insert into player_vars(player_id, espionage_lose, espionage_win, \
			fob_grade, fob_point, fob_rank, is_insurance, league_grade,  \
			league_rank, name, playtime, point) values \
			(%s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
		values = (player_id, 0, 0, 11, 12345, 1, 1, 1, 1, '{}_player01'.format(str(steam_id)), 0, 0)
		self._db.execute_query(sql,values)

#	def _append_session_key(self, command):
#		# session key is required for command
#		# db.get_session_key
#		# do I really need that function?
#		if self.__session_key__:
#			command['session_key'] = 'fgsfds'
#		else:
#			raise Exception('Session key is required for this command, but no key provided')

	def get_error(self):
		# TODO: find all ERR_ codes and use them
		return 1

	def _generate_crypto_key(self):
		# return 'AAAAAAAAAAAAAAAAAAAAAA'
		return 'AQIDBAX///8BAgMEBf///w==' # 0102030405FFFFFF0102030405FFFFFF

	def _generate_session_id(self):
		# TODO salt
		from hashlib import md5
		t = datetime.timestamp(datetime.now())
		return md5(str(t).encode()).hexdigest()

	def cmd_generic_error(self):
		# TODO what
		command = copy.deepcopy(self._command_get('CMD_GET_SVRTIME'))
		return command


#======CMD_GET_URLLIST, working
	def cmd_get_urllist(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_SVRLIST, working
	def cmd_get_srvlist(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_SVRTIME, working
	def cmd_get_srvtime(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		command['data']['date'] = int(time.time())
		return command

#======CMD_AUTH_STEAMTICKET, working only with proxy, probably need a workaround if servers are down
	def cmd_auth_ticket(self, client_request, client_ip):
		# initial auth, just send ticket to konami to get steam_id back
		from .client_proxy import ClientProxy
		proxy = ClientProxy()
		proxied_response = proxy.send_full_command(client_request, 'CMD_AUTH_STEAMTICKET')
		if proxied_response:
			# auth_steamticket is not encoded with session key
			# decode data from konami and use in our db
			from .decoder import Decoder
			decoder = Decoder()
			decoded_kon_resp = decoder.decode(proxied_response)

			self._logger.log_event('Konami response: {}'.format(decoded_kon_resp))

			data = decoded_kon_resp['data']
			player = self._db.player_find_by_steam_id(data['account_id'])
			if player:
				self._logger.log_event('found player {}'.format(data['account_id']))
			else:
				self._logger.log_event('adding new player {}'.format(data['account_id']))
				self._db.player_add(data, client_ip)
				player_id = self._db.player_find_by_steam_id(data['account_id'])[0][0]
				self._populate_player_default_values(player_id, data['account_id'])

		else:
			self._logger.log_event('Konami returned none')
		return decoded_kon_resp

#======CMD_REQAUTH_HTTPS, working
	def cmd_reqauth(self, client_request):
		data = client_request['data']
		self._logger.log_event('Looking for steam_id {}'.format(data['user_name']))
		player = self._db.player_find_by_steam_id(data['user_name'])
		if len(player) != 1:
			self._logger.log_event('Looking for steam_id {}, {} found! This is not supposed to happen!'.format(data['user_name'], len(player)))
			command = None
		else:
			# generate session id and crypto_key
			session_id = self._generate_session_id()
			crypto_key = self._generate_crypto_key()

			sql = 'update players set magic_hash=%s, \
						  session_id=%s, \
						  crypto_key=%s where id = %s'
			values = (data['hash'], session_id, crypto_key, player[0][0])
			self._db.execute_query(sql, values)

			command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
			command['data']['session'] = session_id
			command['data']['crypto_key'] = crypto_key
			command['data']['user_id'] = player[0][0]
			command['data']['smart_device_id'] = player[0][4]
		return command

#======CMD_SEND_IPANDPORT, working, maybe we should save client's ip for pvp
	def cmd_send_ipandport(self, client_request):
		data = client_request['data']
		sql = 'update players set ex_ip=%s,\
					  ex_port=%s,\
					  in_ip=%s,\
					  in_port=%s,\
					  nat=%s,\
					  xnaddr=%s where session_id = %s'
		values = (data['ex_ip'], data['ex_port'], data['in_ip'], data['in_port'],
				data['nat'], data['xnaddr'], client_request['session_key'])
		self._db.execute_query(sql, values)

		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_PLAYERLIST, working, what is that 'index' for?
	def cmd_get_playerlist(self, client_request):
		sql = 'select espionage_lose, espionage_win, fob_grade, fob_point,\
			fob_rank, is_insurance, league_grade, league_rank, \
			name, playtime, point from player_vars JOIN players on player_vars.player_id = players.id \
			WHERE session_id = %s'
		values = (client_request['session_key'],)
		data = self._db.fetch_query(sql, values)[0]
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		d = command['data']['player_list'][0]
		d['espionage_lose'] = data[0]
		d['espionage_win'] = data[1]
		d['fob_grade'] = data[2]
		d['fob_point'] = data[3]
		d['fob_rank'] = data[4]
		d['index'] = 0
		d['is_insurance'] = data[5]
		d['league_grade'] = data[6]
		d['league_rank'] = data[7]
		d['name'] = data[8]
		d['playtime'] = data[9]
		d['point'] = data[10]
		command['data']['player_num'] =  1
		return command

#======CMD_SET_CURRENTPLAYER, working, what is that 'player_id'?
	def cmd_set_currentplayer(self, client_request):
		sql = 'select id from players WHERE session_id = %s'
		values = (client_request['session_key'],)
		data = self._db.fetch_query(sql, values)[0]
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		command['data']['player_id'] = data[0]
		return command

#======CMD_GET_ABOLITION_COUNT, working, what is that 'status'?
	def cmd_get_abolition_count(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		d = command['data']
		d['date'] = int(time.time())
		d['count'] = 1
		d['max'] = 999999
		d['num'] = 0
		d['status'] = 0
		return command

#======CMD_GET_CHALLENGE_TASK_REWARDS, working
	def cmd_get_challenge_task_rewards(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import task_list
		d = command['data']
		d['task_list'] = task_list.task_list
		d['task_count'] = len(task_list.task_list)
		return command

#======CMD_GET_LOGIN_PARAM, working, need a nice function that will compose login params
# login params include:
# -cost of fob platforms
# -your fob event ponts
# -threshold for hero _and not hero_ status (150000 and 100000, what does it mean)
# -list of fob event tasks
# -can you buy fob4 (why exactly 4?)
# -online challenge tasks - ones for singleplayer missions
# -is_stuck_rescue - ?
# -weapon development requrements that overwrite local values
# -names and descriptions for all fob events
# -amount of esp point bonuses (not quite sure) for using staff members
	def cmd_get_login_param(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import login_params
		d = command['data']
		for key in login_params.login_params:
			d[key] = login_params.login_params[key]
		return command

#======CMD_GET_COMBAT_DEPLOY_RESULT, working using dummy data
	def cmd_get_combat_deploy_result(self, client_request):
		# TODO: need to get an example of successful combat deployment
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_SERVER_ITEM_LIST, working with dummy data
	def cmd_get_server_item_list(self, client_request):
		# this is a list of items that client can develop or developed already
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import server_items
		command['data']['item_list'] = copy.deepcopy(server_items.item_list)
		command['data']['item_num'] = len(command['data']['item_list'])
		return command

#======CMD_SYNC_RESOURCE, working using dummy data
	def cmd_sync_resource(self, client_request):
		# TODO: figure out parameters sent by client and what should we send back
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_SYNC_SOLDIER_BIN, working, maybe we should save that data in db?
	def cmd_sync_soldier_bin(self, client_request):
		# essentially, this command does nothing for client
		# if server sends data that differs from client data, client will lose soldiers that were modified
		# so all you need is to count soldiers, strip some data and send it back
		# TODO: decode soldier params from binary (cheatengine guys did it)
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		import base64
		b = base64.decodestring(client_request['data']['soldier_param'].encode())
		soldier_count = 0
		soldiers = [b[i:i+24] for i in range(0, len(b), 24)]
		import binascii
		for n,solly in enumerate(soldiers):
			soldiers[n] = solly[8:]
			#solly[0:8]:
			#------------------------
			#    0: always 0
			#    1: direct contract
			#    2: always 0
			#    3: values from 0 to 9, numbers look like amount of staff per platform (but there are only 7 platforms, brig+medi?)
			#    4: always 0
			#    5: values 0, 3-9, probably something about stats, I have a lot of 9 (~2700) - base stats?
			#    6: always 0
			#    7: values 0, 3-9, numbers look like 5th byte, but slightly different - base stats+buffs?
			#------------------------
			#
			# python > 3.5
			#if solly.hex() != '0'*32:
			#	soldier_count +=1
			if binascii.hexlify(soldiers[n]) != b'0'*32:
				soldier_count +=1
				#TEST
				#self._logger.log_event(binascii.hexlify(soldiers[n]))
				#END TEST
			soldiers_out = b''.join(soldiers)
		command['data']['soldier_param'] = base64.encodestring(soldiers_out).decode().replace('\n','')
		command['data']['soldier_num'] = soldier_count
		command['data']['version'] = client_request['data']['version'] + 1
		# #self._logger.log_event(command)


	#	import json
	#	from .client_proxy import ClientProxy
	#	proxy = ClientProxy()

	#	if client_request['data']['soldier_num'] > 0:
	#		f = open('/tmp/sol_request','w')
	#		f.write(json.dumps(client_request))
	#		f.close()
	#		self._logger.log_event('DUMPONG CLIENT REQ!!')

	#	command = proxy.send_full_command_with_auth(client_request, 'CMD_SYNC_SOLDIER_BIN')
	#	#if proxied_response:
	#	d = open('/tmp/sol_response','w')
	#	d.write(json.dumps(command))
	#	d.close()
	#	self._logger.log_event('DUMPONG KONAMI RESP!!')
	#	command['session_key'] = -1
		return command

#======CMD_SEND_BOOT, working
	def cmd_send_boot(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_INFORMATIONLIST, working using dummy data
	def cmd_get_informationlist(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import infolist
		command['data']['info_list'] = copy.deepcopy(infolist.info_list)
		command['data']['info_num'] = len(command['data']['info_list'])
		return command

#======CMD_SYNC_MOTHER_BASE, working
	def cmd_sync_mother_base(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		player = self._db.player_find_by_session_id(client_request['session_key'], get_dict=True)
		#select mother_base_data->'$.data.mother_base_param[0].cluster_param[0].unique_security.caution_area' from player_vars;
		data = client_request['data']
		sql = 'insert into player_vars(player_id, mother_base_data) values(1, %s)'
		values = (
			json.dumps(j),
			player['id']
		)
		self.execute_query(sql,values)
		self._db.execute_query(sql, values)
		return command

#======CMD_GET_FOB_STATUS, working with dummy data
	def cmd_get_fob_status(self, client_request):
		# TODO: db integration
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_ONLINE_PRISON_LIST, working with dummy data
	def cmd_get_online_prison_list(self, client_request):
		# TODO: get a successful response from server
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_OWN_FOB_LIST, working with dummy data
	def cmd_get_own_fob_list(self, client_request):
		# TODO: db integration 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_MINING_RESOURCE, working with dummy data
	def cmd_mining_resource(self, client_request):
		# TODO: db integration 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_UPDATE_SESSION, working
	def cmd_update_session(self, client_request):
		# TODO: seems ok, check different status flags 
		# flags:
		# -fob_index - always -1 in my netdumps
		# -sneak_mode - always -1 in my netdumps
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_CHALLENGE_TASK_TARGET_VALUES, working with dummy data
	def cmd_get_challenge_task_target_values(self, client_request):
		# TODO: db integration
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_FOB_NOTICE, working with dummy data
	def cmd_get_fob_notice(self, client_request):
		# TODO: tight db integration 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_SEND_MISSION_RESULT, working
	def cmd_send_mission_result(self, client_request):
		# TODO: do we really need to save that data? 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_DAILY_REWARD, working
	def cmd_get_daily_reward(self, client_request):
		# TODO: figure out personell
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		random_reward = self._generate_random_daily_reward()
		command['data']['count'] = random_reward['amount']
		command['data']['reward_type'] = random_reward['id']
		# if random_reward['is_online']:
		#	TODO: update  mysql values
		return command

	def _generate_random_daily_reward(self):
		cars = {'range_low':1,
			'range_high':10,
			'online_ids':[27,29],
			'offline_ids':[59,61]
			}
		flowers = {
			'range_low':50,
			'range_high':2000,
			'online_ids':[17,18,19,20,21,22,23,24],
			'offline_ids':[49,50,51,52,53,54,55,56]
			}
		resources = {
			'range_low':1000,
			'range_high':10000,
			'online_ids':[12,13,14,15,16],
			'offline_ids':[44,45,46,47,48]
			}
		soldiers = {
			'range_low':5,
			'range_high':20,
			'online_ids':[2,3,4,5,6,7,8,9,10,11],
			'offline_ids':[34,35,36,37,38,39,40,41,42,43]
			}
		gmp = {
			'range_low':10000,
			'range_high':1000000,
			'online_ids':[1],
			'offline_ids':[33]
			}
		# mb coins id: 26/58
		# esp score id: 30/62
		# liquid carb missilies id: 31/63 
		# volga id: 28/60 

		rewards = [cars, flowers, resources, soldiers, gmp]
		import random
		reward_type = random.choice(rewards)
		reward_is_online = bool(random.getrandbits(1))
		if reward_is_online:
			online_key = 'online_ids'
		else:
			online_key = 'offline_ids'
		reward_id = random.choice(reward_type[online_key])
		reward_amount = random.choice(range(reward_type['range_low'], reward_type['range_high']+1))
		return {'id':reward_id, 'amount':reward_amount, 'is_online':reward_is_online}


#======CMD_GET_FOB_REWARD_LIST, working with dummy data
	def cmd_get_fob_reward_list(self, client_request):
		# TODO: figure out fob reward format
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		command['data']['version'] = client_request['data']['version'] + 1
		return command

#======CMD_GET_PLAYER_PLATFORM_LIST, untested
	def cmd_get_player_platform_list(self, client_request):
		sql = 'select mother_base_num from player_vars where player_id=%s'
		values = (str(self._player['id']),)
		mb_num = self._db.fetch_query(sql, values)[0][0]
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		info_dict = copy.deepcopy(command['data']['info_list'][0])
		command['data']['info_list'] = []
		for i in range(0, mb_num*8):
			command['data']['info_list'].append(info_dict)
		command['data']['info_num'] = len(command['data']['info_list'])
		return command

#======CMD_SYNC_LOADOUT, untested
	def cmd_sync_loadout(self, client_request):
		# do we need to save loadout for some reason or is it just for checks? 
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_ABORT_MOTHER_BASE, works
	def cmd_abort_mother_base(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_RESOURCE_PARAM, working with dummy data
	def cmd_get_resource_param(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_SERVER_ITEM, works with dummy data 
	def cmd_get_server_item(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		command['data']['item']['id'] = client_request['data']['item_id']
		return command

#======CMD_SALE_RESOURCE, works with dummy data, needs mysql pulls
	def cmd_sale_resource(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		command['data']['resouce_id'] = client_request['data']['resouce_id']
		current_online_gmp = 1000000
		current_resource_amount = 1000000
		command['data']['result_gmp'] = current_online_gmp + client_request['data']['num'] * client_request['data']['unit_price']
		command['data']['result_num'] = current_resource_amount - client_request['data']['num']
		return command

#======CMD_GET_WORMHOLE_LIST, works 
	def cmd_get_wormhole_list(self, client_request):
		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command

#======CMD_GET_FOB_TARGET_LIST, somewhat works, maybe add a fob generator?
	def cmd_get_fob_target_list(self, client_request):
		#types:
		#PICKUP - inf targets same grade
		#PICKUP_HIGH - inf targets high grade
		#ENEMY - retaliation targets
		#FR_ENEMY - indirect retaliation
		#TRIAL - training
		#EVENT - fob event
		#INJURY - intruders
		#CHALLENGE - security challenge
		#DEPLOYED - fob unit deployed
#		proxy = ClientProxy()
#		command = proxy.send_full_command_with_auth(client_request, 'CMD_GET_FOB_TARGET_LIST')
#		f = open('/var/www/mgsv_server/wsgi-scripts/fobstuff','a')
#		f.write(str(command) + '\n')
#		f.close()

		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import get_fob_target_list
		command['data']['type'] = client_request['data']['type']

#		t =	{
#			'area_id': 0,
#			'cluster_param': [],
#			'construct_param': 59072651,
#			#130394987,   # includes fob position on the globe, format unknown
#			'fob_index': 0,			# doesn't seem to affect anything
#			'mother_base_id': 1,
#			'platform_count': 28,
#			'price': 0,			# doesn't appear on ui anywhere
#			'security_rank': 57
#		}
#		q = open('/tmp/i','r')
#		i = int(q.read())
#		i = 5
#		magicstring = '0x03' + hex(i)[2:] + '0028'
#		t['construct_param'] = int(magicstring,0)
		a = copy.deepcopy(get_fob_target_list.enemy)
#		a['mother_base_param'] = []
#		a['mother_base_param'].append(t)
#		a['owner_fob_record']['staff_count'] = [i,0,0,0,0,0,0,0,0,0]
#		a['owner_detail_record']['staff_count'] = i
		command['data']['target_list'].append(a)
#		t['construct_param'] = 59047976 
#		self._logger.log_event('adding ' + str(t['construct_param']) + ": " + str(i) + " " + magicstring )
#		q.close()
#		q = open('/tmp/i','w')
#		q.write(str(i+1))
#		q.close()

		command['data']['target_num'] = len(command['data']['target_list'])
		return command

#======CMD_GET_FOB_TARGET_DETAIL
	def cmd_get_fob_target_detail(self, client_request):
#		proxy = ClientProxy()
#		command = proxy.send_full_command_with_auth(client_request,'CMD_GET_FOB_TARGET_DETAIL')
#		f = open('/var/www/mgsv_server/wsgi-scripts/fobstuff','a')
#		f.write(str(command) + '\n')
#		f.close()

		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		from .vars import fob_details
		command['data']['detail'] = fob_details.details
		return command

#======CMD_SNEAK_MOTHER_BASE
	def cmd_sneak_mother_base(self, client_request):
#		proxy = ClientProxy()
#		command = proxy.send_full_command_with_auth(client_request,'CMD_GET_FOB_TARGET_DETAIL')
#		f = open('/var/www/mgsv_server/wsgi-scripts/fobstuff','a')
#		f.write(str(command) + '\n')
#		f.close()

		command = copy.deepcopy(self._command_get(str(client_request['data']['msgid'])))
		return command
