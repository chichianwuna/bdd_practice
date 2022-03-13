Feature: Testing Paypal payment
  As a user, I should be able to make payments

  Scenario: User should be able to make Paypal payments
    Given I am on the payment page
    When I select payment currency
    And I select or type in payment amount
    And click on the PayPal submit button
    Then I should be redirected to the Paypal portal