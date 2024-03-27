from utility.json_files_reader import read_from_secret_file, read_config


class CardEndPoints:
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
        self.base_endpoints = f'{base_url}/cards/'

    def create_new_card(self, list_id, card_name):
        headers = {
            "Accept": "application/json"
        }

        params = {
            'name': card_name,
            'desc': 'description',
            'idList': list_id,
            'key': self.api_key,
            'token': self.token
        }
        # Make a post request to create a list
        response = self.my_api.api_post_request(self.base_endpoints, params, headers)
        return response

    def get_a_card(self, card_id):
        endpoints = self.base_endpoints + "" + card_id
        params = {
            'key': self.api_key,
            'token': self.token
        }
        # Make a get request to get a list
        response = self.my_api.api_get_request(endpoints, params)
        return response

    def update_card_name(self, card_id, new_name):
        endpoints = self.base_endpoints + "" + card_id
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': new_name
        }
        # Make a put request to update the list name
        response = self.my_api.api_put_request(endpoints, params)
        return response

    def update_card_description(self, card_id, new_description):
        endpoints = self.base_endpoints + "" + card_id
        params = {
            'key': self.api_key,
            'token': self.token,
            'desc': new_description
        }
        # Make a put request to update the list name
        response = self.my_api.api_put_request(endpoints, params)
        return response

    def delete_card(self, card_id):
        endpoints = self.base_endpoints + "" + card_id
        params = {
            'key': self.api_key,
            'token': self.token,
        }
        # Make a delete request to delete the card
        response = self.my_api.api_delete_request(endpoints, params)
        return response

    def get_card_with_wrong_api_token(self, card_id):
        endpoints = self.base_endpoints + "" + card_id
        params = {
            'key': self.api_key + "ah",
            'token': self.token
        }
        # Make a get request to get a list
        response = self.my_api.api_get_request(endpoints, params)
        return response
