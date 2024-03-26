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

        stage('Start Selenium Servers') {
            steps {
                echo 'Starting Selenium Hub...'
                sh 'java -jar selenium-server-4.17.0.jar hub &'

                echo 'Starting Selenium Node...'
                sh 'java -jar selenium-server-4.17.0.jar node &'

                // Wait for a moment to allow servers to start
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
                sh 'python3 -m unittest tests.ui_test.card_page_test.CardPageTests.test_to_simulate_failure_situation || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Add deployment steps here
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
    }
}
