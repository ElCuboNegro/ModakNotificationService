Feature: Run modak info
    Background:
        Given I have installed modak

    Scenario: project is installed
        Given I have installed the modak project
        When I execute the kedro command "moo"
        Then I should get a successful exit code
        And I should get a increment in the variable stored in the .moo directory
