Feature: Shopping cart basic functionality
  As a user of the book store
  I want to manage items in my cart
  So that the cart always shows correct count and totals

  Background:
    Given an empty store with the following books:
      | title                | price |
      | Clean Code           | 30.00 |
      | The Pragmatic Dev    | 25.50 |

  Scenario: Add a single book to cart
    Given I have an empty cart
    When I add "Clean Code" to the cart
    Then the cart should have 1 items
    And the cart total should be 30.00

  Scenario: Remove a book from cart
    Given I have an empty cart
    And I add "Clean Code" to the cart
    When I remove "Clean Code" from the cart
    Then the cart should have 0 items
    And the cart total should be 0.00

  Scenario Outline: Adding a book already in cart increases quantity
    Given I have an empty cart
    When I add "<title>" to the cart
    And I add "<title>" to the cart
    Then the cart should have <qty> of "<title>"
    And the cart total should be <total>

    Examples:
      | title         | qty | total |
      | Clean Code    | 2   | 60.00 |
      | The Pragmatic Dev | 2 | 51.00 |

  Scenario: Cart always shows current sum and item count
    Given I have an empty cart
    And I add "Clean Code" to the cart
    And I add "The Pragmatic Dev" to the cart
    Then the cart should have 2 items
    And the cart total should be 55.50

  Scenario: Empty the cart completely
    Given I have an empty cart
    And I add "Clean Code" to the cart
    And I add "The Pragmatic Dev" to the cart
    When I empty the cart
    Then the cart should have 0 items
    And the cart total should be 0.00
