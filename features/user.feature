Feature: Verify User CRUD Operation

Scenario: Verify Add User API functionality
    Given the User details which needs to be added
    When we execute the Create User PostAPI method
    Then user is successfully added 
    And status code of response should be 200

@remove_users
Scenario: Verify Multiple User Add API functionality
    Given the User details input array which needs to be added
    When we execute the Create list of Users PostAPI method
    Then users are successfully added 
    And status code of response should be 200

Scenario: Verify user added is able to login
    Given the username and password for login
    When user log-in to the system
    Then users is successfully logged-in 
    And status code of response should be 200

Scenario: Verify user is able to log-out
   
    When user logged out of the system
    Then users is successfully logged-out 
    And status code of response should be 200

Scenario: Verify user details by providing user name
    Given the username for details to be fetched
    When user details are fetched
    Then users details matches 
    And status code of response should be 200

Scenario: Verify updation of user details
    Given the username for details to be updated
    When details are updated and sent
    Then details are updated successfully 
    And status code of response should be 200

Scenario: Verify user removal operation
    Given the username needed to be removed
    When remove operation is performed
    Then details are removed successfully 
    And status code of response should be 200


