Feature: Verify Pet Store Order Operation

Scenario: Verify get inventory API functionality
    When we execute the get inventory API method
    Then inventory details are returned 
    And status code of response should be 200

Scenario: Verify Pet Order API functionality
    Given the details of Pet to be Ordered
    When we execute the Order API method
    Then order details are returned 
    And status code of response should be 200
    
Scenario: Verify get order details using order Id
    Given the ID of order that needs to be fetched
    When we execute get Order by ID Method
    Then order details are successfully retrieved 
    And status code of response should be 200

Scenario: Verify delete purchased order using order Id
    Given the ID of order that needs to be deleted
    When we execute Delete Order by ID Method
    Then order details are successfully deleted 
    And status code of response should be 200
    