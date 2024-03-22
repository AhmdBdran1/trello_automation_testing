import requests
from utility.json_files_reader import read_from_secret_file


class BoardEndPoints:
    config = read_from_secret_file()
    token = config['trello_token']
    api_key = config['api_token']
    # Constants for Trello API
    BASE_URL = 'https://api.trello.com/1'
    CREATE_BOARD_URL = f'{BASE_URL}/boards/'

    def create_new_board(self):
        print(self.token)
        print(self.api_key)
        # Parameters for creating a new board
        board_name = 'Ahmd bdran'
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': board_name
        }

        # Make a POST request to create a new board
        response = requests.post(self.CREATE_BOARD_URL, params=params)

        return response
