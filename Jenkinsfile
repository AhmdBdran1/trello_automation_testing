pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'pip3 install -r requirements.txt' // Install other required packages
                sh 'pip3 install --upgrade html-testRunner' // Install or upgrade html-testRunner package

            }
        }

        stage('Create Secrets File') {
            steps {
                echo 'Creating secrets.json file...'
                sh 'echo \'{"trello_email": "vevem14@gmail.com", "trello_password" : "Ah2024bdr", "jira_url" : "https://ahmd1997bdran.atlassian.net", "jira_email": "ahmd1997bdran@gmail.com", "project_token" : "FPM", "jira_token" : "ahmdATATT3xFfGF0UlRZFau-8FLRB2XZKozc00B4WCaRbbJzYBjtQ5PHUMjyYVCZ-b3jYDN9VEVn8E__e0NCvYKbSAZWXfDJx7mzgzD7NvaI2zVXDVOVTpS0vP05XxOmpidm_se8rChsj9YuHnHCDY0jCLoaksko5EBAZjrdzAib5kgpe5uCmjcxKYs=8F1CF113", "trello_token": "ahmdATTA4f14fcd1933bde89ab95ad5f3003ae9e2c09081ad8079f39b3865259dc47671420A43297", "api_token": "ahmdbbe530cb763d9199352c6463e3440ac8"}\' > config/secrets.json'
            }
        }


        stage('Start Selenium Servers') {
            steps {
                echo 'Starting Selenium Hub...'
                sh 'java -jar selenium-server-4.17.0.jar hub &'

                echo 'Starting Selenium Node...'
                sh 'java -jar selenium-server-4.17.0.jar node &'

                // Wait for a moment to allow servers to startt
                sleep 30
            }
        }

        stage('Run API Tests') {
            steps {
                echo 'Running API Tests..'
                sh 'python3 tests_runner/api_test_runner.py'
            }
        }

        stage('Run UI Tests') {
            steps {
                echo 'Running UI Tests..'
                sh 'python3 tests_runner/ui_test_runner.py'
            }
        }

        stage('Run Failure Scenario Testing') {
            steps {
                echo 'Running Failure Scenario Testing..'
                sh 'python3 -m unittest tests.api_test.negative_test.NegativeTest.test_get_card_with_wrong_api_token || true'
            }
        }


        stage('Upload UI test report') {
            steps {
                echo 'Uploading UI test report..'
                archiveArtifacts 'ui-test-reports/*'
            }
        }

        stage('Upload API test report') {
            steps {
                echo 'Uploading API test report..'
                archiveArtifacts 'api-test-reports/*'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Add deployment steps here
            }
        }
    }
}
