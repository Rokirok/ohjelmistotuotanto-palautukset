*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testi  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  salasana
    Output Should Contain  Username has to be at least 3 characters

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  pasi123  salasana
    Output Should Contain  Username must only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  pasi  salis
    Output Should Contain  Password has to be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pasi  salissalasana
    Output Should Contain  Password can not contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command