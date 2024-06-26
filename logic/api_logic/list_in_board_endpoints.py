from utility.json_files_reader import read_from_secret_file, read_config


class ListInBoardEndPoints:
    def __init__(self, my_api, board_id):
        self.my_api = my_api
        secrets_config = read_from_secret_file()
        trello_token_temp_text = secrets_config['trello_token']
        self.token = trello_token_temp_text[4:]
        api_key_temp_test = secrets_config['api_token']
        self.api_key = api_key_temp_test[4:]
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




