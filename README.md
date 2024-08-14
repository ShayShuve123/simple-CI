# Jenkins CI Pipeline Example

This project demonstrates a Continuous Integration (CI) pipeline using Jenkins to automate testing for a simple Python project.

## Project Structure

- `main.py`: Core functions of the application.
- `test_main.py`: Unit tests for the application.
- `requirements.txt`: Python dependencies.
- `Jenkinsfile`: Defines the Jenkins pipeline.

## Jenkins Pipeline Stages

1. **Clone Repository:** Jenkins pulls the latest code from GitHub.
2. **Install Dependencies:** Installs required Python packages.
3. **Run Tests:** Executes unit tests to ensure code functionality.
4. **Publish Test Report:** Generates and publishes a test report.
5. **Clean Workspace:** Cleans up the workspace after the build.

## How to Set Up

1. Clone the repository.
2. Set up a Jenkins pipeline with the provided Jenkinsfile.
3. Configure GitHub webhooks to trigger the pipeline on commits.
4. Push changes to see the pipeline in action.

## Screenshots

![Jenkins Pipeline](path_to_screenshot)
