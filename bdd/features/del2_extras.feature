Feature: Extra functionality: Discount, Stock and Receipt

  Background:
    Given an empty store with the following books:
      | title             | price  | stock |
      | Clean Code        | 30.00  | 5     |
      | The Pragmatic Dev | 25.50  | 100000|
      | Tiny Book         | 1.00   | 0     |

  # --- Discount tests (Scenario Outline) ---
  Scenario Outline: 10% discount applies when buying more than three books (edge cases included)
    Given I have an empty cart
    When I add "<title>" to the cart <qty> times
    And I checkout
    Then the final total should be <expected_total>

    Examples:
      # 2 books -> no discount
      | title               | qty   | expected_total |
      | Clean Code          | 2     | 60.00          |
      # 4 books -> discount 10% on total
      | Clean Code          | 4     | 108.00         |
      # negative unrealistic quantity should be handled (reject or treat as 0) -> we expect 0.00
      | Clean Code          | -1000 | 0.00           |
      # big quantity -> discount applies
      | The Pragmatic Dev   | 64000 | 1468800.00     |

  # --- Stock tests ---
  Scenario: Adding more items than available stock limits the quantity and informs the user
    Given I have an empty cart
    When I add "Clean Code" to the cart 10 times
    Then the cart should have 5 of "Clean Code"
    And I should see a stock limit message for "Clean Code"

  Scenario: Attempt to add an out-of-stock book yields message and no items added
    Given I have an empty cart
    When I add "Tiny Book" to the cart 1 times
    Then the cart should have 0 items
    And I should see a stock limit message for "Tiny Book"

  # --- Receipt test (email simulated) ---
  Scenario: Receipt is created and "sent" when order is completed
    Given I have an empty cart
    And I add "Clean Code" to the cart
    And I login as user "alice" with password "password123"
    When I checkout
    Then a receipt should be created and sent to "alice@example.com"
    And the last sent email should contain "Clean Code"
