

class ServerSettings:
    host = "192.168.0.12"
    port = 10101
    data_length = 1000
    verbose = True
    window_size = 28

class VkSettings:
    base_url = 'https://api.vk.com/method/{METHOD_NAME}?{PARAMETERS}'
    access_token = '0129cb923af5d58d5a273f5670cd03cd5c2c95d0127578352351b743862a5400d0c35804f646cb4972742'
    user_id = '188622142'
    

class MLSettings:
    pkl_file_name = '/home/i.zotov/serv/ML/rand_forest_model_4.pkl'

class DatabaseSettings:
    database = 'cat_movement_logs'
    table = 'logs'
