@login
Feature: User Login
  As a customer
  I want to log in to my account
  So that I can complete my purchase and view order history

  Background:
    Given the following users are registered:
      | Username | Password | Email               |
      | alice    | pass123  | alice@example.com   |
      | bob      | secret   | bob@example.com     |

  Scenario: Successful login with correct credentials
    When I login with username "alice" and password "pass123"
    Then I should be logged in successfully
    And I should see welcome message for "alice"

  Scenario: Failed login with incorrect password
    When I login with username "alice" and password "wrongpass"
    Then I should see error message "Invalid credentials"

  Scenario: Failed login with non-existent username
    When I login with username "charlie" and password "anypass"
    Then I should see error message "Invalid credentials"

  Scenario Outline: Login validation with various inputs
    When I login with username "<username>" and password "<password>"
    Then the login should be <result>

    Examples:
      | username | password | result    |
      | alice    | pass123  | successful|
      | alice    | wrong    | failed    |
      | ""       | pass123  | failed    |
      | bob      | ""       | failed    |

  Scenario: Purchase requires login
    Given I am not logged in
    When I try to checkout
    Then I should be redirected to login page
    And I should see "Please login to complete purchase"