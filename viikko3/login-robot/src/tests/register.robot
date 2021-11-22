*** Settings ***
Resource  resource.robot
Test Setup  Register User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  Maija  Maija123
    Output Should Contain  New user registered  

Register With Already Taken Username And Valid Password
    Create User  Maija  Maija123
    Input Credentials  Maija  Maija124
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  ii  Maija123
    Output Should Contain  Username too short

Register with Valid Username And Too Short Password
    Input Credentials  Maija  ii12
    Output Should Contain  Password too short
 
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  Maija  Maijaaaaaaaa
    Output Should Contain  Password should contain both letters and numbers


**** Keywords ****
Register User
    Input New Command

