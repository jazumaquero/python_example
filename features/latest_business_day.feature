Feature: Get previous business day given some country Id.

  Scenario: Get latest business day before 2018-10-16 in UK (non holiday)
    Given country id equals to UK
    And current day is 2018-10-16
    And shifted days are 1
    When get latest business days
    Then latest business day is 2018-10-15

  Scenario: Get latest business day before 2018-10-16 in NL (non holiday)
    Given country id equals to UK
    And current day is 2018-10-16
    And shifted days are 1
    When get latest business days
    Then latest business day is 2018-10-15

  Scenario: Get latest business day before 2018's New Years Day in UK
    Given country id equals to UK
    And current day is 2018-01-01
    And shifted days are 1
    When get latest business days
    Then latest business day is 2017-12-29

  Scenario: Get latest business day before 2017's New Years Day in UK
    Given country id equals to UK
    And current day is 2017-01-01
    And shifted days are 1
    When get latest business days
    Then latest business day is 2016-12-30

  Scenario: Get two business day after 2018's Ascension Day in NL
    Given country id equals to NL
    And current day is 2018-05-31
    And shifted days are 2
    When get latest business days
    Then latest business day is 2018-05-29
