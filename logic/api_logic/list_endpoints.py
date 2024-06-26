from utility.json_files_reader import read_from_secret_file, read_config


class ListEndPoints:
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
        self.base_endpoints = f'{base_url}/lists/'

    def create_new_list(self, board_id, list_name):
        params = {
            'name': list_name,
            'idBoard': board_id,
            'key': self.api_key,
            'token': self.token
        }
        # Make a post request to create a list
        response = self.my_api.api_post_request(self.base_endpoints, params)
        return response

    def get_a_list(self, list_id):
        endpoints = self.base_endpoints + "" + list_id
        params = {
            'key': self.api_key,
            'token': self.token
        }
        # Make a get request to get a list
        response = self.my_api.api_get_request(endpoints, params)
        return response

    def update_list_name(self, list_id, new_name):
        endpoints = self.base_endpoints + "" + list_id
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': new_name
        }
        # Make a put request to update the list name
        response = self.my_api.api_put_request(endpoints, params)
        return response

    def get_list_cards(self, list_id):
        endpoints = self.base_endpoints + "" + list_id + "/cards"
        headers = {
            "Accept": "application/json"
        }

        params = {
            'key': self.api_key,
            'token': self.token,
        }
        # Make a put request to update the list name
        response = self.my_api.api_get_request(endpoints, params, headers)
        return response

