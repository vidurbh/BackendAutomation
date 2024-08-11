
echo Script started
python -m venv venv
venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt


echo Script finished.



:: To run test cases
@REM pytest -s -v .\TestCases\test_createUser.py --html=Reports/report.html 
@REM pytest -s -v .\TestCases\test_updateUser.py --html=Reports/report.html 
@REM pytest -s -v .\TestCases\test_viewusers.py --html=Reports/report.html
@REM pytest -s -v .\TestCases\test_deleteUser.py --html=Reports/report.html

