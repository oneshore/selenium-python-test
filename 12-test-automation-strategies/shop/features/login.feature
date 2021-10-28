Feature: Login

Scenario Outline: Login attempts
	Given a user with <username> and <password>
	When I login
	Then I should see the <page>

	Examples:
	| user     | password | page  |
    | aaron    | valid    | admin |
	| lakshmi  | valid    | user  |
	| francois | invalid  | error |
