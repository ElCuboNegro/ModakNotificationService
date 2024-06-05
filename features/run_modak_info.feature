Feature: Run modak info
    Background:
        Given I have installed modak-notificationservice

    Scenario: project is installed
        When I execute the modak command "moo"
        Then I should get a successful exit code
        And I should get a increment in the variable stored in the user_directory/.moo directory
