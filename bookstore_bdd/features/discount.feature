@discount
Feature: Shopping Cart Discount
  As a customer
  I want to receive discounts when buying multiple books
  So that I can save money on larger purchases

  Background:
    Given the following books are available:
      | Title               | Price |
      | Book 1              | 100   |
      | Book 2              | 200   |
      | Book 3              | 150   |
      | Book 4              | 50    |

  Scenario: No discount for less than 4 books
    When I add "Book 1" to the cart
    And I add "Book 2" to the cart
    Then I should not receive any discount
    And the final price should be 300 SEK

  Scenario: 10% discount for 4 or more books
    When I add "Book 1" to the cart
    And I add "Book 2" to the cart  
    And I add "Book 3" to the cart
    And I add "Book 4" to the cart
    Then I should receive a 10% discount
    And the final price should be 450 SEK

  Scenario Outline: Discount calculation for edge cases
    When I add <quantity> "Book 1" to the cart
    Then the discount should be <discount>%
    And the final price should be <final_price> SEK

    Examples:
      | quantity | discount | final_price |
      | 0        | 0        | 0           |
      | 1        | 0        | 100         |
      | 3        | 0        | 300         |
      | 4        | 10       | 360         |
      | 10       | 10       | 900         |

  Scenario: Invalid quantity handling
    When I add -5 "Book 1" to the cart
    Then I should see an error message
    And the cart should remain empty