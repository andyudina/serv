import urllib
import requests


class VKApi(object):
    def __init__(self, access_token, base_url, user_id, verbose=True):
        self.token = access_token
        self.base_url = base_url
        self.user_id = user_id
        self.verbose = verbose

    def send_message(self, message):
        if self.verbose:
            print u'\nvk api: stared'
        message = urllib.quote(message.encode('utf-8'))
        if self.verbose:
            print u'sending message: {}'.format(message.encode('utf-8'))
        send_message_url = self._generate_vk_url('messages.send', {'access_token': self.token, 
                                                                  'user_id' : self.user_id, 
                                                                  'message' : message})
        
        if self.verbose:
            print u'with url: {}'.format(send_message_url)

        r = requests.get(send_message_url)
        if self.verbose:
            print r.status_code
            print r.text
        if self.verbose:
            print u'vk api: stopped\n'       

 
    def _generate_vk_url(self, method, params_dict):
        params = '&'.join(['='.join([key, val]) for key, val in params_dict.iteritems()])
        return self.base_url.format(METHOD_NAME=method, 
                                    PARAMETERS=params)
        
