Feature: Contact Management
  As a user
  I want to manage contacts
  So that I can create, read, update, and delete contacts

  Scenario: Create a new contact
    Given I have a new contact with first name "first_name", last name "last_name", and phone number "09390468821"
    When I make a POST request to "/contacts/" endpoint
    Then I should receive a response with status code 201
    And the response should contain the created contact details

  Scenario: Read all contacts
    Given there are existing contacts in the database
    When I make a GET request to "/contacts/" endpoint
    Then I should receive a response with status code 200
    And the response should contain a list of all contacts

  Scenario: Read a specific contact
    Given there is an existing contact with ID 6 in the database
    When I make a GET request to "/contacts/6" endpoint
    Then I should receive a response with status code 200
    And the response should contain details of the contact with ID 6

  Scenario: Update a contact
    Given there is an existing contact with ID 6 in the database
    And I want to update the contact with new phone number "09390468822"
    When I make a PUT request to "/contacts/6" endpoint
    Then I should receive a response with status code 200
    And the response should contain updated details of the contact with ID 6

  Scenario: Delete a contact
    Given there is an existing contact with ID 6 in the database
    When I make a DELETE request to "/contacts/6" endpoint
    Then I should receive a response with status code 204
    And the contact with ID 6 should be removed from the database
