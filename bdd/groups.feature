
Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

Examples:
  |name|header|
  |name1|header1|
  |name2|header2|
