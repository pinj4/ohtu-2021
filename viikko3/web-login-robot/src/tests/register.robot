*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  maija123  maija123
    Submit Credentials
    Registering Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ii
    Set Password  maija123  maija123
    Submit Credentials
    Registering Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  maija
    set Password  maija  maija
    Submit Credentials
    Registering Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  maija
    Set Password  maija123  maija124
    Submit Credentials
    Registering Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  maija
    Set Password  maija123  maija123
    Submit Credentials
    Go To Login Page
    Set Login Username  maija
    Set Login Password  maija123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  maija2
    Set Password  maija123  maija124
    Submit Credentials
    Go To Login Page
    Set Login Username  maija2
    Set Login Password  maija123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}  ${password_confirmation}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password_confirmation}

Registering Should Succeed
    Welcome Page Should Be Open

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
