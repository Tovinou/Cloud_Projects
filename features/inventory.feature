@inventory
Feature: Inventory Management
  As a store manager
  I want to manage book inventory
  So that customers can only purchase available books

  Background:
    Given the following inventory:
      | Book Title         | Stock | Price |
      | Popular Book       | 2     | 100   |
      | Rare Book          | 1     | 200   |
      | Out of Stock Book  | 0     | 150   |

  Scenario: Successful purchase within stock limits
    When I add "Popular Book" to the cart
    Then the cart should contain 1 "Popular Book"
    And the inventory for "Popular Book" should be 1

  Scenario: Prevent over-purchasing limited stock
    When I add "Rare Book" to the cart
    And I try to add "Rare Book" to the cart again
    Then I should see "Only 1 copy available" message
    And the cart should contain 1 "Rare Book"

  Scenario: Cannot purchase out-of-stock books
    When I try to add "Out of Stock Book" to the cart
    Then I should see "Out of stock" message
    And the cart should be empty

  Scenario: Mixed inventory scenarios
    When I add "Popular Book" to the cart
    And I add "Popular Book" to the cart
    And I try to add "Popular Book" to the cart again
    Then I should see "Only 2 copies available" message
    And the cart should contain 2 "Popular Book"