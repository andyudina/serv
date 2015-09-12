import sqlite3
import time
from PhraseGenerator.simple_phrase_generator import generate_phrase
from VKApi.api_wrapper import VKApi
from settings import DatabaseSettings, VkSettings, ServerSettings

class VkSender(object):
    def __init__(self, database, table, vk_api):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.table = table
        self.last_timestamp = self._get_last_timestamp()
        self.vk_api = vk_api

    def _get_last_timestamp(self):
        return self.cursor.execute('''SELECT MAX(timestamp) 
                                     FROM {}'''.format(self.table)).fetchone()[0] 
       
    def _send_last_class_to_vk(self):
        print self.last_timestamp
        last_class = self.cursor.execute(u'''SELECT class 
                                            FROM {}
                                            WHERE timestamp={}
                                            ORDER BY id DESC
                                            LIMIT 1'''.format(self.table, self.last_timestamp)).format(self.table)).fetchone()[0] 
        phrase_to_send = generate_phrase(last_class)
        self.vk_api.send_message(phrase_to_send)


    def send_forever(self):
        while(True):
            real_last_timestamp = self._get_last_timestamp()
            if real_last_timestamp > self.last_timestamp :
                self.last_timestamp = real_last_timestamp       
                self._send_last_class_to_vk()
            time.sleep(10)

if __name__ == "__main__":
    vk_sender = VkSender(DatabaseSettings.database, DatabaseSettings.table,
                         VKApi(VkSettings.access_token, VkSettings.base_url, VkSettings.user_id, ServerSettings.verbose))
    vk_sender.send_forever()

       
