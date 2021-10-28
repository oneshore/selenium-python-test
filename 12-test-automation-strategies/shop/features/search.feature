@shop
Feature: Product Search

As a user on the shopping site
I want to find items
So that I can purchase them

@search
Scenario: Search for mugs

Given I am on the shop home page
When I search for "mugs"
Then I should see "5" items
And each item should be a "mug"
