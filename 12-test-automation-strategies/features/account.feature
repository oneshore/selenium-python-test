Feature: Account

As a bank account holder
I want to withdraw money
So that I can spend it

Scenario:
	Given I have "100" dollars in my account
	And The ATM fee is "1" dollars
	When I withdraw "20" dollars via ATM
	Then I should have "79" dollars in my account

Scenario:
	Given I have "100" dollars in my account
	When I withdraw "20" dollars at the bank
	Then I should have "79" dollars in my account
