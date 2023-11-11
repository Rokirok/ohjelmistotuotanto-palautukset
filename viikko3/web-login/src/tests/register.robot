*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail With Message  Username must have at least 3 letters

Register With Valid Username And Invalid Password
    Set Username  kayttaja
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit Credentials
    Register Should Fail With Message  Password must have numbers or special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle124
    Submit Credentials
    Register Should Fail With Message  Entered passwords do not match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page
    Register Page Should Be Open
