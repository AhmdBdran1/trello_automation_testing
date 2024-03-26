from jira import JIRA
from utility.json_files_reader import read_from_secret_file


def create_jira_issue(summary, description):
    # Create JIRA issue with relevant information
    private_config = read_from_secret_file()
    token = private_config['jira_token']
    token = token[4:]
    email = private_config['jira_email']
    jira_url = private_config['jira_url']
    project_token = private_config['project_token']

    auth_jira = JIRA(
        basic_auth=(email, token),
        options={'server': jira_url}
    )
    issue_dict = {
        'project': {'key': project_token},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Bug'},
    }

    # Create the issue
    auth_jira.create_issue(fields=issue_dict)
