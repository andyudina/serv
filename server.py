from settings import ServerSettings, VkSettings, MLSettings
from DataPreprocessor.binary import BinaryParser
from ML.recoginition_service import RecognitionService
from PhraseGenerator.simple_phrase_generator import generate_phrase
from VKApi.api_wrapper import VKApi
import SocketServer
import time

#TODO: should be a queue. store last timestamp. If new class timestamp is less than stored timestamp, message shouldn't be sent
recognition_service = RecognitionService(MLSettings.pkl_file_name, ServerSettings.verbose)
vk_api = VKApi(VkSettings.access_token, VkSettings.base_url, VkSettings.user_id, ServerSettings.verbose)
parser = BinaryParser(ServerSettings.verbose)

class TCPHandler(SocketServer.BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        self.recognition_service = recognition_service
        self.vk_api = vk_api
        self.parser = parser
        SocketServer.BaseRequestHandler.__init__(self, *args, **kwargs)

    def handle(self):
        
        print '\n\ngot connection'
        try:
            self.data = bytearray(b" " * ServerSettings.data_length)
            self.request.recv_into(self.data)
            serv_timestamp = int(time.time())
            preprocessed_data = self.parser.parse_input_string(serv_timestamp, self.data)
            timestamp, current_movement_class = self.recognition_service.get_movement_class(preprocessed_data)
            phrase_to_send = generate_phrase(current_movement_class)
            self.vk_api.send_message(phrase_to_send)
        except Exception as e:
            print e
        print 'close connection\n\n'

if __name__ == "__main__":
    server = SocketServer.TCPServer((ServerSettings.host, ServerSettings.port), 
                                    TCPHandler)
    server.serve_forever()