import sqlite3
from PhraseGenerator.simple_phrase_generator import generate_phrase
from VKApi.api_wrapper import VKApi
from serv_dev.settings import DatabaseSettings

vk_api = VKApi(VkSettings.access_token, VkSettings.base_url, VkSettings.user_id, ServerSettings.verbose)

class VkSender(object):
    def __init__(self, database, table):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.table = table
        self.last_timestamp = self._get_last_timestamp()
        self.vk_api = vk_api

    def _get_last_timestamp(self):
        return self.cursor.execute('''SELECT MAX(timestamp) 
                                     FROM {}'''.format(table)) 
       
    def _send_last_class_to_vk(self):
        last_class = self.cursor.execute('''SELECT class 
                                            FROM {}
                                            WHERE timestamp={}
                                            ORDER BY id DESC
                                            LIMIT 1'''.format(table, self.last_timestamp))
        phrase_to_send = generate_phrase(current_movement_class)
        self.vk_api.send_message(phrase_to_send)

    def send_forever(self):
        while(True):
            _send_last_class_to_vk()
            time.sleep(10)

if __name__ == "__main__":
    vk_sender = VkSender(DatabaseSettings.database, DatabaseSettings.table)
    vk_sener.send_forever()

       
