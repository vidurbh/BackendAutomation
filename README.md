This project includes a basic framework for API Testing, We have used pytest for running the tests. Code is written in Python and requests library is used

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)


## Installation
To get started with this, clone the repository and install the dependencies:

git clone https://github.com/vidurbh/BackendAutomation.git

# After the repo is cloned, run setup.bat with the following command

.\setup.bat 
# The above command will create a virtual environment in the directory and download the required dependency

# To activate the virtual environment, run the following command
.\venv\Scripts\activate

API Key Setup for GoRest API
To interact with the GoRest API, you need to generate an API key. Follow these steps to obtain and configure your API key:

1. Generate API Key
Login to GoRest using your Google account.
Click on Howdy in the header.
Select API Tokens from the dropdown menu.
Click on New Access Token.
Provide a Label for your API key and click on Submit.
After the API token is generated, make a note of it.

2. Configure the API Key in Your Project
Add the API Token to your project's configuration.
Set the BASE_URL for the API in your configuration.

3. Create .env File
Copy the .env.example file to a new file named .env. This file will contain your API key and BASE_URL.
cp .env.example .env

Ensure the .env file contains the following configuration:
BASE_URL=Base_URL
API_KEY=your_generated_api_key

## Usage
To run the test cases, a few sample test cases are added in the `TestCases` folder. The following commands can be used for running them:

```sh
pytest -s -v .\TestCases\test_viewusers.py --html=Reports/report.html
pytest -s -v .\TestCases\test_createUser.py --html=Reports/report.html
pytest -s -v .\TestCases\test_deleteUser.py --html=Reports/report.html
pytest -s -v .\TestCases\test_updateUser.py --html=Reports/report.html 

# Incase you want to run it through a batch file, you can uncomment the desired command and run it.
.\run.bat





#end of the doc
