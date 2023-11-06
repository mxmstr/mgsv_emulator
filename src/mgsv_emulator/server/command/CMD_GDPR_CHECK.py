from mgsv_emulator.command.Command import Command

class CMD_GDPR_CHECK(Command):

    def __init__(self, receiver):
        super(CMD_GDPR_CHECK, self).__init__(receiver)
        self._receiver.encrypt = False
        self._receiver.compress = True

    def get_data(self):
        data = {
            'addendum_list': [
                {
                    'index': 4,
                    'message_list': [
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 0,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 1,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 2,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 0,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 3,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 4,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 5,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 6,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 7,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 8,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 9,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        },
                        {
                            'confirm': 'Confirm Privacy Policy',
                            'lang': 10,
                            'text': 'Addendum for California Residents',
                            'title': 'Privacy Policy'
                        }
                    ]
                }
            ],
            'ccpa_state_index': 20,
            'crypto_type': 'COMMON',
            'flowid': None,
            'gdpr_country_index': 65,
            'geo_ip_country': 'JP',
            'geo_ip_state': '',
            'msgid': 'CMD_GDPR_CHECK',
            'result': 'NOERR',
            'rqid': 0,
            'xuid': None
        }
        return data

    def execute(self, data):
        data = self.get_data()
        return self._receiver.action(data, self.__class__.__name__)

"""
{
    "compress": false,
    "data": {
        "authcode": "NotImplement",        
        "hash": "AAAAAAAAAAAAAAAAAAAAAA==",
        "issuer_id": 0,
        "lang": 0,
        "msgid": "CMD_GDPR_CHECK",
        "platform": "Steam",
        "rqid": 0,
        "steam_ticket": "aaaaaaaa",
        "steam_ticket_size": 234,
        "user_name": "NotImplement"
    },
    "original_size": 1642,
    "session_crypto": false,
    "session_key": ""
}

{'compress': False, 'data': {'authcode': 'NotImplement', 'hash': 'AAAAAAAAAAAAAAAAAAAAAA==', 'issuer_id': 0, 'lang': 0, 'msgid': 'CMD_GDPR_CHECK', 'platform': 'Steam', 'rqid': 0, 'steam_ticket': 'aaaaaaaa', 'steam_ticket_size': 234, 'user_name': 'NotImplement'}, 'original_size': 1642, 'session_crypto': False, 'session_key': ''}
{"compress": True, "data": {"addendum_list": [{"index": 4, "message_list": [{"confirm": "Confirm Privacy Policy & Addendum for California Residents.", "lang": 0, "text": "Addendum for California Residents", "title": "Privacy Policy & Addendum for California Residents"}, {"confirm": "Veuillez confirmer la Politique de confidentialité et addendum pour les résidents de Californie.", "lang": 1, "text": "Addendum pour les résidents de Californie", "title": "Politique de confidentialité et addendum pour les résidents de Californie"}, {"confirm": "Confirmar Política de Privacidad y Adenda para los Residentes de California.", "lang": 2, "text": "Adenda para los Residentes de California", "title": "Política de Privacidad y Adenda para los Residentes de California"}, {"confirm": "Confirmar Adendo de Política de Privacidade para Residentes da Califórnia.", "lang": 3, "text": "Adendo para Residentes da Califórnia", "title": "Adendo de Política de Privacidade para Residentes da Califórnia"}, {"confirm": "Conferma la Normativa sulla privacy e appendice per i residenti in California.", "lang": 4, "text": "Appendice per i residenti in California", "title": "Informativa sulla privacy e appendice per i residenti in California"}, {"confirm": "Datenschutzrichtlinie & Nachtrag für kalifornische Einwohner zustimmen.", "lang": 5, "text": "Nachtrag für kalifornische Einwohner", "title": "Datenschutzrichtlinie & Nachtrag für kalifornische Einwohner"}, {"confirm": "", "lang": 6, "text": "", "title": ""}, {"confirm": "Примите Политика конфиденциальности и дополнение для жителей Калифорнии.", "lang": 7, "text": "Дополнение для жителей Калифорнии", "title": "Политика конфиденциальности и дополнение для жителей Калифорнии"}, {"confirm": "Privacy Policy & Addendum for California Residents を確認します", "lang": 8, "text": "カリフォルニア州住民向け補足条項", "title": "Privacy Policy & Addendum for California Residents"}, {"confirm": "確認隱私政策及加州居民之附件", "lang": 9, "text": "加州居民之 
附件", "title": "隱私政策及加州居民之附件"}, {"confirm": "캘리포니아 거주자용 개인정보 보호정책 및 부록 확인합 
니다.", "lang": 10, "text": "캘리포니아 거주자에 대한 부록", "title": "캘리포니아 거주자용 개인정보 보호정책 및
 부록"}]}], "ccpa_state_index": 20, "crypto_type": "COMMON", "flowid": None, "gdpr_country_index": 65, "geo_ip_country": "JP", "geo_ip_state": "", "msgid": "CMD_GDPR_CHECK", "result": "NOERR", "rqid": 0, "xuid": None}, "original_size": 2576, "session_crypto": False, "session_key": None}
"""