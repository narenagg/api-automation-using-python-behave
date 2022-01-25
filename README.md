# Automation Test Suite for Pet Store API using Python Requests and Behave(BDD)

This is a demo test suite demonstrating CRUD operation for user API and order API. I am using BDD framework to design this testsuite.
## Project Structure:

1.Separate Feature Files are there for user API and order API. Located under features folder

2.Demonstrated Tear-down Functionality for a scenario using enviornments.py

3.Data is driven through a separate classes under data folder. We can also use csv or DB to provide data for test cases

4.Utilites contain the configs and resources required in the project.

## Steps to Execute:
1. Install Python

2. Run following commands in terminal to install python packages:

pip install behave 

pip install requests

pip install allure-behave

3. Move to current project folder and execute following command:

behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features

4. This command will execute all the features present in features folder(both user and order).Choose allure result folder as per your convenience. This command will generate reports in json format.

5. Download and Install Allure

6. Run following command to convert above json reports to HTML:

allure serve %allure_result_folder%


## Test Approach:
-	Complete User CRUD operation is automated.
-	Test Suite starts with User Creation and ends with User Removal
-	Basic Validations like Success Message, Response Code are validated for all requests
-	Response Validations for Updating, creation operation is also performed.
-	Complete Order CRUD operation is automated.
-	Test Suite starts with inventory details and ends with order removal.
-	Basic Validations like Success Message, Response Code are validated for all requests
-	Created Project Structure using BDD Framework
-	Created Separate resources Class for different APIs
-	Teardown is implemented for Multiple user creation testcase
-	Used property.ini to maintain different config parameters 



#### If this was an actual project, which would be my next steps?
1.	Implement OAuth 2.0 Automation, generally most project does authentication via OAuth 2.0 nowadays.
2.	Add Request Scenario for Negative Cases like (No active Session etc)
3.	Complete Setup Teardown in actual project, otherwise it will keep on creating new data
4.	Data Drive the framework using csv file or db connections to do multiple iterations with different kind of test data to ensure maximum test coverage.

### Reason for choosing the Tech Stack:

Familiarity with python requests and Behave BDD.

