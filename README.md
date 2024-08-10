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

After the venv is activated, go to https://gorest.co.in/ and sign in with your google account
There you need to generate the api key to work with different APIs.
To generate a new api key follow the below mentioned steps:
1. Login to https://gorest.co.in/ with google account
2. Click on Howdy in the header
3. Click on API Tokens
4. Click on New Access Token
5. Provide Label and click on Submit

After the api token is generated, go to project and add your api token and the BASE_URL 


go to terminal and copy the .env.example file to a env file named '.env'




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
