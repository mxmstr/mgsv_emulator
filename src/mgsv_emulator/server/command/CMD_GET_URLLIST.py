from mgsv_emulator.command.Command import Command
from mgsv_emulator.server.entity.Url import Url

class CMD_GET_URLLIST(Command):

    def __init__(self, receiver):
        super(CMD_GET_URLLIST, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = True

    def get_url_list(self):
        # url = Url()
        # all_urls = url.get_all_urls()
        # data = {
        #     'url_list':all_urls,
        #     'url_num': len(all_urls)
        # }
        data = {
            "crypto_type": "COMMON",   
            "flowid": None,
            "msgid": "CMD_GET_URLLIST",
            "result": "NOERR",
            "rqid": 0,
            "url_list": [
                {
                    "type": "GATE",
                    "url": "http://192.168.0.10/mgostm/gate",
                    "version": 0
                },
                {
                    "type": "WEB",
                    "url": "http://192.168.0.10/mgostm/main",
                    "version": 0
                },
                {
                    "type": "HEATMAP",
                    "url": "http://192.168.0.10/tppstmweb/heatmap",
                    "version": 0
                },
                {
                    "type": "DEVICE",
                    "url": "http://192.168.0.10/tppstm/main",
                    "version": 0
                },
                {
                    "type": "EULA",
                    "url": "http://192.168.0.10/tppstmweb/eula/eula.var",
                    "version": 0
                },
                {
                    "type": "EULA_COIN",
                    "url": "http://192.168.0.10/tppstmweb/coin/coin.var",
                    "version": 0
                },
                {
                    "type": "POLICY_GDPR",
                    "url": "http://192.168.0.10/tppstmweb/gdpr/privacy.var",
                    "version": 0
                },
                {
                    "type": "POLICY_JP",
                    "url": "http://192.168.0.10/tppstmweb/privacy_jp/privacy.var",
                    "version": 0
                },
                {
                    "type": "POLICY_ELSE",
                    "url": "http://192.168.0.10/tppstmweb/privacy/privacy.var",
                    "version": 0
                },
                {
                    "type": "LEGAL",
                    "url": "http://192.168.0.10/games/mgsvtpp/",
                    "version": 0
                },
                {
                    "type": "PERMISSION",
                    "url": "http://192.168.0.10/",
                    "version": 0
                },
                {
                    "type": "POLICY_CCPA",
                    "url": "http://192.168.0.10/tppstmweb/privacy_ccpa/privacy.var",
                    "version": 0
                },
                {
                    "type": "EULA_TEXT",
                    "url": "http://192.168.0.10/games/mgsvtpp/terms/",
                    "version": 0
                },
                {
                    "type": "EULA_COIN_TEXT",
                    "url": "http://192.168.0.10/games/mgsvtpp/terms/currency/",
                    "version": 0
                },
                {
                    "type": "POLICY_GDPR_TEXT",
                    "url": "http://192.168.0.10/games/mgsvtpp/",
                    "version": 0
                },
                {
                    "type": "POLICY_JP_TEXT",
                    "url": "http://192.168.0.10/games/privacy/view/",
                    "version": 0
                },
                {
                    "type": "POLICY_ELSE_TEXT",
                    "url": "http://192.168.0.10/games/privacy/view/",
                    "version": 0
                },
                {
                    "type": "POLICY_CCPA_TEXT",
                    "url": "http://192.168.0.10/games/mgsvtpp/ppa4ca/",
                    "version": 0
                }
            ],
            "url_num": 18,
            "xuid": None
        }
        return data

    def execute(self, data):
        data = self.get_url_list()
        return self._receiver.action(data, self.__class__.__name__)
    
"""
{'compress': False, 'data': {'lang': 'ANY', 'msgid': 'CMD_GET_URLLIST', 'region': 'REGION_ALL', 'rqid': 0}, 'original_size': 71, 'session_crypto': False, 'session_key': ''}
{
    "compress": true,
    "data": {
        "crypto_type": "COMMON",   
        "flowid": null,
        "msgid": "CMD_GET_URLLIST",
        "result": "NOERR",
        "rqid": 0,
        "url_list": [
            {
                "type": "GATE",
                "url": "https://mgstpp-game.konamionline.com/mgostm/gate",
                "version": 14
            },
            {
                "type": "WEB",
                "url": "https://mgstpp-game.konamionline.com/mgostm/main",
                "version": 14
            },
            {
                "type": "EULA",
                "url": "http://mgstpp-game.konamionline.com/tppstmweb/eula/eula.var",
                "version": 6
            },
            {
                "type": "EULA_COIN",
                "url": "http://mgstpp-game.konamionline.com/tppstmweb/coin/coin.var",
                "version": 1
            },
            {
                "type": "POLICY_GDPR",
                "url": "http://mgstpp-game.konamionline.com/tppstmweb/gdpr/privacy.var",
                "version": 1
            },
            {
                "type": "POLICY_JP",
                "url": "http://mgstpp-game.konamionline.com/tppstmweb/privacy_jp/privacy.var",
                "version": 2
            },
            {
                "type": "POLICY_ELSE",
                "url": "http://mgstpp-game.konamionline.com/tppstmweb/privacy/privacy.var",
                "version": 1
            },
            {
                "type": "LEGAL",
                "url": "https://legal.konami.com/games/mgsvtpp/",
                "version": 1
            },
            {
                "type": "PERMISSION",
                "url": "https://www.konami.com/",
                "version": 1
            },
            {
                "type": "POLICY_CCPA",
                "url": "http://mgstpp-game.konamionline.com/tppstmweb/privacy_ccpa/privacy.var",
                "version": 1
            },
            {
                "type": "EULA_TEXT",
                "url": "https://legal.konami.com/games/mgsvtpp/terms/",
                "version": 1
            },
            {
                "type": "EULA_COIN_TEXT",
                "url": "https://legal.konami.com/games/mgsvtpp/terms/currency/",
                "version": 1
            },
            {
                "type": "POLICY_GDPR_TEXT",
                "url": "https://legal.konami.com/games/mgsvtpp/",
                "version": 1
            },
            {
                "type": "POLICY_JP_TEXT",
                "url": "https://legal.konami.com/games/privacy/view/",
                "version": 2
            },
            {
                "type": "POLICY_ELSE_TEXT",
                "url": "https://legal.konami.com/games/privacy/view/",
                "version": 1
            },
            {
                "type": "POLICY_CCPA_TEXT",
                "url": "https://legal.konami.com/games/mgsvtpp/ppa4ca/",
                "version": 1
            }
        ],
        "url_num": 16,
        "xuid": null
    },
    "original_size": 1633,
    "session_crypto": false,
    "session_key": null
}




{
    "compress": true,
    "data": {
        "crypto_type": "COMMON",
        "flowid": null,
        "msgid": "CMD_GET_URLLIST",
        "result": "NOERR",
        "rqid": 0,
        "url_list": [
            {
                "type": "HEATMAP",
                "url": "http://192.168.0.10/tppstmweb/heatmap",//
                "version": 0
            },
            {
                "type": "DEVICE",
                "url": "http://192.168.0.10/tppstm/main",
                "version": 0
            },
            {
                "type": "GATE",
                "url": "http://192.168.0.10/mgostm/gate",
                "version": 14
            },
            {
                "type": "WEB",
                "url": "http://192.168.0.10/mgostm/main",
                "version": 14
            },
            {
                "type": "EULA",
                "url": "http://192.168.0.10/tppstmweb/eula/eula.var",
                "version": 6
            },
            {
                "type": "EULA_COIN",
                "url": "http://192.168.0.10/tppstmweb/coin/coin.var",
                "version": 1
            },
            {
                "type": "POLICY_GDPR",
                "url": "http://192.168.0.10/tppstmweb/gdpr/privacy.var",
                "version": 1
            },
            {
                "type": "POLICY_JP",
                "url": "http://192.168.0.10/tppstmweb/privacy_jp/privacy.var",
                "version": 2
            },
            {
                "type": "POLICY_ELSE",
                "url": "http://192.168.0.10/tppstmweb/privacy/privacy.var",
                "version": 1
            },
            {
                "type": "POLICY_CCPA",
                "url": "http://192.168.0.10/tppstmweb/privacy_ccpa/privacy.var",//
                "version": 1
            },
            {
                "type": "LEGAL",
                "url": "http://192.168.0.10/legal",
                "version": 1
            },
            {
                "type": "EULA_TEXT",
                "url": "http://192.168.0.10/legal/mgsvtpp/terms/",
                "version": 1
            },
            {
                "type": "EULA_COIN_TEXT",
                "url": "http://192.168.0.10/legal/mgsvtpp/terms/currency/",
                "version": 1
            },
            {
                "type": "POLICY_GDPR_TEXT",
                "url": "http://192.168.0.10/legal/mgsvtpp/",
                "version": 1
            },
            {
                "type": "POLICY_JP_TEXT",
                "url": "http://192.168.0.10/legal/privacy/view/",
                "version": 2
            },
            {
                "type": "POLICY_ELSE_TEXT",
                "url": "http://192.168.0.10/legal/privacy/view/",
                "version": 1
            },
            {
                "type": "POLICY_CCPA_TEXT",
                "url": "http://192.168.0.10/legal/mgsvtpp/ppa4ca/",
                "version": 1
            },
            {
                "type": "PERMISSION",
                "url": "http://192.168.0.10/permission",
                "version": 1
            }
        ],
        "url_num": 18,
        "xuid": 0
    },
    "original_size": 1610,
    "session_crypto": false,
    "session_key": null
}

"""
