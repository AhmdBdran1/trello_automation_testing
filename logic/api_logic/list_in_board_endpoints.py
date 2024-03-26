from utility.json_files_reader import read_from_secret_file, read_config


class ListInBoardEndPoints:
    def __init__(self, my_api, board_id):
        self.my_api = my_api
        secrets_config = read_from_secret_file()
        self.token = secrets_config['trello_token']
        self.token = self.token[4:]
        self.api_key = secrets_config['api_token']
        self.api_key = self.api_key[4:]
        # Constants for Trello API
        config = read_config()
        base_url = config['api_url']
        self.endpoints = f'{base_url}/boards/{board_id}/lists'

    def create_list_on_a_board(self, list_name):
        headers = {
            "Accept": "application/json"
        }

        params = {
            'key': self.api_key,
            'token': self.token,
            'name': list_name
        }

        # Make a post request to create a list inside the board
        response = self.my_api.api_post_request(self.endpoints, params, headers)
        return response

    def get_lists_on_a_board(self):
        headers = {
            "Accept": "application/json"
        }

        params = {
            'key': self.api_key,
            'token': self.token,
        }
        # Make a get request to get the lists inside the board
        response = self.my_api.api_get_request(self.endpoints, params, headers)
        return response




