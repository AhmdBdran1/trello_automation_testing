# Trello Automation Testing Readme

## Introduction
This project focuses on automating the testing of the Trello website, encompassing both API and UI testing. The project utilizes Selenium for UI testing, leveraging the Selenium Grid for distributed testing. Additionally, API testing is conducted using the `request` library. The project follows the Page Object Model (POM) design pattern and adheres to the Arrange-Act-Assert (AAA) testing principle for clarity and maintainability.

## Features
- **UI Testing**: Selenium is employed for automating UI testing of the Trello website.
- **API Testing**: API testing is conducted using the `request` library to ensure the functionality and reliability of Trello's API endpoints.
- **POM Design Pattern**: The project is structured following the Page Object Model design pattern, enhancing maintainability and readability of the tests.
- **AAA Principle**: Tests are organized into Arrange, Act, and Assert sections, facilitating clarity and ease of understanding.
- **Continuous Integration (CI)**:
  - GitHub Actions: CI is configured using GitHub Actions, ensuring tests are automatically executed upon code changes.
  - Jenkins: CI is also integrated with Jenkins for additional flexibility and control.
- **Bug Tracking**:
  - Jira Integration: Upon test failure, the project automatically creates a bug issue in Jira, streamlining the bug tracking process.
- **Notifications**:
  - Slack Integration: Notifications are sent to Slack upon the completion of builds in GitHub Actions. Additionally, notifications are dispatched when a new bug is opened in Jira.
- **Test Planning and Design**:
  - TestRail: Test cases and test plans are organized and managed in TestRail, providing a centralized location for test design and execution.

## Setup and Configuration
1. **Selenium Grid Setup**: Configure Selenium Grid for distributed testing if necessary.
2. **Environment Setup**: Set up the necessary environment for running UI and API tests.
3. **Project Configuration**: Ensure proper configuration of project settings such as Trello API keys, Jira credentials, Slack integration, etc.
4. **Install Dependencies**: Install project dependencies listed in the `requirements.txt` file.
5. **Test Execution**: Execute tests using appropriate commands or scripts for UI and API testing.
6. **CI/CD Integration**: Ensure proper configuration of CI/CD pipelines in GitHub Actions and Jenkins for automated testing and deployment.
7. **Bug Tracking Integration**: Verify the integration with Jira for automatic bug creation upon test failure.
8. **Notification Setup**: Configure Slack integration for receiving notifications on build completion and bug tracking events.

## Additional Resources
- **STP (Software Test Plan)**: Detailed software test plan document can be found in the repository.
- **STD (Software Test Design)**: Comprehensive software test design document is also available for reference.

## Support
For any inquiries or issues, please contact ahmd1bdran@gmail.com
