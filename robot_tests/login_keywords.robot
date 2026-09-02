*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://the-internet.herokuapp.com/login
${BROWSER}    Chrome

*** Keywords ***
Open Login Page
    Open Browser    ${URL}    ${BROWSER}

Login With Credentials
    [Arguments]    ${username}    ${password}
    Input Text    id:username    ${username}
    Input Text    id:password    ${password}
    Click Button    css:button[type='submit']

*** Test Cases ***
Login With Valid Credentials
    Open Login Page
    Login With Credentials    tomsmith    SuperSecretPassword!
    Wait Until Element Is Visible    css:.flash.success    timeout=10s
    Element Should Contain    css:.flash.success    You logged into a secure area
    Close Browser

Login With Invalid Credentials
    Open Login Page
    Login With Credentials    wronguser    wrongpass
    Wait Until Element Is Visible    css:.flash.error    timeout=10s
    Element Should Contain    css:.flash.error    Your username is invalid
    Close Browser
