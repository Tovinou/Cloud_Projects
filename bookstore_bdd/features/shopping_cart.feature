@shopping_cart
Feature: Shopping Cart Management
  As a customer
  I want to manage books in my shopping cart
  So that I can purchase the books I want

  Background:
    Given the following books are available:
      | Title               | Author          | Price |
      | The Great Gatsby    | F. Scott Fitzgerald | 100 |
      | To Kill a Mockingbird | Harper Lee      | 120  |
      | 1984               | George Orwell    | 90   |

  Scenario: Add a book to the shopping cart
    When I add "The Great Gatsby" to the cart
    Then the cart should contain 1 book
    And the total price should be 100 SEK

  Scenario: Remove a book from the shopping cart
    Given I have added "The Great Gatsby" to the cart
    When I remove "The Great Gatsby" from the cart
    Then the cart should be empty

  Scenario: Update quantity when adding duplicate book
    Given I have added "The Great Gatsby" to the cart
    When I add "The Great Gatsby" to the cart again
    Then the cart should contain 2 of "The Great Gatsby"
    And the total price should be 200 SEK

  Scenario: Clear entire shopping cart
    Given I have added the following books to the cart:
      | Book                 |
      | The Great Gatsby     |
      | To Kill a Mockingbird |
    When I clear the cart
    Then the cart should be empty

  Scenario Outline: Calculate correct total and count
    When I add "<book1>" to the cart
    And I add "<book2>" to the cart
    Then the cart should contain <count> books
    And the total price should be <total> SEK

    Examples:
      | book1                  | book2                  | count | total |
      | The Great Gatsby       | To Kill a Mockingbird  | 2     | 220   |
      | 1984                   | The Great Gatsby       | 2     | 190   |