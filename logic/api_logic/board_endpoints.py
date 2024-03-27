from utility.json_files_reader import read_from_secret_file, read_config


class BoardEndPoints:
    def __init__(self, my_api):
        self.my_api = my_api
        secrets_config = read_from_secret_file()
        trello_token_temp_text = secrets_config['trello_token']
        self.token = trello_token_temp_text[4:]
        api_key_temp_test = secrets_config['api_token']
        self.api_key = api_key_temp_test[4:]
        # Constants for Trello API
        config = read_config()
        base_url = config['api_url']
        self.endpoints = f'{base_url}/boards/'

    def create_new_board(self, board_name):
        # Parameters for creating a new board
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': board_name
        }
        # Make a POST request to create a new board
        response = self.my_api.api_post_request(self.endpoints, params)
        return response

    def delete_a_board(self, board_id):
        board_endpoints = self.endpoints + "" + board_id
        params = {
            'key': self.api_key,
            'token': self.token
        }
        # Make a delete request to remove the board
        response = self.my_api.api_delete_request(board_endpoints, params)
        return response

    def update_board_name(self, board_id, new_name):
        endpoints = self.endpoints + "" + board_id
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': new_name
        }
        # Make a put request to update the board name
        response = self.my_api.api_put_request(endpoints, params)
        return response

    def invite_person_to_board_via_email(self, board_id, email):
        endpoints = self.endpoints + "" + board_id + "/members"
        params = {
            'key': self.api_key,
            'token': self.token,
            'email': email,
            'type': 'normal'
        }
        # Make a put request to invite someone to board via email
        response = self.my_api.api_put_request(endpoints, params)
        return response

