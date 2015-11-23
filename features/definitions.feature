Feature: Conference
  Scenario: Definition
    When a conference is created
    Then it should have a name
    And a date range in which it is held
    And a location

  Scenario: Associations
    Given a conference
    Then the conference can be have many organizers
    And can have many speakers
    And can have many talks

Feature: Organization
  Scenario: Definition
    When a sponsor or organization is created
    Then the sponsor should have a name

  Scenario: Associations
    Given a sponsor
    Then the sponsor can be associated with many conferences
    And can have many speakers
    And can have many organizers

Feature: Speaker
  Scenario: Definition
    When a new speaker is created
    Then the speaker should have a first name, last name

  Scenario: Associations
    Given a speaker
    Then the speaker can belong to many organizations
    And can be associated with many conferences

Feature: Organizer
  Scenario: Definition
    When a member of the selection committee is created
    Then the member should have a first name, last name

  Scenario: Associations
    Given a member of the selection committee
    Then the member can belong to many organizations
    And can be associated with many conferences

Feature: Talk
  Scenario: Definition
    When a talk is created
    Then the talk should have a title
    And an associated speaker
    And an associated conference

