import json
import sys
import argparse
import os.path


def create_tokens_file(dictionary, filename='tokens.json'):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)


def main():
    env_cookies = json.loads(os.environ['SECRET'])
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    config = os.path.join(cur_dir, "config/secrets.json")
    create_tokens_file(env_cookies, config)


if __name__ == "__main__":
    main()
