This project includes a very basic hybrid framework, We have used pytest for running the tests. Code is written in Python

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)


## Installation
To get started with this, clone the repository and install the dependencies:


cd flipkart_automation_framework

# After the repo is cloned, run setup.bat with the following command

.\setup.bat 
# The above command will create a virtual environment in the directory and download the required dependency

# To activate the virtual environment, run the following command
.\venv\Scripts\activate

## Usage
To run the test cases, a few sample test cases are added in the `TestCases` folder. The following commands can be used for running them:

```sh
pytest -v -s -m "sanity" --browser Chrome --html=Reports/report.html  
pytest -v -s .\TestCases\test_selectProduct.py --browser Chrome --html=Reports/report.html  
pytest -v -s .\TestCases\test_navigate.py --browser Chrome --html=Reports/report.html  
pytest -v -s .\TestCases\test_productsearch.py --browser Chrome --html=Reports/report.html  

# Incase you want to run it through a batch file, you can uncomment the desired command and run it.
.\run.bat





#end of the doc
