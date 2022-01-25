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
