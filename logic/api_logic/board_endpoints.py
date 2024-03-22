import requests
from utility.json_files_reader import read_from_secret_file, read_config


class BoardEndPoints:
    def __init__(self, my_api):
        self.my_api = my_api
        secrets_config = read_from_secret_file()
        self.token = secrets_config['trello_token']
        self.api_key = secrets_config['api_token']
        # Constants for Trello API
        config = read_config()
        base_url = config['api_url']
        self.endpoints = f'{base_url}/boards/'

    def create_new_board(self):
        # Parameters for creating a new boardd
        board_name = 'hello'
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': board_name
        }
        # Make a POST request to create a new board
        response = self.my_api.api_post_request(self.endpoints, params)
        return response
